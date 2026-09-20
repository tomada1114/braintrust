# 個人開発者が「発信を主な獲得手段にせず」月$700〜$5,000規模の継続収入に到達した事例 ― どの分野に固まっているか

- 調査日: 2026-09-19
- 調査手段: メインセッションによる WebSearch（セッション上限に到達し途中から使用不可）+ WebFetch（Indie Hackers / Starter Story / StartupFounderStories / Medium / founderclub.com 等の一次記事を直接確認、後半は Bing 検索結果ページの WebFetch 経由）。サブエージェント委譲なし。
- 問い: 「創業者が SNS・ブログ・コミュニティでの継続的な発信を主な獲得手段にしていない」と言える個人開発プロダクトで、月 $700〜$5,000 規模の継続収入に到達した事例を集め、どの分野に固まっているかを明らかにする。

## 結論

- **完全に「非発信」（ストア内検索・マーケットプレイス掲載・口コミのみ）で月 $700〜$5,000 規模に到達したと明確に言える事例は、今回の調査で実質 1 件（BudgetSheet、Google Workspace Marketplace、$1,600+/月）しか確認できなかった。** それも自己申告の Indie Hackers 投稿 1 本のみが根拠で、第三者検証はない。
- 目立って収益を公開している他の事例（Closet Tools、Notion2Sheets/Sync2Sheets、Superpower ChatGPT、Picture It など）は、いずれも「マーケットプレイス内検索」を土台にしつつ、個人ブログでの SEO 記事執筆、Reddit/Twitter/Facebook グループへの投稿、YouTube 動画制作、ニュースレター運営など、何らかの継続的なコンテンツ発信・コミュニティ活動を伴っていた。**「ストアに置いただけで発信ゼロのまま数千ドル規模に到達し、かつそれを維持した」という事例は、母数として非常に薄い、というよりほぼゼロに近い**というのが今回の調査からの率直な所感。
- 非発信寄りの成功が相対的に多く観測されたのは、**Chrome Web Store／Shopify App Store／Google Workspace Marketplace／WordPress プラグインディレクトリなど、巨大プラットフォームに検索導線が内蔵されているカテゴリ**。理由の仮説は「結論に続くグレーゾーン」ではなく「影響する論点」の手前、下記「非発信が観測された分野とその仮説」節にまとめた。
- 「発信なしでは到達できなかった」と創業者自身が一人称で語っている、収益データ付きの証言は、今回のリサーチ時間内では見つけられなかった。見つかったのは逆方向の言説（フォロワー数が少なくても到達できたという反論）が中心で、これも重要な発見として記録する（詳細は後述）。

## 事例一覧

| プロダクト | 分野 | 規模・時点 | 主な獲得経路 | 分類 | 開発者人数 | 出典 | 出典日付 | 確度 |
|---|---|---|---|---|---|---|---|---|
| [BudgetSheet](https://www.indiehackers.com/post/how-i-built-a-google-sheets-extension-making-1-6k-mrr-b42d845e6a)（Google Sheets拡張、個人家計・予算管理） | 個人向け家計簿（銀行口座連携） | 月$1,600+（2022年5月時点） | Google Workspace Marketplace内の検索・配信のみ。本文に「Googleは30億ユーザーを持ち、組み込みのマーケットプレイスと配信チャネルで直接ユーザーを流し込んでくれる」と明記。SNS等の言及なし | **非発信** | 1名（本業と兼業） | [Indie Hackers](https://www.indiehackers.com/post/how-i-built-a-google-sheets-extension-making-1-6k-mrr-b42d845e6a) | 記載なし（本文中「as of May 2022」） | 中（自己申告の単発投稿。Stripe連携等の裏付けは記事からは確認できず） |
| [Closet Tools](https://the-seo-autopilot.com/en/case-studies/jordan-oconnor-closet-tools)（Poshmark自動化ブラウザ拡張） | リセール（中古衣料）出品者向け業務自動化 | 2023年 年商$468,000／2024年 年商$756,500（月換算で本レンジの上限$5,000を大きく超える） | 「ほぼ純粋なSEO＋コンテンツ」。製品発売前に創業者個人ブログで"Poshmark Automation"について執筆し、数百のロングテールキーワードで上位表示→SEOトラフィック＋口コミ | **混合**（SNS発信ではないが、継続的なブログ記事執筆という「発信に近い」活動が土台） | 1名（Jordan O'Connor。後年の従業員有無は未確認） | [the-seo-autopilot.com ケーススタディ](https://the-seo-autopilot.com/en/case-studies/jordan-oconnor-closet-tools) | 記載なし | 中（二次情報のケーススタディ経由。一次のIndie Hackersポッドキャストは未確認） |
| [Superpower ChatGPT](https://www.founderclub.com/saeed-ezzati/)（ChatGPT機能拡張Chrome拡張＋ニュースレター） | ChatGPTユーザー向け生産性ツール | 2023年4月時点で月収$650〜$1,000見込み。後年「5桁MRR」「年収10万ドル超」等の言及もあり出典間で数字が不一致 | Chrome Web Store先行者優位（ChatGPT公開直後の最速リリース）＋r/OpenAIでの投稿が準バイラル化＋日次ニュースレター（後に35万人規模）＋Twitter/Discordでのコミュニティ運営 | **発信主導** | 1名（Saeed Ezzati） | [founderclub.com](https://www.founderclub.com/saeed-ezzati/) | 記載なし（本文内の時系列記述は2023年3〜4月） | 中（創業者インタビューに基づく自己申告） |
| [Notion2Sheets / Sync2Sheets](https://www.starterstory.com/stories/sync2sheets-give-notion-the-superpowers-of-google-sheets)（Google Sheets向けNotion同期アドオン） | Notionユーザー向けデータ連携ツール | 月$8,400〜$9,000（2024年5月時点、本レンジの上限をやや超える） | Google Workspace Marketplaceでの配信を土台に、Reddit（r/Notion等）投稿、Twitter/Facebookグループへの動画・画像投稿、YouTube動画（「Notion Google Sheets」キーワード狙い）、週1のブログ更新を継続。創業者自身「トラフィックの72%はブランド名の直接検索」と回顧しつつ、初期は「マーケティングに真摯でなかった」と反省 | **混合（発信寄り）** | 1名（Leandro Zubrezki） | [Starter Story](https://www.starterstory.com/stories/sync2sheets-give-notion-the-superpowers-of-google-sheets) | 2024年5月（本文記載） | 中（自己申告インタビュー） |
| [Picture It](https://startupfounderstories.com/stories/picture-it-shopify-app-acquisition-3500-mrr)（Shopify商品写真編集アプリ） | ECストア運営者向け商品画像編集 | 月$3,500（2025年時点。$1,000到達まで2年） | 土台はShopifyアプリストア内SEO（カテゴリーリーダー、Built for Shopifyバッジ）だが、2025年第1四半期から「複数チャネルでのコンテンツ作成・投稿を増加」させ、YouTube・Reddit・ChatGPT検索・自社サイトからの流入が増加 | **混合**（土台はストア内検索、成長期に発信を追加） | 1名＋契約開発者1名 | [startupfounderstories.com](https://startupfounderstories.com/stories/picture-it-shopify-app-acquisition-3500-mrr) | 記載なし（本文内「2025年」表記のみ） | 中（自己申告インタビュー） |
| [RotateProduct](https://startupfounderstories.com/stories/lorik-morina-rotateproduct-6k-mrr-shopify-ai-videos)（Shopify商品動画生成アプリ） | ECストア運営者向けAI動画生成 | 月$6.5k（2026年5月時点。本レンジ上限を超える） | Shopify意図の強いユーザー向けに1日$20の有料広告。発信でも純粋な非発信でもなく**有料広告主導** | **有料広告主導**（発信・非発信のどちらにも当てはまらない第三の型として別掲） | 1名（Lorik Morina） | [startupfounderstories.com](https://startupfounderstories.com/stories/lorik-morina-rotateproduct-6k-mrr-shopify-ai-videos) | 2026年5月（本文記載） | 中（自己申告インタビュー） |
| [Easy Folders](https://www.indiehackers.com/product/easy-folders/6-months-post-launch-my-chrome-extension-has-hit-3-700-in-mrr-and-42-000-in-total-revenue--O3qs28VAnAkcJw0j--M)（ChatGPT/Claude用フォルダ・履歴検索Chrome拡張） | AIチャットツールの使い勝手向上 | MRR $3,700+、累計$42,000+（ローンチ6ヶ月後、2024年8月頃） | **記事に獲得経路の記述なし**。「トレンド追従よりpainkillerに集中すべき」という執筆姿勢の言及のみ | **不明（分類不能）** | 記載なし（単独開発者と推定されるが明記なし） | [Indie Hackers](https://www.indiehackers.com/product/easy-folders/6-months-post-launch-my-chrome-extension-has-hit-3-700-in-mrr-and-42-000-in-total-revenue--O3qs28VAnAkcJw0j--M) | 記載なし | 低（獲得経路の一次記述が存在しないため分類の根拠が薄い） |

### 個別事例ではなく市場データ（参考）

| データ | 内容 | 出典 | 出典日付 | 確度 |
|---|---|---|---|---|
| Shopifyアプリストア収益分布 | 上位1%は年商100万ドル超（shipping/fulfillment/subscriptions/reviews/bundles等が優勢）、上位10%は年商10万ドル超（2〜15人チーム）、中間層（月$2,000〜$20,000）が「ソロ起業家と小規模チーム」の主戦場、大半のアプリは月$1,000未満のロングテール。訪問→インストール率は「良いリスティングで3〜8%」「レビュー200件超で5〜8%」で、初期は最初の50件レビュー獲得が最優先とされる | [Week One Labs](https://weekonelabs.com/blog/shopify-app-revenue-benchmarks-2026/) | 2026年7月3日 | 中（第三者ブログの集計。Shopify公式の一次データではない） |

## 非発信が観測された分野とその仮説

今回確認できた非発信寄りの唯一の明確な事例（BudgetSheet）と、混合事例（Closet Tools、Notion2Sheets、Picture It）に共通するのは、いずれも**「ユーザーが既に特定の巨大プラットフォームの中にいて、そのプラットフォーム自身が検索・ディレクトリ機能を提供している」**カテゴリだという点である。

- **Google Workspace Marketplace / Chrome Web Store / Shopify App Store / WordPress プラグインディレクトリ**：これらはいずれも「親プラットフォームの中で、既に何かを探している状態のユーザー」に対して検索結果として表示される。BudgetSheetの創業者が明言した「Googleが30億ユーザーへの配信チャネルを組み込みで提供してくれる」という論理がそのまま当てはまる。
- **課題が検索語として明確な業務自動化・ニッチワークフロー**：Closet Tools（Poshmark特有の出品作業）、Picture It（Shopify商品写真の特定編集ニーズ）のように、「〇〇プラットフォームの△△という定型作業」というピンポイントな課題を持つユーザーは、Google検索やストア内検索で具体的なキーワードを打ち込みやすい。これは Shopify App Store のベンチマークデータが示す「レビュー数と検索順位の連動」というストア内SEOの仕組みとも整合する。
- **代替手段が面倒／専用ツールがないと詰む**：BudgetSheetやNotion2Sheetsのように「異なる2つのプラットフォーム（Google Sheets⇔銀行API、Google Sheets⇔Notion）をつなぐ」というニッチな連携ニーズは、手作業での代替が面倒なため、検索で見つけた瞬間に有料化しやすいと推測される（ただし定量的な裏付けは今回取得できていない仮説）。

一方で、これらの事例の多くが**$5,000/月を超えて成長する段階になると、追加でコンテンツ発信（ブログ、Reddit投稿、YouTube、ニュースレター）を足している**（Notion2Sheets、Picture It、Superpower ChatGPT）。これは「ストア内検索だけで初速は出せても、その先の成長・維持には何らかの継続的な発信が必要になりやすい」ことを示唆しており、「発信を主戦略にしない」という前提が**到達後も**成り立つかどうかには疑問符が付く。

## 反証：「発信なしでは無理だった」という証言の有無

タスクで指定された「発信なしでは無理だった」という一人称証言を意図的に探したが、**収益データを伴う明確な一人称の失敗証言は今回のリサーチ時間内では見つからなかった**。見つかった関連言説は以下の通りで、むしろ逆方向（フォロワー数が少なくても到達できた）の主張が目立った。

- Indie Hackers上の意見投稿「[If your Twitter followers are fewer than a few thousand, don't start developing anything](https://www.indiehackers.com/post/if-your-twitter-followers-are-fewer-than-a-few-thousand-don-t-start-developing-anything-723d093ef4)」（投稿者augusdin）は「フォロワー数千人未満なら開発を始めるな」と主張しているが、これは収益データを伴わない一般論。
- これに対する反論として、strzibny氏は著書のGumroad販売で$40,000の収益を得たが、その間Twitterフォロワーは2,000人未満のままだったと反論（ただし本人は「マーケティング活動自体は必要」と付言しており、完全な非発信を主張しているわけではない）。
- Jeannen氏はmakelogo.aiをフォロワー約500人の状態でリリースし、Twitterで$200、Product Huntで$2,000の売上を得て後に$65,000で売却したと述べているが、これは単発の売上・Product Huntローンチという「継続収入」ではない事例であり、かつProduct Hunt自体がコミュニティ発信の一形態でもある。
- 上記いずれも出典: [Indie Hackers スレッド](https://www.indiehackers.com/post/if-your-twitter-followers-are-fewer-than-a-few-thousand-don-t-start-developing-anything-723d093ef4)（出典日付: 記載なし、確度: 中＝一次スレッドを直接確認したがコミュニティ内の自己申告のみ）
- 間接的な「発信なしでは苦戦していた」ことを示唆する材料としては、Notion2Sheets創業者が「初期段階でマーケティングに真摯でなかった」ことを成長の遅さの一因として回顧し、Reddit/Twitter/YouTubeでの継続的な活動を経て現在の規模に至ったと述べている点が挙げられる（[Starter Story](https://www.starterstory.com/stories/sync2sheets-give-notion-the-superpowers-of-google-sheets)、確度: 中）。これは明示的な「発信なしでは無理だった」という断言ではないが、実質的にそれに近い含意を持つ。

## グレーゾーン・未確認

- **母数そのものが小さいことが最大の発見**：今回のリサーチで収益額・時点・獲得経路の3点すべてが具体的に確認できた事例は10件に満たず、そのうち「非発信」と明確に分類できたのは1件（BudgetSheet）のみだった。これは「非発信で個人開発が月$700〜$5,000に届く事例が乏しい」という仮説を裏付けるものだが、同時に「調査自体のカバレッジが薄い」ことの反映でもあり、両方の可能性を残しておく必要がある。
- **WebSearchツールのセッション上限に到達**：調査の後半（Capterra/G2ディレクトリ経由の獲得、WooCommerceプラグイン、Zapierアプリディレクトリ、Figmaプラグイン、Slackアプリディレクトリの具体的な収益事例など）はWebSearchの発行ができなくなり、Bing検索結果ページのWebFetchで代替した。Bingの検索結果は複雑な複合クエリに対してスニペットをうまく返さないことが多く、後半に調査を予定していた分野（Figmaプラグイン、WooCommerceプラグイン、Slack/Zapierアプリディレクトリ、Capterra/G2経由のB2B SaaS）については、個別の収益事例を1件も特定できなかった。これらの分野に非発信事例が存在するかどうかは、今回の調査では「分からなかった」というのが正直な結論であり、「存在しない」という結論ではない。
- **Reddit（r/SaaS, r/indiehackers, r/SideProject）への直接アクセスがブロック**：`reddit.com`への直接WebFetchはツール側で明示的に拒否された（エラー: "Claude Code is unable to fetch from www.reddit.com"）。そのため、Reddit発の収益報告スレッドの内容は、他記事内での言及（Notion2SheetsがR/Notionに投稿した、Superpower ChatGPTがr/OpenAIでバイラル化した等）を通じた二次的な把握にとどまり、r/SaaS・r/SideProjectそのものの収益報告を直接確認できていない。
- **自己申告の収益に第三者検証はない**：本調査で挙げた全事例（BudgetSheet、Closet Tools、Superpower ChatGPT、Notion2Sheets、Picture It、RotateProduct、Easy Folders）は、いずれも創業者自身によるIndie Hackers投稿またはインタビュー記事が唯一の情報源であり、Stripe等の決済データを外部が検証した形跡はない。Baremetrics Open StartupsやTrustMRR（API連携で決済データを検証する仕組み）については存在を確認したが、今回の分野横断調査で該当する具体的な個人プロダクト事例（該当分野・該当収益レンジ）を特定するには至らなかった。
- **Closet Tools・Notion2Sheets・Picture It・RotateProductは「到達時点」で本レンジ（$700〜$5,000）を超えている**：Closet Toolsは月1で$300 MRRからスタートしたとされるが、その後わずか数ヶ月で$18,000超に達したという言及があり、本レンジ内に留まっていた期間の獲得経路詳細は確認できなかった。Notion2Sheets（$8,400〜$9,000）、RotateProduct（$6.5k）も同様に現在の数字は上限をやや超えている。Picture It（$3,500）とEasy Folders（$3,700）、BudgetSheet（$1,600）は本レンジ内。
- **Judge.me（Shopifyレビューアプリ、年商$3,000万超）**は「コミュニティ主導のブランドアプローチ」とだけ言及されており、創業初期の具体的な獲得経路（発信か非発信か）を裏付ける一次情報は今回見つけられなかった。規模的にも本調査のレンジ（$700〜$5,000/月）を大きく超えるため参考掲載も見送った。
- **WP Buffs（$1.5M ARR）・JustSketchMe**：Indie Hackers上の「SNSなしでどう到達したか」スレッドで言及された事例だが、WP Buffsは獲得経路の75%を「コンテンツマーケティング」（＝継続的なブログ記事執筆）が占めており、これがSNS発信ではないにせよ「発信」に近い継続活動かどうかは評価が分かれる。またチーム規模が「個人開発」の範囲かも未確認。JustSketchMeは獲得経路（SEO・提携・口コミ）は分かるが具体的な収益額の記載がなく、本レンジに該当するか判定できない。いずれも主テーブルには含めず、本節での言及に留めた。
- **「コンテンツSEO」を発信とみなすかどうかは本調査内で判断が割れる**：Closet ToolsやWP Buffsのように「継続的にブログ記事を書いてSEO流入を得る」型は、SNSでの発信ではないが、継続的なコンテンツ制作という点で「発信主導」に近い性質を持つ。本調査では便宜上「混合」に分類したが、これを「非発信」寄りとみなすか「発信」寄りとみなすかで、非発信事例の実質的な数え方は変わる。仮に「コンテンツSEO＝非発信」とみなす立場を取るなら非発信寄りの事例は増えるが、その場合も「継続的な記事執筆という労力」は必要であり、「発信・集客をメインにしない」というオーナーの条件（継続的な発信を主戦略にしない）とは緊張関係にある点は変わらない。

## 影響する論点

- `docs/plan/indie-earning-fields/` のこれから作成される overview.md / open-questions.md における、「発信を主な獲得手段にしない」という個人開発の前提が現実的かどうかという中心的な問いに直接効く。本調査の結論（非発信の明確な事例はほぼゼロに近く、あってもマーケットプレイス組み込み型のニッチツールに限られる）は、対象分野を絞り込む際の強い制約条件になる。
- 対象分野の絞り込みにおいて、「Chrome拡張機能・Shopify/WordPress/Google Workspaceなど既存プラットフォームのアドオン系」を優先候補とする根拠、および「到達後も$5,000超を維持するには結局何らかの継続的発信が必要になりやすい」というリスクの両方を、今後の意思決定に反映する必要がある。
- 既存の `docs/plan/english-saas-venture/research/acquisition-channels.md`（語学学習アプリに限定した先行調査）とも整合的な構図（ビッグキーワードは大手が占有、ロングテールでの個人参入は長年の蓄積が前提）であり、分野を問わず「発信なしでの新規参入」は難易度が高いという傾向を補強する。
