# Anthropic の構造化出力で、フィードバックのスキーマをどこまで縛れるか

- 調査日: 2026-09-07
- 調査手段: Sonnet サブエージェント 1 体 + メインによる原文確認（structured-outputs ページを 2 回、観点を変えて直接取得）
- 問い: フィードバック用の JSON スキーマについて、指摘の件数上限・言い直しの長さといった粒度をスキーマ制約で表現できるか。できないなら代替は何か。

## 結論

**粒度の 2 つは、どちらも生の JSON Schema では縛れない。** 配列は `minItems` の 0 と 1 だけが通り `maxItems` は非対応、文字列長も数値範囲も非対応。したがって「指摘は 1〜2 箇所」の上限も「言い直しは 80 字以内」もスキーマの型システムの外。

ただし逃げ道が 2 本ある。

1. **`pattern`（正規表現、PCRE2）が使える。** 文字列の長さは `^.{20,80}$` のような量指定子で間接的に縛れる。配列の要素数には使えない。
2. **公式 SDK（Python / TypeScript / Ruby / PHP）が自動変換する。** 非対応の制約を書いたまま渡すと、SDK がワイヤースキーマから制約を外し、その内容を description に文章として埋め込み、返ってきたレスポンスを**元のスキーマ（制約込み）に対して検証**する。つまり Zod に `.max(80)` と書いておけば、モデルへの制約にはならないが、アプリ側の検証にはなる。

したがって設計上は「構造（フィールドの有無と型）は constrained decoding が保証し、粒度（件数・長さ）はプロンプトと事後検証で守る」という二層になる。粒度をモデルに強制する手段はない。

Haiku 4.5（`claude-haiku-4-5-20251001`）は対応モデル一覧に明記されており、構造化出力を理由に外す必要はない。

設計に効く副作用が 3 つある。スキーマごとに文法のコンパイルが走り**初回リクエストだけ遅い**（コンパイル結果は最終使用から 24 時間キャッシュ）。構造化出力は**追加のシステムプロンプトが自動で注入され入力トークンが増える**。`output_config.format` を変えると**プロンプトキャッシュが無効化**される。

## 根拠

### 対応・非対応の境界

- 事実: "Structured outputs support standard JSON Schema with some limitations. Both JSON outputs and strict tool use share these limitations."
  対応: "All basic types: object, array, string, integer, number, boolean, null" / "`enum` (strings, numbers, bools, or nulls only - no complex types)" / "`const`" / "`anyOf` and `allOf` (with limitations - `allOf` with `$ref` not supported)" / "`$ref`, `$def`, and `definitions` (external `$ref` not supported)" / "`default` property for all supported types" / "`required` and `additionalProperties` (must be set to `false` for objects)" / "String formats: `date-time`, `time`, `date`, `duration`, `email`, `hostname`, `uri`, `ipv4`, `ipv6`, `uuid`" / "Array `minItems` (only values 0 and 1 supported)"
  非対応: "Recursive schemas" / "Complex types within enums" / "External `$ref`" / "Numerical constraints (such as `minimum`, `maximum`, `multipleOf`)" / "String constraints (`minLength`, `maxLength`)" / "Array constraints beyond `minItems` of 0 or 1" / "`additionalProperties` set to anything other than `false`" / "If you use an unsupported feature, you'll receive a 400 error with details."
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし（ページに更新日表示なし）
  - 確度: 高（メインが原文確認）

### `pattern`（正規表現）は使える

- 事実: ページに "Pattern support (regex)" の節が存在し、"Supported regex features:" が "Full..." で始まる。サブエージェントの取得では "Full PCRE2 syntax support / Most common patterns work as expected (character classes, quantifiers, anchors, etc.) / Lookahead and lookbehind assertions / Named capture groups"、既知の制限として "Recursive patterns are not supported / Some complex backtracking patterns may fail / Pattern matching is applied during response generation, not just validation"。長さを正規表現で表す例として `"pattern": "^[a-zA-Z0-9_]{3,16}$"` が挙がっている。
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: **節の存在と "Full..." で始まることは高**（メインが原文確認）。**PCRE2 という具体名と機能の一覧、コード例は中**（メインの再取得では当該箇所が途中で打ち切られ、完全な引用を得られなかった。サブエージェントの引用に依存）
  - 注記: "Pattern matching is applied during response generation, not just validation" が本当なら、正規表現は生成時の制約として働くことになる。この一文はメインでは未確認。

### SDK の自動変換

- 事実: "The transformation steps: 1. **Remove unsupported constraints** (for example, `minimum`, `maximum`, `minLength`, `maxLength`) 2. **Update descriptions** with constraint info (for example, "Must be at least 100"), when the constraint is not directly supported with structured outputs 3. **Add `additionalProperties: false`** to all objects 4. **Filter string formats** to supported list only 5. **Validate responses** against your original schema (with all constraints)" / "This means Claude receives a simplified schema, but your code still enforces all constraints through validation."
  対象は Python / TypeScript / Ruby / PHP の SDK。C# と Go はネイティブ型からスキーマを導出した場合のみ同じ変換が掛かる。
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認）

### TypeScript での書き方

- 事実: `zodOutputFormat()` を `@anthropic-ai/sdk/helpers/zod` から import し、`client.messages.parse()` の `output_config.format` に渡す。"The `parse()` method accepts a Zod schema, validates the response, and returns a `parsed_output` attribute with the inferred TypeScript type matching the schema." 生の JSON Schema 用に `jsonSchemaOutputFormat()` もある。
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認）
- 事実: SDK ソース `src/helpers/zod.ts` の関数コメントは "Creates a JSON schema output format object from the given Zod schema." のみで、対応する Zod 機能の一覧は存在しない。内部で Zod v4 の `z.toJSONSchema()` を呼んで JSON Schema に変換している。
  - URL: https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/src/helpers/zod.ts
  - 出典日付: 記載なし（main ブランチ現行）
  - 確度: 高（サブエージェントがソース確認）

### Haiku 4.5 の対応

- 事実: サポートモデル一覧に `claude-haiku-4-5-20251001` が含まれる（他に fable-5-1 / mythos-5-1 / fable-5 / mythos-5 / mythos-preview / opus-5 / opus-4-8 / opus-4-7 / opus-4-6 / sonnet-5 / sonnet-4-6 / sonnet-4-5-20250929 / opus-4-5-20251101）。
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認）
  - 注記: 一覧は日付つきスナップショット ID で書かれている。ベアエイリアス `claude-haiku-4-5` でも同じに動くかはページの文言からは断定できない。

### 保証のメカニズム

- 事実: "Structured outputs guarantee schema-compliant responses through constrained decoding: **Always valid:** No more `JSON.parse()` errors / **Type safe:** Guaranteed field types and required fields / **Reliable:** No retries needed for schema violations"
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高（メインが 1 回目の取得で原文確認。ただしグレーゾーンの「文言の揺れ」を参照）

### 設計に効く副作用

- 事実: "**First request latency:** The first time you use a specific schema, there is additional latency while the grammar compiles" / "**Automatic caching:** Compiled grammars are cached for **24 hours from last use**, making subsequent requests much faster" / キャッシュ無効化は "Occurs when schema structure or tool set changes"、"Changing only `name` or `description` fields does not invalidate the cache."
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認）
- 事実: "When using structured outputs, Claude automatically receives an additional system prompt explaining the expected output format. This means: Your input token count is slightly higher / The injected prompt costs you tokens like any other system prompt"
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認）
- 事実: "Changing the `output_config.format` parameter will invalidate any prompt cache for that conversation thread"
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高

### 他機能との併用

- 事実: 構造化出力とツール利用は "You can use these features independently or together in the same request." で併用可。
  - URL: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - 出典日付: 記載なし
  - 確度: 高
- 事実: citations とは併用不可。"**Citations and structured outputs are incompatible** ... the API returns a 400 error. This is because citations require interleaving citation blocks with text output, which is incompatible with the strict JSON schema constraints of structured outputs."
  - URL: https://platform.claude.com/docs/en/build-with-claude/citations
  - 出典日付: 記載なし
  - 確度: 高

## グレーゾーン・未確認

- **SDK が検証失敗時にリトライするかが、同一ページ内で食い違って読める。** トラブルシューティング節はサブエージェントの取得で "These SDKs automatically validate responses against your original schema (including unsupported constraints) and **retry if needed**" とあるが、変換ステップの節をメインが取得したときは検証までしか書かれておらず、リトライへの言及がなかった。**リトライの有無・回数・失敗時に何が投げられるかは未確認。**実装時に実際の挙動を確かめる必要がある。
- **`max_tokens` に途中で達したときの構造化出力の挙動**: structured-outputs ページに記載がない。一般の `stop_reason: "max_tokens"`（応答が truncated、`max_tokens` を上げて再試行）が適用されると推測されるが、途中で切れた JSON がどう返るか、`parsed_output` が null になるのか例外かを明言した一次資料は見つからなかった。**調べたが分からなかった。**
- **"Invalid outputs" 節と「保証」の文言のテンション**: 同ページの "Invalid outputs" 節は、enum の大文字小文字違い・型不一致・必須フィールド欠落・余分なフィールドがエラーになりうると書いている。constrained decoding でスキーマ違反が構造的に起きないという記述と字面上どう両立するのか、ページ自体は説明していない。
- **"constrained decoding" という語の再現性**: メインの 1 回目の取得ではこの語を含む一文が得られたが、サブエージェントの再取得では省略された版が返ることがあった。取得手法（要約モデル経由）の揺れである可能性が高く、メカニズムが文法ベースであること自体は grammar compilation の記述が裏づけている。
- **`pattern` 節の詳細**: メインの再取得では当該節が途中で打ち切られ、PCRE2 という具体名・機能一覧・コード例はサブエージェントの引用に依存している。**設計の根拠に使う前に実装時に再確認すること。**
- **`zodOutputFormat()` が対応する Zod 機能の明示リスト**: ドキュメントにも SDK ソースにも存在しない。実質「`z.toJSONSchema()` が出せる範囲」×「構造化出力が受け付ける範囲」の積になるが、それを直接述べた一次資料はない。
- **ストリーミング・extended thinking・画像入力との併用可否**: ページが沈黙している。citations との非互換だけは別ページで明確だった。**調べたが分からなかった。**
- 参照した Anthropic の docs ページはいずれも**更新日を表示していない**。このファイルの鮮度は「2026-09-07 に取得した」ことしか保証しない。

## 影響する論点

- `open-questions.md`「フィードバックの『決まった形式』の中身」— 直接効く。残っていた粒度（指摘の件数上限、言い直しの長さ、説明の深さ）は**いずれもスキーマでは強制できない**と確定した。件数は `minItems` の 0/1 しか使えず配列に `pattern` は効かないので、プロンプト指示 + 事後検証。長さは `pattern` の量指定子か、SDK に `maxLength` を渡して事後検証させるかの二択。説明の深さは完全にプロンプト側。
- `decisions.md` 2026-09-07「フィードバックは JSON Schema で固定し UI が描画」— 前提は保たれる。ただし保証されるのは**構造**であって粒度ではない、という但し書きが要る。
- `open-questions.md`「LLM ベンダーの選定」— Haiku 4.5 は対応モデル一覧にあり、構造化出力を理由に外す必要はないことを確認。
- 応答速度の実測（実装時）— スキーマごとの文法コンパイルで初回だけ遅く、24 時間キャッシュされる。**実測するなら初回と 2 回目以降を分けて測らないと数字を読み違える。**
- レベル別にスキーマを変える設計にすると、その都度プロンプトキャッシュと文法キャッシュの両方が無効化される。スキーマは共通にしてレベルはプロンプト側の変数にするほうが、キャッシュの観点では有利。
