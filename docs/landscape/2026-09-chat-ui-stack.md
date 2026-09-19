# LLM チャット UI のスタック — Vercel AI SDK と UI 層

- 調査日: 2026-09-15
- 調査手段: メインセッションで ai-sdk.dev の live docs を直接確認 + Sonnet サブエージェント 3 体（Core 層 / UI 層 / UI ライブラリ比較）による並列調査。一次情報は npm レジストリ API、GitHub Releases、`unpkg` から取得した実配布物の型定義（`ai@7.0.102/dist/index.d.ts`）、および公式ドキュメント本文。
- 更新の目安: **3 ヶ月ではなく 2 ヶ月**。AI SDK はメジャーが約 6 ヶ月ごとに出て毎回破壊的変更が入るため、他の landscape ファイルより陳腐化が速い（根拠は「1. バージョンの現状」）。
- 想定用途: LLM を使った**チャット形式**のアプリ（会話練習、添削、対話型ドリル）をブラウザ + 自前サーバーで作る場合の、通信・状態・画面の層をどう組むか。

## 結論（このリポジトリでの前提）

**通信・状態の層は Vercel AI SDK（`ai` + `@ai-sdk/react`）で統一してよい。** 理由は 3 つ。

1. プロバイダを差し替えてもコードは import とモデル ID 文字列しか変わらない。`docs/landscape/2026-09-model-intelligence.md` の結論（第一候補 GPT-5.6 Luna、次点 Gemini 3.8 Flash）はまだ確度に留保がある状態なので、**ベンダーを後から変えられること自体に価値がある**。
2. ストリーミング、中断、再送、ツール呼び出しの状態機械を自前で書かずに済む。ここは書くと必ずバグる領域。
3. Apache-2.0 の OSS で、SDK 自体に別料金がない。

**ただし以下は AI SDK が解決しない。** ここを SDK に期待すると設計を誤る。

- **スレッド管理・履歴保存・採点結果の保存**。SDK は永続化機能を持たない。公式ガイドは「実装例であり認可もエラー処理も含まない」と明記している。
- **画面**。`useChat` は状態機械であって UI ではない。入力欄の見た目も、吹き出しも、スクロールも提供しない。
- **出力の再現性**。構造（スキーマ）への適合は強制・検証できるが、値がブレないことは保証しない。そこはモデル側の設定（temperature 等）の話。

---

## 1. バージョンの現状 — ここが最大の落とし穴

**2026-09-15 時点の現行は v7。npm `ai` の latest は `7.0.102`。**（https://registry.npmjs.org/ai, 確認 2026-09-15, 確度 高）

| メジャー | リリース日 | 前メジャーからの間隔 |
|---|---|---|
| `ai@5.0.0` | 2025-07-31 | — |
| `ai@6.0.0` | 2025-12-22 | 約 5 ヶ月 |
| `ai@7.0.0` | 2026-06-25 | 約 6 ヶ月 |

（npm の `time` フィールドと GitHub Releases の `published_at` が一致。Vercel 公式ブログも "June 25, 2026" と記載。https://registry.npmjs.org/ai, https://github.com/vercel/ai/releases/tag/ai%407.0.0, https://vercel.com/blog/ai-sdk-7, 確認 2026-09-15, 確度 高）

### 落とし穴 1: 情報源が軒並み古い

- **context7 の索引は `ai_6.0.0` まで**しか個別バージョンタグを持たない。context7 だけ見ると v6 を最新と誤認する（確認 2026-09-15, 確度 高）。
- **公式ドキュメント内部にも古い例が残っている。** `vercel/ai` リポジトリの main ブランチを直接確認したところ、2026-09-15 時点で以下は v4 相当の旧 API のままだった。
  - `content/cookbook/00-guides/24-o3.mdx` — `const { messages, input, handleInputChange, handleSubmit, error } = useChat()` と `{message.content}`
  - `content/docs/05-ai-sdk-rsc/10-migrating-to-ui.mdx` — `const { messages, input, setInput, handleSubmit } = useChat()`

  一方 `content/docs/04-ai-sdk-ui/02-chatbot.mdx` などの主要ガイドは現行形に更新済み。**「公式ドキュメントだから現行 API のはず」は成り立たない。**（GitHub の raw main を直接 fetch して確認, 確認 2026-09-15, 確度 高 / 意図的に残しているのか更新漏れかは不明）

**見分け方**: `input` / `handleInputChange` / `handleSubmit` が出てきたら v4 相当の古い形。`message.content` を読んでいたら古い形。現行は `sendMessage` と `message.parts`。

### 落とし穴 2: メジャーごとに破壊的変更が入る

「AI SDK で統一する」という判断は、**約 6 ヶ月ごとに移行作業が発生する**ことを引き受ける判断でもある。個人開発で複数アプリを抱えると、この移行税が効いてくる。実際の変更量は下記。

#### v4 → v5（2025-07-31）— 最大の破壊的変更

- `useChat` が入力欄の state を持たなくなった。`input` / `handleInputChange` / `handleSubmit` を返さなくなり、アプリ側が `useState` で持つ形に。
- `Message` → `UIMessage` に改名。`content: string` → `parts` 配列に。
- transport アーキテクチャの導入。

（https://ai-sdk.dev/docs/migration-guides/migration-guide-5-0, 確認 2026-09-15, 確度 高）

#### v5 → v6（2025-12-22）

- ツール承認フロー（`approval-requested` / `approval-responded` / `output-denied`）の追加。
- `convertToCoreMessages` → `convertToModelMessages`（非同期化）。
- `Experimental_Agent` → `ToolLoopAgent`。

（https://ai-sdk.dev/docs/migration-guides/migration-guide-6-0, 確認 2026-09-15, 確度 高）

#### v6 → v7（2026-06-25）

| 旧 | 新 |
|---|---|
| `system`（生成関数の引数） | `instructions` |
| `onFinish`（サーバー側 `streamText` / agent） | `onEnd` |
| `onStepFinish` | `onStepEnd` |
| `stepCountIs` | `isStepCount` |
| `experimental_output` | `output` |
| `experimental_activeTools` | `activeTools` |
| `experimental_prepareStep` | `prepareStep` |
| `ToolCallOptions` | `ToolExecutionOptions` |
| `streamText().fullStream` | `streamText().stream` |
| `result.toUIMessageStreamResponse()`（インスタンスメソッド） | `createUIMessageStreamResponse()`（トップレベルの無状態関数） |
| `result.totalUsage` | `result.usage`（全ステップ合算に変更） |

さらに:
- **`messages` 配列内の system メッセージが既定で拒否される**。トップレベル `instructions` を使うか `allowSystemInMessages: true` で opt-in。
- file 系 part（`image-data` / `image-url` / `file-data`）が単一の `file` + `mediaType` に統合。`reasoning-file` が新設。
- OpenTelemetry が `@ai-sdk/otel` に分離。
- **Node.js 22+ 必須**（18 / 20 はサポート終了）、**ESM 専用**（`require()` 不可）。

（https://ai-sdk.dev/docs/migration-guides/migration-guide-7-0, https://github.com/vercel/ai/releases/tag/ai%407.0.0, 確認 2026-09-15, 確度 高）

### 落とし穴 3: `onFinish` と `onEnd` が層によって別名

v7 でサーバー側（`streamText` / `generateText` / agent）は `onFinish` → `onEnd` に改名されたが、**クライアント側 `useChat` のオプションは `onFinish` のまま**。同じ「完了時コールバック」が層によって名前が違う。（https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat でメインセッションが直接確認, 確認 2026-09-15, 確度 高）

---

## 2. パッケージ構成とバージョン整合

- `ai`（コア）、`@ai-sdk/react`（UI）、`@ai-sdk/openai` / `@ai-sdk/anthropic` / `@ai-sdk/google`（プロバイダ）に分かれる。すべて Apache-2.0。（https://registry.npmjs.org/ai, 確認 2026-09-15, 確度 高）
- **メジャー番号は揃わない。** コア `ai` が 7.x のとき、`@ai-sdk/react` は 4.0.105、`@ai-sdk/openai` は 4.0.67、`@ai-sdk/anthropic` は 4.0.54。互換性は共有基盤の `@ai-sdk/provider` と `@ai-sdk/provider-utils` のバージョン一致で担保されている。**「コアと同じメジャーを入れる」という直感は誤り。**（https://registry.npmjs.org/@ai-sdk/openai ほか, 確認 2026-09-15, 確度 高）
- Zod は **3 系・4 系どちらも公式サポート**（`peerDependencies.zod = "^3.25.76 || ^4.1.8"`）。（同上, 確認 2026-09-15, 確度 高）
- v7 で「AI SDK Harnesses」という第 3 の柱（`HarnessAgent`）が導入されたが、**コア `ai` ではなく別パッケージ `@ai-sdk/harness`**。Claude Code / Codex / Cursor などの既存エージェントハーネスを統一 API で叩くためのもので、チャットアプリの文脈では通常不要。（https://registry.npmjs.org/@ai-sdk/harness, 確認 2026-09-15, 確度 高）

---

## 3. Core 層 — 会話用と構造化出力用は別物として扱う

### 会話（ストリーミング）

`streamText` を使い、結果の `stream` をトップレベル関数 `createUIMessageStreamResponse()` に渡してレスポンスにする。v6 までのインスタンスメソッド `result.toUIMessageStreamResponse()` は非推奨（互換のため残存）。（`ai@7.0.102/dist/index.d.ts` を直接確認, 確認 2026-09-15, 確度 高）

### 構造化出力（採点・判定）

- `generateObject` / `streamObject` は **v7 でも独立した関数として健在**。ドキュメントのリファレンス索引には出てこないが、実配布物の型定義に明確に存在する。（`ai@7.0.102/dist/index.d.ts`, 確認 2026-09-15, 確度 高 / ドキュメント構成のズレの理由は未確認）
- 旧 `mode`（`json` / `tool` / `auto`）パラメータは**現行 API に存在しない**。かわりに `output`（`'object' | 'array' | 'enum' | 'no-schema'`）で出力形状を指定する。（同上, 確認 2026-09-15, 確度 高）
- 検証に失敗すると `NoObjectGeneratedError`。`repairText`（旧 `experimental_repairText`）でモデルの生出力を JSON パース可能に修復するフックを差し込める。（同上, 確認 2026-09-15, 確度 高）
- **「スキーマ検証に失敗したら自動でモデルに再生成させる」組み込み機構があるかは未確認。** `maxRetries` は通信レベルのリトライであり、意味的な再試行とは別物である可能性が高い。（確度 中・未確認）
- **AI SDK は「構造への適合」を強制・検証するが、「値のブレなさ」は保証しない。** 採点のスコアを安定させたいなら、それはモデル側の設定（temperature 等）とプロンプト設計の話であって SDK の機能ではない。（AI SDK の設計からの解釈。公式に明記された記述は見つけられなかった。確度 低・未確認）

### エージェントループ

- `ToolLoopAgent`（旧 `Experimental_Agent`）。**既定のステップ上限は 20**（暴走によるコスト膨張を防ぐ安全装置と説明されている）。
- v7 新設の `WorkflowAgent`（耐障害・再開可能な実行向け）には**既定のステップ上限がない**。`stopWhen` を明示しないと止まらない。
- 停止条件は `stopWhen` に `isStepCount(n)` / `hasToolCall(name)` / `isLoopFinished()` を配列で渡す。
- `prepareStep` でステップごとに `activeTools` や `toolChoice` を差し替えられる（フェーズ制御）。

（https://ai-sdk.dev/docs/agents/loop-control ほか, 確認 2026-09-15, 確度 高）

---

## 4. UI 層（`useChat`）— 状態機械であって UI ではない

### 返り値（v7 現行）

`messages` / `sendMessage` / `status` / `error` / `stop` / `regenerate` / `setMessages` / `clearError` / `resumeStream` / `addToolOutput` / `addToolApprovalResponse` / `id`。

コールバックは `onFinish` / `onError` / `onData` / `onToolCall` / `sendAutomaticallyWhen`。

（https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat をメインセッションが直接確認, 確認 2026-09-15, 確度 高）

- **入力欄の state はアプリ側が持つ。** 公式サンプルも `const [input, setInput] = useState('')` を自前で書いている。
- `status` は `submitted` / `streaming` / `ready` / `error` の 4 値。`stop()` は `submitted` / `streaming` のときのみ、`regenerate()` は `ready` / `error` のときのみ有効。
- **`stop()` はクライアント側リクエストの中断であって、サーバー側のモデル生成のキャンセルではない。** 課金は止まらない。（https://ai-sdk.dev/docs/troubleshooting/abort-breaks-resumable-streams, 確認 2026-09-15, 確度 中 — 原文ページを直接は開いていない）

### メッセージは `parts` の配列

```ts
interface UIMessage {
  id: string;
  role: 'system' | 'user' | 'assistant';
  metadata?: METADATA;
  parts: Array<UIMessagePart<...>>;
}
```

part の種類（v7）: `text` / `reasoning` / `reasoning-file`（v7 新設）/ `tool-{NAME}` / `dynamic-tool` / `file` / `source-url` / `source-document` / `data-{NAME}` / `custom` / `step-start`。

ツール part の state 遷移: `input-streaming` → `input-available` →（`approval-requested` → `approval-responded` →）`output-available` / `output-error` / `output-denied`。

（https://ai-sdk.dev/docs/reference/ai-sdk-core/ui-message, 確認 2026-09-15, 確度 高）

**採点用に「人間が読む発話だけ」を取り出すには**、`parts.filter(p => p.type === 'text').map(p => p.text).join('')` を自前で書く。これに対応する公式ヘルパーは**見つからなかった**（探したが無かった、という否定的事実。確度 中）。モデルに渡す形式への変換は `convertToModelMessages()`（v7 でも名前は変わっていない）。

### transport

`DefaultChatTransport` でエンドポイント・ヘッダ・ボディを指定する。**既定では全履歴を毎回送る**が、`prepareSendMessagesRequest` で間引ける（直近 N 件のみ、末尾 1 件のみ、いずれも公式に例がある）。（https://ai-sdk.dev/docs/ai-sdk-ui/transport, 確認 2026-09-15, 確度 高）

### 永続化は自前

- **SDK はスレッド管理も履歴保存も持たない。** 公式ガイドは実装例にすぎず、認可もエラー処理も含まないと明記されている。
- 保存すべきは `UIMessage` 形式（`parts` 込み）。`UIMessage` がアプリ状態の source of truth で、`ModelMessage` への変換は必要なときだけ行う設計が推奨されている。
- メッセージ ID は既定だとユーザー分がクライアント、アシスタント分がサーバーで別々に生成される。永続化を安定させるには明示的に発行する。
- サーバーが受け取ったメッセージは `validateUIMessages()` で検証することが推奨されている。

（https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-message-persistence, 確認 2026-09-15, 確度 高）

### 途中切断からの復旧（resumable stream）

存在するが **SDK 単体では完結しない**。クライアント側 `useChat({ id, resume: true })` に加え、サーバー側で `resumable-stream` パッケージ + **Redis** + 「どの stream ID がどのチャットでアクティブか」を追跡する自前の永続化層が要る。さらに明示的な停止操作はこの仕組みと衝突しうるため、専用の停止エンドポイントを別に用意する必要があるとされている。（https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-resume-streams, 確認 2026-09-15, 確度 高）

**個人開発の最初の版では、ここは捨てる判断が妥当**（Redis を足す価値があるかは、切断の実頻度を見てから）。

---

## 5. スタンドアロン利用（Vercel に乗らない）

- **オンボーディングの既定経路は Vercel AI Gateway。** `getting-started/nodejs` の Prerequisites に `AI_GATEWAY_API_KEY` が明記され、`provider-management` にも「デフォルトのグローバルプロバイダは Vercel AI Gateway」との記述がある。コア `ai` は `@ai-sdk/gateway` を通常の依存として含む。（https://ai-sdk.dev/docs/getting-started/nodejs, https://ai-sdk.dev/docs/ai-sdk-core/provider-management, 確認 2026-09-15, 確度 高）
- **Gateway を使わず自前の API キーで直接プロバイダを叩く経路も公式に明記されている**（`pnpm add @ai-sdk/anthropic` → `anthropic('...')`）。（https://ai-sdk.dev/docs/getting-started/choosing-a-provider, 確認 2026-09-15, 確度 高）
- ただし**「Vercel アカウントは一切不要」と断言する一文は公式のどこにも見つからなかった。** 不要と読み取れる状況証拠は強いが、明示的な保証ではない。（複数ページを横断確認, 確認 2026-09-15, 確度 中 —「明記がない」ことの確認）
- ランタイム: Node.js 22+、ESM 専用。Next.js 以外に Node.js / Svelte / Nuxt / Expo / TanStack Start、バックエンドは Express / Hono / Fastify / Nest.js の getting-started がある。（https://ai-sdk.dev/docs/getting-started, 確認 2026-09-15, 確度 中）
- **Edge ランタイム対応は v7 時点の明記を見つけられなかった。**（未確認, 確度 低）

---

## 6. 画面の層 — 4 つの選択肢

`useChat` は状態機械なので、吹き出し・入力欄・スクロールは別に用意する。選択肢は大きく 4 つで、**選ぶ基準は機能数ではなく「チャットの外にどれだけ独自 UI があるか」**。

### AI Elements（Vercel 公式）

- **正体は npm ライブラリではない。** shadcn/ui と同じレジストリ方式で、`npx ai-elements@latest add <component>` でソースコードを自分のリポジトリ（既定で `@/components/ai-elements/`）にコピーする。以後は自分のコードとして編集する。（https://github.com/vercel/ai-elements, 確認 2026-09-15, 確度 高）
- ライセンスは **Apache-2.0**（リポジトリの LICENSE を直接確認, 確認 2026-09-15, 確度 高）。
- **前提条件が重い**: Next.js プロジェクト、shadcn/ui 初期化済み、Tailwind CSS 4（CSS Variables モードのみ）、React 19。事実上 React / Next.js 専用。（https://raw.githubusercontent.com/vercel/ai-elements/main/README.md, 確認 2026-09-15, 確度 高）
- コンポーネントは Conversation / Message / PromptInput / Response / Reasoning / Sources / Tool / Chain of Thought ほか。コード系（Artifact / Code Block / Sandbox）、音声系、ワークフロー系もある。
- **履歴管理・スレッド一覧は持たない。** 会話 UI の部品集。

### assistant-ui

- npm ライブラリ（`@assistant-ui/react`、MIT）。GitHub 12,155 stars、最終 push は 2026-09-15 で非常に活発。（GitHub API, 確認 2026-09-15, 確度 高）
- **AI SDK v7 に対応済み。** AI SDK 連携パッケージ `@assistant-ui/ai-sdk@0.0.6` の依存は `ai@^7.0.93` / `@ai-sdk/react@^4.0.96`（npm レジストリをメインセッションが直接確認, 確認 2026-09-15, 確度 高）。
  - **注意**: 公式ドキュメント本文には「`useChatRuntime` は AI SDK v5 の `useChat` をラップする」という記述が残っているが、実パッケージの依存は v7。**ドキュメントの記述が古い**（確認 2026-09-15, 確度 高 — 依存関係は実データ、記述のズレは観察）。
- 3 段階で使える: **Primitives**（unstyled のビルディングブロック）→ **Elements**（スタイル済み）→ **Examples**（ChatGPT / Claude クローンなど完成テンプレート）。
- **`Thread` コンポーネントはサイドバー（`ThreadList`）なしで単体利用できる。** 「assistant-ui を入れるとサイドバー型になる」は誤解。チャット枠外に独自 UI を置きたい場合は Primitives を直接組む。（https://www.assistant-ui.com/docs/primitives, 確認 2026-09-15, 確度 中 — ドキュメント要約経由、実装サンプル未確認）
- 実装済み: Markdown、自動スクロール、メッセージ仮想化、メッセージ分岐、編集、Resumable Streams、ファイルアップロード、音声入出力。Radix UI ベースでアクセシビリティに配慮。
- 有料の **Assistant Cloud**（スレッド永続化・ログ・分析）があるが、**必須ではない**。自前バックエンド・自前 DB で動く。（https://www.assistant-ui.com/pricing, 確認 2026-09-15, 確度 中）

### OpenAI ChatKit

- フレームワーク非依存の埋め込みチャットウィジェット。React フック `useChatKit` または Web Component `<openai-chatkit>`。フロントエンドは Apache-2.0。（GitHub API: openai/chatkit-js, 確認 2026-09-15, 確度 高）
- **Vercel AI SDK とは直接接続しない。** 独自のクライアント SDK と独自のバックエンドプロトコルを要求する。`useChat` は使えない。（https://openai.github.io/chatkit-js/, 確認 2026-09-15, 確度 中）
- バックエンドは 2 択: (1) OpenAI マネージド、(2) Python SDK `openai-chatkit` で `ChatKitServer` を自前実装。**セルフホストなら `Store` 抽象クラスを自前 DB で実装でき、推論部分も自由に書ける**（公式ガイドのコード例に「ここを自分の推論パイプラインに置き換えろ」というコメントがある）。（GitHub: openai/chatkit-python の guides を直接取得, 確認 2026-09-15, 確度 高）
- ただし**バックエンド SDK が Python のみ**で、TypeScript で統一したい場合は言語が割れる。
- **Agent Builder は 2026-06-03 に廃止が発表され 2026-11-30 終了予定。ChatKit 自体は "ChatKit remains available." と明記されており存続する**が、マネージドバックエンド構成は移行が必要。（https://developers.openai.com/api/docs/deprecations, 確認 2026-09-15, 確度 高）
- チャット内に widgets（カード・フォーム）は出せるが、**チャット面の外側に独自 UI を自由配置できるかは未確認**。「ウィジェットを埋め込む」設計思想が強い。

### CopilotKit

- npm ライブラリ（MIT）。GitHub 37,373 stars、最新 `v1.72.0`（2026-09-15）で 4 つのうち最も活発。（GitHub API, 確認 2026-09-15, 確度 高）
- **`useChat` をそのまま使う設計ではない。** フロント〜ランタイム間は独自のオープンプロトコル **AG-UI**（16 種のイベント型）で通信し、フロントは `useCopilotChat` を使う。（https://www.copilotkit.ai/ag-ui, 確認 2026-09-15, 確度 中）
- ただしバックエンドの BuiltInAgent は内部で Vercel AI SDK を使える。**AI SDK はモデル抽象化層としてバックエンドに入るが、フロントの `@ai-sdk/react` とは別物**という整理。
- 完成コンポーネント（`CopilotChat` / `CopilotSidebar` / `CopilotPopup`）→ ヘッドレス UI → Generative UI の 3 段階。
- 思想は「既存アプリの横に助手を置く」。**練習アプリの主画面そのものを作る道具ではない。**

### 比較表

| 軸 | AI Elements | assistant-ui | ChatKit | CopilotKit |
|---|---|---|---|---|
| 正体 | shadcn 方式（コードをコピー） | npm ライブラリ | 埋め込みウィジェット | npm ライブラリ（3 層スタック） |
| ライセンス | Apache-2.0 | MIT（+ 任意の有料 Cloud） | Apache-2.0（フロント） | MIT（+ 任意の有料 Cloud） |
| `useChat` と直結 | する（Vercel 自社製） | する（v7 対応済み） | **しない** | **しない**（AG-UI） |
| バックエンドの言語 | 任意 | 任意 | **Python SDK のみ**（セルフホスト時） | TypeScript ほか |
| チャット外に独自 UI | 自由（部品集なので） | 自由（Primitives） | 未確認（枠に嵌る可能性） | ヘッドレス UI で可能 |
| 履歴・スレッド管理 | 持たない | 持つ（任意、自前 DB 可） | 持つ | 持つ（OSS 単体で完結するかは未確認） |
| React 以外 | 不可（実質 Next.js 専用） | Vue / RN / Ink に展開中（成熟度未検証） | Web Component なので可 | Angular 等 |

---

## 7. 設計上の分離 — SDK に寄せてはいけないもの

チャット型の学習・練習アプリを設計するとき、以下は**アプリ固有の業務データ**であって、チャット SDK のスレッド機能に寄せると後で壊れる。

- **セッション**（1 回の練習の単位: 課題・制限時間・終了条件）
- **採点結果**（項目点・根拠・合否）
- **履歴**（見返す単位はメッセージではなくセッション）

理由は 2 つ。(1) AI SDK は永続化を持たないので、どのみち自前 DB が要る。(2) UI ライブラリのスレッド機能に寄せると、ライブラリを差し替えたときに採点と履歴まで巻き添えになる。**UI ライブラリは後から変えられるが、採点データの設計は変えにくい。**

あわせて、**会話用のモデル呼び出しと採点用のモデル呼び出しは分ける**。1 つのシステムプロンプトに「優しく話す」と「厳しく採点する」を同居させると、口調も点数も両方崩れる。会話は `streamText`（体感速度が命）、採点は `generateObject` + スキーマ（構造が命）。**合否のしきい値はモデルに判定させず、アプリ側が持つ**（モデルは項目点と根拠を返すだけ）。

この分離は Grok の壁打ち報告（2026-09-15、オーナー持ち込み）で提示された整理と一致する。ただし**この節は設計上の主張であって、公式ドキュメントに裏付けのある事実ではない**（確度: 設計判断）。

---

## グレーゾーン・未確認

- **beta / canary チャンネルの位置づけ**。npm dist-tags は `beta: 7.0.0-beta.187` / `canary: 7.0.0-canary.176` で、v7 内の先行機能なのか次メジャー（v8）の準備なのかバージョン文字列からは判別できない。**v8 が近いかどうかは未確認**で、これは「統一する」判断の移行コスト見積もりに直接効く。
- **構造化出力のプロバイダ間差異**。JSON mode 非対応のプロバイダで `output` がどう実現される（内部でツール呼び出しにフォールバックするか等）かは確認できなかった。
- **スキーマ検証失敗時の自動リトライの有無**。`repairText` フックは存在するが、「検証に失敗したらモデルに再生成させる」組み込み機構があるかは未確認。
- **出力の再現性についての公式の推奨**。`generateObject` + Zod が型安全という点は明確だが、値のブレに関する記述は見つけられず、この部分は設計からの解釈にとどまる。
- **「Vercel アカウント不要」の断定文**。直接プロバイダを使うコード例は豊富だが、明示的な保証文言はない。`ai` が `@ai-sdk/gateway` を通常依存に持つため、Gateway を使わない場合に Vercel 側と一切通信しないかはパッケージのソースを精査していない。
- **AI Gateway の料金体系**は未確認（無料枠の有無、単価）。
- **Edge ランタイム対応**の v7 時点の明記は見つけられなかった。
- **ChatKit セルフホスト時に他社モデルを使えるか**。公式ガイドのコード例は技術的に許容しているように読めるが、「Anthropic 等を使える」と明記した一次情報はない。第三者は「OpenAI 中心に配線されている」と評しており、技術的自由度と実務的前提にギャップがある。
- **ChatKit がチャット枠外の独自 UI をどこまで許すか**は未確認。
- **assistant-ui の Vue / React Native / Ink 対応の成熟度**は見出しレベルの確認のみ。
- **assistant-ui の Resumable Streams が Assistant Cloud なしで完結するか**は未確認。
- **CopilotKit の "Rich Threads" が OSS ランタイム単体で完結するか**（Copilot Cloud が前提か）は未確認。
- **`useChat` の Vue / Svelte / Angular / SolidJS のサポート範囲**について、ai-sdk.dev 内の 2 ページが矛盾している（一方は「React / Svelte / Vue の 3 つ、Vue はツール呼び出し非対応」、他方は「5 フレームワーク全対応」）。どちらが v7 時点で正確か未確定。
- **今回触れていない論点**: AI SDK の evals / 可観測性、音声（Realtime）をチャットと同じ経路に載せられるか、マルチモーダル入力のトークン換算、SSE をプロキシ・CDN が切る問題、モバイルブラウザでの入力欄とキーボードの扱い。
