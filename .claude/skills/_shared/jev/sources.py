#!/usr/bin/env python3
"""Check recorded quotes and claims against the pages they cite. Standard library only.

  sources.py quotes --records R.json --out out.jsonl
      Pure code: is the quote on the page, character for character (after whitespace
      and quote-mark normalisation)? No model involved.

  sources.py claims --claims C.json --out out.jsonl
      C.json: [{"id", "claim", "url"}]. Splits the page into passages and asks Jev which
      passage states the claim, so the main session knows where on the page to read.

Both outputs order the main session's own source check. Neither replaces it: a page
that cannot be fetched from a script (login walls, JS-rendered pages, bot blocks) comes
back as fetch_failed and still has to be opened by hand.
"""
import argparse
import json
import re
import sys
import unicodedata
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import jev  # noqa: E402

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
PASSAGE_CHARS = 1500  # small passages: unrelated text around the sentence acts as a distractor for Jev
MAX_PASSAGES = 80
MIN_PAGE_CHARS = 200
CLAIM_QUESTIONS = Path(__file__).parent / "judgments" / "claim-support.json"
_pages = {}


class _Text(HTMLParser):
    SKIP = {"script", "style", "noscript", "template"}
    BLOCK = {"p", "div", "li", "br", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "section", "article"}

    def __init__(self):
        super().__init__()
        self.parts, self.skipping = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skipping += 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skipping:
            self.skipping -= 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skipping:
            self.parts.append(data)


def fetch_text(url):
    """Returns (text, error). Cached per run so a thread cited ten times is fetched once."""
    if url not in _pages:
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "ja,en;q=0.8"})
            with urllib.request.urlopen(request, timeout=20) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                html = response.read(3_000_000).decode(charset, "replace")
            parser = _Text()
            parser.feed(html)
            _pages[url] = ("".join(parser.parts), None)
        except Exception as error:  # any failure means the same thing here: open it by hand
            _pages[url] = ("", f"{type(error).__name__}: {error}"[:200])
    return _pages[url]


def normalise(text):
    text = unicodedata.normalize("NFKC", text)
    text = text.translate(str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "…": "..."}))
    return re.sub(r"\s+", " ", text).strip().lower()


def check_quote(quote, url):
    text, error = fetch_text(url)
    if error:
        return {"status": "fetch_failed", "detail": error}
    page, wanted = normalise(text), normalise(quote)
    if len(page) < MIN_PAGE_CHARS:
        # A shell page rendered by script: "not on the page" would be a false alarm about the quote.
        return {"status": "fetch_failed", "detail": f"page text is only {len(page)} characters (rendered by script?)"}
    if not wanted:
        return {"status": "not_found", "detail": "empty quote"}
    if wanted in page:
        return {"status": "found"}
    # A quote joined with "…" or "／" by the collector: every fragment has to be on the page.
    # Split before normalising, because NFKC turns "／" into "/", which also occurs inside sentences.
    fragments = [normalise(f) for f in re.split(r"\.\.\.|…|／", quote)]
    fragments = [f for f in fragments if len(f) >= 12]
    if len(fragments) > 1 and all(f in page for f in fragments):
        return {"status": "found", "detail": f"{len(fragments)} fragments"}
    head, tail = wanted[:30], wanted[-30:]
    if len(wanted) > 80 and (head in page or tail in page):
        return {"status": "partial", "detail": "start or end is on the page, the whole sentence is not"}
    return {"status": "not_found"}


def passages(text):
    blocks = [re.sub(r"\s+", " ", b).strip() for b in text.split("\n")]
    out, current = [], ""
    for block in blocks:
        if not block:
            continue
        if current and len(current) + len(block) > PASSAGE_CHARS:
            out.append(current)
            current = ""
        current = (current + " " + block).strip()
        while len(current) > PASSAGE_CHARS * 2:
            out.append(current[:PASSAGE_CHARS])
            current = current[PASSAGE_CHARS:]
    if current:
        out.append(current)
    return out


def check_claim(claim, url, model, questions):
    text, error = fetch_text(url)
    if error:
        return {"status": "fetch_failed", "detail": error}
    if len(normalise(text)) < MIN_PAGE_CHARS:
        return {"status": "fetch_failed", "detail": "page has almost no text (rendered by script?)"}
    chunks = passages(text)
    truncated = len(chunks) > MAX_PASSAGES
    chunks = chunks[:MAX_PASSAGES]
    states = [(i, {"claim": claim, "passage": chunk}) for i, chunk in enumerate(chunks)]
    results = [r for r in jev.ask_many(states, questions, model) if not r.get("error")]
    if not results:
        return {"status": "jev_failed"}
    best = max(results, key=lambda r: r["answers"]["states_claim"]["noul"])
    worst = max(results, key=lambda r: r["answers"]["contradicts_claim"]["noul"])
    return {
        "status": "checked",
        "p_states_claim": round(best["answers"]["states_claim"]["noul"], 3),
        "best_passage": chunks[best["id"]][:700],
        "p_contradicts": round(worst["answers"]["contradicts_claim"]["noul"], 3),
        "contradicting_passage": chunks[worst["id"]][:700] if worst["answers"]["contradicts_claim"]["noul"] >= 0.5 else None,
        "passages": len(chunks),
        "page_truncated": truncated,
        "input_tokens": sum(r["usage"].get("input_tokens", 0) for r in results),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p_quotes = sub.add_parser("quotes")
    p_quotes.add_argument("--records", required=True, help=".json array or .jsonl with quote and url fields")
    p_quotes.add_argument("--quote-field", default="quote")
    p_quotes.add_argument("--url-field", default="url")
    p_quotes.add_argument("--out", required=True)
    p_claims = sub.add_parser("claims")
    p_claims.add_argument("--claims", required=True, help='[{"id", "claim", "url"}]')
    p_claims.add_argument("--out", required=True)
    args = parser.parse_args()

    rows = []
    if args.command == "quotes":
        for i, record in enumerate(jev.load_items(args.records)):
            quote, url = record.get(args.quote_field, ""), record.get(args.url_field, "")
            rows.append({"index": i, "url": url, "quote": quote[:120], **check_quote(quote, url)})
    else:
        model, questions = jev.load_questions(CLAIM_QUESTIONS)
        for claim in jev.load_items(args.claims):
            rows.append({"id": claim.get("id"), "url": claim["url"], "claim": claim["claim"],
                         **check_claim(claim["claim"], claim["url"], model, questions)})

    with open(args.out, "w", encoding="utf-8") as out:
        for row in rows:
            out.write(json.dumps(row, ensure_ascii=False) + "\n")
    counts = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    print(json.dumps(counts, ensure_ascii=False), file=sys.stderr)


if __name__ == "__main__":
    main()
