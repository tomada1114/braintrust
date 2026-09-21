#!/usr/bin/env python3
"""Thin runner for TypeSafe's Jev (System One) API. Standard library only.

Jev returns typed judgments (choice / noul / score) with probabilities. In this
repository it is a fast second opinion used to order research triage -- never the
record of truth. See README.md next to this file.

  jev.py ask --questions Q.json --state S.json
  jev.py run --questions Q.json --left L.json --left-key voice \
             [--right R.json --right-key hypothesis] --out out.jsonl

`run` sends one request per left item (or per left x right pair). The state of each
request is {left_key: left_item, right_key: right_item}.
"""
import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

API_URL = os.environ.get("TYPESAFE_BASE_URL", "https://api.typesafe.ai").rstrip("/") + "/v1/systemone"
DEFAULT_MODEL = "jev-1.13.0"  # pinned, so a cached or recorded judgment stays reproducible
USD_PER_MILLION_INPUT = 0.042  # docs.typesafe.ai/models, read 2026-09-21; output tokens are free
CACHE_DIR = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "braintrust-jev"
RETRY_STATUSES = {429, 500, 502, 503, 504}


class JevUnavailable(Exception):
    pass


def load_items(path):
    text = Path(path).read_text(encoding="utf-8")
    if str(path).endswith(".jsonl"):
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    data = json.loads(text)
    return data if isinstance(data, list) else [data]


def load_questions(path):
    qset = json.loads(Path(path).read_text(encoding="utf-8"))
    return qset.get("model", DEFAULT_MODEL), qset["questions"]


def ask(state, questions, model=DEFAULT_MODEL, use_cache=True):
    """One request. Returns {"answers", "usage", "cached"}."""
    body = {"state": state, "model": model, "questions": questions}
    payload = json.dumps(body, ensure_ascii=False, sort_keys=True).encode("utf-8")
    cache_file = CACHE_DIR / (hashlib.sha256(payload).hexdigest() + ".json")
    if use_cache and cache_file.exists():
        cached = json.loads(cache_file.read_text(encoding="utf-8"))
        return {"answers": cached["answers"], "usage": {"input_tokens": 0}, "cached": True}

    key = os.environ.get("TYPESAFE_API_KEY")
    if not key:
        raise JevUnavailable("TYPESAFE_API_KEY is not set in this shell")
    request = urllib.request.Request(API_URL, data=payload, method="POST", headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    })
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                result = json.loads(response.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as error:
            if error.code not in RETRY_STATUSES or attempt == 4:
                detail = error.read().decode("utf-8", "replace")[:300]
                raise JevUnavailable(f"HTTP {error.code}: {detail}") from error
        except (urllib.error.URLError, TimeoutError) as error:
            if attempt == 4:
                raise JevUnavailable(f"network: {error}") from error
        time.sleep(2 ** attempt)

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
    return {"answers": result["answers"], "usage": result.get("usage", {}), "cached": False}


def ask_many(states, questions, model=DEFAULT_MODEL, concurrency=8, use_cache=True):
    """states: list of (id, state). Returns results in the same order, each with "id".

    A request that fails keeps its place with "error" set, so one bad item does not
    sink the batch.
    """
    def one(entry):
        item_id, state = entry
        try:
            return {"id": item_id, **ask(state, questions, model, use_cache)}
        except JevUnavailable as error:
            return {"id": item_id, "answers": {}, "usage": {}, "cached": False, "error": str(error)}

    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        return list(pool.map(one, states))


def summarize(results):
    tokens = sum(r["usage"].get("input_tokens", 0) for r in results)
    return {
        "requests": len(results),
        "cached": sum(1 for r in results if r["cached"]),
        "failed": sum(1 for r in results if r.get("error")),
        "input_tokens": tokens,
        "usd": round(tokens / 1_000_000 * USD_PER_MILLION_INPUT, 5),
    }


def item_id(item, index, id_field):
    return str(item.get(id_field, index)) if isinstance(item, dict) else str(index)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_ask = sub.add_parser("ask", help="one state, one request")
    p_ask.add_argument("--questions", required=True)
    p_ask.add_argument("--state", required=True, help="JSON file holding the state")

    p_run = sub.add_parser("run", help="one request per left item, or per left x right pair")
    p_run.add_argument("--questions", required=True)
    p_run.add_argument("--left", required=True, help=".json array or .jsonl")
    p_run.add_argument("--left-key", required=True, help="name of the left item inside the state")
    p_run.add_argument("--right")
    p_run.add_argument("--right-key")
    p_run.add_argument("--id-field", default="id")
    p_run.add_argument("--out", required=True)
    p_run.add_argument("--concurrency", type=int, default=8)
    p_run.add_argument("--no-cache", action="store_true")
    p_run.add_argument("--dry-run", action="store_true", help="print the first state and the request count, send nothing")

    args = parser.parse_args()
    model, questions = load_questions(args.questions)

    if args.command == "ask":
        state = json.loads(Path(args.state).read_text(encoding="utf-8"))
        try:
            result = ask(state, questions, model)
        except JevUnavailable as error:
            sys.exit(f"jev: {error}")
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return

    if bool(args.right) != bool(args.right_key):
        sys.exit("jev: --right and --right-key go together")
    left = load_items(args.left)
    right = load_items(args.right) if args.right else [None]
    states = []
    for i, l_item in enumerate(left):
        for j, r_item in enumerate(right):
            state = {args.left_key: l_item}
            pair_id = item_id(l_item, i, args.id_field)
            if r_item is not None:
                state[args.right_key] = r_item
                pair_id += "|" + item_id(r_item, j, args.id_field)
            states.append((pair_id, state))

    if args.dry_run:
        print(json.dumps({"requests": len(states), "model": model, "first_state": states[0][1] if states else None},
                         ensure_ascii=False, indent=1))
        return

    results = ask_many(states, questions, model, args.concurrency, use_cache=not args.no_cache)
    with open(args.out, "w", encoding="utf-8") as out:
        for result in results:
            out.write(json.dumps(result, ensure_ascii=False) + "\n")
    summary = summarize(results)
    print(json.dumps(summary, ensure_ascii=False), file=sys.stderr)
    if summary["failed"] == summary["requests"] and results:
        sys.exit(f"jev: every request failed ({results[0]['error']})")


if __name__ == "__main__":
    main()
