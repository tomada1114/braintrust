---
name: assessing-ai-architecture
description: "Work out whether an LLM is needed at all and, if it is, whether the shape is a single call, a fixed workflow, or an agent; enumerate the model calls the first version strictly requires; and compare vendors on billing, free-tier disclosure, data use, auth, structured output, SDK and lock-in. Reads the dated notes under docs/landscape/ first and says so when the newest one is stale. Use when the owner names an SDK or agent framework, asks how to structure the AI part, asks which vendor to pick, or asks what the first version can drop. Examples: <example>user: 'このアプリは Agent SDK で作りたい' assistant: 'I will use the assessing-ai-architecture skill'</example>"
metadata:
  platforms: claude-code, codex
---

# assessing-ai-architecture

Without this skill, the moment the owner names an SDK the whole discussion assumes an agent, and the two checks that decide the cost of the app — whether an LLM is needed at all, and what the minimum set of calls is — get skipped.

## When this fires

Deciding whether an LLM is needed; choosing between a single call, a fixed workflow and an agent; comparing vendors on billing, auth, data handling; deciding what the first version drops. It comes after the experience is settled — until the experience is fixed, the model calls it needs cannot be.

## Read before asking anything

1. The newest dated file under `docs/landscape/`. If the newest is roughly more than three months old, say so and offer to refresh it through `recording-research` before relying on it. Do not treat it as current merely because it is the newest thing present. If the directory holds no background notes, proceed on the basis that there are none rather than filling the gap from memory.
2. The idea's `experience.md`, `decisions.md`, `open-questions.md` and `research/`.

## Procedure

1. **Run the tier checks** in [references/tiers.md](references/tiers.md). Step 0: can rules, search or an existing non-LLM API do it? If so, say the LLM is not needed. Step 1: single call, fixed workflow, or agent — judged on complexity, value, feasibility and cost of error. **An agent only when all four hold**; any one missing and a fixed workflow does the same job for less money and less debugging.
2. **Enumerate the model calls the first version strictly requires, and argue against anything beyond them** (Step 2 of the same reference). Per-event calls are the default reach and almost never the minimum — a call on every turn and one review call after the session often give the user the same thing at very different cost.
3. **Compare on the axes that matter** — the seven are defined in [references/tiers.md](references/tiers.md). Use only the ones that can change this decision; the rest just fill the table. Take every value from `docs/landscape/` and the idea's `research/`. Where the value is not recorded, treat it as a question for `recording-research`, and do not assert it from memory: figures and terms move, and a wrong one asserted here becomes a premise nobody re-checks.
4. **Lay out the options with their trade-offs and add exactly one recommendation with its reason.** Options handed over without a recommendation put the whole judgement back on the owner, which is not a sounding board.
5. **Record.** Only what the owner explicitly decided goes into the idea's `decisions.md`, with the reason and the rejected options and why they were rejected — without the rejection reasons the same option returns later. Everything still open goes to `open-questions.md`. Both follow `docs/plan/_templates/`; point at the templates rather than copying them.

## Output

Updates to `docs/plan/<idea-slug>/decisions.md` and `open-questions.md`, and research requests handed to `recording-research`. Nothing is implemented and nothing lands at the repository root. Pseudocode and diagrams that explain the call structure are fine.

## Rules that are easy to get wrong

- Naming an SDK is not a decision to use it. Run Step 0 anyway; the owner naming a tool is evidence of familiarity, not of need.
- A recommendation is not a decision. Only an explicit statement from the owner makes it one.
- Do not write prices, free-tier figures, model names or versions into this skill, into `references/tiers.md`, or into any file that is not dated. Values age; the dated files carry them.
- Do not settle the experience here. If the core loop turns out to be unsettled, hand it back to `shaping-experience` — deciding the call structure over an undecided experience just gets redone.
- Say when the background notes are stale rather than quietly using them. An unstated staleness becomes a hidden premise.
