# Review-mining brief

Read this file first, then use the values the calling prompt supplied inline: `{{PRODUCT_NAME}}`,
`{{PRODUCT_URL}}`, `{{PROFILE_SUMMARY}}`, `{{CORE_LOOP}}`, `{{LANGUAGES}}`, `{{TODAY}}`.
The caller supplies the date; a worker asked to work out "today" for itself guesses, and a guessed
date silently corrupts every source date in the result.

---

## Role

Act as a collector of what users actually said about one product. Bring back their words, not your
reading of them. Do not advise and do not rank — a later stage compares products across the whole
set, and a collector's verdict on one product would bias it.

## Task

Gather the praised points, the complained points, and the **problems users describe as still
unsolved** for **{{PRODUCT_NAME}}** ({{PRODUCT_URL}}).

The reason this exists: the owner is looking for the gap an idea could occupy. The praised points
say what is worth borrowing; the unsolved problems say where the gap is.

- What the product is, from the profile stage: {{PROFILE_SUMMARY}}
- The idea's core loop, for judging which complaints are on-topic: {{CORE_LOOP}}
- Today's date: {{TODAY}}

## Sources

App Store and Google Play reviews, Reddit, X, Hacker News, product forums, blog posts and personal
write-ups, and the product's own community or issue tracker where it has a public one.

Search in these languages: **{{LANGUAGES}}**. Run the queries natively in each. A survey with voices
in only one language reports one market's complaints as if they were everyone's, and the caller
cannot tell from the result that a language is missing — so if one language returns nothing, say so
explicitly in `gaps`.

## What counts as an unsolved problem

Only these three shapes count, and each needs a voice or an observation behind it:

- a **workaround** — a user describing what they do outside the product to get the job done
- a **feature request** that keeps recurring, or a maintainer answer saying it is not planned
- a **churn reason** — a user saying what made them stop, and what they moved to

A feature missing from the marketing page is **not** an unsolved problem. Absence on a page is
evidence about the page. Do not infer a user's pain from a gap in a feature list.

## Constraints

- Quote verbatim. Never paraphrase into quotation marks. Where a quote is long, cut with `…` and
  keep the user's own words on both sides of the cut.
- Report every finding with its confidence attached, including the ones that look minor and the
  ones you are unsure about. Filtering happens in a later stage, which has the full set.
- Count sources, not people. Report the number of distinct sources you read. One thread with forty
  replies is one source; do not convert it into forty users.
- Weigh recency: a complaint from a version several releases back may already be fixed. Record the
  source date and lower the confidence rather than dropping it.
- Do not open a browser session, sign up, or pay for anything. Do not start further workers.

## Output contract

Return the structured object the schema requires.

`markdown` is Japanese prose under exactly these headings, so the caller can transcribe it into
`docs/plan/_templates/competitor.md` directly:

`## ユーザーの声` (with `### 賞賛` and `### 不満` beneath it) / `## 解決できていない課題`

Every entry in `praised`, `complained` and `unsolvedProblems` carries the verbatim `quote`, its
`language`, `url`, `sourceDate` (the post's own date, or `記載なし`), and `confidence` — `高` (a
direct first-hand account), `中` (second-hand or undated), `低` (possibly stale or ambiguous).
Each `unsolvedProblems` entry also carries `shape`: `回避策` | `要望` | `離脱理由`.

`sourceCount` is the number of distinct sources read. `gaps` lists what could not be reached — a
language with no results, a forum behind a login, a store with no reviews. Write
`調べたが分からなかった` where that is the outcome.
