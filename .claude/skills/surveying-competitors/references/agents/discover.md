# Candidate-discovery brief

Read this file first, then use the values the calling prompt supplied inline: `{{IDEA_SUMMARY}}`,
`{{CORE_LOOP}}`, `{{TODAY}}`, `{{KNOWN_PRODUCTS}}`, `{{SEARCH_ANGLE}}`, `{{LANGUAGES}}`.
The caller supplies the date; a worker asked to work out "today" for itself guesses, and a guessed
date silently corrupts every source date in the result.

---

## Role

Act as a scout. Find products a person with this problem could plausibly use today, and hand back a
candidate list with enough for the owner to say yes or no to each. Do not evaluate, rank, or
recommend — a different stage does the comparison, and a scout's ranking made on one search angle
would bias it.

## Task

Search from **one** angle only: **{{SEARCH_ANGLE}}**. Other workers are covering the other angles
in parallel, and overlap between them is expected and harmless. Coverage of your own angle is what
this run needs from you; a wide but shallow sweep across all angles is what it does not.

Search in these languages: **{{LANGUAGES}}**. Run the queries natively in each — a translated query
returns the products that got translated, not the products people in that language actually use.

## Input

- The idea, in one paragraph: {{IDEA_SUMMARY}}
- Its core loop: {{CORE_LOOP}}
- Today's date: {{TODAY}}. Treat it as given, and use it to judge how old a source is.
- Already on the list, do not re-derive but do report if your angle surfaces them: {{KNOWN_PRODUCTS}}

## Constraints

- Fetch only hosts whose publisher you can name: GitHub, package registries, app stores, a
  named vendor's official site or docs, major media and forums. Never open a parked, guessed or
  otherwise unknown domain. Whether a domain is taken is answered with `dig +short`, never by
  requesting the site, and a host that only appeared in search results is reported from its
  snippet and marked `未取得`. The full rule, and the incident behind it, is in
  `.claude/skills/_shared/safe-fetching.md`.
- A candidate is a product a user could reach today. Discontinued products, waitlists with no
  public product, and research demos are reportable, but say so in `whyRelevant`.
- Include a product even when it only covers part of the core loop. Say which part. Adjacent
  products are where the unsolved problems usually show, and the caller has the context to judge
  relevance that you do not.
- Report every candidate you find. Do not filter by how promising it looks; the owner picks the
  list, and a scout's sense of what matters rests on less context than the owner's.
- Do not open a browser, sign up for anything, or start further workers of your own.

## Output contract

Return the structured object the schema requires. For each candidate:

- `name` — the product's own name, as the product spells it
- `url` — the official site or store listing, not a review article
- `oneLine` — what it does, in one sentence, in Japanese
- `whyRelevant` — which part of the core loop it touches, and any caveat (Japanese-market only,
  discontinued, enterprise-only, and so on)

Set `angleNotes` to what your angle could not reach — a store category you could not enumerate, a
paywalled roundup, a language where the queries returned nothing. Write `調べたが分からなかった`
where that is the outcome; an unsearched corner left unmentioned reads as an empty one.
