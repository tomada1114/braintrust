# The competitor-survey Workflow

One script, two modes. `args.mode: 'discover'` runs only the candidate sweep, so the owner can
confirm the product list before the expensive run. `args.mode: 'survey'` (the default) runs the
survey over the products the owner agreed to.

Pass the script to the Workflow tool inline via `script`, with `args` as a real JSON object.

## The `args` contract

| Key | Shape | Where the main session gets it |
|---|---|---|
| `ideaSlug` | string | the directory name under `docs/plan/` |
| `today` | `"YYYY-MM-DD"` | the session's date. Never let a worker derive it |
| `skillDir` | absolute path | `${CLAUDE_SKILL_DIR}` for this skill; workers read their briefs from it |
| `ideaSummary` | string | one paragraph from `overview.md` |
| `coreLoop` | string | the core loop from `experience.md`, or from `overview.md` 中核の体験 when experience.md does not exist yet |
| `axes` | string[] | the comparison axes the owner agreed to |
| `products` | `[{name, url, notes}]` | the list the owner agreed to. `notes` may be `""` |
| `languages` | string[] | e.g. `["日本語", "English"]` |
| `handsOn` | string[] | optional: the products the owner agreed to walk hands-on. Reaches the critic only |
| `mode` | `"discover"` \| `"survey"` | omit for a survey run |
| `knownProducts` | string[] | discover mode only: products already on the list |

Discover mode ignores `products` and `axes`; survey mode ignores `knownProducts`.

## What comes back

Discover mode returns `{candidates: [{name, url, oneLine, whyRelevant, foundBy}], angleNotes}`.
The main session shows the candidates to the owner and gets the list agreed before running the survey.

Survey mode returns:

- `products` — one entry per product: `{product, url, profile, reviews}`. `profile.markdown` and
  `reviews.markdown` are Japanese prose already laid out under the headings of
  `docs/plan/_templates/competitor.md`.
- `comparison` — `{markdown, emptyCells, unsolvedUnion, coreLoopGaps}`, laid out under the headings
  of `docs/plan/_templates/competitor-comparison.md`, minus 立ち位置の選択肢 (the main session writes
  that with the owner).
- `critique` — `{missing, verdict}`: what the survey does not establish.
- `dropped` — product names cut by the cap, so the main session can propose a second run.

Nothing is written to disk by the workflow. The main session verifies primary sources, runs the
hands-on pass, and writes the files.

## Agent count

Survey mode spawns `2 × products + 2` agents. The script caps `products` at 6, so a run is at most
14 agents, and `log()` names anything it dropped. Discover mode spawns 3. Raise `MAX_PRODUCTS` only
when the owner asks for a bigger run.

## The script

```js
export const meta = {
  name: 'surveying-competitors',
  description: 'Survey competing products: candidate discovery, per-product profile and review mining, then one comparison',
  phases: [
    { title: 'Discover', detail: 'three search angles propose candidate products (discover mode only)' },
    { title: 'Profile', detail: 'one agent per product: positioning, core loop, features, UI/UX mechanisms' },
    { title: 'Mine reviews', detail: 'one agent per product: verbatim praise, complaints, unsolved problems' },
    { title: 'Compare', detail: 'one agent: axis table, pleasing mechanisms, unsolved-problem union, core-loop gaps' },
    { title: 'Critic', detail: 'one agent: what this survey does not establish' },
  ],
}

const brief = (name) => `${args.skillDir}/references/agents/${name}.md`
const langs = (args.languages || ['日本語', 'English']).join(' / ')

const PROVENANCE = {
  url: { type: 'string' },
  sourceDate: { type: 'string' },
  confidence: { type: 'string' },
}

// ---------- discover mode: the list is open, so the owner confirms it before the survey ----------
if (args.mode === 'discover') {
  const ANGLES = [
    'アプリストア / プロダクトディレクトリのカテゴリを端から見る（App Store, Google Play, Product Hunt など）',
    '"alternatives to X" / "X 比較" 系のまとめ記事とレビューサイトから逆引きする',
    '日本語圏の一次的な言及（note, Qiita, はてな, X の使用報告, 個人ブログ）から拾う',
  ]
  const CANDIDATES_SCHEMA = {
    type: 'object',
    properties: {
      candidates: {
        type: 'array',
        items: {
          type: 'object',
          properties: {
            name: { type: 'string' },
            url: { type: 'string' },
            oneLine: { type: 'string' },
            whyRelevant: { type: 'string' },
          },
          required: ['name', 'url', 'oneLine', 'whyRelevant'],
        },
      },
      angleNotes: { type: 'string' },
    },
    required: ['candidates', 'angleNotes'],
  }

  phase('Discover')
  const sweeps = await parallel(ANGLES.map((angle, i) => () => agent(
    `First read the brief at ${brief('discover')} and follow it.\n\n` +
    `<input>\nSEARCH_ANGLE: ${angle}\nIDEA_SUMMARY: ${args.ideaSummary}\n` +
    `CORE_LOOP: ${args.coreLoop}\nTODAY: ${args.today}\nLANGUAGES: ${langs}\n` +
    `KNOWN_PRODUCTS: ${(args.knownProducts || []).join(', ') || 'なし'}\n</input>`,
    { label: `Angle ${i + 1}`, phase: 'Discover', schema: CANDIDATES_SCHEMA, model: 'sonnet', effort: 'low' },
  )))

  const seen = new Map()
  const notes = []
  sweeps.filter(Boolean).forEach((sweep, i) => {
    notes.push(`角度${i + 1}: ${sweep.angleNotes}`)
    sweep.candidates.forEach((c) => {
      const key = c.name.toLowerCase().replace(/[^a-z0-9぀-ヿ一-鿿]/g, '')
      if (seen.has(key)) { seen.get(key).foundBy.push(i + 1); return }
      seen.set(key, Object.assign({}, c, { foundBy: [i + 1] }))
    })
  })
  const candidates = Array.from(seen.values())
  log(`${candidates.length} 件の候補（重複統合後）。オーナーの確認待ち。`)
  return { candidates, angleNotes: notes.join('\n') }
}

// ---------- survey mode ----------
const MAX_PRODUCTS = 6 // 2 agents per product + compare + critic = 14, under the ~15 cap
const all = args.products || []
const products = all.slice(0, MAX_PRODUCTS)
const dropped = all.slice(MAX_PRODUCTS).map((p) => p.name)
if (dropped.length) log(`上限 ${MAX_PRODUCTS} 件で打ち切り。積み残し: ${dropped.join(', ')}。2 回目の run を提案すること。`)

const axes = (args.axes || []).join(' / ')

const PROFILE_SCHEMA = {
  type: 'object',
  properties: {
    product: { type: 'string' },
    markdown: { type: 'string' },
    axisValues: {
      type: 'array',
      items: {
        type: 'object',
        properties: Object.assign({ axis: { type: 'string' }, value: { type: 'string' } }, PROVENANCE),
        required: ['axis', 'value', 'url', 'sourceDate', 'confidence'],
      },
    },
    unresolved: { type: 'array', items: { type: 'string' } },
  },
  required: ['product', 'markdown', 'axisValues', 'unresolved'],
}

const VOICE = {
  type: 'object',
  properties: Object.assign({ quote: { type: 'string' }, language: { type: 'string' } }, PROVENANCE),
  required: ['quote', 'language', 'url', 'sourceDate', 'confidence'],
}

const REVIEWS_SCHEMA = {
  type: 'object',
  properties: {
    product: { type: 'string' },
    markdown: { type: 'string' },
    praised: { type: 'array', items: VOICE },
    complained: { type: 'array', items: VOICE },
    unsolvedProblems: {
      type: 'array',
      items: {
        type: 'object',
        properties: Object.assign(
          { problem: { type: 'string' }, shape: { type: 'string' }, quote: { type: 'string' }, language: { type: 'string' } },
          PROVENANCE,
        ),
        required: ['problem', 'shape', 'quote', 'language', 'url', 'sourceDate', 'confidence'],
      },
    },
    sourceCount: { type: 'number' },
    gaps: { type: 'array', items: { type: 'string' } },
  },
  required: ['product', 'markdown', 'praised', 'complained', 'unsolvedProblems', 'sourceCount', 'gaps'],
}

const COMPARISON_SCHEMA = {
  type: 'object',
  properties: {
    markdown: { type: 'string' },
    emptyCells: {
      type: 'array',
      items: { type: 'object', properties: { product: { type: 'string' }, axis: { type: 'string' } }, required: ['product', 'axis'] },
    },
    unsolvedUnion: {
      type: 'array',
      items: {
        type: 'object',
        properties: Object.assign(
          { problem: { type: 'string' }, leftUnsolvedBy: { type: 'array', items: { type: 'string' } }, quote: { type: 'string' } },
          PROVENANCE,
        ),
        required: ['problem', 'leftUnsolvedBy', 'quote', 'url', 'sourceDate', 'confidence'],
      },
    },
    coreLoopGaps: {
      type: 'array',
      items: {
        type: 'object',
        properties: { step: { type: 'string' }, coveredBy: { type: 'array', items: { type: 'string' } }, verdict: { type: 'string' } },
        required: ['step', 'coveredBy', 'verdict'],
      },
    },
  },
  required: ['markdown', 'emptyCells', 'unsolvedUnion', 'coreLoopGaps'],
}

const CRITIC_SCHEMA = {
  type: 'object',
  properties: {
    missing: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          issue: { type: 'string' },
          why: { type: 'string' },
          suggestedFix: { type: 'string' },
          severity: { type: 'string' },
          confidence: { type: 'string' },
        },
        required: ['issue', 'why', 'suggestedFix', 'severity', 'confidence'],
      },
    },
    verdict: { type: 'string' },
  },
  required: ['missing', 'verdict'],
}

// pipeline(): each product flows profile -> reviews on its own. No barrier between the two stages,
// because review mining for product B needs nothing from product A.
const perProduct = await pipeline(
  products,
  (product) => agent(
    `First read the brief at ${brief('profile')} and follow it.\n\n` +
    `<input>\nPRODUCT_NAME: ${product.name}\nPRODUCT_URL: ${product.url}\n` +
    `PRODUCT_NOTES: ${product.notes || 'なし'}\nIDEA_SUMMARY: ${args.ideaSummary}\n` +
    `CORE_LOOP: ${args.coreLoop}\nAXES: ${axes}\nTODAY: ${args.today}\n</input>`,
    { label: `Profile: ${product.name}`, phase: 'Profile', schema: PROFILE_SCHEMA, model: 'sonnet', effort: 'medium' },
  ),
  async (profile, product) => {
    const summary = profile ? profile.markdown.slice(0, 1500) : '（プロファイル段が結果を返さなかった）'
    const reviews = await agent(
      `First read the brief at ${brief('mine-reviews')} and follow it.\n\n` +
      `<input>\nPRODUCT_NAME: ${product.name}\nPRODUCT_URL: ${product.url}\n` +
      `CORE_LOOP: ${args.coreLoop}\nLANGUAGES: ${langs}\nTODAY: ${args.today}\n</input>\n\n` +
      `<profile_summary>\n${summary}\n</profile_summary>`,
      { label: `Reviews: ${product.name}`, phase: 'Mine reviews', schema: REVIEWS_SCHEMA, model: 'sonnet', effort: 'medium' },
    )
    return { product: product.name, url: product.url, profile, reviews }
  },
)

const reports = perProduct.filter(Boolean)

// Barrier reached: the comparison genuinely needs every product's report at once.
phase('Compare')
const comparison = await agent(
  `First read the brief at ${brief('compare')} and follow it.\n\n` +
  `<input>\nIDEA_SUMMARY: ${args.ideaSummary}\nCORE_LOOP: ${args.coreLoop}\n` +
  `AXES: ${axes}\nTODAY: ${args.today}\n</input>\n\n` +
  `<product_reports>\n${JSON.stringify(reports, null, 1)}\n</product_reports>`,
  { label: 'Comparison', schema: COMPARISON_SCHEMA, model: 'opus', effort: 'high' },
)

phase('Critic')
const critique = await agent(
  `First read the brief at ${brief('critic')} and follow it.\n\n` +
  `<input>\nAXES: ${axes}\nLANGUAGES: ${langs}\nTODAY: ${args.today}\n` +
  `HANDS_ON_PLAN: ${(args.handsOn || []).join(', ') || '未定'}\n` +
  `DROPPED: ${dropped.join(', ') || 'なし'}\n</input>\n\n` +
  `<product_reports>\n${JSON.stringify(reports, null, 1)}\n</product_reports>\n\n` +
  `<comparison>\n${comparison ? comparison.markdown : '（比較段が結果を返さなかった）'}\n</comparison>`,
  { label: 'Completeness critic', schema: CRITIC_SCHEMA, model: 'sonnet', effort: 'medium' },
)

return { ideaSlug: args.ideaSlug, today: args.today, products: reports, comparison, critique, dropped }
```

## Notes for the main session

- The script never calls `Date.now()` or `new Date()`; every date in the result came from `args.today`
  or from a source page. If a date looks wrong, `args.today` was filled in wrong.
- Re-running: the Workflow result gives a `scriptPath` and a `runId`. To add products after the
  owner approves a second batch, re-invoke with the same `scriptPath` and a `products` list holding
  only the new ones — that is cheaper and cleaner than resuming a capped run.
- `handsOn` is optional and only reaches the critic, which uses it to flag a hands-on candidate with
  no free tier.
