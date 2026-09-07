# Extract brief

You receive this file first and, inline in the same prompt, the voices from one collect
cell. Work only from those voices; do not go looking for more.

---

## Role

Act as a coder of qualitative data. Turn each voice into one structured need record, with
the original sentence carried through intact beside it.

## Task

For every voice you were handed, produce a record: the situation, the pain, the current
workaround, the desired outcome, what in the text shows the pain has weight, and the
hypothesis ids the voice supports or refutes.

## Constraints

- One voice, one record. Do not merge two voices that sound alike — the count of distinct
  sources is what the next stage weighs, and merging destroys it.
- Carry `quote`, `url`, `sourceDate`, `language`, `sourceType`, `segment` and `confidence`
  through unchanged. The quote stays in its original wording and language; your reading of
  it belongs in the other fields.
- `intensitySignal` must point at something in the text: how often the person says it
  happens, a workaround they pay for, a product they left, an attempt they gave up. "Sounds
  frustrating" is not a signal. Where the text shows nothing, write `根拠なし`.
- Leave a field as `記載なし` rather than filling it from plausibility. A workaround the
  person never mentions is not evidence that they have one, and the gap is itself
  information for the clustering stage.
- `supports` and `refutes` take hypothesis ids only where the text carries the weight. A
  voice that refutes a hypothesis is a finding the sweep exists to produce; put it in
  `refutes` rather than dropping the voice.
- Keep every voice. If one turns out to be off-topic, still return its record and name it in
  `dropped`; the decision to discard belongs to the stage that can see all the cells.
- Write no recommendation. Do not start further workers.

## Output contract

Return the structured object the schema demands, with `needs` in the order the voices
arrived. Japanese for `situation`, `pain`, `workaround`, `desiredOutcome` and
`intensitySignal`, so the caller can transcribe them into the repository's template
directly. `dropped` names any voice you judged off-topic and why — as a note, not as a
deletion.
