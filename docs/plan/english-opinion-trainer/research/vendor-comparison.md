# LLM ベンダー比較（Anthropic / OpenAI / Google の小型・高速モデル）

- 調査日: 2026-09-07
- 調査手段: Sonnet サブエージェント 3 体（1 社 1 体）による机上調査 + メインによる原典確認
- 問い: 3 社（Anthropic / OpenAI / Google）の小型・高速モデルを、コストパフォーマンス・応答速度・スキーマ制約つき構造化出力の強さ・有料 API のデータ利用・支出上限（公開アプリの鍵の保護）の 5 軸で比べると何が分かるか。

## 結論

推奨・決定は書かない。決定は decisions.md。以下は事実の整理のみ。

| 軸 | Anthropic（Haiku 4.5） | OpenAI（gpt-5 / 5.4 系 mini・nano） | Google（Gemini 3.x Flash / Flash-Lite） |
|---|---|---|---|
| コストパフォーマンス | 入力 $1・出力 $5 /MTok。キャッシュ読取り 0.1 倍、バッチ 50% 引き併用可（確度高） | mini: 入力 $0.75・出力 $4.50、nano: 入力 $0.20・出力 $1.25 /1M。キャッシュ入力 90% 引き、バッチ 50% 引き（確度高） | Flash-Lite: 入力 $0.30・出力 $2.50、Flash: 入力 $0.75・出力 $3.75（2026-12-31 まで、2027 年から倍増）/1M。キャッシュ・バッチ 50% 引きあり（確度高） |
| 応答速度 | 公式は「Fastest」という相対順位のみ。TTFT・tok/s の絶対値は非公開（確度高＝非公開という事実） | 公式に定量値なし。第三者ベンチマーク（Artificial Analysis）で nano TTFT 0.67s/162tok/s、mini TTFT 0.69s/157tok/s（確度中、未訪問の要約経由） | 公式に TTFT 言及なし。Google 自身が Flash-Lite ページで第三者ベンチマーク値「350 output tokens per second according to the Artificial Analysis Index」を引用（確度中） |
| 構造化出力の強さ | `output_config.format` が GA、Haiku 4.5 対応、constrained decoding により違反が構造的に発生しないと明記。数値・文字列長制約は非対応（確度高、メインが原典を確認） | `text.format={type:"json_schema", strict:true}` でスキーマ準拠を保証。ただし公式の対応モデル一覧は gpt-4o-mini, gpt-4o-2024-08-06 以降までで、gpt-5/5.4 系 mini・nano の名指しは確認できず（確度中、メインが原典を確認） | `responseSchema` は構文的な JSON の正しさのみ保証、値の意味的正しさは保証しない。巨大・深いネストは拒否されうる（確度高） |
| 有料 API のデータ利用 | 有料 API 入出力はデフォルトで学習に使わない。標準保持は受信/生成から 30 日以内に自動削除（確度高） | 2023-03-01 以降デフォルトで学習に使わない。保持は最大 30 日（不正利用監視用）（確度高） | 有料枠は「製品改善に使わない」「人レビューの言及なし」、違反検知目的で一定期間ログ保持のみ。無料枠は製品改善に使い、人レビューもある（確度高、メインが原典を確認） |
| 支出上限（鍵の保護） | 組織単位・ワークスペース単位で支出上限/レート制限を設定可能。上限到達で 400 または 429。API キー単体の上限機能は一次情報上見当たらず（確度高） | 組織単位・プロジェクト単位で hard limit を設定可能。到達時 429（`organization_spend_limit_exceeded`/`project_spend_limit_exceeded`）。プロジェクト単位はそのプロジェクトの課金トラフィックのみに適用。キー単位の言及なし（確度高、メインが原典を確認） | Google Cloud の支出上限（spend cap）で Gemini API を対象サービスに指定可能。100% 到達で新規利用を自動ブロック（手動解除のみ）。キー保護は IP 制限・API 制限が明記（確度高） |

この比較から分かること・分からないこと:

- 応答速度は 3 社とも公式の絶対値（TTFT・tok/s）を一切公開していない。今回引用した数値はすべて第三者ベンチマーク（Artificial Analysis）由来で、いずれも本調査では原典（artificialanalysis.ai）を直接訪問していない。実装時の実測が前提になる。
- 有料 API の入力をデフォルトで学習に使わない点は 3 社共通。ただし Google だけは「有料/無料の境界」が Cloud Billing アカウントの有無で決まる二層構造を持ち、無料枠を使うと人レビューが入る点が他社にはない特徴。
- 構造化出力の保証の強さは 3 社で差がある。Anthropic は一次資料で「constrained decoding により違反が構造的に発生しない」という設計上の保証を明記し、Haiku 4.5 も対応モデルに含まれることを確認した。OpenAI は strict モードの仕組み自体は一次資料で明確だが、対応モデル一覧に gpt-5/5.4 系の mini・nano が名指しされておらず、実機検証が必要な状態。Google は構文的な JSON の正しさのみを保証し、値の意味的な正しさ（スキーマの制約の種類も含め）は保証しないと明記している。
- 支出上限はベンダーごとに設計が異なる。Anthropic は組織/ワークスペース単位、OpenAI は組織/プロジェクト単位で 429 を返す仕組み、Google は Cloud の支出上限（spend cap）で新規利用そのものを遮断する仕組み。3 社とも API キー単体に紐づく上限機能は確認できなかった。

## 根拠

### (1) コストパフォーマンス（単価・キャッシュ・バッチ割引）

**Anthropic（Haiku 4.5）**

- 事実: 入力 $1/MTok、出力 $5/MTok。
  - URL: https://platform.claude.com/docs/en/models/haiku-4-5/overview ／ https://platform.claude.com/docs/en/about-claude/pricing
  - 出典日付: 記載なし
  - 確度: 高
- 事実: プロンプトキャッシュは 5 分書込み 1.25 倍、1 時間書込み 2 倍、読取り（ヒット）0.1 倍。「These multipliers stack with other pricing modifiers, including the Batch API discount」でバッチ割引と併用可能。
  - URL: https://platform.claude.com/docs/en/about-claude/pricing
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Batch API は入出力とも標準価格の 50% 引き（Haiku 4.5 でバッチ入力 $0.50/MTok、バッチ出力 $2.50/MTok）。
  - URL: https://platform.claude.com/docs/en/about-claude/pricing
  - 出典日付: 記載なし
  - 確度: 高
- 事実: ツール利用時にシステムプロンプトの固定トークン（Haiku 4.5 は `auto`/`none` で 496 トークン、`any`/`tool` で 588 トークン）が加算される。新規ユーザーには少額の無料クレジットが付与される（恒久無料枠ではない）。
  - URL: https://platform.claude.com/docs/en/about-claude/pricing
  - 出典日付: 記載なし
  - 確度: 高

**OpenAI（gpt-5 / 5.4 系 mini・nano）**

- 事実: gpt-5.4-mini 入力 $0.75/1M・キャッシュ入力 $0.075/1M・出力 $4.50/1M。gpt-5.4-nano 入力 $0.20/1M・キャッシュ入力 $0.02/1M・出力 $1.25/1M。gpt-5-mini 入力 $0.25/1M・キャッシュ入力 $0.025/1M・出力 $2.00/1M。gpt-5-nano 入力 $0.05/1M・キャッシュ入力 $0.005/1M・出力 $0.40/1M（世代が新しいほど値上がり）。
  - URL: https://developers.openai.com/api/docs/pricing
  - 出典日付: 記載なし
  - 確度: 高（公式価格表を直接取得して確認）
- 事実: バッチ API 割引は標準料金比で一律 50% 引き。キャッシュ入力割引は標準入力価格からおよそ 90% 引き（例: gpt-5.4-mini は $0.75→$0.075）。
  - URL: https://developers.openai.com/api/docs/pricing
  - 出典日付: 記載なし
  - 確度: 高

**Google（Gemini 3.x Flash / Flash-Lite）**

- 事実: Gemini 3.8 Flash は入力 $0.75/100 万トークン・出力 $3.75/100 万トークン（2026-12-31 まで。2027-01-01 以降は入力 $1.50・出力 $7.50 に倍増）。コンテキストキャッシュ $0.075/100 万トークン + $0.50/100 万トークン/時間ストレージ。バッチ API は入出力とも 50% 引き（入力 $0.375・出力 $1.875）。
  - URL: https://ai.google.dev/gemini-api/docs/pricing
  - 出典日付: 2026-09-04（ページ末尾表示）
  - 確度: 高
- 事実: Gemini 3.5 Flash-Lite は入力 $0.30/100 万トークン（テキスト/画像/動画/音声で統一単価）・出力 $2.50/100 万トークン。コンテキストキャッシュ $0.03/100 万トークン + $1.00/100 万トークン/時間ストレージ。バッチ API は 50% 引き（入力 $0.15・出力 $1.25）。
  - URL: https://ai.google.dev/gemini-api/docs/pricing
  - 出典日付: 2026-09-04
  - 確度: 高
- 事実: 無料枠は「Free input & output tokens」「Limited access to certain models」（Flash）、「Free of charge」「Limited access to certain models」（Flash-Lite）と記載。具体的な RPM/TPM/RPD 上限値は pricing ページには出ていない。
  - URL: https://ai.google.dev/gemini-api/docs/pricing
  - 出典日付: 2026-09-04
  - 確度: 高（記載の存在について）／中（無料枠の詳細数値は本ページになし）
- 事実: 有料/無料の境界は「Google AI Studio へのアクセスに使っているアカウントが、有効な Cloud Billing アカウントに紐づいた Cloud Project へのアクセス権を持つ場合」は無料機能でも Paid Service 扱いになる、という定義。
  - URL: https://ai.google.dev/gemini-api/terms
  - 出典日付: 記載なし（メインの確認では Last Updated 2026-04-28 UTC）
  - 確度: 高

### (2) 応答速度

**Anthropic**

- 事実: Claude Haiku 4.5 は「The fastest model with near-frontier intelligence」と紹介。モデル比較表の Latency 列は Haiku 4.5 が "Fastest"、Sonnet 5 が "Fast"、Opus 5 が "Moderate"、Fable 5.1 が "Slower" という相対順位のみ。表の注記は「Comparative latency, relative to the current lineup, as published in the models overview. Actual latency depends on prompt length, output length, and thinking effort.」で、具体的な TTFT や tokens/秒の数値は記載されていない。
  - URL: https://platform.claude.com/docs/en/models/haiku-4-5/overview
  - 出典日付: 記載なし（"Released October 15, 2025" の記載あり）
  - 確度: 高（「数値非公開」という事実自体は一次情報で確認済み）
- 事実: 「レイテンシ削減」ページは Time to First Token（TTFT）と Baseline latency の用語定義はあるが、Haiku 4.5 については「offers the fastest response times while maintaining high intelligence」という定性的な記述のみで、数値ベンチマークは掲載されていない。
  - URL: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency
  - 出典日付: 記載なし
  - 確度: 高

**OpenAI**

- 事実: OpenAI 公式のモデルページ（gpt-5-mini, gpt-5.4-mini, gpt-5.4-nano）には TTFT・トークン/秒などの定量的レイテンシ指標の記載がない。「faster, more cost-efficient」「designed for tasks where speed and cost matter most」といった定性的表現のみ。
  - URL: https://developers.openai.com/api/docs/models/gpt-5-mini ／ https://developers.openai.com/api/docs/models/gpt-5.4-mini ／ https://developers.openai.com/api/docs/models/gpt-5.4-nano
  - 出典日付: 記載なし（gpt-5-mini は knowledge cutoff 2025-08-07 の表記あり）
  - 確度: 高（「数値記載がない」という事実についてのみ）
- 事実: 第三者ベンチマーク Artificial Analysis によれば、GPT-5.4 nano（Non-Reasoning）TTFT 0.67 秒・出力速度 162.0 tok/s、GPT-5.4 mini（Non-Reasoning）TTFT 0.69 秒・出力速度 157.2 tok/s、旧世代 GPT-5 mini TTFT 0.98 秒・出力速度 101.9 tok/s。
  - URL: https://artificialanalysis.ai/models/gpt-5-4-nano-non-reasoning/providers ／ https://artificialanalysis.ai/models/gpt-5-4-mini-non-reasoning/providers
  - 出典日付: 記載なし
  - 確度: 中（第三者ベンチマークのみ、WebSearch 経由の要約で原典未訪問）

**Google**

- 事実: Gemini 3.5 Flash-Lite の紹介ページで Google は「350 output tokens per second according to the Artificial Analysis Index」という第三者ベンチマーク由来の数値を自ら引用している。また「3.5 Flash-Lite executes high volume tasks at a lower latency than 3.5 Flash」という相対比較の記述がある。
  - URL: https://deepmind.google/models/gemini/flash-lite/
  - 出典日付: 記載なし
  - 確度: 中（Google 公式ページだが数値自体は第三者ベンチマークの引用）
- 事実: 同ページには TTFT（time to first token）の公式言及はない。
  - URL: https://deepmind.google/models/gemini/flash-lite/
  - 出典日付: 記載なし
  - 確度: 高（「記載がない」ことの確認）
- 事実: 「Gemini 3.1 Flash Lite は 2.5 Flash 比で TTFT が 2.5 倍速い」という言明が検索結果に現れたが、Google の一次資料で直接確認できていない。
  - URL: 未特定（検索結果の要約、原典未訪問）
  - 出典日付: 記載なし
  - 確度: 低
- 事実: Artificial Analysis の独自計測値として「Gemini 3.1 Flash-Lite で 381.9 tok/s、TTFT 5.33 秒 on Google AI Studio」という数値が検索結果に現れたが、第三者サイトであり原典未訪問。
  - URL: https://artificialanalysis.ai/models/gemini-3-1-flash-lite-preview（未訪問、検索要約のみ）
  - 出典日付: 記載なし
  - 確度: 低

### (3) 構造化出力（スキーマ制約つき JSON）

**Anthropic**

- 事実（メインが原典を確認）: 構造化出力は GA（一般提供）で、パラメータは `output_config.format`。対応モデル一覧に `claude-haiku-4-5-20251001` が含まれる。「Structured outputs guarantee schema-compliant responses through constrained decoding」「Always valid: No more JSON.parse() errors」「Reliable: No retries needed for schema violations」。非対応: recursive schemas、数値制約（minimum/maximum/multipleOf）、文字列制約（minLength/maxLength）、minItems 0/1 を超える配列制約、`false` 以外の `additionalProperties`、外部 `$ref`。「If you use an unsupported feature, you'll receive a 400 error with details」。
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高（メインが原典を確認）
- 事実: 構造化出力には 2 系統ある。① `output_config.format`（`type: "json_schema"`）でレスポンス全体を JSON Schema に制約する「JSON outputs」、② `strict: true` をツール定義に付ける「Strict tool use」。旧ベータヘッダー（`structured-outputs-2025-11-13`）と旧パラメータ `output_format` は後方互換で残るが非推奨。
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高
- 事実: サポートされる JSON Schema 機能は object/array/string/integer/number/boolean/null の基本型、`enum`（文字列・数値・真偽値・null のみ）、`const`、`anyOf`・`allOf`（`allOf`＋`$ref` の組合せは不可）、`$ref`/`$def`/`definitions`（外部 `$ref` は不可）、`required`、`additionalProperties`（object では `false` 必須）、文字列フォーマット（date-time/time/date/duration/email/hostname/uri/ipv4/ipv6/uuid）、配列の `minItems`（0 と 1 のみ）。
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 初回リクエスト時にスキーマの「グラマー」コンパイルでレイテンシが増える。コンパイル済みグラマーは 24 時間キャッシュされ、スキーマ構造やツールセットの変更でキャッシュが無効化される。
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 中（AI 要約経由、一次ページの該当箇所は未直接確認）
- 事実: データ保持の観点（HIPAA/PHI 文脈）で、構造化出力・strict tool use 使用時、JSON Schema 自体は最大 24 時間キャッシュされる。プロンプト・レスポンス本文は保存されないが、スキーマ（プロパティ名・`enum`値・`const`値・`pattern`正規表現）にはプロンプトと同じ保護が適用されないため PHI を含めるべきでないと明記。
  - URL: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
  - 出典日付: 記載なし
  - 確度: 高

**OpenAI**

- 事実（メインが原典を確認）: `text.format = {type: "json_schema", strict: true, schema: ...}` を指定する。対応モデルの公式記載は「Structured Outputs is available in our latest large language models, starting with GPT-4o」「Compatible models: gpt-4o-mini, gpt-4o-2024-08-06, and later」で、gpt-5-mini/nano や gpt-5.4-mini/nano を名指しした対応表は確認できなかった。
  - URL: https://developers.openai.com/api/docs/guides/structured-outputs
  - 出典日付: 記載なし
  - 確度: 中（"and later" の解釈次第で mini/nano を含むかどうかがグレー。メインが原典を確認したうえでの評価）
- 事実: 「モデルは常に指定した JSON Schema に準拠した応答を生成する」ことを保証し、必須キーの欠落や不正な enum 値の幻覚を防ぐと明記。strict モードの要件は、すべてのオブジェクトで `additionalProperties: false` が必須、`required` フィールドの明示的宣言が必要。
  - URL: https://developers.openai.com/api/docs/guides/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 失敗時の挙動として、モデルが応答を拒否した場合はスキーマに沿わない `refusal` フィールドが応答に追加される。`max_output_tokens` 超過や `content_filter` トリガー時は `status: "incomplete"` として区別される。拒否以外の正常応答はスキーマ準拠が保証される。
  - URL: https://developers.openai.com/api/docs/guides/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 第三者情報の集約によれば、文字列側の minLength/maxLength/pattern/format、数値側の minimum/maximum/multipleOf、オブジェクト側の patternProperties/unevaluatedProperties/propertyNames/minProperties/maxProperties、配列側の minItems/maxItems/uniqueItems/contains 等は非対応。ネスト深さ上限 5 階層、オブジェクトプロパティ総数上限 100 が言及されている。
  - URL（第三者）: https://www.codewords.ai/blog/openai-structured-outputs-json-schema 等の集約情報
  - 出典日付: 記載なし
  - 確度: 中（第三者情報。公式ページからの直接引用としての確認はできず）

**Google**

- 事実: サポートされる型は string, number, integer, boolean, object, array, null。サポートされるキーワードは title, description, properties, required, additionalProperties（object）、enum・format（date-time/date/time、string）、enum・minimum・maximum（number/integer）、items・prefixItems・minItems・maxItems（array）、`$ref`（自己参照 `"$ref": "#"` の例あり）、anyOf（条件分岐スキーマの例あり）。
  - URL: https://ai.google.dev/gemini-api/docs/generate-content/structured-output
  - 出典日付: 記載なし
  - 確度: 中（一次資料だが WebFetch 経由の要約であり、フィールド名表記に揺れがある）
- 事実: 「非常に大きい、または深くネストしたスキーマは API が拒否する場合がある（"The API may reject very large or deeply nested schemas"）」。エラー時はプロパティ名を短くする、ネストを減らす、制約数を減らすといった簡略化を試みるよう案内。
  - URL: https://ai.google.dev/gemini-api/docs/generate-content/structured-output
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「構造化出力は構文的に正しい JSON を保証するが、値が意味的に正しいことは保証しない（"structured output guarantees syntactically correct JSON, it does not guarantee the values are semantically correct"）」。失敗時の自動リトライやエラー訂正の明記はなし。
  - URL: https://ai.google.dev/gemini-api/docs/generate-content/structured-output
  - 出典日付: 記載なし
  - 確度: 高
- 事実: propertyOrdering は Gemini 2.0 系モデルで明示指定が必要と記載されているが、最新の Flash/Flash-Lite（3.x 系）での要否はフェッチ結果からは明確でない。
  - URL: https://ai.google.dev/gemini-api/docs/generate-content/structured-output
  - 出典日付: 記載なし
  - 確度: 低（推測を含む）

### (4) 有料 API のデータ利用ポリシー

**Anthropic**

- 事実: 「デフォルトでは、商用製品（Claude for Work、Anthropic API、Claude Gov 等）からの入出力をモデル学習に使用しません（By default, we will not use your inputs or outputs from our commercial products ... to train our models）」。例外はユーザーが明示的にフィードバック（thumbs up/down）を送った場合のみで、組織管理者が無効化可能。
  - URL: https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
  - 出典日付: 「Updated over 2 weeks ago」表示のみ（具体的日付記載なしに近い）
  - 確度: 高
- 事実: Claude API の一般的な保持ポリシー（ZDR 契約なしの場合）は「バックエンド上で入出力を受信/生成から 30 日以内に自動削除する（we automatically delete inputs and outputs on our backend within 30 days of receipt or generation）」。長期保持サービスの利用、特別契約、ポリシー違反対応、法令順守の場合は例外。
  - URL: https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
  - 出典日付: 2026-07-01（"Last Updated" 表示）
  - 確度: 高
- 事実: 開発者向け「API and data retention」ページでは「会話内容（プロンプトとレスポンス）はデフォルトでは保持されない。例外は Covered Models（Fable 5.1 / Mythos 5.1 / Fable 5 / Mythos 5）で 30 日保持が必須」と記載。Haiku 4.5 は Covered Models に含まれない。
  - URL: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
  - 出典日付: 記載なし
  - 確度: 高
- 事実: ZDR（Zero Data Retention）は組織単位で個別に有効化が必要（営業窓口への申請制、セルフサーブ不可）。ZDR は Messages/Token Counting API の主要機能に適用されるが、Batch 処理・Files API・Code execution・MCP connector・Claude Managed Agents などステートフルな機能は対象外。構造化出力／strict tool use は「Yes (qualified)」＝プロンプト・レスポンス本文は保存されないが JSON Schema 自体は最大 24 時間キャッシュされるという限定付き。
  - URL: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
  - 出典日付: 記載なし
  - 確度: 高

**OpenAI**

- 事実: 「2023 年 3 月 1 日以降、OpenAI API に送信されたデータはモデルの学習・改善に使用されない（明示的にデータ共有をオプトインしない限り）」。デフォルトの保持期間は大半のエンドポイントで不正利用監視のため最大 30 日間、その後は法的保持義務がない限りシステムから削除。
  - URL: https://developers.openai.com/api/docs/guides/your-data
  - 出典日付: 記載なし（ポリシー適用開始日として 2023-03-01 が本文中に明記）
  - 確度: 高
- 事実: ZDR（ゼロデータ保持）は事前承認制。適格顧客は不正利用監視ログからも顧客コンテンツを除外可能。承認を得るには営業チームへの問い合わせが必要。有効化されると `store` パラメータを明示的に true にしても false 扱いになる。
  - URL: https://developers.openai.com/api/docs/guides/your-data
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 企業向けプライバシーページの補強情報として「OpenAI は ChatGPT Enterprise/Business/Edu 等および API プラットフォームの入出力データを、デフォルトではモデルの学習・改善に使用しない」「適格な組織は ZDR を含むデータ保持期間を設定できる」との記載。ただし openai.com/enterprise-privacy/ と openai.com/business-data/ は直接フェッチが 403 で拒否されたため、WebSearch のスニペット経由での確認にとどまる。
  - URL: https://openai.com/enterprise-privacy/ ／ https://openai.com/business-data/（直接アクセス不可、検索結果スニペット経由）
  - 出典日付: 記載なし
  - 確度: 中

**Google**

- 事実（メインが原典を確認）: Paid Services について「Google doesn't use your prompts (including associated system instructions, cached content, and files such as images, videos, or documents) or responses to improve our products」、および「logs prompts and responses for a limited period of time, solely for detecting and preventing violations of the Prohibited Use Policy」。Unpaid Services については「Google uses the content you submit to the Services and any generated responses to provide, improve, and develop Google products and services and machine learning technologies」、「human reviewers may read, annotate, and process your API input and output」、そして警告として「Do not submit sensitive, confidential, or personal information to the Unpaid Services」。Paid の定義は「Google AI Studio へのアクセスに使っているアカウントが、有効な Cloud Billing アカウントに紐づいた Cloud Project へのアクセス権を持つ場合」。
  - URL: https://ai.google.dev/gemini-api/terms
  - 出典日付: Last Updated 2026-04-28 UTC（メインの確認で判明。サブエージェントの一次フェッチでは日付欄が「記載なし」だった）
  - 確度: 高（メインが原典を確認）
- 事実: 利用規約は無料枠について「機密情報・個人情報を Unpaid Services に送信しないこと」と明記して注意喚起している（上記メイン確認と同一文言）。
  - URL: https://ai.google.dev/gemini-api/terms
  - 出典日付: Last Updated 2026-04-28 UTC
  - 確度: 高

### (5) 支出上限・レート制限（公開アプリの鍵の保護）

**Anthropic**

- 事実: 「Spend limits（支出上限）」は組織が月あたりに使える最大コスト、「Rate limits（レート制限）」は一定期間あたりの最大リクエスト数を定めるもの。使用ティアごとの月次支出上限は Start $500、Build $1,000、Scale $200,000。Custom ティアは上限なし（個別契約）。
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 組織はティア上限以下で自分で支出上限を設定可能（Console > Settings > Billing > Spend limits > Adjust limit）。設定した上限に達すると HTTP 400（`invalid_request_error`）を返す。ティア自体の上限（サービス側の強制上限）に達した場合は HTTP 429（`rate_limit_error`、`error_code: enforced_spend_limit_reached`）を返し、翌月 1 日 00:00 UTC まで利用停止（ティア引き上げ申請で早期回復可）。
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高
- 事実: レート制限は RPM・ITPM・OTPM でモデルごとに設定。Start tier での Haiku 4.5 は RPM 1,000 / ITPM 2,000,000 / OTPM 400,000。超過時は 429 エラーと `retry-after` ヘッダーが返る。
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高
- 事実: ワークスペース単位で支出・レート制限を個別に設定可能（組織全体の制限より低い値のみ設定可、デフォルトワークスペースには設定不可）。「他のワークスペースの過剰利用から保護するため」の仕組みとして説明されている。
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Spend Limits API という管理者向け API があり、組織のデフォルト支出上限のほか、メンバー単位（per-user）のオーバーライドを `POST /v1/organizations/spend_limits` で設定できる。ただし「Claude Code workspace のみがユーザー単位の月次支出上限をサポートする」と明記されており、一般の pay-as-you-go ワークスペースでのユーザー単位上限には言及がない。
  - URL: https://platform.claude.com/docs/en/manage-claude/spend-limits-api（WebSearch の AI 要約経由、原文未直接確認）
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 個々の API キー単体に紐づく支出上限・レート制限の機能は、一次情報（rate-limits ページ、pricing ページ）上に見当たらなかった。支出・レート制限は一貫して「組織」または「ワークスペース」の単位で設定するものとして説明されている。
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高（消極的事実の確認）
- 事実: ZDR 契約下では CORS がサポートされない（ブラウザから直接 API を呼べない）ため、バックエンドプロキシ経由が必要と明記。
  - URL: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
  - 出典日付: 記載なし
  - 確度: 高

**OpenAI**

- 事実（メインが原典を確認）: 組織単位・プロジェクト単位それぞれで spend limit（月次支出上限）を設定可能。「hard limit」を有効化すると、上限到達時に該当 API リクエストが 429 エラーを返し、「affected API requests return a 429 error with the organization_spend_limit_exceeded or project_spend_limit_exceeded code」。プロジェクト単位の hard limit は「only to API traffic billed to that project」に適用される。per-API-key の上限は本ページに言及なし。
  - URL: https://developers.openai.com/api/docs/guides/spend-limits
  - 出典日付: 記載なし
  - 確度: 高（メインが原典を確認）
- 事実: 計測の即時性の限界により、実際の消費が設定額をわずかに超過してから遮断される場合がある、との注記あり。spend alert（通知のみ）と hard spend limit（遮断あり）は独立して併用可能。
  - URL: https://developers.openai.com/api/docs/guides/spend-limits
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「Projects」機能により 1 組織内で複数プロジェクトに分割し、それぞれ個別の予算・API キー・モデル権限を割り当て可能（例: ステージング環境の暴走がプロダクション環境の与信を消費しない構成にできる）。
  - URL: https://developers.openai.com/api/docs/guides/spend-limits
  - 出典日付: 記載なし
  - 確度: 高
- 事実: レート制限は RPM/RPD（リクエスト数）、TPM/TPD（トークン数）、画像系は IPM。利用ティアは累計支払額に応じて自動昇格し（例: Free tier 月 $100 上限、上位ティアほど上限拡大）、この「OpenAI 承認済み利用上限」は自分で設定する spend limit とは別物。
  - URL: https://developers.openai.com/api/docs/guides/rate-limits
  - 出典日付: 記載なし
  - 確度: 高

**Google**

- 事実（メインが原典を確認）: Google Cloud の「支出上限（spend cap）」予算で Gemini API を対象サービスに指定可能。累計支出が 50%・80% に達するとメール通知、100% に達すると「対象サービス・対象プロジェクトの新規利用がすべてブロックされる（"all new usage for the specific service in the specified project is blocked"）」。進行中のリクエストは完了まで処理され、解除は手動のみ。実コストの反映には最大 24 時間超のラグがある旨も明記。
  - URL: https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps
  - 出典日付: 記載なし
  - 確度: 高（Gemini API が対象サービスに明示的に含まれることを確認）
- 事実（メインが原典を確認）: API キー保護について「本番環境でクライアントサイドにキーを直接埋め込むな（"Never expose keys client-side in production: Do not hardcode API keys directly in web or mobile apps"）」「クライアントサイドアプリを保護するにはバックエンドプロキシサーバーを経由して実際の API 呼び出しを行え（"run a backend proxy server to make the actual API calls"）」と明記。制限手段として IP アドレス制限、および Generative Language API（Gemini API）のみに絞る API 制限が挙げられている。
  - URL: https://ai.google.dev/gemini-api/docs/api-key
  - 出典日付: 記載なし
  - 確度: 高
- 事実: レート制限の階層は Free / Tier 1（有効な課金設定必須、上限 $250）/ Tier 2（累計 $100 以上の支払い + 初回支払いから 3 日経過、上限 $2,000）/ Tier 3（累計 $1,000 以上 + 初回支払いから 30 日経過、上限 $20,000〜$100,000+）の 4 段階。Free から Tier 1 への昇格は即時、以降の昇格は 10 分以内に反映されるとされる。
  - URL: https://ai.google.dev/gemini-api/docs/rate-limits
  - 出典日付: 記載なし
  - 確度: 中（WebFetch 要約経由。数値そのものは明確に引用されている）
- 事実: 支出ベースのレート制限が 10 分のローリングウィンドウで働き、超過時は `429 RESOURCE_EXHAUSTED` を返すと記載されている。
  - URL: https://ai.google.dev/gemini-api/docs/rate-limits
  - 出典日付: 記載なし
  - 確度: 中

## グレーゾーン・未確認

**3 社共通**

- 応答速度は 3 社とも公式の絶対値（TTFT・tok/s）を持たない。今回引用した数値はすべて第三者ベンチマーク（Artificial Analysis）由来で、いずれも本調査では原典（artificialanalysis.ai）を直接訪問していない。確度は低〜中にとどまる。
- 個々の API キー単体（プロジェクト/ワークスペースより下の粒度）に紐づく支出上限・レート制限機能は、3 社いずれの一次情報にも見当たらなかった。公開アプリの鍵漏洩に対する保護は、3 社とも「組織/プロジェクト/ワークスペース単位で分離する」設計が前提になる。

**Anthropic**

- 標準保持期間について、一次情報（Privacy Center、2026-07-01 更新）は「30 日以内に自動削除」と明記する一方、WebSearch で見つかった第三者記事（anarlog.so 等）は「2025 年 9 月 14 日付で API ログ保持期間が 30 日から 7 日に短縮された」と主張しており矛盾する。今回確認した一次ページ（プライバシーセンター、開発者向け data-retention ページ）には 7 日短縮の記述は見当たらず、確認できなかった。
- 構造化出力の対応モデル一覧・失敗時挙動の一部細部（400 エラーの詳細条件、24 時間グラマーキャッシュの挙動）は WebFetch の AI 要約経由の確認が残っており、原文ページの該当箇所を一字一句までは再確認していない。
- API キー単位の支出保護の実務パターン（専用ワークスペースを切るのが公式推奨か）は、一次情報上「他ワークスペースの過剰利用から保護する」目的としか説明されておらず、公開アプリのキー漏洩シナリオを名指しした記述は見当たらなかった。
- Spend Limits API の per-user オーバーライドがどこまで一般ワークスペースに適用されるかは、「Claude Code workspace のみがユーザー単位の月次支出上限をサポートする」という WebSearch 経由の情報のみで、原文（spend-limits-api ページ）は未直接確認。
- バッチ割引とキャッシュ割引の併用で「非キャッシュ標準リクエストの 5% 程度まで下がる」という趣旨の記述は WebSearch の AI 要約（サードパーティ寄り）に基づき、公式ページ本文に具体的な 5% という数値の明記は確認できなかった。

**OpenAI**

- gpt-5-mini / gpt-5-nano / gpt-5.4-mini / gpt-5.4-nano が Structured Outputs（json_schema strict）に正式対応しているかは、公式の対応モデル一覧に明示的な記載が見当たらず確認できなかった。"gpt-4o-mini, gpt-4o-2024-08-06, and later" という表現がこれらの新モデルを包含する趣旨か、単に一覧が更新されていないだけかは判別できない。GitHub 上のサードパーティ製品（dify）の Issue で「gpt-5-nano モデルで JSON Schema による構造化出力が機能しない」という未検証のコミュニティ報告が見つかった。実装前の実機疎通確認を要する事実として記録する。
- モデルカタログページ（developers.openai.com/api/docs/models）を 2 通りの角度で取得したところ、一方では「GPT-5.6 モデル（コードネーム Sol/Terra/Luna）がフラッグシップ」、もう一方では「新規プロジェクトは gpt-6-astra から始めることを推奨」という相互に整合しない記述が返ってきた。公式価格表で実在が直接確認できたのは gpt-5-mini/nano と gpt-5.4-mini/nano までで、それより新しい世代（5.5 系、5.6 系、あるいは「6-astra」系列）に mini/nano 相当の軽量モデルが存在するかは今回の調査では確定できなかった。
- 構造化出力で非対応とされる JSON Schema キーワードの網羅的リストとネスト制限（5 階層・100 プロパティ）は、公式ドキュメントを直接引用した形での確認ができておらず、第三者による集約情報に依拠している。
- openai.com ドメインの enterprise-privacy / business-data ページは WebFetch で 403 が返り、直接内容を確認できなかった。学習利用なし・ZDR 提供という記載自体は developers.openai.com 側（一次ソース）と整合しているため信頼度は高いと判断したが、ページ自体の最終更新日や文言の一字一句は未検証。
- バッチ API の 50% 割引が mini/nano 系すべてのモデルに一律適用されるのか、モデル固有の例外があるかは価格表の総論記載のみで、個別モデルページでの明記は確認していない。
- 支出上限の API キー単位（プロジェクト単位ではなくキー単位）での予算分離機能があるかは、公式ページ本文に明記がなく確認できなかった。プロジェクト単位の分離のみ確認できた。

**Google**

- 有料枠のログ保持期間は「limited period of time（一定期間）」としか記載されておらず、具体的な日数・週数は利用規約の該当箇所からは確認できなかった。
- 無料枠のデータ保持期間についても、具体的な期間の記載は確認できなかった。
- TTFT の Google 公式絶対値は見つからなかった。DeepMind の Flash-Lite ページは第三者ベンチマーク由来の数値を引用するにとどまり、TTFT については言及自体がない。「2.5 倍速い」という言明は検索結果の要約に現れたが原典未確認、確度は低いままである。
- 最新 Flash / Flash-Lite の無料枠・Tier 別の具体的な RPM/TPM/RPD 数値は rate-limits ページ本文には掲載されておらず、AI Studio コンソール上でしか確認できない旨の案内のみだった。
- `responseSchema` のフィールド名表記に食い違いが出た。同じ構造化出力ドキュメントの異なるフェッチ結果で、あるときは `response_format`/`schema`、あるときは `responseFormat`/`text`/`schema` という異なる表記が返ってきた。WebFetch ツールが内部で小型モデルによる要約を挟んでいるための表記揺れの可能性があり、正式なフィールド名（`generationConfig.responseSchema`/`responseMimeType` なのか、新しい統合 API の `responseFormat` なのか）は本調査だけでは断定できない。実装時に SDK の型定義または公式リファレンスの直接確認を要する。
- HTTP リファラ制限の有無について、検索結果の要約では「HTTP リファラでの制限が可能」との言及があった一方、`ai.google.dev/gemini-api/docs/api-key` の直接フェッチ結果では「HTTP リファラ制限はこのページには言及されていない」とされ、IP 制限と API 制限のみが明記されていた。両者は矛盾しており、どちらが最新の実態かは本調査では確定できなかった。
- 通常の予算アラート（spend cap ではない標準の budgets 機能）が Gemini API 利用のブロックまで行うか通知のみかについては、一次資料を直接フェッチしておらず検索エンジンの要約のみに依拠している。
- propertyOrdering の要否について、Gemini 2.0 系モデルで明示指定が必要という記載はあったが、最新の Flash / Flash-Lite（3.x 系）で同様の制約があるかは、フェッチ結果からは明確に読み取れなかった。

## 影響する論点

- `open-questions.md`「LLM ベンダーの選定」: コストパフォーマンス・応答速度・構造化出力の強さ・データ利用・支出上限の 5 軸のうち材料が揃った。応答速度は 3 社とも公式値がなく、実装時に実測する前提が確認された。構造化出力の保証は Anthropic が一次資料で明確、OpenAI は小型モデルの対応が公式一覧に未記載、Google は構文の正しさのみ保証。
- `open-questions.md`「公開範囲と LLM 呼び出しの保護」: 支出上限は Anthropic が組織/ワークスペース単位、OpenAI が組織/プロジェクト単位で 429、Google が Cloud の支出上限で新規利用を遮断、という異なる仕組みを持つ。API キー単体の上限は 3 社とも未確認。
- `decisions.md` 2026-09-07「ベンダーは Claude に限定しない。リポジトリ層で抽象化し、コスパと速度で選ぶ」: 本調査はその決定に沿って 3 社を横並びで比較する材料を提供する。
- `decisions.md` 2026-09-07「フィードバックは JSON Schema で固定し UI が描画」: 構造化出力の保証の強さ（Anthropic の constrained decoding による保証、OpenAI の対応モデル未確認、Google の構文のみ保証）は、この決定を実装する際にベンダーごとの挙動差として効く。
