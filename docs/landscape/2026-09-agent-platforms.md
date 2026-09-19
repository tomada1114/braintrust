# エージェント基盤・フレームワーク

- 調査日: 2026-09-06
- 調査手段: Dynamic Workflow(Sonnet 調査 + Sonnet 検証 + Opus 執筆)
- 更新の目安: 3 ヶ月

## 選ぶときの軸

- **課金** — フレームワーク自体は OSS で無料でも、実行基盤(マネージドサンドボックス、ホスティング)に別建ての課金が乗る。Anthropic Managed Agents はトークンに加えセッション稼働時間課金。
- **無料枠** — OSS ライブラリ(Agent SDK、OpenAI Agents SDK、ADK、Vercel AI SDK、Mastra、LangGraph)は自前ホストなら基盤モデルの API 料金だけで動く。マネージド実行基盤を使った時点で別料金。
- **データ利用** — Managed Agents はステートフル設計のため ZDR / HIPAA BAA の対象外。OpenAI Agents SDK のトレーシングはデフォルトで OpenAI へ送信される。
- **認証とサブスク転用の可否** — Claude Agent SDK は claude.ai ログインや無料枠のレート制限を第三者製品に提供することを(事前承認なしには)禁じている。
- **構造化出力** — Zod / Valibot / JSON Schema をどこまで受け付け、検証失敗時の挙動を制御できるか。
- **SDK** — TypeScript が第一級か、Python 版の後追いか。ADK は多言語、Agent SDK は Python/TS のみ。
- **ロックイン** — 組み込みツールが特定ベンダーのモデルに縛られるか(ADK の組み込みツールは Gemini 前提)。ライセンスが本番運用を縛るか(LangGraph Platform は Elastic License 2.0)。

## Anthropic のエージェント面

Anthropic は 3 層に分かれている。Tool Runner(通常 SDK のベータ機能・ループだけ自動化)、Claude Agent SDK(Claude Code のライブラリ化・自前ホスト)、Managed Agents(Anthropic がループとサンドボックスをホスト)。

- Claude Agent SDK は「Claude Code をライブラリとして使う」もので、同じエージェントループ・組み込みツール・コンテキスト管理を呼び出せる。ホスティングは自分で行う。パッケージは `claude-agent-sdk`(PyPI)と `@anthropic-ai/claude-agent-sdk`(npm)(https://code.claude.com/docs/en/agent-sdk/overview, 確認 2026-09-06, 確度 高)
- 組み込みで持つのは、ツール(読み書き編集・コマンド実行・Web 検索)、フック、サブエージェント、MCP 接続、権限制御、セッション(再開・分岐)、`.claude/` からのスキル/コマンド/メモリ読み込み、プラグイン(https://code.claude.com/docs/en/agent-sdk/overview, 確認 2026-09-06, 確度 高)
- 要件は Node.js 18+ または Python 3.10+。認証は `ANTHROPIC_API_KEY` が基本で、Bedrock / Claude Platform on AWS / Vertex / Foundry 経由も可。claude.ai ログインや無料枠のレート制限を第三者製品に提供することは事前承認なしには禁止されている(https://code.claude.com/docs/en/agent-sdk/quickstart, 確認 2026-09-06, 確度 高)
- 利用は商用利用規約に従う。ブランディングでは「Claude Agent」等は可、「Claude Code」を名乗るのは不可(https://code.claude.com/docs/en/agent-sdk/overview, 確認 2026-09-06, 確度 高)
- 公式の使い分け: ツールループを自作したくない → Agent SDK、対話的な開発やワンオフ → Claude Code CLI、API を直接叩いて自分でループを書く → Client SDK、サンドボックスやセッション基盤を自分で管理せず長時間・非同期に動かす → Managed Agents(https://code.claude.com/docs/en/agent-sdk/overview, 確認 2026-09-06, 確度 高)
- Managed Agents の中核概念は Agent(モデル・システムプロンプト・ツール・MCP・スキル) / Environment(クラウドまたは自己ホストのサンドボックス) / Session(実行中インスタンス) / Events(アプリとの往復)。プロンプトキャッシュや圧縮も内蔵(https://platform.claude.com/docs/en/managed-agents/overview, 確認 2026-09-06, 確度 高)
- Managed Agents が想定するのは、数分〜数時間の長時間タスク、ネットワークアクセス可能な安全なサンドボックス、コンプライアンス都合の自己ホストサンドボックス、永続ファイルシステムとステートフルセッション、cron による定期実行(https://platform.claude.com/docs/en/managed-agents/overview, 確認 2026-09-06, 確度 高)
- 組み込みツールは Bash、ファイル操作(読み書き編集・glob・grep)、Web 検索/フェッチ(ドメイン許可・拒否リスト可)、MCP 接続。`agent_toolset_20260401` で一式を有効化する(https://platform.claude.com/docs/en/managed-agents/overview, 確認 2026-09-06, 確度 高)
- Managed Agents はベータで、全エンドポイントに `managed-agents-2026-04-01` ヘッダーが必須(SDK が自動設定)。API アカウントにはデフォルトで有効。MCP トンネルと「dreaming」はさらに限定的なリサーチプレビューで別途申請が必要(https://platform.claude.com/docs/en/managed-agents/overview, 確認 2026-09-06, 確度 高)
- パブリックベータ開始が 2026-04-08 という日付はドキュメント本文に見当たらない。**未確認**(https://platform.claude.com/docs/en/managed-agents/overview, 確認 2026-09-06, 確度 低)
- ステートフル設計のため Managed Agents は ZDR スコープや HIPAA BAA の対象になっていない。セッションとアップロードファイルは API でいつでも削除できる(https://platform.claude.com/docs/en/managed-agents/overview, 確認 2026-09-06, 確度 高)
- 課金は二軸。トークンは通常の Claude API 料金と同一(Web 検索は $10/1000 件)、セッション稼働時間は $0.08/session-hour で `running` の間だけミリ秒単位で計測される。idle / rescheduling / terminated は課金されない。Batch 割引やクラウドプラットフォーム料金は適用されず、`inference_geo:"us"` を使うとトークン料金が 1.1 倍。コード実行ツールのコンテナ時間課金の代替であり二重課金にはならない(https://platform.claude.com/docs/en/about-claude/pricing, 確認 2026-09-06, 確度 高)
- Tool Runner はエージェントループ・エラーラッピング・型安全性を自動化する薄いヘルパーでベータ扱い。人間承認・カスタムログ・条件付き実行が要るなら manual loop を使うよう案内されている。Python / TS / C# / Go / Java / PHP / Ruby の SDK で利用可能(https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner, 確認 2026-09-06, 確度 高)
- 公式スキルは「Tool Runner != Claude Agent SDK」と明記する。Tool Runner は `client.beta.messages.tool_runner` からアクセスする `POST /v1/messages` の薄いラッパーで、組み込みツールもファイルシステムアクセスもサンドボックスもない。Tool Runner と Agent SDK はどちらも harness-only(自分でホスト)で、マネージドデプロイを提供するのは Managed Agents だけ(https://github.com/anthropics/skills/blob/main/skills/claude-api/SKILL.md, 確認 2026-09-06, 確度 中)
- Managed Agents のセットアップは ant CLI と標準 SDK(`anthropic` / `@anthropic-ai/sdk`)を使い、エージェント作成 → 環境作成 → セッション作成 → イベント送受信(SSE)の 4 ステップ。名前空間は `client.beta.agents` / `.environments` / `.sessions`(https://platform.claude.com/docs/en/managed-agents/quickstart, 確認 2026-09-06, 確度 高)

## OpenAI Agents SDK

- TypeScript 版は `@openai/agents` として提供され、Agents / Handoffs / Guardrails / Sessions / Tracing / MCP 対応を Python 版と同様に備える(https://openai.github.io/openai-agents-js/, 確認 2026-09-06, 確度 中)
- Guardrails は Input / Output に加えツール呼び出し前後の Tool Input / Tool Output まで細分化され、違反時は `InputGuardrailTripwireTriggered` 等の専用例外を投げる(https://openai.github.io/openai-agents-js/guides/guardrails/, 確認 2026-09-06, 確度 中)
- Handoffs はエージェント間の作業委譲、Sessions は実行をまたいだ会話履歴の自動管理(https://openai.github.io/openai-agents-js/, 確認 2026-09-06, 確度 中)
- OpenAI ホスト型の組み込みツールは WebSearchTool / FileSearchTool / CodeInterpreterTool / ImageGenerationTool / HostedMCPTool / ToolSearchTool / ProgrammaticToolCallingTool / ShellTool(https://openai.github.io/openai-agents-python/tools/, 確認 2026-09-06, 確度 中)
- トレーシングは既定で OpenAI の Traces ダッシュボードへ送られ、OpenAI API キーが前提。ZDR ポリシー下の組織では利用不可。`OPENAI_AGENTS_DISABLE_TRACING=1` や `set_tracing_disabled(True)` で無効化でき、`add_trace_processor` / `set_trace_processors` で送信先を差し替えられる(https://openai.github.io/openai-agents-python/tracing/, 確認 2026-09-06, 確度 中)
- 非 OpenAI モデルは 3 通りでネイティブに繋がる: `set_default_openai_client()` によるグローバル指定、`Runner.run()` 単位の ModelProvider、`Agent.model` によるエージェント個別指定。加えてベータのアダプタ `openai-agents[litellm]` / `openai-agents[any-llm]` があり、`litellm/...` `any-llm/...` プレフィックスで他社モデルを呼べる(https://openai.github.io/openai-agents-python/models/, 確認 2026-09-06, 確度 中)
- Python 版は PyPI `openai-agents`、2026-08-19 時点で 0.22.0、Python 3.10 以上、MIT。Docker sandbox / E2B / Modal / Vercel / AWS / Temporal / Daytona との連携をオプション依存として持つ(=自前ホストの OSS ライブラリが基本形)(https://pypi.org/project/openai-agents/, 確認 2026-09-06, 確度 中)

## Google ADK

- PyPI `google-adk`、2026-09-06 時点で 2.8.0。Gemini 向けに最適化されつつ他の LLM プロバイダやデプロイ環境とも互換とされ、Cloud Run へのコンテナデプロイと Vertex AI Agent Engine へのスケールアウトが公式サポート(https://pypi.org/project/google-adk/, 確認 2026-09-06, 確度 中)
- 階層的なマルチエージェント構成(専門エージェントの合成・委譲・協調)をネイティブに扱う。セッション / メモリ / ツール出力 / アーティファクトは生の履歴ではなく構造化コンテキストとして管理され、セッションの自動作成・巻き戻し・コンテキスト圧縮に対応(https://adk.dev/, 確認 2026-09-06, 確度 中)
- 非 Gemini モデルは、文字列や識別子で直接指定できる Gemini / Claude / Agent Platform ホスト型のレジストリに加え、`ApigeeLlm` / `LiteLlm` / Ollama・vLLM・LiteRT-LM といったラッパークラスで繋ぐ(https://adk.dev/agents/models/, 確認 2026-09-06, 確度 中)
- 組み込みツール(`BuiltInCodeExecutor`、Google 検索、`VertexAiSearchTool`、BigQuery ツールセット等)は Gemini 前提で設計されており、モデルをアダプタで非 Gemini 化しても組み込みツールの互換性は別問題になる。公式ページが JS 描画で本文を直接確認できていない。**未確認**(https://adk.dev/tools/built-in-tools/, 確認 2026-09-06, 確度 低)
- SDK は Python / TypeScript・JS(adk-js) / Go / Java / Kotlin の複数言語(https://github.com/google/adk-docs, 確認 2026-09-06, 確度 中)
- ADK は 2025-04-09 の Google Cloud NEXT 2025 で発表された OSS フレームワーク。2026 年には GitHub / Jira / MongoDB 連携や可観測性統合を含む「エージェント実行レイヤー」として再定位されている(https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/, 確認 2026-09-06, 確度 中)

## TypeScript 中心のフレームワーク

### Vercel AI SDK

> **この節は 2026-09-06 時点・v6 以前の記述。** チャット UI の文脈では `docs/landscape/2026-09-chat-ui-stack.md`（2026-09-15、v7 基準）を先に読む。以下の記述のうち `isStepCount` / `ToolLoopAgent` / 構造化出力は v7 でも有効だが、UI 層（`useChat` の形）とサーバー側のレスポンス生成は v7 で変わっている。

- Apache License 2.0 の OSS(https://github.com/vercel/ai/blob/main/LICENSE, 確認 2026-09-06, 確度 高)
- 公式 24・コミュニティ 33 の provider パッケージを持ち、OpenAI / Anthropic / Google / Vertex / Bedrock / Mistral / Cohere / Groq / DeepSeek 等をカバー。Ollama や LM Studio は `@ai-sdk/openai-compatible` やコミュニティ provider 経由(https://ai-sdk.dev/docs/foundations/providers-and-models, 確認 2026-09-06, 確度 中)
- `@ai-sdk/openai-compatible` は baseURL と API キーを直接指定してカスタム provider を作る軽量パッケージで、Vercel AI Gateway や Vercel アカウントを経由せずローカルサーバーに直接繋げる(https://ai-sdk.dev/providers/openai-compatible-providers, 確認 2026-09-06, 確度 中)
- 構造化出力は `generateText` / `streamText` の `output` プロパティや `generateObject` / `streamObject` で、Zod・Valibot・JSON Schema を検証する。`partialOutputStream` / `elementStream` でストリーミング配信もできる(https://ai-sdk.dev/docs/ai-sdk-core/generating-structured-data, 確認 2026-09-06, 確度 中)
- エージェントループは `stopWhen`(`isStepCount` / `hasToolCall` / `isLoopFinished` 等)で制御。`ToolLoopAgent` はデフォルト 20 ステップの安全上限を持ち、`prepareStep` でステップごとにモデルやツールを差し替えられる(https://ai-sdk.dev/docs/agents/loop-control, 確認 2026-09-06, 確度 中)
- UI 層は React(`@ai-sdk/react`)の useChat / useCompletion / useObject を中核に、Vue・Svelte・Angular 向けパッケージとコミュニティの SolidJS 版がある(https://ai-sdk.dev/docs/ai-sdk-ui/overview, 確認 2026-09-06, 確度 中)

### Mastra

- 2026 年に Elastic License 2.0 から Apache License 2.0 へ全面移行。ただし `ee/` 配下のエンタープライズ機能は Mastra Enterprise Edition License v1.0 の下でソース利用可能にとどまり、本番利用には別途契約が必要(https://mastra.ai/blog/apache-license, 確認 2026-09-06, 確度 中)
- GitHub 上で約 27.7k star・2.7k fork・18,971 コミット(https://github.com/mastra-ai/mastra, 確認 2026-09-06, 確度 中)
- Ollama のセルフホストモデルは `ollama-ai-provider-v2` 経由で利用できる。具体モデル名(gpt-oss / Qwen3 / DeepSeek)や Ollama Cloud 向けドキュメントの存在は今回の取得範囲では確認できていない。**未確認**(https://mastra.ai/models/providers/ollama, 確認 2026-09-06, 確度 中 / 詳細は 低)
- 構造化出力は `structuredOutput.schema` に Zod / Valibot / ArkType / JSON Schema を渡し、`errorStrategy`(strict / warn / fallback)で検証失敗時の挙動を制御する(https://mastra.ai/docs/agents/structured-output, 確認 2026-09-06, 確度 中)

### LangChain.js / LangGraph.js

- LangChain.js 本体と LangGraph.js(langgraph, langchain-core, 各 model integration)は MIT(https://github.com/langchain-ai/langgraph/blob/main/LICENSE, 確認 2026-09-06, 確度 高)
- 一方 LangGraph Platform の実行サーバー `langgraph-api`(`langgraph dev`、Studio 連携、assistants/threads/runs の HTTP API、cron)は Elastic License 2.0 で、本番運用に商用ライセンスキーが必要になるケースがある。自前の Node/Express から `langchain` / `langgraph` を直接 import するだけなら MIT の範囲(https://pypi.org/pypi/langgraph-api/json, 確認 2026-09-06, 確度 中)
- `@langchain/ollama` が ChatOllama / OllamaEmbeddings を提供し、既定で `http://localhost:11434` に接続、`baseUrl` で変更できる(https://reference.langchain.com/javascript/langchain-ollama, 確認 2026-09-06, 確度 中)
- LangChain.js / LangGraph.js 自体は React 向け UI フックを持たないが、`@ai-sdk/langchain` アダプタ(`toBaseMessages()` / `toUIMessageStream()`)で LangGraph のイベントストリームを Vercel AI SDK の UIMessageStream に変換し、既存の useChat でレンダリングできる。ツール呼び出しのストリーミングにも対応(https://ai-sdk.dev/providers/adapters/langchain, 確認 2026-09-06, 確度 中)
- LangGraph.js の star 数・ダウンロード数が Python 版の 1/10〜1/6 という比較、および 2026 年時点で主要機能が Python 版とパリティに達しているという評価は第三者ブログ由来で一次データを確認していない。**未確認**(https://www.crewship.dev/learn/langgraph-vs-langgraphjs, 確認 2026-09-06, 確度 低)

### 参考: PydanticAI(Python)

- MIT ライセンスで、2026-09-06 時点の GitHub star は 19.8k(https://github.com/pydantic/pydantic-ai, 確認 2026-09-06, 確度 中)
- OpenAI / Anthropic / Gemini(Google API・Vertex) / xAI / Bedrock / Cerebras / Cohere / Groq / Hugging Face / Mistral / OpenRouter 等をネイティブサポートし、Ollama・vLLM・DeepSeek などは OpenAI 互換(`OpenAIChatModel`)経由。ストリーミングは `StreamedResponse` 抽象クラス、構造化出力対応は `model.profile` の `supports_json_schema_output` 等のフラグで判別する(https://pydantic.dev/docs/ai/models/overview/, 確認 2026-09-06, 確度 中)

## グレーゾーン・未確認

- Claude Agent SDK / Tool Runner 固有の追加課金を明記したページはなく、通常の Messages API トークン課金がそのまま適用されると解釈するしかない。pricing ページに「Agent SDK」という独立項目は存在しない。
- Tool Runner が 7 言語に実装される一方 Agent SDK が Python / TS のみである理由について、公式の説明は見当たらない。
- Managed Agents の AWS 版での機能差異、提供リージョンとデータレジデンシーの選択肢、自己ホストサンドボックスのネットワーク要件は未確認。「dreaming」と MCP トンネルの内容も未確認。
- OpenAI Agents SDK のトレーシングについて、保存期間・容量上限・追加課金の有無を明記した公式記述は見つからなかった。TS 版に Python 版と同等の非 OpenAI モデル対応(`set_default_openai_client` 相当)が揃っているかも未確認。Sessions の永続化バックエンドの選択肢一覧も未調査。
- ADK の GA / SemVer ポリシー(2.8.0 が API 安定を意味するか)を明言する一次情報に到達できていない。ADK 自体を自前ホストした場合と Vertex AI Agent Engine を使った場合の課金の切り分けも一次情報で確認できていない。
- Mastra の現行バージョンと GA 状況(v1 Beta のページが存在するため一部 API が未安定の可能性)は確定できていない。
- LangGraph Platform の Self-Hosted Lite / Enterprise の無料枠の正確な境界(ノード数上限等)は未確認。
- Vercel AI SDK が Vercel アカウントや AI Gateway 登録なしで完全にスタンドアロン動作すると明言した公式の一文は見つからず、provider 実装からの推測にとどまる。
- 検証で落とした記述: Mastra の `Agent.stream()` が toolCalls / toolResults / steps を個別の Promise として公開するという挙動(構造化出力ページに記載なし)、`@ai-sdk/langchain` の reasoning ブロック対応と `interrupt()` による Human-in-the-Loop 対応(アダプタページ本文に明記なし)、Managed Agents の 2026-04-08 ローンチ日。
- 今回の調査が触れていない論点: 3 大エコシステムを横並びにした TCO 表、SLA と可用性保証、SOC2 / ISO27001 / FedRAMP 等の認証、各基盤のレート制限の実数値、Mastra Cloud / LangGraph Platform の料金プランと無料枠、音声・リアルタイムエージェントの比較、Human-in-the-Loop 実装パターンの横並び、評価(Evals)ツールの比較、バージョン安定性の横断比較、プロンプトインジェクション対策とサンドボックス強度、成果物の知的財産上の扱い、フレームワーク間の移行コスト、MCP 対応成熟度の横断比較、日本語での性能。
