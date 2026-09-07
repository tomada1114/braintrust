---
name: handing-off-plans
description: "Write docs/plan/<idea-slug>/handoff.md for an idea that is moving to implementation: what to build, the decisions that affect implementation with their dates, the questions the product repository still has to decide, the constraints, and pointers to the research with stale findings marked 要再確認. Then set that idea's row in docs/plan/README.md to the 実装へ state. Makes no new decisions along the way. Use when the owner says an idea moves to implementation, asks for the handoff, or asks what the product repository needs to know. Examples: <example>user: 'small-talk-trainer を実装に進める' assistant: 'I will use the handing-off-plans skill'</example>"
metadata:
  platforms: claude-code, codex
---

# handing-off-plans

Without this skill the first session in the product repository starts from whatever survived in chat, and research from months ago gets used as if it were current.

## When this fires

The owner says an idea moves to implementation, or asks for the handoff. This is the graduation step: everything before it stays in this repository, and this document is what leaves.

## Read before asking anything

Read all of the idea's files first — `overview.md`, `experience.md`, `decisions.md`, `open-questions.md` and everything under `research/`. The handoff is a selection from what is already recorded, so anything not read cannot be selected.

If `experience.md` does not exist, say so plainly in the handoff. The implementation side will otherwise have to work the experience out again from scratch without knowing that it was never settled here.

## Procedure

1. **Write `docs/plan/<idea-slug>/handoff.md`** in the format of `docs/plan/_templates/handoff.md` (作成日 / 引き継ぎ先, then 何を作るか / 決まっていること / 決まっていないこと / 制約 / 調査へのポインタ). Point at the template rather than copying it; it is versioned in the repository.
   - **何を作るか** — one paragraph, summarising `overview.md` and `experience.md`.
   - **決まっていること** — from `decisions.md`, **only what affects implementation**, each item with the date it was decided. A date lets the reader judge how much the decision has aged; a decision list without dates has to be taken entirely on faith.
   - **決まっていないこと** — anything still open. Where the intent is that the product repository decides it, say so, so it is read as a task and not as an omission.
   - **制約** — cost, data handling, technical limits.
   - **調査へのポインタ** — one line per `research/<topic>.md` saying what it establishes. Where the 調査日 is roughly more than three months old, mark it `要再確認`. Terms, limits and prices move, and an unmarked stale note is read as current.
2. **Set the idea's row in the `## 一覧` table of `docs/plan/README.md` to `実装へ`.** An index out of step with reality breaks the next session's starting point.
3. **Make no new decisions while writing.** A gap found during the write goes into 決まっていないこと, and tell the owner it is there. A decision taken at handoff time never went through the discussion the rest of them went through, and it arrives in the product repository looking equally settled.

## Output

`docs/plan/<idea-slug>/handoff.md`, and the state cell updated in `docs/plan/README.md`. Nothing at the repository root and nothing that runs; this repository graduates a document, not a codebase.

## Rules that are easy to get wrong

- Do not fill a gap with a plausible answer because the handoff looks incomplete with a hole in it. The hole is the accurate report.
- Do not rewrite past entries in `decisions.md` while selecting from them. That file is append-only, and this step only reads it.
- Do not re-date research to today because it was re-read today. `要再確認` is decided by the recorded 調査日.
- Keep 決まっていないこと explicit about who decides. "Undecided" and "the product repository decides this" are read very differently by the receiving session.
