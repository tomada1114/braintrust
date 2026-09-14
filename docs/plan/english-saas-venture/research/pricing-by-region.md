# 地域別価格戦略：$15/月 は誰にとって現実的か

- 調査日: 2026-09-14
- 調査手段: メインセッション（Sonnet）単独によるデスクリサーチ。WebSearch はセッション開始時点でクォータ枯渇（`this session has used its web search budget (200 of 200 WebSearch calls)` と実際にエラーを受けて確認済み）。WebFetch / curl による公式サイト・公式ドキュメントの直接フェッチ、Apple App Store 国別ストアページの構造化データ、World Bank API、Numbeo、HN Algolia 検索 API を使用。原文はすべてこのセッション内で自分で確認しており、伝聞は含まない。Reddit は今回試行していない（他の手段で十分な材料が得られたため）。
- 問い: グローバル向けの語学学習アプリを個人が有料で売るとき、地域ごとの価格感度をどう扱うべきか。$15/月 は誰にとって現実的で、誰にとって非現実的か。

## 結論

$15/月 は、北米・西欧・日本・韓国の平均的な所得層にとっては年収の 0.2〜0.5%程度の負担で「現実的」な水準だが、インドの平均的な所得層（World Bank 統計での GNI per capita）にとっては年収の 6.5% 相当、ブラジルでも 1.7% 相当に達し、そのままでは非現実的な水準になる。実在する語学アプリの挙動は割れている。Duolingo・ELSA Speak は Apple App Store の国別ストア価格で見る限りインド向けに 65〜85% 程度の大幅な値引きをしている一方、Babbel は 16〜27% 程度の小幅な値引きに留まり、Speak・italki はむしろ USD 換算でインドの方が同額かそれ以上になっている（値引きなし、あるいは為替を無視した桁の使い回し）。つまり「PPP 値引きをしなければ新興国で売れない」は言い過ぎで、値引きをしないまま成立しているプレイヤーも実在する。Stripe・Paddle は地域別価格を安価に技術実装できる（Stripe は `currency_options`、Paddle は `unit_price_overrides`）ため、技術的な参入障壁は低い。一方で VPN・請求先住所偽装による回避、EU域内での価格差別の法的グレーゾーン、サポート・不正対策コストの増加という実務上の落とし穴がある。依頼者（月 150〜200 人の有料継続で目標達成）の状況では、最初のフェーズで地域別値引きに手を広げるより、購買力のある地域に定価 $15/月 で絞り込む方が筋が良いと考える（詳細は末尾）。

## 製品別の価格表

| 製品 | 地域別価格の有無 | 実際の価格（確認できた範囲） | 出典 URL | 出典日付 | 確度 |
|---|---|---|---|---|---|
| Duolingo Super | あり（大幅） | US: 月額 $9.99〜$12.99、年額/ファミリー $79.99〜$119.99。India: 月額 ₹199〜215（≈$2.1〜2.3）、年額系 ₹1,199〜1,749（≈$12.5〜18.3）。同一ラベル内で India は US の約 15〜21%（≈4.5〜6.7 倍安い） | https://apps.apple.com/us/app/duolingo-language-lessons/id570060128 、https://apps.apple.com/in/app/duolingo-language-lessons/id570060128 | 2026-09-14（Apple App Store 現行掲載） | 高（Apple公式ストアの構造化データを直接取得。ただし同一ラベルに複数価格が並ぶため、旧価格が混在している可能性は残る＝下記グレーゾーン参照） |
| Duolingo Max | 未確認 | App Store の IAP 一覧に "Duolingo Max" の項目が見当たらなかった（Web版限定課金の可能性） | 同上 | 2026-09-14 | 低（見つからなかった） |
| Babbel | あり（小幅） | US: 月額 $17.99、12ヶ月プラン $107.99、言語別年間 $89.99。India: 月額 ₹1,249（≈$13.1、US比 27%引き）、12ヶ月 ₹8,700（≈$91、16%引き） | https://apps.apple.com/us/app/babbel-language-learning/id829587759 、https://apps.apple.com/in/app/babbel-language-learning/id829587759 | 2026-09-14 | 高 |
| Busuu | あり（幅が大きく一貫性に欠ける） | US: 月額 $9.99〜$23.49、年間 $70〜$138.99。India: 月額 ₹305〜719（≈$3.2〜7.5）、年間 ₹909〜1,800（≈$9.5〜18.8）。同一ラベルの中に複数価格が混在し、正確な現行価格の特定は不能 | https://apps.apple.com/us/app/busuu-language-learning-app/id379968583 、in版同ID | 2026-09-14 | 中（値引きの存在は明確だが、正確な倍率は特定できず） |
| ELSA Speak | あり（大幅） | US: 月額 $19.99、年額 $99.99〜$129.99。India: 月額 ₹499（≈$5.2、74%引き）、年額 ₹3,449〜3,599（≈$36〜38、64〜71%引き） | https://apps.apple.com/us/app/elsa-speak-english-learning/id1083804886 、in版同ID | 2026-09-14 | 高 |
| Speak | あり、ただし逆転（値引きなし・むしろ割高） | US: 月額 $17.99〜$39.99、年額 $83.99〜$164.99。India: 月額 ₹1,899〜4,999（≈$20〜52）、年額 ₹9,900〜22,900（≈$104〜240）。USD換算で India の方が同等かむしろ高い | https://apps.apple.com/us/app/speak-language-learning/id1286609883 、in版同ID | 2026-09-14 | 高 |
| italki Plus | 実質なし（数字だけ現地通貨に置き換え） | US: 月額 $5.99、年額 $59.99。India: 月額 ₹599（≈$6.3）、年額 ₹5,900（≈$62）。「5.99」の数字をそのまま「599」に置き換えただけで、為替・購買力を反映していない | https://apps.apple.com/us/app/italki-language-learning/id1140000003 、in版同ID | 2026-09-14 | 高 |
| Preply | 未確認 | 公式サイト（preply.com）はJS描画のSPAでフェッチ不能。App Store の当該アプリ（id1352790442）に IAP 掲載が見当たらず、レッスン単位の従量課金（マーケットプレイス型）でアプリ内課金を使っていない可能性 | https://preply.com/en/pricing （フェッチ失敗）、https://apps.apple.com/us/app/preply-language-learning-app/id1352790442 | 2026-09-14 | 低（取得できなかった） |
| WaniKani | 未確認 | 公式サイト（wanikani.com）が完全な JS 描画 SPA でサーバー側に価格情報が存在せず、curl/WebFetch とも取得不能。公式 iOS アプリも存在しない（サードパーティ製 "Tsurukame" のみ App Store で確認） | https://www.wanikani.com/pricing （フェッチ失敗） | 2026-09-14 | - （取得できなかった。想定価格をここに書くと捏造になるため記載しない） |
| Bunpro | なし（単一価格・USD建て） | Free（文法・語彙ページと読解パッセージの閲覧のみ、SRS復習は不可）／Premium $5/月／Lifetime $150（買い切り）。地域別価格への言及なし | https://bunpro.jp/pricing | 2026-09-14 | 高（WebFetch で本文を直接取得。同ページはJSに依存せずサーバー側でレンダリングされていた） |

**留保**: Apple App Store の「In-App Purchases」欄は、同じラベル（例: "12 Months Premium"）の下に複数の価格が併記されることがある。これはユーザーが過去に購入した旧価格帯（据え置き契約）と現行の新規販売価格が同じ掲載枠に混在するためと見られる。よって上表の価格レンジは「現在確認できた価格帯」であり、「今この瞬間の唯一の正規価格」を断定するものではない。それでも Duolingo と ELSA の India 価格が US 価格の 1/4〜1/6 程度に収まっている一方、Speak と italki の India 価格が US 価格と同等かそれ以上になっている、という**相対的な傾向**は複数のラベル・複数の価格帯にわたって一貫しており、傾向としての確度は高いと判断した。

## PPP プライシングの実務と落とし穴

### Stripe

- Stripe には 2 つの異なる仕組みがある。
  1. **Adaptive Pricing**（為替ベースの単純換算）: 「Stripe uses machine learning to determine the most relevant presentment currency, then automatically calculates the localized price and handles all currency conversion.」150 カ国以上に対応。これは**購買力平価ではなく、単に中間市場為替レートに基づく通貨換算**であり、開発者は個別に何もしなくても現地通貨で表示できる。ただし「You pay 0% / Your customers pay 2–4%」と明記されており、**顧客側が為替手数料 2〜4% を負担する**。Adaptive Pricing はインドの事業者には現状非対応（"Adaptive Pricing isn't supported for Indian businesses."）。
     - 出典: https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md 、出典日付: 記載なし（2026-09-14 時点の現行ドキュメント）、確度: 高
  2. **Manual currency prices**（開発者が任意の価格を通貨ごとに手動設定）: `Price` オブジェクトの `currency_options` に通貨ごとの `unit_amount` を個別指定できる。例: `-d currency=usd -d unit_amount=1000 -d "currency_options[eur][unit_amount]=950" -d "currency_options[jpy][unit_amount]=1500"`。これが**真の意味での PPP 的値引き（為替レートを無視した任意価格）を実現する唯一の公式な方法**。Stripe 自身は「Adaptive Pricing の方を推奨する」と明記しているが、それは為替変動リスクの回避が理由で、PPP 値引きをしたい場合はむしろこの手動設定が必要になる。
     - 出典: https://docs.stripe.com/payments/checkout/localize-prices/manual-currency-prices.md 、出典日付: 記載なし、確度: 高

### Paddle

- Paddle には「price overrides」という機能があり、「Price overrides let you override the base price with a custom price and currency for any country.」`unit_price_overrides` パラメータで国ごとに任意の価格・通貨を設定できる。Stripe の Adaptive Pricing と違い、**最初から任意価格（＝PPP 的値引き）を前提にした設計**になっている。トライアル付きプランの場合は「For every base price override, you must provide a matching trial price override」という制約がある。
  - 出典: https://developer.paddle.com/build/products/create-products-prices 、出典日付: 記載なし、確度: 高

### Lemon Squeezy

- Lemon Squeezy 自体には**ネイティブの PPP 機能がない**。公式ドキュメントのチュートリアルは「ParityDeals」という外部サービスとの連携方法を説明しており、「You cannot add the ParityDeals banner directly to your Lemon Squeezy storefront because the storefront doesn't support adding custom scripts. However, you can still use ParityDeals on your own website or app.」と明記している。仕組みは、ParityDeals 側で地域ごとの割引コードを生成し、それを Lemon Squeezy の Discounts 機能に同期する、という間接的な統合。
  - 出典: https://docs.lemonsqueezy.com/guides/tutorials/ppp-with-paritydeals 、出典日付: 記載なし、確度: 高

### VPN・請求先偽装による回避と実務上の落とし穴（Hacker News の議論より）

2022 年の HN スレッド「Purchasing Power Parity: Fair pricing for SaaS products」（21 件のコメント）から、実務上の論点を抽出した。

- **回避は技術的には可能だが、実際にはあまり起きない**という実装者の証言:
  > "I was aware of this potential issue when I implemented PPP on my course. It turns out almost nobody uses this trick, although a few told my about it. I guess when you are transparent with your users, they are actually happy to pay the fair price?"（投稿者 scastiel、記事著者本人、2022-11-07）
  - 出典: https://news.ycombinator.com/item?id=33509258 、確度: 中（単一の実装者の一次体験談。規模・ジャンルが明示されていない小規模コース）
- **顧客側から見た好意的な受け止め**（ブラジル在住者のコメント）:
  > "As Brazilian, I always ask for parity prices for services charged in dollar... Surprisingly (or not), most SaaS I do business with give me parity prices. I really appreciate that and it makes me more loyal to them."（rpgbr、2022-11-08）
  - 確度: 中（個人の主観的体験談）
- **回避の主な手口として挙がったもの**: VPN によるジオIP偽装、プリペイドカード等での請求先住所偽装。対策として複数のコメントが「請求先住所（カード発行国）で判定する方がジオIPより堅い」と指摘（JimDabell, FormFollowsFunc ら）。ただし「システムを複雑にするほど裁定（アービトラージ）を誘発する」という反論もある（dzink）。
- **収益性への懐疑**: 「限界費用（COGS）がゼロに近いデジタル財でなければ PPP 値引きは成立しない」という指摘（freediver, matchagaucho）。ソフトウェアは概ね限界費用が低いため成立しやすいが、ホスティング費・サポート費が顧客あたりで無視できない場合は要注意という反論も並記されている。
- **EU の価格差別規制への言及**（未検証・一次資料ではない）:
  > "This is not necessarily legal in the EU. https://europa.eu/youreurope/citizens/consumers/unfair-treat... 'Price discrimination is not allowed'"（tpmx、2022-11-08）
  - これは HN コメント内での言及であり、今回 europa.eu の当該ページを直接確認していない。**EU 域内の消費者に対する地理的価格差別（Geo-blocking Regulation 等）に抵触するリスクがあるという指摘はグレーゾーンとして扱い、実装前に一次資料での確認が必要**。
- **2025年の最近の議論**（Ask HN、2025-08-19）:
  > "today chatgpt launched a new pricing tier for India. Grok already has purchasing power parity pricing. If this helps signups and revenue, why are products still not doing location based pricing? Is it tech or just mindset?"（sachinneravath）
  > 返信: "Increased usage, but with decreased revenue/profit is not a business strategy often employed. Losing money does not get fixed by scaling up... most companies are fine with simply not entering markets where the business model doesn't add up."（codingdave）
  - 出典: https://news.ycombinator.com/item?id=44952602 、確度: 中（コメント1件のみで議論の広がりが薄い）
- **ParityDeals 自身のブログでの「売上15%増」事例**（利益相反あり）: ParityDeals（PPP 値引きツールのベンダー）自身のブログに、lightGallery というJSライブラリの作者 Sachin Neravath の事例が掲載されている。「前年の最初の4ヶ月間で合計 $8,190 の売上（うち低購買力国からは $512、6%）」→「PPP導入後7ヶ月間で $37,394 の売上（320%増、うち低PPP国から $5,815、14%）」「開発途上国からの売上は800%増、全体売上は15%増」。ただし著者自身が「v2リリースが売上増に大きく貢献した」と認めており、**PPP単独の効果は分離できていない**。かつ掲載元が PPP ツールベンダー自身のブログである点で利益相反がある。
  - 出典: https://www.paritydeals.com/blog/how-i-increased-revenue-by-15-just-by-offering-purchasing-power-parity-pricing/ 、出典日付: 記載なし（HN投稿日 2025-09-09）、確度: 低（ベンダー自身の宣伝ブログ、交絡因子を著者自身が認めている）

## 新興国市場の実勢

### GNI per capita（World Bank, Atlas method, 現行US$, 2025年データ）

| 国 | GNI per capita（年, US$） | $15/月（$180/年）が年収に占める比率 |
|---|---|---|
| 米国 | $88,810 | 0.20% |
| ドイツ | $60,200 | 0.30% |
| 英国 | $54,550 | 0.33% |
| フランス | $48,630 | 0.37% |
| 日本 | $38,340 | 0.47% |
| 韓国 | $37,880 | 0.48% |
| ブラジル | $10,550 | 1.71% |
| インド | $2,760 | 6.52% |

- 出典: World Bank API（`NY.GNP.PCAP.CD` 指標）https://api.worldbank.org/v2/country/USA;JPN;KOR;DEU;FRA;GBR;IND;BRA/indicator/NY.GNP.PCAP.CD?format=json 、出典日付: データセット最終更新 2026-07-13（World Bank API レスポンス内の `lastupdated` フィールド）、確度: 高（世界銀行公式統計）

### インドの実勢賃金（都市部・自己申告データ、参考値）

- Numbeo（クラウドソース型の生活費データベース）によるインドの平均月間手取り給与: **₹41,821.90**（2026年9月14日時点の集計。過去12ヶ月間に2,756人の投稿者による32,363件のデータに基づく）。1米ドル ≈ ₹95.6（2026-09-14、open.er-api.com 取得）で換算すると、**約 $437〜504/月**。この場合、$15/月 は月収の約 3.0〜3.4% に相当する。
  - 出典: https://www.numbeo.com/cost-of-living/country_result.jsp?country=India 、出典日付: 2026-09-14（ページ内 "Last update" 表記）、確度: 中（自己申告のクラウドソースデータであり、都市部・ネットリテラシーの高い層に偏っている可能性が高い。World Bank の GNI per capita（全人口平均、農村部含む）とは前提が異なるため、両者の数字は単純比較できない＝下記グレーゾーン参照）

### 実例からの傍証

上記の App Store 価格表が示す通り、Duolingo と ELSA Speak はインド向けに US 価格の 15〜35% 程度（つまり 65〜85% 引き）まで値引きしており、これは「インドの平均的な購買力では $15/月 相当の定価はそのままでは支払われない」という前提に立った価格設定だと解釈できる。一方で Speak と italki はインドで値引きをしておらず、むしろ USD 換算で同等かそれ以上の価格になっている。この 2 系統が同じ市場で共存している事実は、「PPP値引きなしでは新興国で一切売れない」という単純な仮説を支持しない。ただし italki・Speak がインド市場でどれだけ実売上を出せているかは今回確認できていない（下記グレーゾーン参照）。

## 開発者の証言

Hacker News（HN Algolia 検索 API、クエリ "purchasing power parity pricing" で 40 件ヒット中の主要スレッドを精査）から。詳細な引用は上記「PPP プライシングの実務と落とし穴」節にまとめた。要点のみ再掲する。

- **良かった**: scastiel（コース販売者、2022）「透明にすれば大半の顧客は正規の値引き価格をそのまま受け入れ、VPN回避はほとんど起きなかった」。rpgbr（ブラジルの顧客側、2022）「PPP価格をくれるSaaSにはより忠誠心を感じる」。ParityDeals自身のブログ経由の Sachin Neravath の事例（lightGallery、2025、低確度）「導入後7ヶ月で売上320%増、うち低PPP国からの売上が800%増」ただし交絡因子あり。
- **悪かった／慎重であるべき**: freediver・matchagaucho（2022）「COGS（ホスティング費等）が無視できない場合、値引きはそのまま損失になりうる」。codingdave（2025）「値引きは利用者増をもたらしても、収益・利益の増加を伴わないことが多く、多くの企業はビジネスモデルが成立しない市場には端から入らない」。encoderer（2022、B2B文脈）「B2Cならまだしも、B2Bなら値引きより優良顧客からの単価アップに労力を割くべき」。
- **ツール需要の傍証**: PPP値引きを自動化するツール（ParityDeals、TierWise、Play Console Pricing Adjuster、Pricetag for App Store Connect）が複数の個人開発者によって Show HN に投稿されている。いずれも支持（points）は低く（1〜5点）、強い実証にはならないが、「個人開発者側にPPP値引きを実装したいという一定の需要がある」ことの傍証にはなる。

## 「購買力のある地域に絞る」戦略の評価

### 市場規模の手がかり（人口, World Bank 2025年推計）

| 地域 | 人口 |
|---|---|
| 米国 | 3億4,178万人 |
| 日本 | 1億2,337万人 |
| ドイツ | 8,349万人 |
| 英国 | 6,949万人 |
| フランス | 6,872万人 |
| 韓国 | 5,168万人 |
| （参考）ブラジル | 2億1,281万人 |
| （参考）インド | 14億6,387万人 |

- 出典: World Bank API（`SP.POP.TOTL` 指標）https://api.worldbank.org/v2/country/USA;JPN;KOR;DEU;FRA;GBR;IND;BRA/indicator/SP.POP.TOTL?format=json 、出典日付: 2025年推計値（World Bank、2026-07-13時点のデータセット）、確度: 高

米国・日本・ドイツ・英国・フランス・韓国だけで合計 6.9 億人規模の人口があり、GNI per capita はいずれも $37,000 以上（$15/月 は年収の 0.5% 未満）。依頼者が必要としているのは有料継続 150〜200 人（$15/月 の場合）という絶対数であり、この規模の人口母集団に対しては極めて小さい割合で足りる計算になる。ただし「これらの国に何人の英語学習者がいるか」「そのうち何人がアプリ課金に前向きか」という母数の精度については、今回のデスクリサーチでは確認できなかった（下記グレーゾーン）。人口全体の数字を英語学習者数の代理指標として使うのは粗い近似であることを明記しておく。

### 是非

HN の議論では、B2B文脈での「優良顧客への単価アップに労力を割くべき」という指摘（encoderer）や、「ビジネスモデルが成立しない市場には端から入らない」という指摘（codingdave）が、間接的にこの戦略を支持する。一方で、値引きを実装するコスト自体は Stripe・Paddle いずれも技術的には低い（`currency_options` や `unit_price_overrides` を設定するだけ）ため、「技術的に難しいから絞る」という理由づけは成立しない。絞るべき理由があるとすれば、値引き後の市場で成立させるために必要な**運用面のオーバーヘッド**（多通貨対応の会計・不正利用対策・多言語サポート・獲得チャネルの多様化）であり、これは `docs/plan/english-saas-venture/open-questions.md` に記録されている「月数本の発信」という制約と正面から衝突する論点である。

## グレーゾーン・未確認

- **Preply・WaniKani の価格**: いずれも公式サイトが JS 描画の SPA でサーバー側に価格情報が存在せず、curl・WebFetch のどちらでも取得できなかった。WaniKani には公式 iOS アプリが存在しないことも確認したため、App Store 経由での代替取得もできなかった。
- **Duolingo Max の個別価格**: App Store の IAP 一覧に見当たらなかった。Web版限定課金である可能性があるが未検証。
- **Apple App Store 価格の「現行性」**: 同一ラベルに複数の価格が併記される仕様のため、掲載されている価格すべてが「今この瞬間に新規ユーザーへ提示される価格」であるとは断定できない（旧価格帯の混在の可能性）。相対的な傾向（Duolingo/ELSAは大幅値引き、Speak/italkiは値引きなし）は複数データ点で一貫しているため確度は高いと判断したが、個別の金額の最終確定はしていない。
- **App Store の地域別価格が「開発元の意図的なPPP戦略」か「Appleの自動価格帯変換」かの切り分け**: 今回の調査では、Duolingo・ELSA・Babbel・Busuu・Speak・italki のいずれについても、公式が「これはPPP戦略である」と明言している一次資料は見つけられなかった。価格の傾向から推測しているに過ぎない点に注意。
- **EU域内の価格差別規制（Geo-blocking Regulation等）とPPP値引きの適法性**: HNコメント内の言及のみで、europa.eu の一次資料を今回直接確認していない。実装前に法務面での確認が必要な論点として残す。
- **World Bank GNI per capita と Numbeo自己申告賃金の乖離**: 前者（全人口平均、農村部含む）$2,760/年 ≈ $230/月、後者（都市部・クラウドソース自己申告）$437〜504/月と、2倍以上の開きがある。どちらも「インドの語学アプリターゲット層の実質的な購買力」を正確に表しているとは言い切れず、実際のターゲット層（都市部・ある程度の可処分所得を持つ英語学習者）はこの中間かそれ以上に位置すると推測されるが、これは推測の域を出ない。
- **italki・Speak がインドで値引きなしのまま実売上をどれだけ確保できているか**: 確認できなかった。値引きなしの価格設定が「機能していない」のか「機能しているが規模が小さい」のかは判断材料がない。
- **Reddit の声**: 今回試行していない（HN・公式ドキュメント・App Store データで問いに答えるのに十分な材料が得られたため）。試行すれば追加の開発者証言が得られる可能性はあるが、過去の経験則通り 403 で取得できない可能性が高い。
- **依頼者が想定する主要市場のうち、中国・東欧・韓国・中南米については、今回は詳細な価格実勢調査を行っていない**（インド・ブラジルのみ数値を確認）。中国は決済インフラ（Alipay/WeChat Pay）と規制の特殊性があるため、別途調査が必要。

## この依頼者が取るべき価格戦略（確度: 中）

依頼者の状況（月 30 万円目標、$15/月なら有料継続150〜200人で達成、発信は月数本という制約）を踏まえると、**最初のフェーズでは地域別値引き（PPP価格）を実装せず、北米・西欧・日本・韓国を中心とした購買力のある地域に定価 $15/月 で絞り込む**のが推奨である。理由は3つ。第一に、これらの地域だけで人口6.9億人規模の母集団があり、必要な有料継続者数（150〜200人）は極めて小さい割合で足りる計算になる。第二に、実例を見てもitalki・Speakのように値引きなしで成立しているプレイヤーが存在し、「値引きしなければ新興国以外でも売れない」わけではないことが示唆される。第三に、値引きを機能させるための運用コスト（不正利用対策・多通貨会計・多言語サポート・追加の獲得チャネル開拓）は、「月数本の発信」という限られたリソースと衝突する。ただし、Stripe の `currency_options` や Paddle の `unit_price_overrides` を使えば技術的な追加コストは低いため、**将来的にインド・ブラジル等向けの低価格ティア（Bunproの$5/月やDuolingoのインド価格帯を参考に $3〜5/月程度）を「後から追加するオプション」として設計だけはしておく**のは合理的である。この推奨の確度を「中」に留める理由は、（1）推奨の妥当性が「発信は月数本」という現時点でまだ確定していない制約に依存していること（2）「北米・西欧・日本・韓国の英語学習者が実際にどれだけいて、どれだけ課金に前向きか」という母数の精度を今回のデスクリサーチでは確認できていないこと（3）獲得チャネルそのものが `docs/plan/english-saas-venture/open-questions.md` の「獲得経路は未解決のまま残っている」で最大の論点として残っており、価格戦略だけを単独で決め切れる状態にないこと、の3点による。

## 影響する論点

- `docs/plan/english-saas-venture/open-questions.md`「事業としてのゴールライン（金額）」: 月30万円という目標額自体の妥当性の再検討材料になる。
- 同「引き下げ後の目標金額をいくらに置くか」: 目標額を引き下げる場合、$15/月・富裕地域限定なら必要人数がさらに少なくなる計算になる。
- 同「グローバル × 月30万円の組み合わせに前例が無いことをどう扱うか」: 「地域を絞ったグローバル」（富裕国限定のグローバル展開）という中間的な選択肢を提示する材料になる。
- 同「獲得経路は未解決のまま残っている」: 価格戦略の推奨は獲得チャネルの制約（発信は月数本）を前提にしており、この論点が動けば価格戦略の推奨も再検討が必要。
