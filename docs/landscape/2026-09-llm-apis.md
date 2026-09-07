# LLM API — ホスト型 API とローカル LLM

- 調査日: 2026-09-06
- 調査手段: Dynamic Workflow(Sonnet 調査 + Sonnet 検証 + Opus 執筆)
- 更新の目安: 3 ヶ月

## 一覧

| ベンダー | 無料枠 | 最安モデル価格(入力/出力, per MTok) | 無料枠のデータ利用 | サブスク転用 | 構造化出力 | TS SDK |
|---|---|---|---|---|---|---|
| Anthropic | なし(新規に少額クレジットのみ) | $1 / $5 (Haiku 4.5) | — | Agent SDK 経由のみ・規約上グレー | JSON Schema + strict tools | `@anthropic-ai/sdk` |
| OpenAI | 恒久枠なし(データ共有プログラムは未確認) | 公式表で確認できた最安は $1.25 / $10 (gpt-5.1) | 共有プログラムは学習利用が前提 | 不可(Codex 製品内に限る) | json_schema | `openai` |
| Google | あり(主要 Flash 系) | $0.10 / $0.40 (2.5 Flash-Lite) | 製品改善に利用・人によるレビューあり | 不可(AI Studio Web UI 内のみ) | JSON Schema サブセット | `@google/genai` |
| Groq | あり(RPD 制限つき) | $0.11 / $0.34 (Llama 4 Scout, 確度 低) | 公式記載を確認できず | — | OpenAI 互換 | OpenAI SDK 互換 |
| Cerebras | $5 クレジット | 公式単価を確認できず | 未確認 | — | OpenAI 互換 | OpenAI SDK 互換 |
| Mistral | あり(Experiment 枠, 上限値は未確認) | $0.5 / $1.5 (Mistral Large) | 無料枠のオプトアウト可否は未確認 | — | OpenAI 互換 | OpenAI SDK 互換 |
| OpenRouter | あり(`:free` モデル) | $0(`:free` 系) | ルーティング先プロバイダ次第 | — | 転送先モデル依存 | OpenAI SDK 互換 |
| Together AI | 登録時クレジットのみ(額は不確定) | $0.14 / $0.28 (DeepSeek V4 Flash, 未確認) | 未確認 | — | OpenAI 互換 | OpenAI SDK 互換 |
| DeepSeek | なし | $0.22 / $0.66 (v4-flash, オフピーク) | — | — | OpenAI 互換 | OpenAI SDK 互換 |
| xAI | $150/月クレジット(データ共有と引き換え, 確度 低) | $0.20 (Grok 4.1 Fast, 確度 低) | 学習利用に同意が条件 | — | OpenAI 互換 | OpenAI SDK 互換 |
| ローカル(Ollama / LM Studio / llama.cpp / MLX) | 無料 | $0(電気代のみ) | 端末外に出ない | — | OpenAI 互換で対応 | OpenAI SDK 互換 |

## 選ぶときの軸

- **課金** — トークン単価だけでなく、キャッシュ倍率・バッチ割引・長文脈の追加料金で実効コストが変わる。
- **無料枠** — 恒久枠か初回クレジットか。恒久枠があるのは Google・Groq・Mistral・OpenRouter。
- **データ利用** — 無料枠と有料枠でポリシーが変わるベンダーがある(Google が典型)。学習利用の有無、保持期間、ZDR の可否。
- **認証とサブスク転用の可否** — 個人のサブスク(Claude Pro/Max、ChatGPT Plus、Google AI Pro)を自作アプリの決済手段に転用できるか。Google は公式に不可、OpenAI は Codex 製品内限定、Anthropic はグレー。
- **構造化出力** — JSON Schema をどこまで受け付けるか(全機能かサブセットか)、ツール呼び出しと併用できるか。
- **SDK** — 公式 TypeScript SDK があるか、OpenAI 互換で済ませられるか。
- **ロックイン** — OpenAI 互換エンドポイントなら base_url の差し替えで移れる。独自 API・独自機能に寄せるほど移行コストが上がる。

## Anthropic

- 現行単価は Opus 5 = $5/$25、Sonnet 5 = $2/$10(2026-09-01 に予定されていた $3/$15 への値上げは撤回)、Haiku 4.5 = $1/$5、Fable 5.1 / Mythos 5.1 = $10/$50(https://platform.claude.com/docs/en/about-claude/pricing, 確認 2026-09-06, 確度 高)
- プロンプトキャッシュは 5 分書込 1.25x / 1 時間書込 2x / 読取 0.1x(Fable 5.1・Mythos 5.1 のみ読取 0.025x)。Batch 割引やデータレジデンシー倍率と併用できる(https://platform.claude.com/docs/en/about-claude/pricing, 確認 2026-09-06, 確度 高)
- Message Batches API は入出力とも 50% 割引(Opus 5 は $2.50/$12.50、Sonnet 5 は $1/$5、Haiku 4.5 は $0.50/$2.50)。キャッシュとの併用可(https://platform.claude.com/docs/en/about-claude/pricing, 確認 2026-09-06, 確度 高)
- 恒久的な無料枠はない。FAQ は "New users receive a small amount of free credits to test the API" とのみ記載(https://platform.claude.com/docs/en/about-claude/pricing, 確認 2026-09-06, 確度 高)
- 会話内容(プロンプトと出力)はデフォルトで保持されない。30 日保持は Fable 5.1 / Mythos 5.1 / Fable 5 / Mythos 5 という Covered Models 固有の必須要件で、これらは Anthropic の明示許可がない限り ZDR を選べない(https://platform.claude.com/docs/en/manage-claude/api-and-data-retention, 確認 2026-09-06, 確度 高)
- 学習利用について公式は "We will not use your chats or coding sessions to train our models, unless you choose to participate in our Development Partner Program." と記載(https://privacy.claude.com/en/articles/7996885-how-do-you-use-personal-data-in-model-training, 確認 2026-09-06, 確度 高)
- 2026-05-13 に発表された「Agent SDK / `claude -p` / サードパーティアプリをサブスク枠から切り離して月額クレジット制へ移す」変更は、施行日の 2026-06-15 当日に一時停止された。公式文言: "We're pausing the changes to Claude Agent SDK usage described below. For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription's usage limits." 再開の続報は 2026-09-06 時点で見つからない(https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan, ページ更新 2026-06-16, メインセッションが原文確認, 確度 高)
- 本番・共有用途には Agent SDK のサブスク認証ではなく API キーによる従量課金が案内されている(https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan, 確認 2026-09-06, 確度 中)
- 構造化出力は `output_config.format`(json_schema)とツールの `strict: true` の 2 機構。`enum` / `const` / `anyOf` / ローカル `$ref` は可、数値・文字列長の制約、再帰スキーマ、外部 `$ref`、`additionalProperties:true` は不可。ヘルパーは `messages.parse()`(Python)、`zodOutputFormat()`(TS)(https://platform.claude.com/docs/en/build-with-claude/structured-outputs, 確認 2026-09-06, 確度 高)
- 公式 SDK は Python `anthropic`、TypeScript `@anthropic-ai/sdk`(https://platform.claude.com/docs/en/get-started, 確認 2026-09-06, 確度 高)
- Claude 4.6 以降と Fable / Mythos 系は 1M トークンのコンテキストを標準価格のまま提供し、900k のリクエストも 9k と同単価(https://platform.claude.com/docs/en/about-claude/pricing, 確認 2026-09-06, 確度 高)
- 使用量ティアの月間支出上限は Start $500 / Build $1,000 / Scale $200,000。キャッシュ読取トークンは Haiku 3.5 を除き ITPM にカウントされない(https://platform.claude.com/docs/en/api/rate-limits, 確認 2026-09-06, 確度 高)

## OpenAI

- 公式料金表で確認できた単価: gpt-5.1 $1.25/$10、gpt-5.2 $1.75/$14、gpt-4.1 $2/$8、gpt-5.6-terra $2/$12、gpt-4o $2.50/$10、gpt-5.6-sol $4/$20、gpt-6-astra $10/$50、o1 $15/$60、o1-pro $150/$600(https://developers.openai.com/api/docs/pricing, 確認 2026-09-06, 確度 高)
- gpt-5-nano($0.05/$0.40)・gpt-4.1-mini・gpt-3.5-turbo・gpt-5.4-mini は再取得した料金表に現れず、掲載が消えたのか取得漏れか判別できない。**未確認**(https://developers.openai.com/api/docs/pricing, 確認 2026-09-06, 確度 低)
- GPT-6 Astra が 2026-09-03 に発表され ChatGPT 各 tier・API・AWS 経由で提供されるとされる。**未確認**(発表ページを取得できず)(https://openai.com/index/gpt-6-astra/, 2026-09-03, 確度 低)
- Batch API は同期呼び出しに対し 50% 割引、24 時間以内(多くはより早く)完了(https://developers.openai.com/api/docs/guides/batch, 確認 2026-09-06, 確度 高)
- 2023-03-01 以降、API に送ったデータはオプトインしない限り学習に使われない(https://developers.openai.com/api/docs/guides/your-data, 確認 2026-09-06, 確度 高)
- API 入出力は不正利用監視のためデフォルト最大 30 日保持。ZDR は要事前承認の適格顧客向けで、Assistants / Conversations など状態保持が前提のエンドポイントは対象外(https://developers.openai.com/api/docs/guides/your-data, 確認 2026-09-06, 確度 高)
- 「データ共有で無料トークン」プログラム(大規模モデル日次 1M、mini/nano 系 日次 10M)は、記事本文を取得できず現存も上限値も裏が取れていない。**未確認**(https://help.openai.com/en/articles/10306912-sharing-feedback-evaluation-and-fine-tuning-data-and-api-inputs-and-outputs-with-openai, 確認 2026-09-06, 確度 低)
- Codex cloud は ChatGPT サインインのみ対応、Codex CLI と IDE 拡張は API キーと ChatGPT サインインの両方に対応(https://learn.chatgpt.com/docs/auth, 確認 2026-09-06, 確度 中)
- API キーでのサインインは標準 API 従量課金、ChatGPT サインインはプラン内の利用枠を消費するとされる。**未確認**(記事本文を取得できず)(https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan, 確認 2026-09-06, 確度 低)
- 構造化出力は Responses / Chat Completions / Assistants / Fine-tuning / Batch で利用可。json_schema は gpt-4o-mini-2024-07-18 と gpt-4o-2024-08-06 以降のスナップショットのみで、それ以前は JSON mode だけ(https://developers.openai.com/api/docs/guides/structured-outputs, 確認 2026-09-06, 確度 高)
- 公式 SDK は Python も Node/TS も同名の `openai`(https://developers.openai.com/api/docs/libraries, 確認 2026-09-06, 確度 高)

## Google(Gemini)

- 無料枠は Gemini 3.8/3.7/3.6/3.5 Flash、3.5/3.1 Flash-Lite、2.5 Pro/Flash/Flash-Lite などにある一方、Gemini 3.1 Pro Preview・Omni Flash・Veo・Lyria は "Not available"(https://ai.google.dev/gemini-api/docs/pricing, 確認 2026-09-04, 確度 高)
- レート制限の具体値(RPM/TPM/RPD)は公式ドキュメントに載っておらず AI Studio のダッシュボードでのみ確認できる。公開されているのは支出ベースの階層(Tier 1 $10 / Tier 2 $50 / Tier 3 $200、10 分ローリング)だけ(https://ai.google.dev/gemini-api/docs/rate-limits, 確認 2026-09-02, 確度 高)
- 代表単価: 3.8 Flash $0.75/$3.75(2027-01 から $1.50/$7.50)、3.5 Flash $1.50/$9.00、3.5 Flash-Lite $0.30/$2.50、2.5 Pro $1.25/$10.00、2.5 Flash $0.30/$2.50、2.5 Flash-Lite $0.10/$0.40、3.1 Pro Preview $2.00〜$4.00/$12.00〜$18.00。バッチは概ね 50% 割引(https://ai.google.dev/gemini-api/docs/pricing, 確認 2026-09-04, 確度 高)
- 無料版の規約は "Google uses the content you submit to the Services and any generated responses to provide, improve, and develop Google products" とし、"human reviewers may read, annotate, and process your API input and output" と明記。機密情報を無料枠に投げないよう注意喚起がある(https://ai.google.dev/gemini-api/terms, 発効 2026-03-23, 確度 高)
- 有料版は "Google doesn't use your prompts ... or responses to improve our products"。ログは禁止用途の検知目的で短期保持のみ(https://ai.google.dev/gemini-api/terms, 発効 2026-03-23, 確度 高)
- EEA / 英国 / スイスのユーザーは無料利用でも有料相当の扱いが適用される(https://ai.google.dev/gemini-api/terms, 発効 2026-03-23, 確度 中)
- Google AI Pro/Ultra の特典は AI Studio の Web UI 内に限られ、API キー経由の利用は別課金と公式に明記されている(https://ai.google.dev/gemini-api/docs/google-ai-plans, 確認 2026-08-18, 確度 高)
- AI Studio は API キー認証、Vertex(Enterprise Agent Platform)は GCP サービスアカウント認証。公式は "Most developers should use the Gemini Developer API unless there is a need for specific enterprise controls" としている(https://ai.google.dev/gemini-api/docs/migrate-to-cloud, 確認 2026-09-02, 確度 高)
- 構造化出力は JSON Schema のサブセット。Pydantic / Zod でスキーマを書ける。ツール呼び出しと組み合わせた構造化出力は Gemini 3 系のみ(https://ai.google.dev/gemini-api/docs/structured-output, 確認 2026-09-02, 確度 高)
- 公式 SDK は `@google/genai`(npm)と `google-genai`(PyPI)。旧 `@google/generativeai` / `google-generativeai` は 2025-11-30 付で非推奨(https://ai.google.dev/gemini-api/docs/sdks, 確認 2026-09-06, 確度 高)
- モデル一覧ページ(Gemini 3 系と 2.5 系の併存)は今回の検証で再取得しておらず、料金ページからの間接確認にとどまる。**未確認**(https://ai.google.dev/gemini-api/docs/models, 確認 2026-09-04, 確度 低)

## その他のホスト型プロバイダ

- Groq の無料枠は Qwen / GPT-OSS 系が 30 RPM・1,000 RPD・8K TPM・200K TPD、Whisper 系が 20 RPM・2K RPD。Llama 3.3 70B は 2026-08-26 以降エンタープライズ専用に移行(https://console.groq.com/docs/rate-limits, 確認 2026-09-06, 確度 中)
- Groq のエンドポイントは `https://api.groq.com/openai/v1/` で OpenAI 互換(https://console.groq.com/docs/api-reference, 確認 2026-09-06, 確度 高)
- Groq の単価(Llama 4 Scout $0.11/$0.34、Maverick $0.50/$0.77)は公式ページが JS 描画で取得できず第三者集計による。無料枠の学習利用ポリシーも公式記載を確認できていない。**未確認**(https://console.groq.com/settings/billing/plans, 確認 2026-09-06, 確度 低)
- Cerebras はサインアップ後 $5 の無料クレジット、Developer ティアは $10 から(https://www.cerebras.ai/pricing, 確認 2026-09-06, 確度 中)
- Cerebras 無料枠の詳細レート制限(5 RPM・30K TPM・8,192 トークン上限)は参照 URL が 404 で正しい公式ページを特定できていない。**未確認**(https://inference-docs.cerebras.ai/support/rate-limits, 確認 2026-09-06, 確度 低)
- Mistral は Mistral Large $0.5/$1.5、バッチ 50% 割引、キャッシュ最大 90% 割引(https://mistral.ai/pricing, 確認 2026-09-06, 確度 中)。Medium 3.5 / Small 4 / Codestral の個別単価は再取得で確認できず **未確認**(確度 低)
- Mistral の無料 Experiment 枠の上限(1 req/秒、500,000 TPM、月間約 10 億トークン)は参照 URL が 404。**未確認**(https://help.mistral.ai/en/articles/225174-what-are-the-limits-of-the-free-tier, 確認 2026-09-06, 確度 低)
- OpenRouter の `:free` モデルは残高 $0 で 20 RPM・50 RPD、生涯 $10 以上の購入後は 1,000 RPD に緩和(1 分あたりは 20 のまま)(https://openrouter.ai/docs/api-reference/limits, 確認 2026-09-06, 確度 高)
- OpenRouter 自体は入出力を学習に使わないが、ルーティング先のプロバイダは独自方針で学習利用しうる(https://openrouter.ai/privacy, 確認 2026-09-06, 確度 高)。回避手段としての `data_collection:"deny"` 設定名は privacy ページ本文で確認できず **未確認**(確度 低)
- Together AI は `https://api.together.xyz/v1` で OpenAI SDK 互換(https://docs.together.ai/docs/openai-api-compatibility, 確認 2026-09-06, 確度 高)。登録時クレジット額(情報源により $1〜$25 と食い違う)、モデル別単価、無料枠のデータ利用ポリシーはいずれも **未確認**(https://www.together.ai/pricing, 確認 2026-09-06, 確度 低)
- DeepSeek に無料枠はない。2026-08-14 からピーク/オフピーク料金制、8/23 から週末もオフピーク扱い。ピークは UTC 月〜金 01:00-04:00 と 06:00-10:00。v4-flash は入力(キャッシュミス)$0.22/$0.44・出力 $0.66/$1.32、v4-pro は $0.66/$1.32・$1.98/$3.96(https://api-docs.deepseek.com/quick_start/pricing/, 確認 2026-09-06, 確度 高)
- DeepSeek は `https://api.deepseek.com` の OpenAI Format(https://api-docs.deepseek.com/quick_start/pricing/, 確認 2026-09-06, 確度 高)。ただし入出力を暗号化・匿名化のうえ学習に使いうる規約とされる点は原文で裏が取れていない。**未確認**(https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html, 確認 2026-09-06, 確度 低)
- xAI の月 $150 無料クレジットはデータ共有への同意が条件で、最低 $5 の利用実績が必要、オプトイン後の撤回不可とされる。単価(Grok 4.3 $1.25/$2.50 等)ともに公式ページを直接取得できていない。**未確認**(https://docs.x.ai, 確認 2026-09-06, 確度 低)

## ローカル LLM

- Ollama の構造化出力は "Structured outputs work through the OpenAI-compatible API via response_format" と公式に記載があり、互換エンドポイント経由で `response_format` が機能する(ネイティブ API 側は `format` パラメータ)。Ollama Cloud では構造化出力は非対応(https://docs.ollama.com/capabilities/structured-outputs, 確認 2026-09-06, 確度 中)
- LM Studio は `/v1/chat/completions` で OpenAI 形式の json_schema を受け付ける。GGUF は llama.cpp の grammar、MLX は Outlines で実装され、7B 未満の一部モデルは構造化出力に対応しない(https://lmstudio.ai/docs/developer/openai-compat/structured-output, 確認 2026-09-06, 確度 中)
- llama-server は `response_format`(json_object / json_schema)と GBNF grammar を別個のパラメータとして持つ。両者は独立した制約機構で、組み合わせ時の挙動はドキュメントからは読み取れない(https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md, 確認 2026-09-06, 確度 中)
- MLX(mlx-lm)は Apple Silicon のユニファイドメモリ上で CPU/GPU 間のコピーなしに動作する。GGUF は扱わず独自形式。mlx-community に約 4,800 の量子化済みモデルがあるとされるが今回再取得していない。**未確認**(https://github.com/ml-explore/mlx-lm, 確認 2026-09-06, 確度 低)
- Gemma 4 は 2026-04-02 に Apache 2.0 で公開され、Gemma 1〜3 の独自 Gemma Terms of Use から転換した。サイズ内訳(E2B / E4B / 26B MoE / 31B Dense)はブログ本文に明記がなく「エッジデバイスから 31B まで」としか書かれていない。**未確認**(https://opensource.googleblog.com/2026/03/gemma-4-expanding-the-gemmaverse-with-apache-20.html, 2026-04-02, 確度 高 / 内訳は 低)
- Gemma 3(1B/4B/12B/27B)は独自 Gemma Terms of Use。商用利用は可だが下流配布者への利用制限の転記義務や蒸留禁止が付く(https://ai.google.dev/gemma/terms, 最終更新 2026-04-01, 確度 高)
- Llama 4 は Meta の Community License。月間アクティブユーザー 7 億人超の企業は別途商用ライセンスが必要、派生モデル名に "Llama" 接頭辞と "Built with Llama" 表示の義務がある(https://developer.meta.com/ai/llama4/license/, 発効 2025-04-05, 確度 高)
- Qwen3 の dense 6 モデル(0.6B/1.7B/4B/8B/14B/32B)は Apache 2.0、2025-04-29 リリース。MoE 2 モデル(30B-A3B / 235B-A22B)はブログ上 "open-weighted" としか書かれておらず Apache 2.0 と断定できない。**未確認**(https://qwenlm.github.io/blog/qwen3/, 2025-04, 確度 中 / MoE ライセンスは 低)
- Mistral Small 3(24B)は 2025-01-30 に Apache 2.0 で公開(https://mistral.ai/news/mistral-small-3/, 2025-01-30, 確度 高)。Mistral 3 ファミリー(Ministral 3: 3B/8B/14B、Mistral Large 3: 675B 総 / 41B アクティブ・256K コンテキスト)は 2025-12-02 発表で全モデル Apache 2.0(https://mistral.ai/news/mistral-3/, 2025-12-02, 確度 高)
- メモリの概算は RAM(GB) ≈ パラメータ数(B) × バイト/パラメータ × 1.2 + コンテキスト分。Q4_K_M で 7B が約 4.1GB、13B が約 7.9GB。第三者サイトの目安(https://ggufloader.github.io/gguf-memory-calculator.html, 確認 2026-09-06, 確度 低)
- Claude Haiku 4.5 は入力 $1 / 出力 $5 per MTok、20 万トークンコンテキスト。ローカル小型モデルとの比較基準になる(https://claude.com/pricing, 確認 2026-09-06, 確度 高)

## グレーゾーン・未確認

- 自作アプリから Claude Pro/Max のサブスク認証(OAuth)を Agent SDK 経由で使うことが、個人利用限定なのか第三者配布・商用も許容されるのかは公式記事群に明文の規定がない。2026-06 に一時停止された課金変更は「撤回」ではなく、将来分離される可能性が残る。
- Claude Mythos 5.1 のキャッシュ読取価格が Fable 5.1 と同じ 0.025x になるかは公式脚注で "open at launch" とされ未確定。ZDR の申請条件・審査基準も個人開発者向けの記述がない。
- OpenAI の新規アカウント $5 トライアルクレジットの現況、データ共有プログラムの現存と上限、ChatGPT サブスクを第三者アプリの決済手段に開放する計画の進捗は、いずれも公式一次情報で確認できていない。Batch 50% 割引が全モデル一律かも未確認。
- Gemini のレート制限の実数値は AI Studio ログイン後にしか見えず、事前見積もりができない。Google AI Pro/Ultra の月額は情報源により表記が食い違う。コンテキストキャッシュのモデル別内訳も未取得。
- Groq / Cerebras / Together AI / Mistral の無料枠における学習データ利用ポリシーは、いずれも公式ページで確認できなかった。DeepSeek の有料アカウントが学習対象外になっているかも原文未確認。
- ローカル小型モデル(7B〜24B)とホスト型 Haiku / Flash 級の品質・レイテンシを直接比較した公式ベンチマークは存在しない。存在するのは第三者比較のみ。
- 検証で落とした記述: Anthropic の「API 入出力は原則 30 日で自動削除」(実際はデフォルト保持なし)、「フィードバック送信で学習利用され得る」(実際は Development Partner Program 参加時のみ)、Ollama の「OpenAI の response_format は無視される場合がある」(互換エンドポイントでは機能する)。
- 今回の調査が触れていない論点: 日本など米国外からの支払い・請求(インボイス、消費税)、埋め込みモデルの価格と無料枠、ファインチューニングの提供状況、マルチモーダル入力のトークン換算、モデル廃止の通知期間、SLA と障害時の返金、生成物の著作権補償、EU AI Act 対応、Windows/Linux + NVIDIA でのローカル要件、チーム開発時の SSO / キー権限分離、日本語トークナイザ効率と日本語ベンチマーク。
