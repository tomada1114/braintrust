# Tier checks and comparison axes

Criteria only. No vendor names, no model names, no prices, no free-tier figures — those
age, and a figure frozen into a reference gets used long after it stopped being true.
Take the values from the dated files under `docs/landscape/` and from
`docs/plan/<idea-slug>/research/`.

## Step 0 — Is an LLM needed at all

Three questions. If any one of them points at "not needed", say so out loud rather than
letting the assumption stand.

- **Can it be written as rules?** A fixed, enumerable mapping from input to output is
  cheaper, faster and testable, and it does not drift between runs.
- **Is search, or an existing non-LLM API, enough?** Retrieval and a purpose-built API
  return the same answer every time and can be checked against a source.
- **Does variation in the output do harm?** Where every run must agree — totals,
  identifiers, anything a later step compares — variation is a defect, not a feature.

A "no LLM needed" verdict here is a real outcome of this skill, not a failure to design.

## Step 1 — What shape

- **Single call** — input to output closes in one round trip.
- **Fixed workflow** — the steps can be enumerated in advance, so write them down and
  call the model at the points that need it.
- **Agent** — the path cannot be enumerated in advance.

An agent only when **all four** hold. Any one missing and a fixed workflow does the same
job for less money, less latency and far less debugging:

1. **Complexity** — the path genuinely cannot be listed ahead of time. If it can, it is a workflow.
2. **Value** — the task is worth the tokens and the wait it will cost.
3. **Feasibility** — the loop can actually be walked with the models and tools available now,
   not with ones that would have to exist.
4. **Cost of error** — a wrong step is recoverable. Where a wrong step is not recoverable,
   the loop needs a human in it, which makes it a workflow with an approval point.

## Step 2 — The minimum set of calls

1. List the model calls the first version strictly requires.
2. Argue against each one with a cheaper alternative: batch several into one call, move it
   after the fact into a single review call, or do it without a model at all.
3. What survives that argument is the first version. Everything else is a later version.

The point of the argument is that per-event calls are the default people reach for and
almost never the minimum. A per-turn call and one call at the end of a session often
produce the same value to the user at very different cost.

## Comparison axes

Do not run all eight every time. Pick the ones that actually move this decision; axes that
cannot change the answer only crowd the table.

| Axis | What to look at | Why it bites |
|---|---|---|
| Billing (課金) | How usage is charged, and what happens at the ceiling | Sets the running cost, and whether the app can be given away |
| Free-tier disclosure (無料枠と上限の公開状況) | Whether the limits are published as terms, or only described loosely | An undisclosed limit cannot be designed against and can move without notice |
| Data use (データ利用) | Whether inputs are used for training, and whether humans review them | Decides what content the app may send at all |
| Auth and subscription reuse (認証とサブスク転用) | What credential is required, and whether an existing subscription can be used instead of usage billing | Changes who pays and what each user must set up before first use |
| Structured output (構造化出力) | Whether schema-constrained output is supported, and what happens when it fails | Free-text output that has to be parsed becomes the app's most fragile seam |
| SDK and language (SDK と言語) | Which languages have a maintained SDK, and what the alternative is | Has to match the stack chosen in `experience.md`, or the stack changes |
| Lock-in (ロックイン) | How much would have to be rewritten to switch | Sets how reversible this decision is, which is what makes it safe to make early |
| 応答速度 (latency) | Time to first token and total time for the call shape the app uses, and whether the vendor publishes it | For an interactive single-call app the wait is the experience, and a published figure is rarely the figure in production, so it usually ends as "measure at implementation" |
| Reasoning effort (推論強度) | How much latency and quality change between the model's effort levels (low/medium/high, or equivalent) | The shape of this trade-off is not uniform across vendors — some models lose almost no latency going from high to medium, others lose almost no quality. Check the per-model table in `docs/landscape/` rather than assuming a pattern from one vendor generalizes to another |

Values for every axis come from `docs/landscape/` and `docs/plan/<idea-slug>/research/`.
Where neither has the value, that is a research question for `recording-research`, not
something to assert from memory.
