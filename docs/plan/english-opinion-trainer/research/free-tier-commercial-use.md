# 無料プランのまま有料アプリ（商用利用）を運用してよいか

- 調査日: 2026-09-07
- 調査手段: Sonnet サブエージェント 1 体 + メインによる原文確認（Vercel Hobby プランページ、Vercel Fair Use Guidelines、Cloudflare Self-Serve Subscription Agreement の 3 本を直接取得）
- 問い: 課金して使わせる有料アプリを、各基盤の無料プランのまま運用してよいのか。規約に何と書かれているか。

## 結論

推奨は書かない。決定は decisions.md。以下は事実の整理のみ。

| 基盤 | 無料のまま商用可か | 根拠となる文言 | 商用に要する最低額 |
|---|---|---|---|
| Vercel Hobby | **不可（規約に明記）** | 「非商用・個人利用に限る」と 3 箇所に明記。「商用」の定義と具体例まで書かれており、決済処理が筆頭に挙がる | Pro **$20/月** |
| Cloudflare Workers Free | 商用を禁じる文言は**見当たらない**。ただし別条項が刺さる | 商用制限なし。ただし「無料サービスを受けている web property 上でのカード情報の処理・収集」を禁止 | 規約上の必須プランなし（実務上は Workers Paid **$5/月**） |
| Netlify Free | 商用を禁じる文言は**見当たらない** | Terms of Use・AUP・料金ページのいずれにも該当語なし | 規約上の必須プランなし（次点は Personal 約 $9/月） |
| AWS Lambda | 商用を禁じる文言は**見当たらない** | Customer Agreement・AUP・無料枠ページのいずれにも該当語なし | 該当なし（常時従量課金でプラン概念がない） |

**Vercel だけが明確に不可**で、残り 3 つは「禁じる文言が見つからなかった」。ただしこれは**沈黙であって、明示的な許可ではない**。この区別はこのファイルの結論の一部として扱うこと。

## 根拠

### Vercel Hobby — 不可（メインが原文確認）

- 事実: "**Hobby teams** are restricted to non-commercial personal use only. All commercial usage of the platform requires either a Pro or Enterprise plan."
  「商用」の定義: "Commercial usage is defined as any Deployment that is used for the purpose of financial gain of **anyone** involved in **any part of the production** of the project, including a paid employee or consultant writing the code."
  例として列挙されているもの: "Any method of requesting or processing payment from visitors of the site" / "Advertising the sale of a product or service" / "Receiving payment to create, update, or host the site" / "Affiliate linking is the primary purpose of the site" / "The inclusion of advertisements, including but not limited to online advertising platforms like Google AdSense"
  例外: "Asking for Donations **does not** fall under commercial usage."
  - URL: https://vercel.com/docs/limits/fair-use-guidelines
  - 出典日付: 2026-07-29
  - 確度: 高（メインが原文確認）
- 事実: "As stated in the fair use guidelines, the Hobby plan restricts users to non-commercial, personal use only."
  - URL: https://vercel.com/docs/plans/hobby
  - 出典日付: 2026-08-31
  - 確度: 高（メインが原文確認）
- 事実: 利用規約本体にも "You shall only use the Services under a Hobby plan for your personal or non-commercial use." 違反時の措置として "We reserve the right to disable or remove any Project or website deployment on the Hobby plan with or without notice at our sole discretion." / "We may shut down and terminate projects or deployments using the Hobby plan without notice for any reason or no reason."
  - URL: https://vercel.com/legal/terms
  - 出典日付: 2026-06-01
  - 確度: 高（一次情報、メイン未確認）
- 事実: Pro は料金ページ上 "$20/mo."
  - URL: https://vercel.com/pricing
  - 出典日付: 記載なし
  - 確度: 中（月払いか年払いかの区別は未確認。グレーゾーン参照）

### Cloudflare Workers Free — 商用制限はないが、決済に関する条項がある（メインが原文確認）

- 事実: Self-Serve Subscription Agreement を通読した範囲で、**無料プランを非商用・個人利用に限る条項は存在しない。**
  - URL: https://www.cloudflare.com/terms/
  - 出典日付: 2025-09-12
  - 確度: 高（メインが原文確認。ただし「不在の確認」である点はグレーゾーン参照）
- 事実: 禁止行為の列挙のうち Section 2.2.1(h) が "process or collect personal or business credit card information on any web property that is receiving Free Services" を禁じている。
  - URL: https://www.cloudflare.com/terms/
  - 出典日付: 2025-09-12
  - 確度: 高（メインが原文確認）
  - 注記: **商用一般ではなく「無料サービスを受けている web property 上でのカード情報の処理・収集」を禁じる条項。**外部ホスト型の決済（決済事業者のドメインに遷移する形）で回避できるかどうかは規約文言からは断定できず、**解釈が要る。**有料プランに上げれば当該プロパティは "receiving Free Services" ではなくなる、という読み方も同様に解釈を要する。
- 事実: 再販の禁止として Section 2.2.1(a) が "rent, lease, loan, export, or sell access to the Services to any third party, or sign up for the Services on behalf of a third party" を挙げる。
  - URL: https://www.cloudflare.com/terms/
  - 出典日付: 2025-09-12
  - 確度: 高（メインが原文確認）
  - 注記: 自作アプリを有料で提供することが「Cloudflare の Services へのアクセスを売る」に当たるかは別問題であり、通常は当たらないと読めるが、**解釈が要る。**
- 事実: かつての Section 2.8（HTML 以外の大量配信の制限）は現行の Self-Serve Subscription Agreement に**見当たらない**。ただし後継にあたる条項が CDN 向けの Service-Specific Terms に現存する: "Cloudflare reserves the right to disable or limit your access to or use of the CDN...if you use or are suspected of using the CDN without such Paid Services to serve video or a disproportionate percentage of pictures, audio files, or other large files."
  - URL: https://www.cloudflare.com/service-specific-terms-application-services/
  - 出典日付: 2026-06-02
  - 確度: 高（一次情報、メイン未確認）
  - 注記: これは **CDN サービスに対する条項**であり、Workers 経由の配信に及ぶかは規約上明記されていない。**解釈が要る。**将来この製品が音声を扱うなら関係しうる。
- 事実: Workers Paid は "a minimum charge of $5 USD per month"。
  - URL: https://developers.cloudflare.com/workers/platform/pricing/
  - 出典日付: 記載なし
  - 確度: 高（一次情報、メイン未確認）

### Netlify Free — 商用制限は見当たらない

- 事実: Terms of Use、Acceptable Use Policy、料金ページのいずれにも "commercial" / "non-commercial" / "personal use" / "business use" に相当する制限文言が確認できなかった。
  - URL: https://www.netlify.com/legal/terms-of-use/ (出典日付 2026-03-26) / https://www.netlify.com/legal/acceptable-use-policy/ (出典日付 2023-03-08) / https://www.netlify.com/pricing/ (出典日付 記載なし)
  - 確度: 中（不在の確認。メイン未確認）
- 事実: AUP に、文脈の異なる即時停止条項がある: "Any user deemed to be using Netlify Services solely as a remote storage server will have their account immediately terminated and will have all files associated with their account permanently removed."
  - URL: https://www.netlify.com/legal/acceptable-use-policy/
  - 出典日付: 2023-03-08
  - 確度: 高（一次情報、メイン未確認）
  - 注記: リモートストレージ専用利用に関する規定で、商用利用一般とは無関係。

### AWS Lambda — 商用制限は見当たらない

- 事実: AWS Customer Agreement、AWS Acceptable Use Policy、無料利用枠ページのいずれにも商用利用を制限する文言が確認できなかった。Lambda は常時従量課金モデルで「プラン」概念がない。
  - URL: https://aws.amazon.com/agreement/ (発効日 2026-08-14) / https://aws.amazon.com/aup/ (出典日付 2021-07-01) / https://aws.amazon.com/free/ (出典日付 記載なし)
  - 確度: 中（不在の確認。メイン未確認）
- 事実: Customer Agreement Section 6.2 に一般条項として "You will ensure that Your Content and your and End Users' use of Your Content or the Services will not violate any of the Policies or any applicable law."
  - URL: https://aws.amazon.com/agreement/
  - 出典日付: 2026-08-14
  - 確度: 高（一次情報、メイン未確認）

## グレーゾーン・未確認

- **3 基盤の「制限が無い」は沈黙であって許可ではない。** 規約が意図的に無制限としているのか、単に触れていないのかは文言からは判定できない。Cloudflare の一般的な終了条項（Section 8、原文未取得）や AWS の Policies 遵守条項のように、裁量で制限しうる契約構造は残っている。
- **Cloudflare Section 2.2.1(h) の適用範囲は解釈が要る。** 外部ホスト型の決済に遷移させる形が「その web property 上でカード情報を処理・収集する」に当たらないかどうか、有料プランに上げれば当該プロパティが "receiving Free Services" から外れるかどうか、どちらも規約文言だけでは断定できない。**有料化の実装方式を決める前に、必要ならサポートに確認すべき論点。**
- **Cloudflare の CDN 向け大量ファイル配信制限が Workers に及ぶかは規約上未確定。** 音声を扱う設計に将来広げる場合に関係しうる。
- **Workers がどの Service-Specific Terms の管轄下にあるかが確定していない。** Developer Platform 向けのページを調べたが商用・制限に関する条項が見当たらず、そのページが最新・正しいものかの確証も取れていない。**調べたが分からなかった。**
- **Vercel Pro の $20/月が月払いか年払いかを一次情報で確認できていない。** 第三者は「年払い $20 / 月払い $24」としているが一次情報ではない。**要再確認。**
- **Vercel の Acceptable Use Policy 本文は未取得。** 利用規約から参照されているのみで、帯域再販禁止などの具体的禁止行為は未確認。
- **Netlify の料金ページの価格表記に取得ツール側の整形崩れの疑いがある**（"$9//month" 等）。実際の表記は目視の再確認が要る。
- **Netlify の AUP は 2023-03-08、AWS の AUP は 2021-07-01 が最終更新**で、いずれも現行のプラン構成より前の文書である可能性がある。内容が現行と整合しているかは未確認。
- **Netlify に Self-Serve Subscription Agreement 相当の別契約文書があるかは未チェック。**
- このファイルは法的助言ではない。規約の解釈が事業判断に直結する段階（実際に課金を始める段階）では、原文を自分で読み直すこと。

## 影響する論点

- `open-questions.md`「サーバーレス関数をどこで動かすか」— 直接効く。有料公開を視野に入れると **Vercel Hobby は候補から落ちる**。「商用」の定義が「訪問者からの決済処理」を筆頭に挙げており、想定している形態が正面から該当する。しかも違反時は予告なしの停止・削除がありうると規約に明記されている。
- `decisions.md` 2026-09-07「公開時の LLM 呼び出しの保護は最初の版の対象外」— 「他人に配る＝本番＝課金」という前提を置いた以上、基盤の選定でも有料化後を見ておく必要がある、という形でこの調査に繋がった。
- `decisions.md` 2026-09-07「サーバーレス実行基盤の選定軸」— 有料化したときの固定費は Cloudflare $5/月 < Netlify 約 $9/月 < Vercel $20/月、AWS は従量のみ。オーナーの第 2 の軸（有料で複数案が並ぶなら AWS）は、有料化の段では発火しうる。
