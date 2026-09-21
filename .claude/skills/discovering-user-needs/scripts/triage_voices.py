#!/usr/bin/env python3
"""Order the main session's source check after a user-needs sweep.

  triage_voices.py --records records.json --hypotheses hypotheses.json --out triage.md

`records` is the `records` array the Workflow returned; `hypotheses` is the array that went
into its `args`. Two independent signals are laid beside the extract stage's reading:

  - code: is each quote on the page it cites (../../_shared/jev/sources.py)
  - Jev:  a second opinion on supports / refutes per voice x hypothesis, read from the quote
          alone, never from the extract stage's fields

The output is a checklist of which sources to open first. It carries no verdict. Jev's
answers are a fast reference, and a disagreement means "look here", not "the worker was wrong".
"""
import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

SHARED = Path(__file__).resolve().parents[2] / "_shared" / "jev"
sys.path.insert(0, str(SHARED))
import jev  # noqa: E402
import sources  # noqa: E402

QUESTIONS = Path(__file__).resolve().parents[1] / "references" / "judgments" / "voice-stance.json"
LOW_CONFIDENCE = 0.5  # a starting point, not a calibrated threshold
HYPOTHESIS_FIELDS = ("who", "situation", "pain", "workaround", "refutedBy")


def worker_label(record, hypothesis_id):
    if hypothesis_id in record.get("supports", []):
        return "supports"
    if hypothesis_id in record.get("refutes", []):
        return "refutes"
    return "none"


def jev_label(choice):
    return choice if choice in ("supports", "refutes") else "none"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--records", required=True)
    parser.add_argument("--hypotheses", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--skip-fetch", action="store_true", help="skip the quote-on-page check")
    args = parser.parse_args()

    records = jev.load_items(args.records)
    hypotheses = jev.load_items(args.hypotheses)
    model, questions = jev.load_questions(QUESTIONS)

    quote_status = [{"status": "skipped"}] * len(records) if args.skip_fetch else [
        sources.check_quote(r.get("quote", ""), r.get("url", "")) for r in records]

    states, keys = [], []
    for i, record in enumerate(records):
        voice = {"quote": record.get("quote", ""), "sourceType": record.get("sourceType", "")}
        for hypothesis in hypotheses:
            keys.append((i, hypothesis["id"]))
            states.append((len(states), {"voice": voice,
                                         "hypothesis": {k: hypothesis.get(k, "") for k in HYPOTHESIS_FIELDS}}))
    results = jev.ask_many(states, questions, model)
    usage = jev.summarize(results)
    jev_down = usage["failed"] == usage["requests"]

    rows = []
    for (i, hypothesis_id), result in zip(keys, results):
        if result.get("error"):
            continue
        stance = result["answers"]["stance"]
        rows.append({
            "i": i, "h": hypothesis_id,
            "worker": worker_label(records[i], hypothesis_id),
            "jev": jev_label(stance["choice"]), "jev_raw": stance["choice"],
            "confidence": stance["confidence"],
            "first_hand": result["answers"]["first_hand"]["noul"],
            "intensity": result["answers"]["intensity"]["score"],
        })

    def reasons(i):
        found = []
        if quote_status[i]["status"] in ("not_found", "partial"):
            found.append((0, f"引用がページに見つからない（{quote_status[i]['status']}）"))
        if quote_status[i]["status"] == "fetch_failed":
            found.append((2, "スクリプトからページを取得できない。手で開く"))
        for row in (r for r in rows if r["i"] == i):
            if row["worker"] != row["jev"]:
                found.append((1, f"{row['h']}: extract は {row['worker']}、Jev は {row['jev_raw']}（confidence {row['confidence']:.2f}）"))
            elif row["jev"] != "none" and row["confidence"] < LOW_CONFIDENCE:
                found.append((3, f"{row['h']}: {row['jev']} で一致するが Jev の confidence が低い（{row['confidence']:.2f}）"))
        return sorted(found)

    flagged = sorted(((reasons(i), i) for i in range(len(records)) if reasons(i)), key=lambda x: (x[0][0][0], x[1]))

    lines = [
        "# 原典確認の順番（参考）",
        "",
        f"- 対象: {len(records)} 件の声 × {len(hypotheses)} 仮説。Jev モデル `{model}`、{usage['requests']} リクエスト"
        f"（キャッシュ {usage['cached']}、失敗 {usage['failed']}）、入力 {usage['input_tokens']} トークン、約 ${usage['usd']}",
        "- これは確認の順番を決めるための参考で、判定ではない。Jev は引用文だけを読んだ素早い第二意見であり、"
        "食い違いは「ここを見よ」の意味しか持たない。仮説の判定は原典を開いたメインセッションが下す。",
    ]
    if jev_down:
        lines.append(f"- **Jev は使えなかった**（{results[0].get('error', '') if results else 'no requests'}）。以下は引用の機械照合だけ。")
    lines += ["", "## 先に開くもの", ""]
    if not flagged:
        lines.append("旗の立った声はない。主要クラスタごとに最低 1 件を開く通常の確認に進む。")
    for found, i in flagged:
        record = records[i]
        lines.append(f"- [ ] #{i} {record.get('sourceType', '')} — {record.get('url', '')}")
        lines.append(f"  - 「{record.get('quote', '')[:160]}」")
        lines += [f"  - {text}" for _, text in found]

    lines += ["", "## 仮説ごとの出典数（コードで数えた。重複 URL は 1 件）", "",
              "| 仮説 | extract: 支持 | extract: 反証 | Jev: 支持 | Jev: 反証 | 両者一致の支持 | うち一人称らしい (first_hand ≥ 0.7) |",
              "| --- | --- | --- | --- | --- | --- | --- |"]
    for hypothesis in hypotheses:
        mine = [r for r in rows if r["h"] == hypothesis["id"]]
        urls = lambda pred: len({records[r["i"]].get("url") for r in mine if pred(r)})  # noqa: E731
        lines.append("| {} | {} | {} | {} | {} | {} | {} |".format(
            hypothesis["id"],
            urls(lambda r: r["worker"] == "supports"), urls(lambda r: r["worker"] == "refutes"),
            urls(lambda r: r["jev"] == "supports"), urls(lambda r: r["jev"] == "refutes"),
            urls(lambda r: r["worker"] == r["jev"] == "supports"),
            urls(lambda r: r["worker"] == r["jev"] == "supports" and r["first_hand"] >= 0.7)))

    languages, domains, undated = {}, {}, 0
    for record in records:
        languages[record.get("language", "?")] = languages.get(record.get("language", "?"), 0) + 1
        domain = urlparse(record.get("url", "")).netloc or "?"
        domains[domain] = domains.get(domain, 0) + 1
        undated += record.get("sourceDate", "記載なし") == "記載なし"
    statuses = {}
    for status in quote_status:
        statuses[status["status"]] = statuses.get(status["status"], 0) + 1
    agree = sum(1 for r in rows if r["worker"] == r["jev"])
    lines += ["", "## 偏りと来歴（コードで数えた）", "",
              f"- 言語: {json.dumps(languages, ensure_ascii=False)}",
              f"- ドメイン: {json.dumps(dict(sorted(domains.items(), key=lambda x: -x[1])), ensure_ascii=False)}",
              f"- 出典日付が `記載なし`: {undated} / {len(records)}",
              f"- 引用の機械照合: {json.dumps(statuses, ensure_ascii=False)}",
              f"- extract と Jev の一致: {agree} / {len(rows)} ペア" if rows else "- extract と Jev の一致: 計測なし",
              ""]
    Path(args.out).write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {args.out}: {len(flagged)} flagged of {len(records)} voices, {json.dumps(usage)}", file=sys.stderr)


if __name__ == "__main__":
    main()
