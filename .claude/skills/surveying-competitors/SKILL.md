---
name: surveying-competitors
description: "Survey the products an idea competes with and write docs/plan/<idea-slug>/research/competitors/: one file per product covering positioning, the core loop a first-time user walks, the UI/UX traits and the mechanism that makes each pleasant, verbatim user voices, and the problems it leaves unsolved, plus a comparison file with an axis table and the gaps no product covers. Desk research after the owner agrees the scope, then a hands-on pass through the top 1-3 in the owner's own browser. Use when 既存プロダクトとの違い in overview.md is still a guess, when the owner asks what existing apps do or why they feel pleasant, or before concluding an idea is not a weaker copy of what exists. Examples: <example>user: '競合を調べたい' assistant: 'I will use the surveying-competitors skill'</example>"
metadata:
  platforms: claude-code
---

# surveying-competitors

Without this skill the session names the two competitors it happens to remember, lists their features, and 既存プロダクトとの違い in `overview.md` stays a guess — with no idea why those products feel good to use, and no evidence about what they leave unsolved.

## When this fires

The owner asks what already exists, what those products do, why they are pleasant to use, or whether this idea is just a weaker copy. It also fires from `intaking-ideas` and `shaping-experience` when 既存プロダクトとの違い or 便利さの定義 turns out to rest on memory rather than evidence.

This skill feeds those two and never writes their files. It produces research notes and hands back options with one recommendation; the owner decides what `overview.md` and `experience.md` end up saying.

This is comparison-class research under `docs/decisions.md` (2026-09-06 事実確認は先に進める。比較調査は同意を取ってから): propose the scope and wait. `recording-research` still covers a single factual question about one product — use it rather than a survey run when that is all that is needed.

## Read before asking anything

Read in this order, then ask only about what is still missing.

1. `docs/plan/README.md` — the index.
2. The idea's `overview.md` (especially 既存プロダクトとの違い), `experience.md` if it exists, `decisions.md`, `open-questions.md`.
3. Everything already under the idea's `research/`, including `research/competitors/`. A product already profiled needs re-profiling only if its 調査日 is old; re-running a survey the repository already holds spends the owner's tokens on a file that exists.

## Procedure

1. **Frame the survey and propose the scope, then wait for agreement.** Collect candidates: the products the owner has already named, plus the ones this session knows. Ask 2–4 questions in one round, each with options, the trade-off and exactly one recommendation. Put on the table:
   - the candidate list — and, when the long tail matters, a short discovery stage first (step 2);
   - the comparison axes. Default set: 対象ユーザー, 位置づけ, 中核のループ, 主要機能, UI・UX の特徴とそれが嬉しい理由, 課金のモデル, プラットフォーム, 賞賛されている点, 不満が出ている点, 解決できていない課題. Add axes the idea needs; dropping one needs a reason, which goes in the comparison file's グレーゾーン;
   - which 1–3 products get the hands-on pass, and whether each has a free tier or web version — when the candidate list is open and a discovery stage will run, agree this **after** the discovery stage, not before; the owner cannot pick from a list that does not exist yet;
   - the agent count and model mix from `references/workflow.md`, so the owner is agreeing to the cost as well as the scope.

   Before seeding an owner-named product as a known product, confirm its real name and official URL — a wrong name defeats de-duplication in the discovery stage.

   The owner's agreement is what authorises running the Workflow. Do not start it on an assumed yes.
2. **Run the Workflow in [references/workflow.md](references/workflow.md).** When the candidate list is open, run discover mode first as its own small call, show the owner the candidates, and get the list agreed before the survey run. Fill `args` from what the owner agreed — including `today`, because a worker left to derive the date guesses it and corrupts every source date downstream. The script caps the run at 6 products and `log()`s what it dropped; if something load-bearing was dropped, propose a second run rather than quietly leaving it out.
3. **Open at least one primary source per product yourself** — the official page — and confirm the core claims: what the product is for, its core loop, whether a free tier exists. To decide where else to look, run the two checks in [../_shared/jev/README.md](../_shared/jev/README.md) from the scratchpad: `sources.py quotes` over every voice in `reviews.praised` / `complained` / `unsolvedProblems` (is the sentence on the page, character for character — plain code), and `sources.py claims` over `profile.axisValues` written as `[{"id", "claim": "<product> — <axis>: <value>", "url"}]` (Jev finds the passage that states it, or one that contradicts it). Open what comes back `not_found`, `partial`, low `p_states_claim` or high `p_contradicts` before anything else. Both are a reference for ordering the check, not a result: nothing is marked confirmed because a script said so, and `fetch_failed` — most app-store and social pages — means open it by hand. Skip this when the key or the API is unavailable. A worker's summary is one restatement away from the source. Anything you could not confirm stays marked `未確認`.
4. **Walk the agreed products hands-on.** The hands-on pass may be delegated to ONE `sonnet` sub-agent that runs strictly serially <!-- derived from orchestrating-models §2 -->; the main session writes the brief (which products, what to observe, the 一次観察 bullet format from the template) and verifies the result against the primary source. Follow the global `operating-chrome` skill for the browser mechanics; it drives the owner's real Chrome with their existing logins, which is the only reason this pass is possible at all. Walk the core loop as a first-time user: open or sign in, the first screen, the first meaningful action, what comes back, what is left behind. Record the steps, the friction points, the moments of delight, and **the mechanism behind each one** — "three suggested replies appear before the user types, so the blank-page moment never happens". Label the whole thing `一次観察` with the date it happened.
   - Only the products the owner agreed to, only with the owner's own accounts, only within a free tier or web version.
   - Stop when a sign-up wall or a payment appears, and record where you stopped. Ask before creating an account, paying, or changing any setting.
   - The brief must state these hard rules: never run two browser agents in parallel — parallel Chrome automation breaks; never send text into an existing conversation, task or draft of the owner's — always start a new one; never edit any file except the assigned output file; stop at sign-up walls, payments and settings changes.
   - Screenshots only when the owner asks for them; they go under `docs/plan/<idea-slug>/research/competitors/img/`.
5. **Write the files**, following the templates rather than inventing headings — they are versioned in the repository.
   - `docs/plan/<idea-slug>/research/competitors/<product-slug>.md` per product, format: `docs/plan/_templates/competitor.md`.
   - `docs/plan/<idea-slug>/research/competitors/_comparison.md`, format: `docs/plan/_templates/competitor-comparison.md`. The workflow leaves このアイデアの立ち位置の選択肢 empty on purpose: write the options and the trade-offs there yourself, with exactly one recommendation and its reason, marked as a recommendation and not a decision.
   - Work the completeness critic's findings in: fix what is cheap to fix, and record the rest in グレーゾーン rather than letting the file read as complete.
6. **Link back and say what it bears on.** Name the files by relative path in the 材料 line of every `open-questions.md` question they touch — a note nothing points at is not found again. Then tell the owner, with options and one recommendation for each: what this changes in 既存プロダクトとの違い in `overview.md`, and what it changes in 便利さの定義 in `experience.md`, where 便利 is measured against the alternative that now has a name and a profile. Edit neither file here. `decisions.md` gets an entry only after the owner explicitly decides.

## Output

`docs/plan/<idea-slug>/research/competitors/<product-slug>.md` (one per product), `docs/plan/<idea-slug>/research/competitors/_comparison.md`, optionally `research/competitors/img/`, and the 材料 lines updated in that idea's `open-questions.md`. Nothing at the repository root, and no edits to `overview.md` or `experience.md`.

## Rules that are easy to get wrong

- **A feature list is not the finding.** "Has suggested replies" is a list entry; "shows three suggested replies before the user types, so the blank-page moment never happens" is the finding. If the mechanism sentence is missing, the survey has recorded what to copy without recording why it works, and the copy will be a worse version.
- **An unsolved problem comes from a user voice or from first-hand observation**, never from a feature missing off a marketing page. Absence on a page is evidence about the page. A gap invented this way is the easiest way for a survey to justify building something nobody wants.
- **A product the owner likes gets the same axes and the same evidence bar as the rest.** Going soft on the favourite produces a comparison that only confirms what the owner already believed.
- **Keep 一次観察 dated and separate from web-sourced claims**, and do not promote a demo video into first-hand observation. A video is evidence about what the vendor chose to show.
- **Report 出典の件数, not user counts.** One thread with forty replies is one source. Agent counts are not user counts either.
- **Quote verbatim.** A paraphrase inside quotation marks is the one error in this file that no later reader can detect.
- Prices and free-tier figures belong in these dated research files with their source dates, and nowhere else — not in `overview.md`, not in `experience.md`, not in this skill.
- A hands-on pass of one or two turns is a small sample. When it contradicts something the owner has observed repeatedly, do not recommend overturning the owner's observation; record both, with the conditions each was seen under, and leave the condition as an open question.
