# サーバーレス中継の実行基盤の比較（Cloudflare Workers / Vercel / Netlify / AWS Lambda）

- 調査日: 2026-09-07
- 調査手段: Sonnet サブエージェント 1 体（机上調査）+ メインによる原文確認（AWS Lambda 料金ページ、AWS 無料利用枠 FAQ）
- 問い: 静的 SPA から呼ぶ「薄いサーバーレス関数 1 本」（Anthropic Messages API への中継のみ、TypeScript）を動かす基盤として 4 つを比べると何が分かるか。特に「AWS は無料かつ十分簡単なのか、それとも無料・簡単は別基盤で AWS は有料側の選択肢なのか」。

## 結論

推奨は書かない。決定は decisions.md。以下は事実の整理のみ。

| 軸 | Cloudflare Workers | Vercel (Hobby) | Netlify (Free) | AWS Lambda (+ Function URL) |
|---|---|---|---|---|
| 無料枠 | 恒久。10 万 req/日、CPU 10ms/req（I/O 待ちは CPU 時間に含まれない） | 恒久。呼び出し 100 万/月、Active CPU 4 時間/月。**非商用・個人利用限定** | 恒久（$0 forever）。300 クレジット/月（Compute は 10 クレジット/GB 時間） | 100 万 req/月 + 400,000 GB 秒/月。**恒久かどうかは料金ページに書かれていない**（下記グレーゾーン） |
| クレカ登録 | 不要（確度 中、公式明言なし） | 不要（確度 中、公式明言なし） | 不要（確度 中、公式明言なし） | **必須**（確度 高、公式明言あり） |
| 超過時 | 失敗する（自動課金なし） | 機能停止、30 日待ち（自動課金なし） | 全サイト停止（自動課金なし） | **自動課金に移行** |
| セットアップ | `npm create cloudflare@latest` → `wrangler deploy` の実質 3〜4 コマンドで `*.workers.dev` の HTTPS | `/api/*.ts` を置くだけでゼロコンフィグ | `netlify/functions/*.mts` を置くだけ | コンソールで数クリック（Function URL 発行）。IaC なら SAM か CDK + IAM 認証情報の設定 |
| 鍵の持たせ方 | Secrets（`wrangler secret put`）。値は CLI・ダッシュボードからも非表示 | Environment Variables（保存時暗号化、1 デプロイ 64KB まで） | Environment variables（`netlify env:set`） | Lambda 環境変数（保存時暗号化）。ただし **AWS 公式は API キーには Secrets Manager を推奨**と明記 |
| TypeScript / SDK | ネイティブ。Node API は `nodejs_compat` フラグ要。**`@anthropic-ai/sdk` の README が Cloudflare Workers を公式サポート対象に列挙** | ネイティブ。Node ランタイムは Node API 完全サポート。**README が Vercel Edge Runtime を公式サポート対象に列挙** | ネイティブ（`.mts`）。内部は AWS Lambda の Node ランタイム | Node 公式マネージドランタイム。TS は事前トランスパイルが要る（明言する一次資料は未発見） |
| コールドスタート | **公式は数値を出していない** | **公式は数値を出していない** | **公式は数値を出していない** | **公式は数値を出していない** |
| 静的 SPA の同居 | 可（Workers Static Assets で 1 プロジェクトに統合） | 可（標準のデプロイモデル） | 可（標準のデプロイモデル） | **不可。** S3 + CloudFront か Amplify Hosting が別に要る |
| 有料の入口 | $5/月〜 | $20/月〜 | $9/月〜 | 固定月額なし・従量（$0.20/100 万 req + $0.0000166667/GB 秒） |

問いへの答え: **AWS は「関数 1 本」だけを見ればセットアップも無料枠も他の 3 つに近い水準にある。差が出るのは周辺**。①アカウント作成に支払い方法が必須、②静的ホスティングが同居せず S3 + CloudFront か Amplify Hosting が別に要る、③その静的側の無料枠の恒久性が公式一次情報で確認できない、④超過時に停止ではなく自動課金に移行する。したがって「無料でセットアップが簡単」という基準では他の 3 つと同列には並ばない。

## 根拠

### メインが原文で確認した分

- 事実: Lambda の無料枠は "The free tier includes one million requests and 400,000 GB-seconds per month." **ページはこれが恒久か 12 ヶ月かを述べていない。**
  - URL: https://aws.amazon.com/lambda/pricing/
  - 出典日付: 記載なし
  - 確度: 高（金額は高。恒久性については「書かれていない」という事実が高）
- 事実: "You can access over 30 services with always free offers. Services with an Always Free offer allow you to use the product for free up to specified limits as long as you are an AWS customer." ただし**このページに Lambda を名指しした一覧はない。**
  - URL: https://aws.amazon.com/free/free-tier-faqs/
  - 出典日付: 記載なし
  - 確度: 高（引用は高。Lambda が該当するかは中）
- 事実: "AWS requires a valid payment method to verify your identity and prevent abuse of AWS resources. AWS will not charge your payment method until you upgrade to paid plan."
  - URL: https://aws.amazon.com/free/free-tier-faqs/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 同 FAQ ページに、S3 / CloudFront の無料枠が 12 ヶ月か恒久かを述べる記述は**見当たらなかった**。
  - URL: https://aws.amazon.com/free/free-tier-faqs/
  - 出典日付: 記載なし
  - 確度: 中（不在の確認）

### サブエージェントの調査分（メイン未確認）

- 事実: Cloudflare Workers 無料枠は "100,000 per day" のリクエスト、CPU 時間は Free で 10ms/リクエスト。超過時は "further operations of that type will fail with an error."
  - URL: https://developers.cloudflare.com/workers/platform/pricing/ , https://developers.cloudflare.com/workers/platform/limits/
  - 出典日付: 記載なし / 確度: 高（一次情報だがメイン未確認）
- 事実: Workers の CPU 時間について "Waiting on network requests (such as fetch() calls...) does not count toward CPU time."
  - URL: 検索結果からの言い換え（原文ページ未直接確認）
  - 出典日付: 記載なし / 確度: 中
  - 注記: これが正しければ、Anthropic API の応答待ちが 10ms の CPU 上限を消費しないことになり、この用途で Free 枠が成立するかの鍵になる。**実装前に一次情報で確認すべき項目。**
- 事実: Workers Secrets は "a type of binding that allow you to attach encrypted text values to your Worker."、値は "not visible within Wrangler or Cloudflare dashboard"。
  - URL: https://developers.cloudflare.com/workers/configuration/secrets/
  - 出典日付: 記載なし / 確度: 高（一次情報、メイン未確認）
- 事実: `@anthropic-ai/sdk` の公式 README が Cloudflare Workers と Vercel Edge Runtime をサポート対象ランタイムとして列挙している。
  - URL: https://github.com/anthropics/anthropic-sdk-typescript
  - 出典日付: 記載なし / 確度: 高（SDK 自身の一次情報、メイン未確認）
- 事実: Vercel Hobby は "Function Invocations: First 1,000,000"、"Active CPU: 4 CPU-hrs"。超過時は "you will have to wait until 30 days have passed before you can use the feature again."。"the Hobby plan restricts users to non-commercial, personal use only."
  - URL: https://vercel.com/docs/plans/hobby
  - 出典日付: 2026-08-31 / 確度: 高（一次情報、メイン未確認）
- 事実: Netlify Free は "$0 forever" で 300 クレジット/月。使い切ると "all of your web projects (sites/apps) are paused and visitors... will find a 'Site not available' page."
  - URL: https://www.netlify.com/pricing/ , https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/
  - 出典日付: 記載なし / 確度: 高（一次情報、メイン未確認）
- 事実: AWS 公式の Function URL と API Gateway の使い分け: "We recommend function URLs for simple applications or prototyping where you only need basic authentication methods... API Gateway is a better choice for production applications at scale." Function URL の認証は `AWS_IAM` か `NONE` のみ。Function URL 自体に追加料金はなく Lambda 料金のみ。
  - URL: https://docs.aws.amazon.com/lambda/latest/dg/furls-http-invoke-decision.md
  - 出典日付: 記載なし / 確度: 高（一次情報、メイン未確認）
- 事実: AWS 公式は "we recommend that you use AWS Secrets Manager instead of environment variables to store... API keys" と明記。
  - URL: https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html
  - 出典日付: 記載なし / 確度: 高（一次情報、メイン未確認）
- 事実: Amplify Hosting の無料枠は "No cost up to 1,000 build minutes"、"5 GB stored on CDN"、"15 GB" 転送/月だが **"Free for 12 months" と明記**（恒久ではない）。
  - URL: https://aws.amazon.com/amplify/pricing/
  - 出典日付: 記載なし / 確度: 高（一次情報、メイン未確認）
- 事実: API Gateway の無料枠は "These free tier offers are only available to new AWS customers, and are available for 12 months following your AWS sign-up date."
  - URL: https://aws.amazon.com/api-gateway/pricing/
  - 出典日付: 記載なし / 確度: 高（一次情報、メイン未確認）

## グレーゾーン・未確認

- **サブエージェントが AWS 無料利用枠 FAQ に帰した「2025-07-15 以降の新規顧客は $100 + 最大 $100 のクレジット型に変わった」という記述を、メインの取得では当該ページに確認できなかった。**「このページには書かれていない」という回答が返った。取得手法（要約モデル経由）の限界で見落とした可能性は残るが、**現時点では未確認として扱う。**この変更が実在するかどうかは、AWS を選ぶ場合に無料枠の前提が変わるため、選定前に確かめる必要がある。
- **Lambda の無料枠が恒久かどうか。** 料金ページは金額を書くが期間を書かず、FAQ は「30 以上のサービスに always free がある」と書くが Lambda を名指ししていない。**2 つの一次情報を突き合わせても確定できなかった。**
- **S3 / CloudFront の無料枠が恒久か 12 ヶ月か。** FAQ に記述がなく、CloudFront の料金ページにも期間の明記がないとサブエージェントが報告。**調べたが分からなかった。**
- **コールドスタートの数値は 4 基盤とも公式が一切出していない**（これは確認済みの事実）。第三者ベンチマークは食い違いが大きく（Cloudflare「<5ms」対 Lambda「p95 1.2〜2.8 秒」）、測定条件がばらばらで比較可能性が低い。`@anthropic-ai/sdk` を積んだ場合の実測はどの情報源にも見つからなかった。
- **各基盤のクレカ登録不要の明言**は、Cloudflare・Vercel・Netlify いずれも公式ページ本文で確認できず、第三者記事の一致にとどまる。AWS の「必須」だけが公式明言。
- **Workers の CPU 時間に I/O 待ちが含まれない**という点はメイン・サブエージェントとも一次情報の原文を直接確認できていない。この用途で Free 枠が成立するかの鍵なので、実装前の確認項目。
- **Lambda で TypeScript に事前ビルドが要る**ことを明言する一次資料の一文は見つかっていない（ランタイム一覧からの推論）。
- **API Gateway 経由のレイテンシ増分**は公式にも第三者にも定量的な言及が見つからなかった。
- **Netlify Functions で `@anthropic-ai/sdk` が動く**ことを名指しした一次資料はない（OpenAI SDK の例で代替確認）。
- 無料枠の消費速度の試算（このアプリが実際に何 req/月 使うか）は今回のスコープ外。枠の「定義」の比較のみ。

## 影響する論点

- `open-questions.md`「サーバーレス関数をどこで動かすか」— 直接効く。
- `decisions.md` 2026-09-07「サーバーレス実行基盤の選定軸は『無料・簡単が先、有料で並ぶなら AWS』」— この軸を当てると、**AWS は「無料・簡単」の側では他の 3 つと同列に並ばない**（クレカ必須、静的が別建て、静的側の無料枠が不確実、超過で自動課金）。一方、この規模なら 4 基盤とも無料枠に収まる可能性が高く「有料の選択肢が複数並ぶ」局面が来ない可能性がある。つまりオーナーの決めた第 2 の軸（AWS 優先）が発火しないまま決まる公算が大きい。
- `decisions.md` 2026-09-07「技術スタックは静的 SPA + 薄いサーバーレス中継」— 「配布は URL を渡すだけ」という理由は、静的と関数が同居する 3 基盤ではそのまま成立するが、AWS では 2 サービスの組み合わせになる。
