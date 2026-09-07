---
name: discovering-user-needs
description: "Sweep public voices — app-store reviews of adjacent products, Reddit and forums, X, Q&A sites, blogs, GitHub issues — in Japanese and English, and write docs/plan/<idea-slug>/research/user-needs/<topic>.md: needs clustered with verbatim quotes carrying URL, source date and confidence, a verdict on each of the owner's pain hypotheses, and the needs the owner never mentioned. Desk research only, no interviews and no simulated personas; the scope is proposed and agreed before the sweep runs. Use when an idea rests on the owner's own pain and it is unclear whether anyone else feels it, when open-questions.md still carries the question of whether it holds for users other than the owner, or when the owner asks who else wants this. Examples: <example>user: 'この困りごと、自分以外にもあるのか調べたい' assistant: 'I will use the discovering-user-needs skill'</example>"
metadata:
  platforms: claude-code
---

# discovering-user-needs

Without this skill the session treats the owner's own observation as the whole market, or fills the gap with plausible users nobody ever wrote a word.

## When this fires

The idea rests on the owner's own pain and whether anyone else feels it is unsettled — the standing question `shaping-experience` always leaves open in `open-questions.md`. Also when the owner asks who else wants this, whether the pain is common enough to matter, or what needs they themselves have not yet put into words — other people's voices are where an owner's hidden needs tend to surface.

It feeds `intaking-ideas` and `shaping-experience`; it never writes `overview.md` or `experience.md` itself. The result is put to the owner as options, and the owner decides what changes.

This is comparison-class research. The sweep is expensive, so the scope is proposed and agreed before it runs.

## Read before asking anything

1. `docs/plan/README.md` — the index, for the idea's state.
2. The idea's `overview.md` (誰の何の困りごとか / 実在する痛みか), `experience.md` (想定ユーザーの広がり), `decisions.md`, `open-questions.md`.
3. Everything already under the idea's `research/`, including `research/user-needs/`. A sweep already recorded there needs re-running only if its 調査日 is old or the segments were different — say which, rather than starting a fresh one over the top.

## Procedure

1. **Frame, then wait.** Derive 2–5 pain hypotheses from `overview.md` and `experience.md` — each with who feels it, in what situation, what hurts, what they do about it today, and what a voice would have to say for the hypothesis to be wrong. Then propose the sweep: target segments, which source modalities, which languages, how many agents and on which models. Ask 2–4 questions in one round, each with its options, the trade-off and exactly one recommendation with its reason. **Wait for the owner's agreement** — it is what authorises the Workflow run and the money it costs.
2. **Run the sweep.** Follow [references/workflow.md](references/workflow.md): pass the script to the Workflow tool with `args` = `{ideaSlug, today, skillDir, ideaSummary, hypotheses, cells}`. Write the hypotheses and the per-cell queries yourself. A worker handed "go find users" invents its own scope and returns something adjacent to the question; the orienting work belongs here, where the whole idea is in context. Search both Japanese and English unless the agreed scope says otherwise.
3. **Verify in this session.** Open at least one source per major cluster and find the quote on the page. A quote you cannot locate is marked `未確認` and never carries a hypothesis verdict. The workers' quotes are one copy away from the page, and that is exactly where a verbatim voice turns into a paraphrase.
4. **Write `docs/plan/<idea-slug>/research/user-needs/<topic>.md`** — one question per file, in the format of `docs/plan/_templates/user-needs.md` (調査日 / 調査手段 / 問い / 対象セグメント / 情報源, then 仮説と判定 / ニーズ一覧 / オーナーの観察との突き合わせ / グレーゾーン・未確認 / 影響する論点). Point at the template rather than copying it; it is versioned in the repository. Every voice keeps its URL, source date, language, source type, segment and confidence (`高` / `中` / `低`), and the gray-zone section carries what the critic found.
5. **Report the critic's gaps and let the owner choose.** A second round is a new Workflow call the owner agrees to, with the cells named. Never start one silently on the way to a tidier map.
6. **Link it back and put the choice to the owner.** Name the file by relative path in the 材料 line of every `open-questions.md` question it bears on, starting with the "does this hold for users other than the owner" one. Then say which sections of `overview.md` (誰の何の困りごとか / 実在する痛みか) and `experience.md` (想定ユーザーの広がり) the result bears on, lay out the options — widen the target, narrow it, drop a hypothesis, leave it as it stands — with trade-offs and exactly one recommendation. Append to `decisions.md` only after the owner has explicitly decided, with the reason and the rejected options and why they were rejected.

## Output

`docs/plan/<idea-slug>/research/user-needs/<topic>.md`, plus the 材料 lines updated in that idea's `open-questions.md`. Nothing at the repository root. Voices and their sources only — the decision is the owner's and goes to `decisions.md`.

## Rules that are easy to get wrong

- Agent count is not evidence count. Six workers that all surfaced the same thread found one source. Report `出典数`, counted over distinct pages and authors, and never write "N 人のユーザーが".
- A paraphrase is not a quote. If the sentence in the file is not the sentence on the page, the file is reporting an invented user in a real user's clothes.
- A review of an adjacent product is evidence about that product's users. Keep the segment label attached all the way into the file; the moment it drops off, borrowed evidence reads as evidence about this idea.
- Refutation is the sweep working. A hypothesis that comes back `反証` is worth more than the run cost, and it goes into the file with the same weight as a supported one.
- Do not let the workers decide what matters. They report everything with a confidence; the filtering happens in the synthesis stage, which can see all the cells at once.
- No interviews, no surveys, no simulated users. Nothing goes into the file that a person did not write in public, on a page that can be opened.
- A recommendation is not a decision, and this skill does not edit `overview.md` or `experience.md`. It proposes; the owner decides.
