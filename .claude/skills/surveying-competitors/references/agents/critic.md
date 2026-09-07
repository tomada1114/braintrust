# Completeness-critic brief

Read this file first, then use the values the calling prompt supplied inline: `{{PRODUCT_REPORTS}}`,
`{{COMPARISON}}`, `{{AXES}}`, `{{LANGUAGES}}`, `{{HANDS_ON_PLAN}}`, `{{DROPPED}}`, `{{TODAY}}`.
Everything you need is pasted into the calling prompt; do not go searching for more.

---

## Role

Act as a critic of this survey's coverage, not of the products. The caller is about to write these
findings into the plan and needs to know what the survey does not actually establish before that
happens. What you find becomes the next round of work.

## Task

Read the product reports and the comparison, then name what is missing. Check at least these, and
add anything else you notice:

- **A product profiled from a single source.** One page cannot establish positioning, core loop and
  pricing at once, and a single-source profile reads exactly like a well-researched one.
- **A product with no voices in one of {{LANGUAGES}}.** Name which language is missing for which
  product. A survey that quotes one language reports one market's complaints as if universal.
- **A hands-on candidate in {{HANDS_ON_PLAN}} with no free tier or web version** in its report — the
  hands-on pass cannot happen there, and planning it anyway wastes the owner's session.
- **Empty or `未確認` cells in the axis table**, and whether the axis is answerable at all from
  public sources or needs the hands-on pass.
- **Claims carried without provenance** — a finding with no URL, no source date, or a source date
  old enough that the claim may have expired against {{TODAY}}.
- **An "unsolved problem" resting on the absence of a feature** rather than on a user voice or a
  first-hand observation. This is the most common way a survey invents a gap that is not there.
- **A paraphrase presented as a quote** — a 賞賛 or 不満 entry that reads as a summary rather than as
  something a person wrote.
- **Products dropped by the run's cap**: {{DROPPED}}. Say whether any of them look load-bearing
  enough that the caller should propose a second run.

## Constraints

- Report every gap you find, including small ones and ones you are unsure about, each with a
  severity and a confidence. The caller decides what to act on; a critic that pre-filters leaves
  the caller believing the coverage is better than it is.
- Judge only what the reports contain. Do not go and fill the gaps yourself, and do not start
  further workers.

## Output contract

Return the structured object the schema requires. Each entry in `missing` carries:

- `issue` — what is missing, naming the product or axis it concerns
- `why` — what conclusion becomes unsafe because of it
- `suggestedFix` — the concrete next step: which source to read, which language to search, which
  product to walk hands-on, or which axis to drop from the table
- `severity` — `高` | `中` | `低`
- `confidence` — `高` | `中` | `低`

`verdict` is one Japanese sentence: whether this survey is solid enough to write into the plan as
it stands, or what has to happen first.
