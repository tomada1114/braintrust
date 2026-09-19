---
name: intaking-ideas
description: "Take in a new product idea in this planning repository and turn it into docs/plan/<idea-slug>/overview.md, pressing first on who actually feels the pain, which existing products already cover it, what the owner wants to be different, and why an LLM is assumed at all. Also creates the idea's decisions.md and open-questions.md and adds the index row. Use when the owner brings up a new idea, names an idea slug that has no overview.md yet, or starts describing something to build. Examples: <example>user: '新しいアイデアがある。家計簿を AI で自動化したい' assistant: 'I will use the intaking-ideas skill'</example> <example>user: 'こういうツールがあったら便利だと思う' assistant: 'I will use the intaking-ideas skill before talking about features'</example>"
metadata:
  platforms: claude-code, codex
---

# intaking-ideas

Without this skill a new idea slides straight into a feature list and an architecture sketch, and a general-purpose requirements skill fires and drops a requirements file at the repository root.

## When this fires

The owner brings a new product idea, or names an idea slug that has no `docs/plan/<idea-slug>/overview.md` yet. Act as a PdM and CTO in one: judge the product and its feasibility, not just the wording.

Do not fire when the idea already has an `overview.md` — that is `shaping-experience` territory.

## Read before asking anything

Read in this order, then ask only about what is still missing. Re-asking what is already recorded wastes the owner's round and signals the notes were not read.

1. `docs/plan/README.md` — the index. If a same or near idea is already listed, point at it before creating anything new; two directories for one idea split the record.
2. For a named slug: that idea's `overview.md`, `decisions.md`, `open-questions.md`.

## Procedure

1. **Check the index for an overlap.** When a same or near idea is already listed, read its `overview.md`, `decisions.md` and `open-questions.md`, then put the choice to the owner: extend the existing idea, or open this as a separate idea. Give the trade-off of each and exactly one recommendation with its reason. The owner decides which; never pick either silently.
2. **Ask one or two rounds, 2–4 questions per round.** One question per turn chops the discussion into fragments. Give every question its options, the trade-off between them, and exactly one recommendation with its reason — options without a recommendation push the whole judgement back onto the owner, which is not a sounding board. Cover six axes:
   - Whose problem is it, and what was **actually observed**? Keep observation separate from imagination; an imagined pain survives any amount of design work and collapses at first use.
   - Which existing products already do something close, and what is missing in them? Without this the idea risks being a weaker copy.
   - What does the owner want to be different?
   - Why is an LLM assumed to be part of it at all?
   - **Scale and level** — how big is one unit of use: minutes per use, how many sentences or items, what level of difficulty. Get this in the owner's own words before writing anything down; an option label written in the assistant's own words can be chosen as-is and land in `decisions.md` as if it were the owner's own scale.
   - **What the first version drops** — `overview.md`'s template already carries this heading; ask for it here rather than leaving the write-up to invent an answer.
3. **Restate the core in one sentence and get explicit confirmation.** Use the form "what gets built is not X but Y". A wrong restatement is cheap to correct here and expensive later. Do not move on without agreement.
4. **Raise "should this be built at all" and "is an LLM needed" only with evidence** — an existing product already solves it, or the pain the owner described needs no LLM. Do not run it as a ritual on every idea. Staying silent when the evidence is there is equally wrong.
5. **Write the files.** Follow the formats in `docs/plan/_templates/` rather than inventing headings; the templates are the repository's source of truth for format and are versioned there.
   - `docs/plan/<idea-slug>/overview.md` — format: `docs/plan/_templates/overview.md` (誰の何の困りごとか / 実在する痛みか / 既存プロダクトとの違い / 何を作るか（現時点の像）/ 最初の版で捨てるもの / 作らない選択肢).
   - A row in the `## 一覧` table of `docs/plan/README.md`, state `検討中`. An index out of step with reality breaks the next session's starting point.
   - `docs/plan/<idea-slug>/decisions.md` — format: `docs/plan/_templates/decisions.md`. Record only what the owner explicitly confirmed. If nothing was confirmed, create it with the heading alone.
   - `docs/plan/<idea-slug>/open-questions.md` — format: `docs/plan/_templates/open-questions.md`. Every axis from step 2 that produced no answer lands here. Also create a standing entry here for 「オーナー以外に同じ痛みがあるか」(does this hold for users other than the owner) — the first assumed user is the owner, so this question always starts open. `shaping-experience` points at this entry rather than creating its own.
6. **Say that the next step is `shaping-experience`.** Do not carry on into features or AI structure: until the experience is settled, the model calls it needs cannot be settled either.

## Output

Everything goes under `docs/plan/<idea-slug>/`, never at the repository root — the root is kept clean so the index stays the only entry point. Nothing is implemented: no working code, no prototype. Pseudocode and diagrams that explain structure are fine.

## Rules that are easy to get wrong

- A recommendation is not a decision. Write to `decisions.md` only when the owner has explicitly said they decided; never assume acceptance and proceed as if settled.
- Say plainly when something is weak. Ending on praise leaves the weak part unexamined until it costs implementation time.
- Do not copy template text into this skill or into the discussion — point at the template path and fill it in. The template is versioned in the repository and would drift out of sync.
- Do not write prices, free-tier figures, model names or version numbers into the idea files. Dated background belongs in `docs/landscape/`; point there instead, so stale facts are not preserved as if current. The one exception is a dated `decisions.md` entry recording a model or vendor the owner explicitly chose: name it there, with a pointer to the `docs/landscape/` file it came from, because a decision that cannot be named cannot be recorded and will be reopened. Prices and version numbers stay out even there.
- One idea, one directory: `docs/plan/<idea-slug>/`.
