---
name: shaping-experience
description: "Shape what the app actually has to be like to be worth using, and write docs/plan/<idea-slug>/experience.md: the usage scene, the core loop, what would count as useful against the current alternative, how far the first version's experience goes, and a feasibility pass that names the hard parts and offers coarse tech-stack candidates with trade-offs and one recommendation. Stays at concept level, never screens, colours or tokens, and leaves the AI call design and the vendor choice to assessing-ai-architecture. Use right after an idea is taken in, or when the owner asks about usability, user needs, the core experience, feasibility, or which stack to build on. Examples: <example>user: 'small-talk-trainer の使い勝手を詰めたい' assistant: 'I will use the shaping-experience skill'</example>"
metadata:
  platforms: claude-code, codex
---

# shaping-experience

Without this skill the conversation jumps from the idea to the AI structure, so whether the thing is useful as an app is never examined, and the stack gets picked by name — "I want to build it in X" passes unchallenged.

## When this fires

Right after `intaking-ideas`, once `overview.md` exists, and before `assessing-ai-architecture`. Also whenever the owner asks about usability, user needs, the core experience, feasibility, or which stack to build on.

Act as a PdM and CTO in one: give both the product judgement and the feasibility judgement in the same round, because a desirable experience that cannot be built is not a plan.

## Read before asking anything

Read the idea's `overview.md`, `decisions.md`, `open-questions.md` and `research/` first, then ask only about what is still open. Do not re-ask anything already recorded.

## Procedure

1. **Ask one or two rounds, 2–4 questions per round.** Each question carries options, the trade-off, and exactly one recommendation with its reason. Four axes:
   - **Usage scene** — when, where, and in what state is the user? How many minutes per use? What starts a session and what ends it? A core loop that has no moment in the day to happen in never gets used.
   - **Core loop** — the user does X, Y comes back, and what is left behind afterwards.
   - **What counts as useful** — against the current alternative, what gets easier? And, deliberately, what would do no harm by being absent?
   - **How far the first version's experience goes** — what is in, and what is dropped.
2. **Run the feasibility pass.** Name the hard parts explicitly, in three kinds: technical, content, and operational. Content and operational difficulty are missed far more often than technical difficulty, and they sink more ideas.
3. **Offer coarse tech-stack candidates**, at the granularity of: shape of execution (CLI / local server plus browser / mobile and the like), language, where data is stored, and how the UI is built. Choose between them on four axes — the owner's familiarity, how it gets distributed, cost, and how well it fits the AI side. Lay out options and trade-offs, then one recommendation with its reason. Do **not** settle the AI call design or the vendor here: hand those to `assessing-ai-architecture`, because deciding the vendor before the experience puts the means ahead of the end and leaves two skills writing the same decision.
4. **Stop at concept level.** Do not go into screens, colour or tokens. If the owner asks for that, say the global `designing-wireframes` and `ui-ux-designing` skills cover it, and that whatever they produce belongs under `docs/plan/<idea-slug>/`. Implementation artifacts such as a token stylesheet are not placed in this repository at all — this repository keeps research notes and the record of decisions, nothing that runs.
5. **Write the files.**
   - `docs/plan/<idea-slug>/experience.md` — format: `docs/plan/_templates/experience.md` (利用場面 / 中核の体験 / 便利さの定義 / 最初の版で成立させる体験 / 実現性 / 想定ユーザーの広がり). Follow the template rather than inventing headings; it is versioned in the repository.
   - Append to the idea's `decisions.md` only what the owner explicitly decided, with the reason and the rejected options and why they were rejected. Without the rejection reasons the same option comes back later.
   - Everything else goes to `open-questions.md`. **Always leave "does this hold for users other than the owner" open there.** The first assumed user is the owner, whose own observation is primary evidence; whether it generalises is a separate question and stays separate.

## Output

`docs/plan/<idea-slug>/experience.md`, plus updates to that idea's `decisions.md` and `open-questions.md`. Nothing at the repository root, no running code, no prototype. Pseudocode and diagrams are fine.

## Rules that are easy to get wrong

- A recommendation is not a decision. Only an explicit statement from the owner makes it one; do not proceed as if a recommendation had been accepted.
- Say which parts are weak. Praise that ends the review leaves the weak part in place.
- Do not paste template text here or into the answer — point at the template path.
- Do not write prices, free-tier figures, model names or versions into the files. Dated background lives in `docs/landscape/`; point at it so stale facts are not frozen into the plan.
- Vendor, billing and data-handling comparisons are not this skill's job even when the owner raises them mid-feasibility. Note them and pass them on.
