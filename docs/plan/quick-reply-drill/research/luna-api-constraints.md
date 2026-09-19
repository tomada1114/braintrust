# Luna（GPT-5.6 Luna）の API 制約調査

- 調査日: 2026-09-15
- 調査手段: Sonnet サブエージェント 1 体が developers.openai.com（モデル各ページ・deprecations・reasoning・structured-outputs）と ai-sdk.dev / unpkg の `@ai-sdk/openai` 型定義を確認 + メインセッションが Luna のモデルページを直接確認
- 問い: 採点モデルとして OpenAI GPT-5.6 Luna を固定運用できるか（日付つきスナップショットの有無、temperature の可否、reasoning effort の値、Structured Outputs の可否、Vercel AI SDK からの指定方法）。

## 結論

- 日付つきスナップショットは、公開ドキュメント上は確認できない。Luna / Terra / Sol / Astra のモデルページはいずれもエイリアス 1 個（`gpt-5.6-luna` など）しか列挙していない。廃止予告はモデル個別ではなく一般ポリシー(GA モデル最低 6 ヶ月、専門バリアント最低 3 ヶ月、preview 最短 2 週間程度)。
- temperature / top_p が Luna で指定できるかは OpenAI 公式ドキュメントに記述がない。Vercel AI SDK の公式プロバイダページは「GPT-6 以降は reasoning 有効時に temperature / topP / logprobs 非対応」と明言するが、GPT-5.6 世代に及ぶかは書かれていない。旧世代 reasoning モデルでは温度が固定・拒否されたという第三者報告あり。
- reasoning.effort は Luna / Terra / Sol で none, low, medium（既定）, high, xhigh, max の 6 値。Astra は none 不可の 5 値。一般ガイドにある minimal は 4 モデルの個別ページには載っていない。
- Structured Outputs（json_schema strict）は Luna / Terra / Sol / Astra の個別ページで `structured_outputs` がサポート機能として明記されている。専用ガイドページは古い一般論のままで個別言及なし。
- Vercel AI SDK `@ai-sdk/openai` では `providerOptions.openai.reasoningEffort` で強度を、`providerOptions.openai.strictJsonSchema`（既定で有効）で strict を指定する。`openai.responses()` が既定 API。Zod の `.optional()` / `.nullish()` は OpenAI の Structured Outputs で許容されず `.nullable()` に書き換える必要がある。

## 根拠

- 事実: Luna のモデルページの「利用可能なスナップショットとエイリアス」は `gpt-5.6-luna` のみ。
  - URL: https://developers.openai.com/api/docs/models/gpt-5.6-luna
  - 出典日付: 記載なし
  - 確度: 中→高（メインセッションで原文確認済み。ただし動的表示の見落としの可能性は残る）
- 事実: Terra / Sol / Astra も単一エイリアスのみ。
  - URL: https://developers.openai.com/api/docs/models/gpt-5.6-terra , https://developers.openai.com/api/docs/models/gpt-5.6-sol , https://developers.openai.com/api/docs/models/gpt-6-astra
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 廃止予告期間ポリシー「GA モデル: 少なくとも 6 ヶ月」「専門バリアント: 少なくとも 3 ヶ月」「preview: 最短 2 週間程度」。安全性・コンプライアンス上の理由がある場合は例外。
  - URL: https://developers.openai.com/api/docs/deprecations
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Luna / Terra / Sol / Astra 自体の廃止予告は現時点で出ていない（旧モデルの移行先として言及されるのみ）。
  - URL: 同上
  - 確度: 中
- 事実: reasoning ガイド「reasoning.effort は none, minimal, low, medium, high, xhigh, max を取りうるが、サポートする値はモデル依存。GPT-6 Astra は none 非対応で 400 を返す」。
  - URL: https://developers.openai.com/api/docs/guides/reasoning
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Luna のページ "Reasoning.effort supports: none, low, medium (default), high, xhigh, and max."
  - URL: https://developers.openai.com/api/docs/models/gpt-5.6-luna
  - 出典日付: 記載なし
  - 確度: 高（メインセッションで原文確認済み）
- 事実: Luna のページに temperature / top_p の記述はない（メインセッションで原文確認済み）。reasoning ガイドにも記述なし。
  - 確度: 中（消極的事実）
- 事実: Vercel AI SDK プロバイダページ「GPT-6 以降のモデルは reasoning 有効時に temperature、topP、logprobs、レガシーの promptCacheRetention をサポートしない」「reasoningEffort を設定すると非互換の設定は自動的に取り除かれ warning が返る」。
  - URL: https://ai-sdk.dev/providers/ai-sdk-providers/openai
  - 出典日付: 記載なし
  - 確度: 中（Vercel 公式だが OpenAI 自身の記述ではなく、対象が GPT-6 以降）
- 事実（第三者）: 旧世代 reasoning モデル（o1 / o3 / gpt-5 系）では temperature・top_p・n が 1 に固定され、temperature 指定は 400 で拒否、top_p 等はサイレント無視という報告。gpt-5.1 は effort=none のときだけ制御可という報告も。
  - URL: OpenAI Developer Community / GitHub issue 群（個別 URL 未取得）
  - 出典日付: 記載なし
  - 確度: 低
- 事実: Structured Outputs ガイドは「GPT-4o から対応、新規は gpt-6-astra 推奨」と書き、Luna 等への個別言及なし。
  - URL: https://developers.openai.com/api/docs/guides/structured-outputs
  - 出典日付: 記載なし
  - 確度: 中
- 事実: Luna のページの「サポートする機能」に `structured_outputs` が明記（メインセッションで原文確認済み）。Terra / Sol / Astra も同様。
  - 確度: 高（Luna）/ 中（他）
- 事実: `@ai-sdk/openai` は `providerOptions.openai.reasoningEffort` で強度指定。型定義上の値は 'low' | 'medium' | 'high' | 'xhigh' | 'max' | 'none' | 'minimal'。
  - URL: https://ai-sdk.dev/providers/ai-sdk-providers/openai , https://unpkg.com/@ai-sdk/openai/dist/index.d.ts
  - 出典日付: 記載なし
  - 確度: 高（ドキュメント）/ 中（型定義の版は未確認）
- 事実: Structured Outputs は `Output.object({ schema })` と `generateText` / `generateObject` で使い、strict は既定で有効、`providerOptions.openai.strictJsonSchema: false` で無効化。Zod の `.optional()` / `.nullish()` は許容されず `.nullable()` に書き換える。
  - URL: https://ai-sdk.dev/providers/ai-sdk-providers/openai
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `openai.responses()` が AI SDK 5 以降の既定 API（Responses API）、`openai.chat()` は Chat Completions。GPT-6 以降は Responses 側でパラメータ互換ルールが異なるとの記載。
  - URL: 同上
  - 確度: 中

## グレーゾーン・未確認

- 日付つきスナップショットは「ページに記載がない」までしか確認できていない。未整備か、動的表示の見落としか、方針変更かは調べたが分からなかった。
- temperature / top_p が Luna で指定できるか・拒否されるか・無視されるかは一次情報で確認できなかった。reasoning モデルである以上、無視か拒否の可能性が高いという傍証はあるが確証はない。「温度を下げて採点をブレさせない」という前提は当てにできない。
- Structured Outputs ガイドとモデル個別ページの食い違い（ガイドが古いだけか、制約があるのか）は未確認。
- minimal が Luna で使えるかはガイドと個別ページで食い違う。個別ページ（載っていない）を優先すべきと思われる。
- Luna が GA モデルと専門バリアントのどちらの廃止予告期間に当たるかは明記なし。
- `@ai-sdk/openai` の型定義を確認した unpkg 上の版が latest かは未確認。

## 影響する論点

- open-questions.md「モデル版の固定と採点の再現性」（新設）: スナップショットで版を固定する手が使えない可能性があるので、記録にモデル別名・推論強度・採点基準のバージョンを刻み、いつの採点かを追えるようにする必要がある。温度による安定化も当てにできず、再現性は「記述で固定した尺度 + 推論強度の固定」に頼ることになる。
- decisions.md「ベンダーとモデル」: 質問生成の最弱強度は none が使える。
- 実装側への注意: Zod スキーマは `.optional()` を使わず `.nullable()`。強度は `providerOptions.openai.reasoningEffort`。
