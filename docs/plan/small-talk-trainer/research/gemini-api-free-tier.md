# Gemini API の無料枠

- 調査日: 2026-09-06
- 調査手段: Sonnet サブエージェントによる Web 調査 + メインセッションによる原文確認
- 問い: Gemini API の無料枠は個人の練習アプリに足りるか。無料枠のデータ利用条件。構造化出力・TS SDK の有無。Claude / OpenAI との比較。

## 結論

Gemini API には Gemini 3.8/3.7/3.6/3.5 Flash、3.5/3.1 Flash-Lite、2.5 Pro/Flash/Flash-Lite など複数モデルに "Free of charge" の無料枠が公式に用意されている。ただし RPM/TPM/RPD といった具体的なレート制限値は公式ページには載っておらず、Google AI Studio にログインしないと確認できない(=事前の見積もりができず、使って測るしかない)。無料枠では入力・出力データが Google の製品改善やモデル学習、人間によるレビューに使われる旨が規約に明記されており、有料枠ではこれが行われない。構造化出力(responseSchema)やシステム指示は無料枠でも tier を問わず使え、公式 TypeScript SDK(`@google/genai`)も存在する。比較対象として、Claude API には無料枠がなく最安でも入力 $1 / 出力 $5 per MTok(Haiku 4.5)、OpenAI の最安モデルは入力 $0.05 / 出力 $0.40 per MTok(gpt-5-nano、第三者集計で公式未確認)。

## 根拠

- 事実: 料金ページに Gemini 3.8/3.7/3.6/3.5 Flash、3.5/3.1 Flash-Lite、2.5 Pro/Flash/Flash-Lite などが "Free Tier: Free of charge" と記載されている。
  URL: https://ai.google.dev/gemini-api/docs/pricing
  出典日付: 確認 2026-09-06
  確度: 高

- 事実: レート制限(RPM/TPM/RPD)の具体値は公式ページに掲載されておらず、「Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio」とのみ記載されている(ログインが必要)。
  URL: https://ai.google.dev/gemini-api/docs/rate-limits
  出典日付: 確認 2026-09-06
  確度: 高(「非公開である」という事実について)

- 事実: 第三者ブログは「Gemini 3 Flash: 10 RPM / 250,000 TPM / 1,500 RPD」「3.1 Flash-Lite: 15 RPM / 1,000 RPD」等の具体値を報告しているが、公式による裏付けはない。
  URL: (第三者ブログ、複数)
  出典日付: 確認 2026-09-06
  確度: 低〜中

- 事実: 利用規約原文に、無料枠は「Google uses the content you submit to the Services and any generated responses to provide, improve, and develop Google products and services and machine learning technologies」および「human reviewers may read, annotate, and process your API input and output」とある。一方、有料枠は「Google doesn't use your prompts (including associated system instructions, cached content, and files such as images, videos, or documents) or responses to improve our products」とある。
  URL: https://ai.google.dev/gemini-api/terms
  出典日付: 確認 2026-09-06
  確度: 高

- 事実: 料金ページの "Used to improve our products: Yes/No" 列も上記の無料枠/有料枠の違いと一致している。
  URL: https://ai.google.dev/gemini-api/docs/pricing
  出典日付: 確認 2026-09-06
  確度: 高

- 事実: 構造化出力(responseSchema)は tier を問わず利用できる。システム指示も標準でサポートされている。
  URL: https://ai.google.dev/gemini-api/docs/structured-output
  出典日付: 確認 2026-09-06
  確度: 高(機能自体)/ 中(tier 制限が一切ないと断定できる点)

- 事実: 公式 TypeScript SDK は `@google/genai`(旧 `@google/generative-ai` から移行)で、npm 最新は v2.21.0(2026-09-02 頃公開)。
  URL: (npm パッケージページ)
  出典日付: 確認 2026-09-06
  確度: 高

- 事実: Claude API には無料枠がなく、最安モデルの Haiku 4.5 でも入力 $1 / 出力 $5 per MTok。
  URL: https://claude.com/pricing
  出典日付: 確認 2026-09-06
  確度: 高

- 事実: OpenAI の最安モデルは gpt-5-nano で入力 $0.05 / 出力 $0.40 per MTok とされる(第三者集計サイト、公式ページでは未確認)。
  URL: (第三者集計サイト)
  出典日付: 確認 2026-09-06
  確度: 中

## グレーゾーン・未確認

無料枠のレート制限の具体的な数値は Google AI Studio でしか確認できず、事前に見積もることができない。第三者ブログの数値は目安程度にしかならない。

## 影響する論点

- モデル・ベンダーの選定(open-questions.md)
- 無料枠のデータ利用を許容するか(open-questions.md)
- 無料枠の上限が公式に非公開である点(open-questions.md)
