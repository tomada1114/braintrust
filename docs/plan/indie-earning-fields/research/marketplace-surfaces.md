# 個人開発者にとっての「検索流入が実在するストア／マーケットプレイス」調査

- 調査日: 2026-09-19
- 調査手段: メインエージェント(Sonnet)による一次情報(公式ドキュメント・公式ヘルプセンター)の直接WebFetch確認を中心に、Sonnetサブエージェント(並列5系統)によるWebSearch/WebFetch調査を補助的に利用。サブエージェントの一部はさらに孫エージェントへの再委任を試みたため、優先度の高いプラットフォーム(Chrome Web Store、VS Code Marketplace、Raycast Store、Obsidian、Figma、Notion、Canva)はメインエージェントが自ら一次情報に当たり直して裏取りした。WebSearchはセッション上限(200回)に複数回到達し、後半はWebFetch直接取得中心に切り替えている。
- 問い: 個人開発者が「作って置いておけば検索流入で見つかる」入口として現実的に機能する、プラットフォームのアプリストア／マーケットプレイスはどれか。

## 結論

断定はできないが、収集した事実からは次のことが言える。

1. **「検索流入が構造的に存在する」ことと「新規参入者が実際にそこで見つけてもらえる」ことは別問題である。** 調べた全プラットフォームで、ランキング・レコメンドはインストール数/レビュー数/エンゲージメントといった実績シグナルに強く依存する設計になっており(Chrome Web Store, Atlassian Marketplace, HubSpot App Marketplaceで一次情報により確認)、新規アプリが実績ゼロの状態で検索経由の流入を得られるかどうかの定量データは、調査した範囲では一つも見つからなかった。HubSpotは「30日以内に3件以上のインストールがないと掲載自体がされない」という、新規参入者にとって明確な鶏卵問題を規約上明記している。
2. **「自前Stripe等で直接課金し、入金を自分でコントロールする」という条件を満たせるプラットフォームと、満たせないプラットフォームがはっきり分かれる。** WordPress.org、Slack App Directory、Zapier、Make(Community Apps)、Airtable、Raycast(構造的にほぼ無料前提)、Obsidian、Webflow(規約上の沈黙から推定)は自前決済が可能、または自前決済しか選択肢がない。逆にShopify App Store、Atlassian Marketplace、Salesforce AppExchange、monday.comはプラットフォーム課金が必須で、独自Stripe直接課金は規約上不可と一次情報で確認できた。Chrome Web Storeは2013年に独自の「Chrome Web Store Payments」を提供していたが、現在の公式ドキュメント(program-policies/accepting-payment、developer.chrome.com、最終更新2022-11-01 UTC)は「Googleではなく開発者が販売者である」ことを明記しており、独自決済(自前Stripe等)が前提の記述になっている。ただし当時の廃止告知そのもの(cws-payments-deprecationページ)は現在404で、正確な廃止年月日を一次情報で直接確認することはできなかった(後述)。
3. **月$700〜$5,000規模にソロ開発者が到達した「自己申告かつ具体名・URL付き」の実例は、Shopify App Store、Google Workspace Marketplace、monday.com、Airtable(一部)で複数見つかったが、いずれも自己申告であり第三者検証済みの事例は一件も確認できなかった。** Chrome Web Store、VS Code Marketplace、Raycast Store、Obsidian、Figma、Notion(単体テンプレート販売者)、WordPress.org、Webflow、Framer、Atlassian、Salesforce、Slack、Microsoft 365、Zapier、Make、HubSpot、Discord、MCPディレクトリ、ChatGPT Apps/GPT Store、Claude Software Directoryについては、この粒度の実例を発見できなかった(「出典が沈黙している」)。
4. **プラットフォーム依存リスクは全プラットフォームで構造的に存在し、実例も多数確認できた。** 特にChrome Web StoreのManifest V3強制移行(2025年7月に旧仕様が全面無効化、2026年8月31日に旧仕様の拡張機能がストアから完全削除)、WordPressのACF強制フォーク事件(2024年10月)、Atlassianの手数料率引き上げ(2026年4月・10月)、Shopifyのレベニューシェア条件の複数回変更、Figmaが新規の有料コミュニティリソース販売者の承認を現在停止していること、は個人開発者にとって「作って置いておけば安泰」ではないことを裏付ける具体的な事実である。
5. 以上を総合すると、**「入口として現実的に機能する」の意味を「新規参入でもゼロから検索流入が得られる」まで厳しく取るなら、それを裏付ける定量データはどのプラットフォームにも見つからなかった。** 一方「自前決済を維持しながら参入できる」という条件だけで絞るなら、WordPress.org、Obsidian、Zapier/Make、Airtable、Slack App Directory、Raycast(ただし収益化の仕組み自体が存在しない)、Webflowが候補になり、「参入障壁は高いが実績のある個人開発者向け実例が複数あるプラットフォーム」という条件ではShopify App StoreとGoogle Workspace Marketplaceが最も裏付けが厚い。

## 比較表

| プラットフォーム | 検索流入の実在性 | 自前Stripe等の直接課金 | 手数料/レベニューシェア | 参入障壁 | ソロ到達実績($700〜5,000/月規模、自己申告) | 依存リスクの実例 |
|---|---|---|---|---|---|---|
| Chrome Web Store | インストール/アンインストール推移・評価に基づくランキング(公式)。新規は数時間〜で検索に反映されるが上位化の定量データはなし | 現行ポリシー上は開発者=販売者が前提(独自CWS決済は過去に存在したが現在は開発者側決済が前提) | 記載なし(現行はプラットフォーム手数料の明記が見当たらない) | 登録料は一回限り(金額は公式ページに明記なし、通称$5)。審査は数日〜数週間 | 見つからず(出典が沈黙) | Manifest V3強制移行で2025年7月に旧仕様拡張機能が無効化、2026年8月31日に旧仕様拡張機能がストアから完全削除(一次情報) |
| VS Code Marketplace | 公式の発見性・ランキング解説ページ自体が見当たらず不明 | 事実上、自前課金以外の選択肢がない(Marketplace自体に決済機能なし、記載なしからの推定) | 該当なし(仕組みがない) | 登録は無料、Publisher検証は5営業日目安(公式) | 見つからず(出典が沈黙) | 具体事例は未確認 |
| Raycast Store | 「Trending」等の一覧はあるが算出ロジック非公開 | 該当なし(公式が「拡張機能で収益化する意図はない」と明言) | 該当なし(収益化の仕組みが存在しない) | 審査は無償、公開はオープンソース必須。期間の記載なし | 見つからず(構造的に成立しない) | 具体事例は未確認 |
| Obsidian コミュニティプラグイン | 公式に発見性の説明なし | 可能(有料化は許可されているが決済手段はOBSidianが仲介しない) | 該当なし(プラットフォームが決済を仲介しない) | 登録無料、審査期間の明記なし | 見つからず(出典が沈黙) | 具体事例は未確認 |
| Figma Community / Plugins | 発見性の仕組みの説明は限定的 | 選択可能(Figma決済 or 外部サードパーティ決済) | Figma決済利用時15%定額 | **現在、新規の有料コミュニティリソース販売者の承認を停止中**(一次情報)。Generative pluginsは有料化自体が非対応 | 見つからず(出典が沈黙) | 新規有料販売者の受付停止という参入障壁自体が依存リスクの一種 |
| WordPress.org プラグインディレクトリ | Active Install数偏重の検索設計、約19%が「0+installs」のまま埋もれるとの第三者集計 | 可能(トライアルウェア禁止だが外部SaaS課金・別配布のプレミアム版は許可) | 該当なし(登録・掲載無料) | 登録無料、2025年通期承認率69.5%、審査待ちキューは変動大(2026年に急増した記録あり) | 見つからず(古いFreemius統計はあるが具体名なし) | ACF強制フォーク事件(2024年10月、開発者の同意なく看板プロダクトを置き換え) |
| Slack App Directory | 掲載数以外の発見性データなし | 可能(Slack自体に決済機能がない) | 該当なし | 最低10アクティブワークスペース等の基準あり。セキュリティレビューは実施時期非公開 | 見つからず(出典が沈黙) | データエクスポート/LLM学習アプリの掲載禁止など事後的な規制強化 |
| Atlassian Marketplace | OpenSearchはインストール数以外にレビュー・エンゲージメントも加味(公式)。Rovo等新チャネルのロジックは非公開 | 不可(Atlassian課金必須) | Connect 80%、Forge84%(2026年4月時点)、2026年10月にさらに開発者取り分減 | パートナー検証必須化(2025年6月)、バグバウンティ公開義務化(2026年6月30日まで) | 見つからず(出典が沈黙) | 手数料率の複数回・段階的引き上げが進行中 |
| Salesforce AppExchange | 定量データなし | 不可(AppExchange Checkout必須) | 15%(累計2000万ドル超で10%)、OEMは25% | セキュリティレビュー費用999ドル/提出、審査6〜9週間(いずれも一次情報未直接確認、複数二次情報が一致) | 見つからず(法人・チーム規模の事例のみ) | 2023年にレビュー料金体系を変更(初回2,550ドル+年150ドル→提出ごと999ドル) |
| Google Workspace Marketplace | 定量データなし | 可能(インストール自体への課金は禁止だが、インストール後の外部課金は運用上可能) | 該当なし(明記なし) | 通常審査数日、制限スコープはCASA評価必須で数週間 | BudgetSheet: MRR $1,600超(自己申告、Indie Hackers 2022-05-04) | CASA評価の年次更新義務など継続コストの追加 |
| Microsoft 365 / Excel アドイン(AppSource) | 定量データなし | 可能(Microsoft課金は必須ではない) | トランザクトオファーのみ3%(2021年7月に20%から引き下げ) | 出品無料、審査3〜5営業日目安 | 見つからず(検索要約の未確認情報は棄却) | 2021年の手数料率引き下げ(20%→3%、開発者に有利な変更例) |
| Shopify App Store | 循環的な検索順位構造(実績なしでは上がらない)との第三者指摘 | 不可(Shopify課金基盤必須) | 生涯累計100万ドルまで0%、以降15%+決済手数料2.9%(2025年変更で年次リセット→生涯上限に改悪) | 登録料19ドル、審査5〜10営業日目安だが3週間以上の証言もあり | 複数の自己申告(Indie Hackers): MRR $12.5万、$4.6万、$2.5万等 | レベニューシェア条件が2021年・2025年と複数回変更 |
| Webflow App Marketplace | コミュニティ自身が発見性の実態を把握できていない状況 | 規約に収益分配の明記なし(自前決済が事実上可能と推定、断定不可) | 該当なし(規約に記載なし) | 審査目標10〜15営業日 | 見つからず(コミュニティも情報がないと認識) | 具体事例は未確認 |
| Framer Marketplace | Trending/Best算出ロジック非公開 | 開発者が価格モデル自由選択(決済手段の詳細は非公開) | プラグインは手数料0%(公式) | 審査なし・即時公開(公式) | 見つからず(プラットフォーム全体集計値のみ) | 具体事例は未確認 |
| Notion Marketplace(テンプレート) | Featured選定基準は公式に明記(人気度・新規性等) | 可能(Notion決済 or Gumroad等外部) | Notion決済利用時8%+$0.40/取引 | 審査は「数ヶ月かかる可能性がある」(公式) | 見つからず(第三者記事は403で未検証) | 具体事例は未確認 |
| Canva Apps | 定量データなし | 可能(Canva SDKはアプリ内購入非対応、外部決済リンクを案内) | Premium Apps Programは使用量ベース(詳細は403で未確認) | 詳細不明(Premium Apps Programページ403) | 見つからず | 具体事例は未確認 |
| Zapier Developer Platform | 審査待ち28〜60日超との開発者証言あり | 該当なし(Zapierは収益分配・アフィリエイトを提供しないと公式が明言) | 該当なし | 登録無料、公式SLAは「1週間以内返信」だが遅延事例あり | 見つからず(構造的に前提が成立しない) | Tables/Interfaces/Agents等の自社機能拡張によるcommoditizationの構造は存在 |
| Make(旧Integromat) | 定量データなし | 可能(Community Appsは決済自体をMakeが提供しない) | 該当なし(Community Appsは手数料0%を明記) | Community Appsの審査は2〜3営業日(ビジネス審査のみ) | 見つからず | 契約上「類似アプリをMakeが自ら開発できる」権利を明記(commoditizationが契約に明文化) |
| HubSpot App Marketplace | インストール数バケット表示によりロングテールが可視化。**新規掲載には30日以内に3件以上のインストール実績が必須という構造的障壁あり** | 可能(手数料・収益分配なしと公式が明言) | 該当なし(公式が無料と明言) | 登録無料、認定は10営業日で着手・60日以内完了・2年ごと更新 | 見つからず | 2025年9月のマーケットプレイス全面刷新(レコメンドエンジン変更) |
| monday.com apps marketplace | 定量データなし | 不可(プラットフォーム課金必須、外部決済禁止) | 生涯累計20万ドルまで0%、以降15%(2024年9月開始) | 審査期間非公開、AI生成コードは審査対象外という独自規定 | Pioneera: 「数ヶ月でMRR $30,000」(monday.com自身の広報記事、自己申告・第三者検証なし) | 収益分配プログラム自体が2024年に新設(条件は今後も変わりうる) |
| Airtable マーケットプレイス | 開発者証言:「利用統計はほぼ開示されない」「宣伝投稿は削除される」 | 可能(Airtable自体は決済を提供しない) | 該当なし | 登録無料、審査は「長く厳しい」との証言(期間非公開) | Olive氏の「Punch」: 累計$1,100〜1,700(単発課金、月次基準は未達) | Proプランでのアプリ数制限など後発的制約 |
| Discord App Directory | 未認証(100サーバー未満)は公式Discoveryの対象外という構造的除外(公式) | 公式のSKU/Entitlements APIあり | Premium Apps標準30%(初年度$100万まで15%)、Server Subscriptions 10%(いずれも一次情報403のため二次情報の一致による中確度) | 100サーバー以上で認証必須、18歳以上等の条件 | 見つからず | Privileged Intents要件の変更(二次情報、未検証) |
| MCPサーバーディレクトリ群 | 検索・カテゴリUIはあるが90%以上が未認証/未claimという指摘(Glama) | 該当なし(ディレクトリに決済基盤が存在しない。個々の開発者が独自Stripe等を実装) | 該当なし | 概して低い(GitHub OAuth等で登録) | 見つからず | 主要ディレクトリSmitheryが2026年8月にArcade.devへ買収され将来像が不透明 |
| ChatGPT Apps / GPT Store | 「スパム的GPTが上位表示される」との報道あり | 現状は外部決済(Stripe等)が唯一の一般提供パス | 該当なし(プラットフォーム内課金は招待制ベータのみ) | 個人でも申請可能。収益分配プログラムは米国拠点限定 | 見つからず | 2023年発表の収益分配プログラムが2年近く本格展開されず |
| Claude Software Directory(Anthropic) | ランキング説明なし。「同じ顔ぶれが繰り返し出る」との単独証言(未検証) | 該当なし(決済・収益分配の仕組みがToSに一切ない) | 該当なし | 開発者連絡先確認等が条件、法人格の明記なし | 見つからず(構造的に成立しない) | いつでも通知なく掲載取り下げ可能とToSに明記 |

## 根拠

### Chrome Web Store

- 事実: 現行のプログラムポリシー(決済受け入れ)は「Googleではなく開発者が販売者であることを明確に識別する」ことを開発者に義務付けており、独自の決済処理・機密情報の安全な取り扱いも開発者の責任としている。CWS独自の決済システムへの言及は本文中にない。
  - URL: https://developer.chrome.com/docs/webstore/program-policies/accepting-payment
  - 出典日付: 2022-11-01(ページ記載の最終更新日、UTC)
  - 確度: 高
- 事実: 「Chrome Web Store payments deprecation」という名称のページ(`/docs/webstore/cws-payments-deprecation`)は、`using-api`ページから現在もリンクされているが、直接アクセスすると404となり、現在のサイトマップにも存在しない。すなわち廃止告知の一次ページ自体が現時点でウェブから削除されている。
  - URL: https://developer.chrome.com/docs/webstore/using-api (リンク元) / https://developer.chrome.com/docs/webstore/cws-payments-deprecation (リンク先、404)
  - 出典日付: 記載なし(404のため確認不可)
  - 確度: 高(404であること自体は確認済み)、廃止の正確な年月日は確度: 低(未確認)
- 事実: 有料アイテム・追加機能・サブスクリプションを提供する場合、開発者アカウントに物理住所の登録が必須。
  - URL: https://developer.chrome.com/docs/webstore/set-up-account
  - 出典日付: 記載なし
  - 確度: 高
- 事実: EU向けの「Trader disclosure」要件が、非トレーダーの透明性要件は2022年5月28日、トレーダー検証要件は2024年2月17日に施行された。
  - URL: https://developer.chrome.com/docs/webstore/program-policies/trader-disclosure
  - 出典日付: 2024-02-09(ページ記載の最終更新日、UTC)
  - 確度: 高
- 事実: 拡張機能のランキングは「ユーザー評価、インストール数とアンインストール数の推移などの利用統計」に基づくヒューリスティックで決まり、リスティングページのメタデータも検索順位に影響する。新規公開が検索結果に反映されるまで数時間かかることがある。
  - URL: https://developer.chrome.com/docs/webstore/discovery
  - 出典日付: 2022-03-21(ページ記載の最終更新日、UTC)
  - 確度: 高
- 事実: 審査は「ほとんどの拡張機能で数日以内」だが「数週間かかる場合もある」。新規開発者や危険な権限要求は追加審査の対象になり得る。
  - URL: https://developer.chrome.com/docs/webstore/review-process
  - 出典日付: 2021-12-10(ページ記載の最終更新日、UTC)
  - 確度: 高
- 事実: 開発者登録は「一回限りの登録料(one-time registration fee)」を支払う必要があるが、金額は当該公式ページに明記されていない(通称5ドルとして広く知られているが、この金額を明記する一次情報のページは今回発見できなかった)。
  - URL: https://developer.chrome.com/docs/webstore/register
  - 出典日付: 記載なし
  - 確度: 中(登録料の存在は高確度、金額は未確認)
- 事実: Manifest V2からV3への移行スケジュールとして、2025年3月31日に全チャネルでMV2拡張機能がデフォルト無効化、2025年7月24日(Chrome 138)に再有効化不可、2026年8月31日に残存するMV2拡張機能がChrome Web Storeから完全に削除されると明記されている(既存インストール分は動作継続するが更新・再インストール不可)。
  - URL: https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline
  - 出典日付: 2026-09-09(ページ記載の最終更新日、UTC)
  - 確度: 高
- 不明: ソロ開発者が月$700〜$5,000規模に到達した具体名・金額・出典URL付きの事例は、本調査(直接WebFetch、WebSearch予算超過のため限定的)では発見できなかった。

### VS Code Marketplace

- 事実: 公式ドキュメント`code.visualstudio.com/api`配下のサイトマップ全体を確認したが、収益化・課金・決済に関するページは一件も存在しなかった(拡張機能の「pricing」プロパティは「Free」「Free Trial」ラベル表示のみで、実際の決済機能ではない)。
  - URL: https://code.visualstudio.com/api/working-with-extensions/publishing-extension
  - 出典日付: 2026-09-16(ページ記載の日付表記)
  - 確度: 中(「記載がないこと」の確認であり、断定的な「不可」ではない)
- 事実: Publisher検証は、Marketplaceチームが要件を確認し5営業日以内に結果を通知するとされている。
  - URL: https://code.visualstudio.com/api/working-with-extensions/publishing-extension
  - 出典日付: 2026-09-16
  - 確度: 高
- 不明: 審査(公開時のレビュー)プロセスの有無・期間、登録料、法人格の要否について、公式ドキュメントに明確な記載を見つけられなかった。
- 不明: ソロ開発者の月$700〜$5,000規模到達事例は、Indie Hackers上のThunder Client(VS Code拡張機能)のプロダクトページを確認したが、2021年3月のProduct Hunt立ち上げ時点の「$0/mo」報告しか見つからず、その後の収益マイルストーンは確認できなかった。
  - URL: https://www.indiehackers.com/product/thunder-client
  - 出典日付: 2021-03-31
  - 確度: 低(古い情報かつ目標金額に到達したことを示す情報ではない)

### Raycast Store

- 事実: Raycast公式ブログで「We didn't intend to monetize through extensions(拡張機能を通じた収益化は意図していなかった)」と明言されている。同記事では拡張機能はすべてオープンソースであることが審査要件とされ、GitHubのプルリクエストワークフローで審査される。
  - URL: https://www.raycast.com/blog/how-raycast-api-extensions-work
  - 出典日付: 2023-05-31
  - 確度: 高
- 事実: 開発者向け公式ドキュメント(developers.raycast.com)のサイトマップ全体を確認したが、「monetization」「earn」「revenue」といった収益化関連ページは一件も存在しない。
  - URL: https://developers.raycast.com/sitemap.md
  - 出典日付: 記載なし
  - 確度: 高(ページの不在という事実そのものは確認済み)
- 事実: 拡張機能公開(publish-an-extension)のドキュメントには審査期間の記載がなく、「プルリクエストを開いた後、レビューし、必要に応じて変更をリクエストする」とのみ記載。
  - URL: https://developers.raycast.com/basics/publish-an-extension
  - 出典日付: 記載なし
  - 確度: 高
- 不明: ソロ開発者の収益実績は、収益化の仕組み自体が存在しないため構造的に該当事例が見つからない。

### Obsidian コミュニティプラグイン

- 事実: 開発者ポリシーでは、支払いが必要な場合はREADMEで明確に開示することが求められており、「Payment is required for full access」のような表記が許可されている。Stripe等特定の決済手段への言及はない。
  - URL: https://docs.obsidian.md/community-directory/developer-policies
  - 出典日付: 記載なし
  - 確度: 高
- 事実: コミュニティディレクトリのFAQでは支払いモデルを「Free」「Optional payment(第三者サービスが課金する場合や機能を有料化する場合)」「Paid(支払いなしではアクセス不可)」の3種類に分類しているのみで、具体的な決済手段や手数料についての記載はない。
  - URL: https://docs.obsidian.md/community-directory/faq
  - 出典日付: 記載なし
  - 確度: 高
- 不明: 審査プロセスの所要期間、法人格の要否、検索・発見のされやすさに関する定量データは、公式ドキュメント(developer-policies, faq, submission-requirements-for-plugins)のいずれにも記載がなかった。
- 不明: ソロ開発者の月$700〜$5,000規模到達事例は、本調査では発見できなかった。

### WordPress.org プラグインディレクトリ

- 事実: プラグインディレクトリのガイドラインでは、外部の有料サービス(SaaS)と連携するプラグインは有料サービスであっても許可されるが、「トライアルウェア」(支払い後に機能をアンロックする形式)はディレクトリ上で禁止されており、プレミアム版は別配布とする必要がある。
  - URL: https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 2025年通年で12,713件のプラグインをレビューし(前年比+40.6%)、承認率69.5%。
  - URL: https://make.wordpress.org/plugins/2026/01/07/a-year-in-the-plugins-team-2025/
  - 出典日付: 2026-01-07
  - 確度: 高
- 事実: 2026年に入り申請数が急増し、審査待ちキューが1月の約300件から4月中旬に約1,050件まで積み上がったが、新規レビュアー投入で5月に一時ゼロまで解消。
  - URL: https://make.wordpress.org/plugins/2026/06/13/update-on-the-status-of-the-team-june-2026/
  - 出典日付: 2026-06-13
  - 確度: 高
- 事実: 全プラグインの約19%(10,500本超)が「0+installs」表示のまま埋もれているとの第三者集計がある。
  - URL: https://dev.to/dmtlo/almost-20-of-wordpressorg-plugins-are-stuck-at-0-installs-45lp
  - 出典日付: 記載なし
  - 確度: 中(個人ブログの独自集計、一次データ未確認)
- 事実: 2024年10月12日、WordPress共同創業者Matt Mullenweg氏が人気プラグイン「Advanced Custom Fields(ACF)」を作者の同意なく「Secure Custom Fields」としてフォークし、公式ディレクトリ上で置き換えた。
  - URL: https://www.creolestudios.com/scf-vs-acf-why-wordpress-forked-advanced-custom-fields/
  - 出典日付: 記載なし(2024年10月12日の出来事として言及)
  - 確度: 中〜高(複数の第三者記事が同一事実を報じている、一次発表元は未確認)
- 不明: 月$700〜$5,000規模到達の具体名を伴うソロ開発者の一次資料は、本調査では発見できなかった。Freemius社が引用する統計(平均年間売上約3,838ドル、97.6%が月$1,001未満)は約9年前のデータに基づくと記事自身が注記しており、現在の実態を反映しているか不明。

### Shopify App Store

- 事実: 公開アプリは独自の外部課金(off-platform billing)が禁止されており、Shopify App PricingまたはBilling API経由の課金が必須。
  - URL: https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements
  - 出典日付: 記載なし
  - 確度: 高
- 事実: レベニューシェアは2025年1月1日以降の生涯累計収益で最初の100万ドルが0%、それ以降は15%(+決済処理手数料2.9%)。2025年6月16日発効の契約改定で、従来「年次リセット」だった100万ドル免税枠が「生涯一回限り」に変更された。
  - URL: https://shopify.dev/docs/apps/launch/distribution/revenue-share ; https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share
  - 出典日付: 2025-06-16(changelog発効日)
  - 確度: 高
- 事実: レベニューシェアプラン登録には1パートナーアカウントあたり19ドルの一回限りの登録料が必要。
  - URL: https://shopify.dev/docs/apps/launch/distribution/revenue-share
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 支払いは月次基本、初回は「標準30日保留」があり、「支払い可否の最終決定権はShopifyにある」と明記。
  - URL: https://help.shopify.com/en/partners/partner-program/how-to-earn
  - 出典日付: 記載なし
  - 確度: 高
- 事実: レビュー所要期間は目安5〜10営業日とされるが、3週間〜1か月近く音沙汰がなかったという開発者の証言もある。
  - URL: https://www.growave.io/blog/how-long-does-shopify-app-review-take ; https://community.shopify.com/t/frustratingly-opaque-app-submission-requirements/306382
  - 出典日付: 記載なし
  - 確度: 中
- 事実(自己申告): Zigpoll開発者Jason Zigelbaum氏がソロファウンダーとしてMRR 12.5万ドルに到達したと公表。
  - URL: https://www.indiehackers.com/post/tech/hitting-125k-mrr-as-a-solo-founder-by-doubling-down-on-the-right-segment-c4o2Tfs6mjdpip5yZhaO
  - 出典日付: 記載なし
  - 確度: 中(自己申告、第三者検証なし)
- 事実(自己申告): 別のAMAで、1年未満でMRR 2.5万ドル、または500人超の有料顧客を獲得したという公表がある。
  - URL: https://www.indiehackers.com/post/i-bootstrapped-a-shopify-app-to-25k-mrr-in-less-than-a-year-ama-89f3d4c471 ; https://www.indiehackers.com/post/bootstrapped-a-shopify-app-to-500-paying-clients-with-an-mvp-ama-7dbaf8084e
  - 出典日付: 記載なし
  - 確度: 中(自己申告)
- 事実: 別のIndie Hackersまとめ投稿では、集計対象アプリの72%(約4,516本)が月間MRR $1,000未満と紹介されており、高額到達は少数派であることも同時に示されている。
  - URL: https://www.indiehackers.com/post/shopify-apps-by-revenue-mrr-95d499c311
  - 出典日付: 記載なし
  - 確度: 中
- 事実: パートナー契約に「Shopifyはいつでも合理的な通知の上でパートナープログラムの全部または一部を変更・廃止できる」「いずれの当事者も理由の有無を問わず即時に契約を解除できる」との条項がある。
  - URL: Shopify Partner Program Agreement(https://www.shopify.com/partners/terms 経由)
  - 出典日付: 最終更新2026-02-27と明記
  - 確度: 高

### Webflow App Marketplace

- 事実: Marketplace Guidelines公式ページには収益分配率・決済手数料・Webflow独自決済基盤の使用義務についての記述が一切なく、唯一の関連条項は「手数料・サブスクリプション・アプリ内課金について明確かつ透明な情報を提供すること」という開示義務のみ。
  - URL: https://developers.webflow.com/apps/docs/marketplace-guidelines
  - 出典日付: 記載なし
  - 確度: 高(規約原文を直接確認)
- 事実: Webflow Developer Agreement(バージョン日付2025年10月21日)の全文に"revenue"・"commission"・"payout"・"Stripe"・"billing"のいずれのキーワードも登場しない。
  - URL: https://developers.webflow.com/apps/developer-terms-of-service
  - 出典日付: 契約バージョン日付2025-10-21
  - 確度: 高
- 事実: 審査目標期間は10〜15営業日。
  - URL: https://developers.webflow.com/data/v2.0.0-beta/docs/marketplace/submitting-your-app
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Webflowコミュニティフォーラムで開発者自身が「マーケットプレイスでの発見性は実際どの程度機能しているのか」と質問しており、有効な回答が得られていない状況。
  - URL: https://community.webflow.com/ask-answer/post/questions-for-webflow-app-developers-and-agencies-about-monetization-and-WNgEaFt4bKzovaq
  - 出典日付: 記載なし
  - 確度: 低(未回答の質問投稿、情報の空白を示す状況証拠)
- 不明: 独自Stripe課金が事実上許容されているのか、単に規約整備が追いついていないだけなのかは、規約の沈黙のみからは判別できない。ソロ開発者の到達実績も発見できなかった。

### Framer Marketplace

- 事実: Framerは「Marketplaceでの収益からFramerは0%の手数料しか取らない、クリエイターは収益の100%を受け取る」と明言(プラグイン・コンポーネント・ベクター対象。テンプレートのみ紹介プログラムの対象で最大50%のアフィリエイトコミッションが別途ある)。
  - URL: https://www.framer.com/creators
  - 出典日付: 記載なし(2026-09-19時点の閲覧内容)
  - 確度: 高
- 事実: プラグイン公開に審査プロセスは存在しない。「Plugins are published immediately after you submit them. There is no review process or waiting period.」と明記。
  - URL: https://www.framer.com/help/articles/how-to-submit-a-plugin-to-the-marketplace/
  - 出典日付: 2026-09-16(ページ最終更新日として明記)
  - 確度: 高
- 事実(参考、プラットフォーム全体の集計値): Framerは「2025年にクリエイターへ合計650万ドルを支払った」と公表しているが、個別開発者の内訳は不明。
  - URL: https://www.framer.com/creators
  - 出典日付: 記載なし
  - 確度: 中(自社公表の集計値、第三者検証なし)
- 不明: 個別ソロ開発者の到達実績、検索・ランキングロジックの詳細は発見できなかった。

### Figma Community / Plugins

- 事実: Figma Communityでのリソース(プラグイン・ウィジェット・テンプレート等)販売は、Figmaの決済プラットフォームまたはサードパーティ決済サイトを選択できる。Figma決済利用時の手数料は15%の定額。
  - URL: https://help.figma.com/hc/en-us/articles/12067637274519-About-selling-Community-resources
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 支払い可能になるのは売上から30営業日後、入金頻度は最大週1回、対象国は70カ国以上。
  - URL: 同上
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「We are not approving new creators to sell paid files on Community at this time(現在、新規のCommunity有料販売者の承認は行っていない)」と明記されている。
  - URL: 同上
  - 出典日付: 記載なし(2026-09-19時点の閲覧内容)
  - 確度: 高
- 事実: クラシックプラグインは有料化(monetize)が可能だが、生成系(Generative)プラグインは有料化が「Not supported」と明記。
  - URL: https://help.figma.com/hc/en-us/articles/41407987481879-About-building-plugins-in-Figma
  - 出典日付: 記載なし(2026-09-19時点の閲覧内容)
  - 確度: 高
- 不明: 検索・カテゴリ・ランキングの仕組み、審査期間、ソロ開発者の月$700〜$5,000到達事例は本調査では発見できなかった。

### Notion(テンプレート・インテグレーション)

- 事実: Notion経由での決済(Stripe連携)を選ぶ場合、審査・承認に「数ヶ月かかる可能性がある」。承認後はStripeダッシュボードにアクセス可能。Notion経由を選ばない場合はGumroad等の第三者プラットフォームへのリンクも可能。
  - URL: https://www.notion.com/help/selling-on-marketplace
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Notion経由決済の手数料は8%+$0.40/取引。米国外の創作者には為替手数料1%が追加。入金は2週間ごとの木曜日、最低残高$20、14日間の資金保有期間あり。対象国は100カ国以上。
  - URL: 同上
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Template Galleryの掲載審査基準は「Value」「Build quality」「Popularity」「Price」「Novelty」「Visual design」「Thumbnail」「Seasonality」の8項目。Featured選定はNotion編集チームが「Timing」「Quality」「Use case」「Popularity」「Audience targeting」で選ぶ。
  - URL: https://www.notion.com/help/getting-featured-in-the-template-gallery
  - 出典日付: 記載なし
  - 確度: 高
- 不明: ソロ開発者の月$700〜$5,000到達の具体名付き事例は、第三者記事(Notion2Sheetsが月$8,400MRRとする記事)が403でアクセス不可となり、検索結果の要約のみで本文を確認できなかったため、事実として採用できなかった。

### Slack App Directory

- 事実: Slackには自前のBuyボタン等の課金機能がなく、開発者は自前のチェックアウト(Stripe等)をホストしワークスペースIDに紐づけて課金を管理する必要がある。
  - URL: https://dodopayments.com/blogs/monetize-slack-app
  - 出典日付: 記載なし
  - 確度: 中(公式ドキュメントでの直接的な断定は未確認、二次情報)
- 事実: Marketplace掲載には10アクティブワークスペース未満・週間アクティブユーザー10人未満のアプリは対象外という最低基準がある。データエクスポート/バックアップ機能やLLM学習目的のデータ利用を行うアプリは掲載不可。
  - URL: https://docs.slack.dev/slack-marketplace/slack-marketplace-app-guidelines-and-requirements
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「Slack Security Review」は提出のたびに実施され得るが実施時期は事前告知されない。
  - URL: https://docs.slack.dev/slack-marketplace/marketplace-terms-conditions/slack-security-review/
  - 出典日付: 記載なし
  - 確度: 高
- 不明: 審査所要期間・費用、法人格の要否、インストール数分布、ソロ開発者の到達実績はいずれも発見できなかった。

### Atlassian Marketplace(Jira / Confluence)

- 事実: 検索結果はOpenSearchによりNLPとエンゲージメント信号を使い、インストール数はランキング要因の一つに過ぎない。レビュー数・評価・スクリーンショット等がエンゲージメントスコアと検索順位に影響する。
  - URL: https://developer.atlassian.com/platform/marketplace/marketplace-search-results-and-rankings/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Rovo(AIアシスタント)経由の推薦などの新しい発見経路が増えているが、そのランキングロジックはAtlassianから公開されていない、とコミュニティ記事は指摘している。
  - URL: https://community.atlassian.com/forums/App-Central-discussions/Marketplace-Discovery-Is-Fragmenting-and-Small-Vendors-Feel-It/td-p/3249570
  - 出典日付: 記載なし
  - 確度: 中(コミュニティの考察であり一次データではない)
- 事実: 収益分配率は2026年4月1日時点でConnect 80%、Forge84%、Data Center 75%(いずれも開発者取り分)。2026年10月1日にさらに開発者取り分が引き下げ予定。
  - URL: https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/ ; https://www.atlassian.com/blog/development/updates-to-marketplace-revenue-share-2026
  - 出典日付: 記載なし(ブログは2026年発表)
  - 確度: 高
- 事実: 支払いは月内累計利益500ドル以上が発生した月の月末から30日以内(最大60日以内)。自前Stripe直接課金は不可。
  - URL: https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 重大な脆弱性は10日以内の是正義務、パートナー本人確認が2025年6月2日以降すべての新規承認の前提条件、バグバウンティプログラムの公開義務が2026年6月30日までに必須化。
  - URL: https://developer.atlassian.com/platform/marketplace/marketplace-security-enforcement-policy/
  - 出典日付: 記載なし(本文中の期限日は明記)
  - 確度: 高
- 不明: ソロ開発者の月$700〜$5,000到達の一次/第三者検証事例は発見できなかった。

### Salesforce AppExchange

- 事実: 自前Stripe等での直接課金は不可、AppExchange Checkout経由が前提。収益分配は銀行振込15%(累計2,000万ドル超で10%)、クレジットカード決済時は15%+取引ごとに0.30ドル追加。OEMパートナーは25%(2,000万ドル超で15%)。
  - URL: https://help.salesforce.com/s/articleView?id=000394757
  - 出典日付: 2026-04-20
  - 確度: 中〜高(一次のdeveloper.salesforce.com側ページは403で直接確認不可、help.salesforce.comの一次記事で代替確認)
- 事実: セキュリティレビュー費用は2023年3月16日以降、有料アプリで1回の提出につき999ドル(旧モデルの初回2,550ドル+年間150ドルは廃止)。無料アプリは費用なし。
  - URL: 一次ページ(developer.salesforce.com/.../security_review_fees.htm)は403のため直接未確認。複数の第三者記事(appnigma.ai、noltic.com、concret.io)が一致して同額を報告。
  - 出典日付: 記載なし(2023年3月16日改定という言及あり)
  - 確度: 中(一次情報未直接確認、複数の独立した第三者ソースが一致)
- 事実: 審査期間は初回パスまで6〜9週間、再提出ごとに2〜3週間との第三者報告(一次ページ403のため未直接確認)。
  - 出典日付: 記載なし
  - 確度: 低〜中
- 不明: ソロ開発者の実例は発見できず。見つかったのは法人・チーム規模の成功事例(Vlocity、Metazoa)のみで、ソロ開発者の到達実績としては該当しない。

### Google Workspace Marketplace

- 事実: インストール自体への課金は規約上禁止されているが、インストール後に自前のライセンス/課金(Stripe、Gumroad等)で機能に課金することは運用上可能(一次ポリシーに直接的な「Stripe可」の明記はないが、BudgetSheetの実例で確認)。
  - URL: https://developers.google.com/workspace/marketplace/terms/policies
  - 出典日付: 2025-08-28更新(ページヘッダー記載)
  - 確度: 中
- 事実: 通常審査は数日、機密(Sensitive)OAuthスコープは3〜5営業日。制限(Restricted)スコープでサードパーティサーバー経由アクセスの場合、CASA(第三者セキュリティ評価)が必須で完了に数週間かかることがあり、12か月ごとの再評価が必要。
  - URL: https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification ; https://developers.google.com/workspace/marketplace/about-app-review
  - 出典日付: 「Last updated 2026-09-03 UTC」
  - 確度: 高
- 事実(自己申告): 「BudgetSheet」(Google Sheets向け家計管理アドオン、ソロ開発者Vance Lucas氏)は約2年でMRR $1,600超に到達。決済はGumroadライセンスキー方式。
  - URL: https://www.indiehackers.com/post/how-i-built-a-google-sheets-extension-making-1-6k-mrr-b42d845e6a
  - 出典日付: 2022-05-04
  - 確度: 中(自己申告)
- 不明: 「Notion2Sheets」が月$8,400MRRに到達したという情報は、原典記事が403でアクセス不可のため本文を確認できず、事実として採用しなかった。

### Microsoft 365 / Excel アドイン(AppSource)

- 事実: Microsoft Marketplaceへの出品自体は無料。「トランザクト」オファーとして顧客がMicrosoft Marketplace経由で購入した場合、Microsoftは標準ストアサービス手数料3%を徴収する。これは2021年7月1日付で従来の20%から引き下げられたもの。
  - URL: https://learn.microsoft.com/en-us/partner-center/marketplace-offers/marketplace-commercial-transaction-capabilities-and-considerations ; https://www.geekwire.com/2021/microsoft-drop-commercial-marketplace-fees-3-20-latest-dig-platform-rivals/
  - 出典日付: GeekWire記事は2021年7月付。Learn記事に明確な更新日の記載なし
  - 確度: 高
- 事実: AppSource/Microsoft Marketplaceへの出品は無料。審査(証明)はマニフェスト検証と手動動作レビューを含み、通常3〜5営業日(提出キューの混雑状況による)。
  - URL: https://learn.microsoft.com/en-us/partner-center/marketplace-offers/submit-to-appsource-via-partner-center
  - 出典日付: 記載なし
  - 確度: 高
- 不明: WebSearch要約で見つかった「Excel add-inがProduct Hunt掲載後にMRR $22万に到達」という趣旨の情報は、原典を直接確認したところ該当する記述が存在せず、事実として採用しなかった(棄却)。Excel/Officeアドイン限定のソロ開発者到達実績は本調査では確認できなかった。

### Zapier Developer Platform

- 事実: 公開統合は無料、9,000以上のアプリ・66,000以上のトリガー/アクションが存在。
  - URL: https://zapier.com/developer-platform
  - 出典日付: 記載なし
  - 確度: 中
- 事実: Zapierスタッフが「アフィリエイトプログラムやアプリ利用に対する報酬制度は提供していない」と公式コミュニティで明言。
  - URL: https://community.zapier.com/how-do-i-3/do-i-get-any-revenue-as-my-app-is-used-23345
  - 出典日付: 2023-04-25
  - 確度: 高
- 事実: 開発者コミュニティでは審査待ちが28〜60日超に及ぶという苦情が2026年に複数投稿されている。
  - URL: community.zapier.com上の複数スレッド(2026-05-13、2026-06-26)
  - 出典日付: 2026年5〜6月
  - 確度: 高
- 不明: Zapierには課金・収益分配の仕組みそのものがないため、ソロ開発者の「Zapier由来の収入」という形の実例は構造的に成立しにくく、発見できなかった。

### Make(旧Integromat)

- 事実: Community Appsでは「Makeは一切手数料を取らず、パートナーが収益の100%を保持する」と明記。ただし決済基盤はMakeが提供せず、開発者が独自に構築する必要がある。
  - URL: https://developers.make.com/custom-apps-documentation/community-apps/how-does-it-work.md
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Community Appsの審査は2〜3営業日(ビジネス審査のみ、技術審査ではない)。
  - URL: developers.make.com上のドキュメント
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 契約条項上、Makeは「パートナーアプリと類似のアプリを自ら開発・公開できる」権利を明記している。開発者が対応を放棄した場合、Makeが当該アプリのコードへのアクセス・所有権を引き継ぐ権利も留保。
  - URL: https://developers.make.com/custom-apps-documentation/community-apps/terms-and-conditions.md
  - 出典日付: 記載なし
  - 確度: 高
- 不明: ソロ開発者の到達実績は発見できなかった。

### HubSpot App Marketplace

- 事実: 掲載・認定・インストールに一切手数料を課さない、収益分配もしないと公式文書に明記(2025年8月5日時点)。
  - URL: https://developers.hubspot.com/docs/apps/developer-platform/list-apps/apply-for-certification/certification-requirements
  - 出典日付: 「As of August 5, 2025」と本文に明記
  - 確度: 高
- 事実: 掲載には「30日以内に3件以上のユニークインストール実績」が必須で、新規アプリはマーケットプレイス外で最初の3件を獲得しない限り検索に現れない。
  - URL: https://developers.hubspot.com/docs/apps/developer-platform/list-apps/listing-your-app/app-marketplace-listing-requirements
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 2025年9月にマーケットプレイスを刷新し9種類のレコメンドアルゴリズムを導入。「レコメンドされたアプリはインストール率が2倍」と公式発表。
  - URL: https://developers.hubspot.com/blog/reimagined-marketplace-for-app-developers
  - 出典日付: 2025-09-03
  - 確度: 高
- 不明: ソロ開発者の月$700〜$5,000規模到達の具体的事例は発見できなかった。

### monday.com apps marketplace

- 事実: 新規マーケットプレイスアプリはすべてmonday独自の課金基盤で収益化する必要があり、外部決済システムは不可と明記。
  - URL: https://developer.monday.com/apps/docs/monetization
  - 出典日付: 2025-10-23(ページ更新日として明記)
  - 確度: 高
- 事実: 生涯累計収益20万ドルまで手数料0%、それ以降15%(2024年9月1日開始のプログラム)。
  - URL: https://developer.monday.com/apps/changelog/announcing-the-revshare-program
  - 出典日付: 記載なし(2024年9月開始と明記)
  - 確度: 高
- 事実(自己申告): monday.com公式ブログで、非技術系創業者Snir Alayof氏(Pioneera)が「数ヶ月でMRR $30,000」に到達したと紹介されている(monday.com自身の広報記事、第三者検証なし)。
  - URL: https://monday.com/appdeveloper/blog/build-30k-saas-monday-marketplace/
  - 出典日付: 2025-02-18
  - 確度: 低(自己申告かつプラットフォーム自身の広報記事)
- 事実: ノーコードやAI生成の「バイブコード」で作られたアプリは明示的に審査対象外という規定がある。
  - URL: https://developer.monday.com/apps/docs/monday-app-development-process
  - 出典日付: 2026-06-04(ページ更新日として明記)
  - 確度: 高

### Airtable マーケットプレイス

- 事実: Airtable自身が2020年のAMAで「マーケットプレイスはアプリを販売しない、広く利用可能にするだけ」と明言しており、プラットフォーム内課金は存在しない。
  - URL: https://community.airtable.com/development-apis-11/ama-apps-marketplace-edition-7089
  - 出典日付: 2020-09-17
  - 確度: 中(6年前の情報で現状の再確認はできていない)
- 事実: 開発者コミュニティで「利用統計はほぼ開発者に開示されない」「フィードバック募集の投稿をすると削除される」との証言がある。
  - URL: https://community.airtable.com/other-questions-13/lack-of-apps-marketplace-8780
  - 出典日付: 投稿期間2022-04〜2023-11
  - 確度: 中
- 事実(自己申告): 非技術系創業者Olive氏がAirtableベースの「Punch/Punch Pro」を自サイトで1回払い$19〜29で販売し、58人の有料ユーザーを獲得(累計$1,100〜1,700程度、月次収益ではない)。
  - URL: https://nocodeexits.substack.com/p/how-olive-built-an-app-with-airtable
  - 出典日付: 2024-02-23
  - 確度: 中(自己申告、かつ月$700〜$5,000という基準を厳密には満たさない)
- 不明: 月次$700〜$5,000規模の到達事例は発見できなかった。

### Discord App Directory

- 事実: 未認証(概ね100サーバー未満)のBotは公式Discovery(App Directory含む)の対象から構造的に除外される。約12,000認証済みアプリ、週間43万以上のBot利用、アクティブサーバーの30%以上がBotを利用という規模データも同時公表。
  - URL: https://discord.com/blog/discord-bots-and-app-discovery-announcement
  - 出典日付: 2021-11-17
  - 確度: 高
- 事実: 公式のSKU/Entitlements/Subscriptions APIによるBot内課金の仕組みが存在する。
  - URL: https://docs.discord.com/developers/monetization/overview
  - 出典日付: 記載なし
  - 確度: 高(仕組みの存在自体)
- 事実: 手数料率(Premium Apps標準30%、初年度$100万まで実績があれば15%、Server Subscriptionsは10%)は一次資料(support-dev.discord.com等)が403で直接確認できず、複数の二次情報源(postiz.com、flat.social等)の一致にとどまる。
  - 出典日付: 記載なし
  - 確度: 中(一次資料未確認)
- 不明: ソロ開発者の月$700〜$5,000到達事例、Discord Storeの終了経緯、Groovy/Rythm Bot停止事例は、いずれも一次資料に到達できず未検証。

### MCPサーバーディレクトリ群(公式レジストリ / Smithery / mcp.so / Glama / PulseMCP等)

- 事実: 公式MCP Registryのローンチ記事を含め、調査した全ディレクトリで開発者向けの決済基盤・サブスク機構・収益分配プログラムは一つも確認できなかった。
  - URL: https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/
  - 出典日付: 2025-09-08
  - 確度: 高
- 事実: Glamaは89,726件のMCPサーバーを索引しているが、うち「公式」5,781件・「claimed」5,174件で90%以上が未認証・未claimというノイズの多さを示している。
  - URL: https://glama.ai/mcp/servers
  - 出典日付: 記載なし(2026-09-20更新表記との言及あり)
  - 確度: 中
- 事実: 主要ディレクトリの一つSmitheryが2026年8月5日にArcade.devに買収され、買収発表ブログでは既存ディレクトリの独立運営継続についての明確なコミットメントがない。
  - URL: https://www.arcade.dev/blog/smithery-is-now-part-of-arcade
  - 出典日付: 2026-08-05
  - 確度: 高
- 事実: PulseMCPは21,869件を掲載しているが、現在新規登録を一時停止中(再開時期未定)。
  - URL: https://www.pulsemcp.com/servers
  - 出典日付: 記載なし
  - 確度: 高
- 不明: ソロ開発者の到達実績は発見できなかった。

### ChatGPT Apps / GPT Store(OpenAI)

- 事実: 2023年11月に発表された利用実績連動の収益分配プログラムは、2025年末時点でも「米国拠点の一部ビルダーのみを対象とした招待制パイロット」の域を出ておらず、新規募集も停止中。
  - URL: https://community.openai.com/t/what-is-the-status-with-gpt-store-revenue-share/839172
  - 出典日付: 2025年12月頃の状況を反映(投稿自体の正確な日付は要再確認)
  - 確度: 高
- 事実: 2025年12月開始の「Apps in ChatGPT」(Apps SDK)では、開発者自身のStripe等外部決済(External checkout)が現状唯一の一般提供パスで、プラットフォーム内課金は一部パートナー限定のプライベートベータにとどまる。
  - URL: https://developers.openai.com/apps-sdk/build/monetization/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「GPT Storeはバックエンド分析機能が乏しく、オンボーディングも弱いため開発者がユーザー獲得に苦戦」「スパム的GPTが上位表示される」との報道がある。
  - URL: https://techcrunch.com/2024/03/20/openais-chatbot-store-is-filling-up-with-spam/
  - 出典日付: 2024-03-20
  - 確度: 高
- 不明: ソロ開発者の到達実績は発見できなかった(理論値の試算はあるが実測値ではない)。

### Claude Software Directory(Anthropic)

- 事実: Anthropicの公式ポリシー文書は「金銭・暗号資産の移転や金融取引を実行するソフトウェア」「広告・スポンサーコンテンツを表示するソフトウェア」を明示的に禁止しており、収益分配・決済連携プログラムはToS上に一切記載がない。
  - URL: https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy ; https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms
  - 出典日付: 記載なし(2026年9月時点の一次資料)
  - 確度: 高
- 事実: Anthropicは「理由の如何を問わずいつでも通知なしに掲載を取り下げる権利」をToSで留保している。
  - URL: 同上
  - 出典日付: 記載なし
  - 確度: 高
- 不明: 検索・ランキングの仕組み、ソロ開発者の到達実績は発見できなかった(構造的にも決済手段自体が存在しないため成立しにくい)。

## グレーゾーン・未確認

- **Chrome Web Store Paymentsの正確な廃止年月日**: 「Chrome Web Store payments deprecation」という一次情報ページは現在404で削除されており、廃止告知そのものの原文・正確な年月日を一次情報で直接確認することはできなかった。現行の`accepting-payment`ポリシー(最終更新2022-11-01)は「開発者が販売者である」ことを前提とした記述になっており、独自決済が既に存在しないことは間接的に確認できるが、「2021年に廃止された」という具体的な年について一次情報での直接裏取りはできなかった。
- **インストール数分布・「新規アプリが埋もれる」度合いの定量データ**: 調べた全プラットフォームで、この点を直接示す公開統計・第三者調査は、WordPress.orgの約19%が0installsという第三者集計(一次データ未確認)以外にほとんど見つからなかった。HubSpotの「30日以内3インストール必須」やDiscordの「100サーバー未満は公式Discovery対象外」は規約上の構造的事実として確認できたが、これ以外のプラットフォームでは開発者の定性的な証言レベルにとどまる。
- **ソロ開発者の月$700〜$5,000到達の第三者検証済み事例**: 全プラットフォームを通じて、第三者(会計監査・プラットフォーム公式以外の独立した検証者)による検証済みの収益実績は一件も確認できなかった。すべて自己申告(Indie Hackers、開発者本人のブログ・SNS)または、プラットフォーム自身が広報目的で紹介した事例(monday.comのPioneera事例)のいずれかである。
- **Reddit上の開発者の生の証言に、調査ツールの制約上ほぼ到達できなかった**: 複数のサブエージェントがwww.reddit.comへのWebFetchが一貫してブロックされたと報告している。これは「新規アプリが埋もれる」という軸1、および「ソロ開発者の到達実績」という軸4の証言収集において、全プラットフォーム共通の限界となっている。
- **Discordの手数料率、Salesforceのセキュリティレビュー詳細ページ**: いずれも一次ページがHTTP 403で直接確認できず、複数の独立した二次情報源の一致に基づいて中程度の確度で記載した。数字を意思決定に使う場合は、ログイン済み環境での一次資料の再確認を推奨する。
- **Webflowの実質的な課金方式**: 規約に収益分配率の記載が一切ないため、「独自Stripe課金が事実上許容されているのか、単に規約整備が追いついていないだけなのか」は判別できなかった。
- **VS Code Marketplaceの参入障壁と検索アルゴリズム**: 公式ドキュメントに審査プロセス・法人格要否・検索ランキングロジックについての明確な記載が見当たらず、「情報が存在しない」のか「単に発見できなかった」のかを本調査では区別できなかった。
- **Canva Premium Apps Programの詳細**: 公式ページ(canva.com/developers/premium-apps-program/)がHTTP 403で直接確認できず、手数料率・審査要件・対象国について十分な裏取りができなかった。
- **NotionのGumroad等外部販売実績**: Notionテンプレートを外部プラットフォーム(Gumroad等)で販売しているソロ開発者の月$700〜$5,000到達実績について、原典記事へのアクセスが403でブロックされ、確認できなかった。
- **調査プロセス自体の限界**: 本調査はセッションのWebSearch呼び出し上限(200回)に複数回到達したため、後半はWebFetchによる直接取得やBing/DuckDuckGo経由の代替検索に依存した。また、並列起動した5系統のサブエージェントのうち2系統は、割り当てられた調査を自ら実行せずさらに孫エージェントへ委任しようとする挙動を示したため、該当領域(Chrome Web Store、VS Code Marketplace、Raycast Store、Obsidian、Figma、Notion、Canva)はメインエージェントが直接一次情報を再確認する形で補完した。この経緯により、これらのプラットフォームは相対的に一次情報への到達度が高く、それ以外のプラットフォーム(Atlassian、Salesforce、Slack等)は一部で二次情報・第三者記事への依存度がやや高い。

## 影響する論点

- `docs/plan/indie-earning-fields/open-questions.md`(存在する場合)における「検索流入だけで新規ユーザーが獲得できるプラットフォームはどれか」という論点に対し、本調査は「実績ゼロからの検索流入獲得を裏付ける定量データはどのプラットフォームにも見つからなかった」という否定的材料を提供する。オーナーの「発信・集客をメインにしない」という前提条件は、少なくとも初速(最初のインストール実績)を獲得する段階では、多くのプラットフォームで何らかの形の外部集客(コミュニティ投稿、SNS、既存ユーザーからの紹介等)を必要とする可能性が高いことを示唆している。
- `docs/plan/indie-earning-fields/decisions.md`における「プラットフォーム内課金を避け、自前Stripeで入金をコントロールする」という条件について、Shopify App Store・Atlassian Marketplace・Salesforce AppExchange・monday.comはこの条件に構造的に反する(プラットフォーム課金必須)ため、候補から除外するかどうかの判断材料になる。逆にWordPress.org、Obsidian、Zapier/Make、Airtable、Slack App Directory、Webflowはこの条件と両立し得る。
- Figmaの「新規有料コミュニティ販売者の承認を現在停止中」という事実は、Figma Communityを収益化の入口として検討する場合、現時点では実質的に選択肢から外れることを意味し、関連する論点があれば更新が必要。
- Chrome Web StoreのManifest V3強制移行(2026年8月31日に旧仕様完全削除)は、もしChrome拡張機能を検討する場合、開発時点で必ずManifest V3準拠を前提とすべきという実装上の制約として、実装計画に反映すべき論点である。
