---
name: recording-research
description: "Run and record a factual check or a comparison in this planning repository: classify fact-check (proceed) versus comparison (propose the scope and wait for agreement), delegate one sonnet sub-agent per topic, confirm at least one primary source in the main session, then write docs/plan/<idea-slug>/research/<topic>.md with source URL, source date, confidence and an explicit gray-zone section. Use when a factual question would change a decision (whether an SDK supports something, what terms of service say, pricing, free-tier limits) or when the owner agrees to a comparison. Examples: <example>user: 'Gemini の無料枠でデータは学習に使われる?' assistant: 'I will use the recording-research skill'</example>"
metadata:
  platforms: claude-code, codex
---

# recording-research

Without this skill the findings live only in the chat and vanish with it, source URLs and dates are lost, and a worker's claim gets transcribed into the plan without anyone checking it against the original.

## When this fires

A factual question comes up that would change a decision — whether an SDK supports something, what the terms of service say, pricing, the ceiling on a free tier — or the owner agrees to a comparison. It fires from any stage of the discussion, not a fixed point in the sequence.

## Read before asking anything

Read the idea's `open-questions.md` and its existing `research/` files. A question already answered there needs a re-check only if the recorded 調査日 is old.

## Procedure

1. **Classify the question first**, because the two classes need different permission:
   - **Fact check** — proceed without asking. Letting the discussion run on a wrong premise costs more than the check.
   - **Comparison, or anything long-running** (competitor sweeps, technology comparisons) — propose the purpose and the scope, and **wait for agreement** before starting. The cost is the owner's to accept.
2. **Delegate one topic to one `sonnet` worker, at most 3 per session** <!-- derived from orchestrating-models §2 -->, using the brief in [references/agents/fact-check.md](references/agents/fact-check.md). Go past 3 only when the owner asks for it. Fill in the brief's placeholders — the question, today's date, the idea slug, why it matters, what is already known — before handing it over.
3. **Open at least one primary source yourself and read the quote you are going to rely on.** When the worker returned more than a handful of findings, let Jev point at where to read first: write the findings as `[{"id", "claim", "url"}]` to the scratchpad and run `sources.py claims` as [../_shared/jev/README.md](../_shared/jev/README.md) describes. For each claim it returns the passage on the cited page most likely to state it, and any passage that seems to contradict it. Start with the claims whose `p_states_claim` is low or whose `p_contradicts` is high. This orders your reading and nothing more — a high probability is not a confirmation, the confidence (`高` / `中` / `低`) in the file still comes from what you read, and a `fetch_failed` page is one to open by hand. Skip it when the key or the API is unavailable. Never carry a claim into a decision on hearsay: the worker's summary is one restatement away from the source, and the difference is exactly where terms of service go wrong. Anything you could not confirm stays marked as unconfirmed.
4. **Write `docs/plan/<idea-slug>/research/<topic>.md`** — one topic per file, in the format of `docs/plan/_templates/research.md` (調査日 / 調査手段 / 問い, then 結論 / 根拠 / グレーゾーン・未確認 / 影響する論点). Point at the template rather than copying it; it is versioned in the repository. Every finding carries its source URL, source date and confidence (`高` / `中` / `低`), and the gray-zone section is filled in, not dropped when it would be empty-looking.
5. **Link the note back from `open-questions.md`**: in the 材料 line of the question it bears on, name the file by relative path. A note nothing points at is not found again.
6. **Where delegation is unavailable, run the same brief inline, one topic at a time.** The requirements on the output do not change with how the work was run.

## Output

`docs/plan/<idea-slug>/research/<topic>.md`, plus the 材料 line updated in that idea's `open-questions.md`. Nothing at the repository root. Facts and sources only — no decision is made here; a decision belongs to the owner and goes to `decisions.md`.

## Rules that are easy to get wrong

- Never have a worker, a script or yourself fetch a host nobody has identified. Whether a domain is taken is a DNS question (`dig +short`), and a parked or guessed domain is never opened to "see what is there" — that is how a quarantined download reached the owner's machine on 2026-09-21. Known publishers (GitHub, package registries, app stores, a named vendor's site, major media and forums) are fine. Every ad-hoc worker prompt that may touch the network carries this rule too, and URLs on unknown hosts are dropped before `sources.py` runs. Details: [../_shared/safe-fetching.md](../_shared/safe-fetching.md).
- Do not skip step 3 because the worker sounded confident. Confidence in a summary carries no evidence.
- Record the source date as the page shows it, or `記載なし`. Do not substitute the day you looked.
- Keep the gray zone honest: what the sources are silent about, where they contradict each other, and what could not be checked. Silence recorded as agreement is the failure this section exists to prevent.
- Do not write the findings into the skill or into background notes as if they were permanent. Values age; the dated files under `docs/landscape/` and this idea's `research/` are where they belong.
- One topic, one file. A file covering three questions cannot be re-checked or superseded topic by topic.
