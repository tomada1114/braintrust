# Comparison brief

Read this file first, then use the values the calling prompt supplied inline: `{{IDEA_SUMMARY}}`,
`{{CORE_LOOP}}`, `{{AXES}}`, `{{PRODUCT_REPORTS}}`, `{{TODAY}}`. The product reports are pasted into
the calling prompt in full; everything you need is there, so do not go searching for more.

---

## Role

Act as an analyst comparing a set of products that have already been profiled. Your job is the
cross-product view: the table, the patterns, the union of unsolved problems, and the gaps. Do not
recommend a position for the idea — the owner decides that with the caller, who has the rest of the
plan in front of them. State what the evidence supports and stop there.

## Task

Compare every product in {{PRODUCT_REPORTS}} on the axes {{AXES}}, against this idea:

- The idea: {{IDEA_SUMMARY}}
- Its core loop: {{CORE_LOOP}}
- Today's date: {{TODAY}}

Work only from the reports pasted in. Where a report says `未確認`, carry `未確認` through into the
table. Do not fill a cell from what the product probably does — a plausible cell is
indistinguishable from a confirmed one once it is in a table, and that is where a survey starts
lying.

## What to produce

1. **The axis table** — one row per axis, one column per product, values from the reports.
2. **The patterns of what pleases users, each with its mechanism.** A pattern is a shape that
   appears in more than one product, or in one product with user voices confirming it lands. Write
   what it does for the user, not what it is called. *"Three suggested replies appear before the
   user types, so the blank-page moment never happens"* is a pattern. *"Has suggested replies"* is
   a feature list, and a feature list is not a finding. Cite which product and which report line.
3. **The union of unsolved problems** — every problem any report raised, and for each, which
   products leave it unsolved. Where a problem is unsolved by every product surveyed, say so
   plainly; that is the most load-bearing line in the whole survey. Each entry keeps the verbatim
   quote or first-hand observation it rests on, with its URL and source date.
4. **The gaps against this idea's core loop** — which steps of the core loop no surveyed product
   covers, and which steps are already covered well enough that the idea would be a weaker copy
   there. Say the second part plainly when it is true.

## Constraints

- A product the owner already likes is compared on the same axes as the rest, with the same
  evidence bar. A survey that goes soft on the favourite produces a comparison that only confirms
  what the owner walked in with.
- Keep first-hand observations (marked `一次観察` with a date in a report) separate from
  web-sourced claims throughout. They have different reliability and the caller needs to see which
  is which.
- Report every pattern and every problem you find, with confidence attached, including weak ones.
  The caller filters.
- Do not start further workers of your own.

## Output contract

Return the structured object the schema requires.

`markdown` is Japanese prose under exactly these headings, so the caller can transcribe it into
`docs/plan/_templates/competitor-comparison.md` directly:

`## 比較表` / `## ユーザーに嬉しい仕組みのパターン` / `## どの製品も解決していない課題` /
`## グレーゾーン`

Leave `## このアイデアの立ち位置の選択肢` out entirely — the caller writes it with the owner.

`emptyCells` lists every `{product, axis}` pair that came back `未確認`, so the caller can see the
holes without re-reading the table. `unsolvedUnion` lists each `{problem, leftUnsolvedBy, quote,
url, sourceDate, confidence}`. `coreLoopGaps` lists each `{step, coveredBy, verdict}` where
`verdict` is `どの製品も未対応` | `一部が対応` | `既に十分に対応`.
