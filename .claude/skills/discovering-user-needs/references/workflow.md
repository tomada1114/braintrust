# The user-needs sweep workflow

The script below is the whole sweep. Pass it to the Workflow tool inline as `script`, with
`args` filled as described here. Run it only after the owner has agreed to the scope — the
agreement is what authorises the run, and the run is the expensive part.

## Contents

- [What the main session fills into `args`](#what-the-main-session-fills-into-args)
- [Shape](#shape)
- [The script](#the-script)
- [What comes back](#what-comes-back)

## What the main session fills into `args`

```json
{
  "ideaSlug": "small-talk-trainer",
  "today": "2026-09-07",
  "skillDir": "<the expansion of ${CLAUDE_SKILL_DIR} for this skill>",
  "ideaSummary": "2-4 sentences from overview.md: who, the situation, the pain, the current alternative.",
  "hypotheses": [
    {
      "id": "H1",
      "who": "who is supposed to feel it",
      "situation": "when it happens",
      "pain": "what hurts",
      "workaround": "what they do about it today",
      "refutedBy": "what a voice would have to say for this hypothesis to be wrong"
    }
  ],
  "cells": [
    {
      "modality": "App Store / Google Play reviews",
      "segment": "users of <adjacent product>",
      "language": "ja",
      "queries": ["…", "…"]
    }
  ]
}
```

`hypotheses` and `cells` are the main session's work, not the workers'. Derive the
hypotheses from `overview.md` and `experience.md`, and write the queries yourself: a worker
handed "go find users" invents its own scope and comes back with something adjacent to the
question. Every cell is one modality × one segment × one language; the segment label travels
with every voice the cell returns, so name the adjacent product in it rather than writing
"users".

`today` is passed in because the script cannot call `new Date()` and a worker asked to work
out the date guesses, which silently corrupts every source date in the result.

## Shape

Six collect cells at most, each pipelined straight into its own extract stage, then one
barrier before synthesis. That is 6 + 6 + 1 + 1 = 14 agents, inside the ~15 cap. Cells past
the sixth are dropped and named in the run log — pick the six that cover the most distinct
modalities and both languages before handing them over, rather than letting the cap choose.

Collect and extract are pipelined, not barriered: extraction of one cell needs only that
cell. Synthesis is the first stage that genuinely needs everything at once, because
clustering and the distinct-source counts are cross-cell by definition.

The critic runs last and its output comes back to the main session. A second round is a new
Workflow call the owner agrees to, never a loop inside this script.

## The script

```js
export const meta = {
  name: 'user-needs-sweep',
  description: 'Desk-research sweep of public voices for one idea, returning a needs map judged against the owner hypotheses',
  phases: [
    { title: 'Collect', detail: 'one agent per modality x segment x language cell, verbatim voices with URL and date', model: 'sonnet' },
    { title: 'Extract', detail: 'turn each voice into a structured need record', model: 'sonnet' },
    { title: 'Synthesize', detail: 'cluster into a needs map and judge every hypothesis', model: 'opus' },
    { title: 'Critic', detail: 'name what the sweep is missing', model: 'sonnet' },
  ],
}

const CELL_CAP = 6
const requested = args.cells || []
const cells = requested.slice(0, CELL_CAP)
if (requested.length > CELL_CAP) {
  const dropped = requested.slice(CELL_CAP).map(c => `${c.modality}/${c.segment}/${c.language}`)
  log(`cell cap ${CELL_CAP} reached; NOT run: ${dropped.join(' | ')}`)
}
log(`${cells.length} cells, ${args.hypotheses.length} hypotheses, idea ${args.ideaSlug}`)

const VOICE_PROPS = {
  quote: { type: 'string' },
  url: { type: 'string' },
  sourceDate: { type: 'string' },
  language: { type: 'string' },
  sourceType: { type: 'string' },
  segment: { type: 'string' },
  confidence: { type: 'string' },
}

const COLLECT_SCHEMA = {
  type: 'object',
  properties: {
    cell: { type: 'string' },
    queriesRun: { type: 'array', items: { type: 'string' } },
    voices: {
      type: 'array',
      items: {
        type: 'object',
        properties: Object.assign({}, VOICE_PROPS, {
          bearsOn: { type: 'array', items: { type: 'string' } },
        }),
        required: ['quote', 'url', 'sourceDate', 'language', 'sourceType', 'segment', 'confidence', 'bearsOn'],
      },
    },
    notFound: { type: 'string' },
  },
  required: ['cell', 'queriesRun', 'voices', 'notFound'],
}

const EXTRACT_SCHEMA = {
  type: 'object',
  properties: {
    cell: { type: 'string' },
    needs: {
      type: 'array',
      items: {
        type: 'object',
        properties: Object.assign({}, VOICE_PROPS, {
          situation: { type: 'string' },
          pain: { type: 'string' },
          workaround: { type: 'string' },
          desiredOutcome: { type: 'string' },
          intensitySignal: { type: 'string' },
          supports: { type: 'array', items: { type: 'string' } },
          refutes: { type: 'array', items: { type: 'string' } },
        }),
        required: ['quote', 'url', 'sourceDate', 'language', 'sourceType', 'segment', 'confidence',
          'situation', 'pain', 'workaround', 'desiredOutcome', 'intensitySignal', 'supports', 'refutes'],
      },
    },
    dropped: { type: 'string' },
  },
  required: ['cell', 'needs', 'dropped'],
}

const SYNTH_SCHEMA = {
  type: 'object',
  properties: {
    clusters: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          name: { type: 'string' },
          situation: { type: 'string' },
          pain: { type: 'string' },
          workaround: { type: 'string' },
          desiredOutcome: { type: 'string' },
          intensityEvidence: { type: 'string' },
          distinctSourceCount: { type: 'number' },
          segments: { type: 'array', items: { type: 'string' } },
          representativeQuotes: {
            type: 'array',
            items: { type: 'object', properties: VOICE_PROPS, required: Object.keys(VOICE_PROPS) },
          },
          ownerMentioned: { type: 'boolean' },
        },
        required: ['name', 'situation', 'pain', 'workaround', 'desiredOutcome', 'intensityEvidence',
          'distinctSourceCount', 'segments', 'representativeQuotes', 'ownerMentioned'],
      },
    },
    hypothesisVerdicts: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          verdict: { type: 'string' },
          evidence: { type: 'string' },
          counterEvidence: { type: 'string' },
          distinctSourceCount: { type: 'number' },
        },
        required: ['id', 'verdict', 'evidence', 'counterEvidence', 'distinctSourceCount'],
      },
    },
    contradictions: { type: 'array', items: { type: 'string' } },
    needsOwnerDidNotMention: { type: 'array', items: { type: 'string' } },
    languageBalance: { type: 'string' },
  },
  required: ['clusters', 'hypothesisVerdicts', 'contradictions', 'needsOwnerDidNotMention', 'languageBalance'],
}

const CRITIC_SCHEMA = {
  type: 'object',
  properties: {
    gaps: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          kind: { type: 'string' },
          detail: { type: 'string' },
          suggestedCell: { type: 'string' },
        },
        required: ['kind', 'detail', 'suggestedCell'],
      },
    },
    quotesWithoutProvenance: { type: 'array', items: { type: 'string' } },
    hypothesesWithNoEvidence: { type: 'array', items: { type: 'string' } },
    languageSkew: { type: 'string' },
    secondRoundWorthIt: { type: 'string' },
  },
  required: ['gaps', 'quotesWithoutProvenance', 'hypothesesWithNoEvidence', 'languageSkew', 'secondRoundWorthIt'],
}

const cellId = (cell, i) => `C${i + 1} ${cell.modality} / ${cell.segment} / ${cell.language}`

const collectPrompt = (cell, i) => [
  '<instructions>',
  `Read ${args.skillDir}/references/agents/collect.md in full before anything else. It is your brief; follow it.`,
  '</instructions>',
  '<intent>',
  `The main session is testing whether the pain behind the idea "${args.ideaSlug}" exists for people other than its owner.`,
  'Your verbatim voices are the only evidence the later stages ever see, so a paraphrase here becomes an invented user downstream.',
  '</intent>',
  '<context>',
  `Today: ${args.today}`,
  `The idea: ${args.ideaSummary}`,
  `Hypotheses under test: ${JSON.stringify(args.hypotheses)}`,
  '</context>',
  '<input>',
  `Your cell: ${cellId(cell, i)}`,
  `Modality: ${cell.modality}`,
  `Segment: ${cell.segment}`,
  `Language to search and quote in: ${cell.language}`,
  `Queries: ${JSON.stringify(cell.queries)}`,
  'Run every query. Vary the wording where a query returns nothing, but stay inside this cell’s modality, segment and language.',
  '</input>',
].join('\n')

const extractPrompt = (cell, i, collected) => [
  '<instructions>',
  `Read ${args.skillDir}/references/agents/extract.md in full before anything else. It is your brief; follow it.`,
  '</instructions>',
  '<intent>',
  `The clustering stage sees only your records, so what you leave out of them leaves the sweep for good.`,
  '</intent>',
  '<context>',
  `The idea: ${args.ideaSummary}`,
  `Hypotheses, with the id to use in supports/refutes: ${JSON.stringify(args.hypotheses)}`,
  '</context>',
  '<input>',
  `Cell: ${cellId(cell, i)}`,
  `Voices collected in this cell: ${JSON.stringify(collected.voices)}`,
  `The collector reported this as not found: ${collected.notFound}`,
  '</input>',
].join('\n')

const synthesizePrompt = (records, ranCells) => [
  '<instructions>',
  `Read ${args.skillDir}/references/agents/synthesize.md in full before anything else. It is your brief; follow it.`,
  '</instructions>',
  '<intent>',
  `The main session will transcribe your map into docs/plan/${args.ideaSlug}/research/user-needs/ and then ask the owner which parts of overview.md and experience.md it changes.`,
  'The owner makes that call, so the map has to carry the evidence and stop short of advising.',
  '</intent>',
  '<context>',
  `The idea, as its owner describes it: ${args.ideaSummary}`,
  `Hypotheses under test: ${JSON.stringify(args.hypotheses)}`,
  `Cells that were actually run: ${JSON.stringify(ranCells.map((c, i) => cellId(c, i)))}`,
  '</context>',
  '<input>',
  `All need records from the sweep (${records.length}): ${JSON.stringify(records)}`,
  '</input>',
].join('\n')

const criticPrompt = (map, records, ranCells, droppedCells) => [
  '<instructions>',
  `Read ${args.skillDir}/references/agents/critic.md in full before anything else. It is your brief; follow it.`,
  '</instructions>',
  '<intent>',
  'The main session uses your list to decide whether to ask the owner for a second round. A gap you do not name is one nobody closes.',
  '</intent>',
  '<context>',
  `Hypotheses under test: ${JSON.stringify(args.hypotheses)}`,
  `Cells run: ${JSON.stringify(ranCells.map((c, i) => cellId(c, i)))}`,
  `Cells requested but dropped by the cap: ${JSON.stringify(droppedCells)}`,
  '</context>',
  '<input>',
  `The needs map: ${JSON.stringify(map)}`,
  `Provenance of every record behind it: ${JSON.stringify(records.map(r => ({ url: r.url, sourceDate: r.sourceDate, language: r.language, sourceType: r.sourceType, segment: r.segment, confidence: r.confidence })))}`,
  '</input>',
].join('\n')

phase('Collect')
const perCell = await pipeline(
  cells,
  (cell, _item, i) => agent(collectPrompt(cell, i), {
    label: `collect ${cell.modality} / ${cell.language}`,
    phase: 'Collect',
    schema: COLLECT_SCHEMA,
    model: 'sonnet',
    effort: 'low',
  }),
  (collected, cell, i) => collected
    ? agent(extractPrompt(cell, i, collected), {
        label: `extract ${cell.modality} / ${cell.language}`,
        phase: 'Extract',
        schema: EXTRACT_SCHEMA,
        model: 'sonnet',
        effort: 'medium',
      })
    : null,
)

const done = perCell.filter(Boolean)
const records = done.flatMap(r => r.needs || [])
log(`${records.length} need records from ${done.length}/${cells.length} cells`)
if (done.length < cells.length) log(`${cells.length - done.length} cell(s) returned nothing; the map is built without them`)

phase('Synthesize')
const needsMap = await agent(synthesizePrompt(records, cells), {
  label: 'cluster and judge hypotheses',
  phase: 'Synthesize',
  schema: SYNTH_SCHEMA,
  model: 'opus',
  effort: 'high',
})

phase('Critic')
const droppedCells = requested.slice(CELL_CAP).map(c => `${c.modality}/${c.segment}/${c.language}`)
const critique = needsMap
  ? await agent(criticPrompt(needsMap, records, cells, droppedCells), {
      label: 'what is missing',
      phase: 'Critic',
      schema: CRITIC_SCHEMA,
      model: 'sonnet',
      effort: 'medium',
    })
  : null

return {
  ideaSlug: args.ideaSlug,
  today: args.today,
  cellsRun: cells.map((c, i) => cellId(c, i)),
  cellsDropped: droppedCells,
  recordCount: records.length,
  records,
  needsMap,
  critique,
}
```

## What comes back

`needsMap.clusters` with their distinct-source counts and verbatim quotes, `needsMap.hypothesisVerdicts`,
`needsMap.contradictions`, `needsMap.needsOwnerDidNotMention`, the flat `records` behind all of it,
and `critique`. `cellsDropped` is non-empty whenever the cap bit.

The clusters and verdicts are not yet usable: the main session opens at least one source per
major cluster and confirms the quote is on the page before any of it reaches a file.
