# アプリ名候補12個の検索衝突・埋没リスク調査

- 調査日: 2026-09-21
- 調査手段: Sonnet サブエージェント + メインによる原文確認(メインが確認した原典: nock/nock が 13,126★ で活発、reticlehq/reticle が 803★ で活発、GitHub のリポジトリ検索で clavigate は 1 件(0★)のみ、formulae.brew.sh の cask/clavigate と formula/clavigate が 404、clavigate.app と clavigate.dev に A レコードなし・clavigate.com は応答あり。第 2 弾でメインが確認した原典: GitHub のリポジトリ名検索で hintjump と hintkey は 0 件・同名のユーザー/組織なし、letterhop は同名の Organization(2026-08-12 作成)あり、letterjump は 0★ のリポジトリ 1 件、rsaz/keyhop は Rust・11★・説明文「You don't need a mouse!」、DNS 照会で hintjump と hintkey の .com / .app / .dev はいずれも A レコードなし。それ以外はサブエージェントの報告のまま)
- 問い: 12 個のアプリ名候補に、検索で埋もれる原因になる衝突があるか

## 結論

オーナーは 2026-09-21 に Clavigate と Clavio を「由来を知らないとピンとこない」として却下した。
第 2 弾の候補 Keyvia は、同名の中国企業サイト(keyvia.cn)が存在するため調査前に外した。第 1 弾でドメインを直接取得したことが原因でオーナーのウイルス対策ソフトがダウンロードを隔離したため、第 2 弾ではドメインは DNS 照会のみで確認した(.claude/skills/_shared/safe-fetching.md)。

12 候補いずれも Homebrew(cask/formula)には未登録(全件 404)。一方で、Google 検索・GitHub・既存アプリ・企業名のいずれかで無視できない衝突が全候補に見つかった。衝突の性質は候補ごとに異なり(辞書語による飽和、著名企業・著名 OSS ライブラリとの一致、同音異義語による誤記リスクなど)、どれが最も深刻かは論点(検索順位で埋もれるか/同音異義語で誤記されるか/商標紛争リスクか)によって評価が変わるため、本調査では順位付けや推奨は行わない。事実は以下の通り。

| 名前 | 最大の衝突 | Homebrew | ドメインの状況 |
|---|---|---|---|
| Clavigate | 明確な衝突なし(類似語 Claviger 等が混在する程度) | cask/formula とも 404(未登録) | .app/.dev は DNS 解決失敗、.com は応答ありだが GoDaddy 製の「Coming Soon」プレースホルダー |
| Pressto | macOS 向け既存アプリが複数(LLM テキスト変換アプリ、YouTube→WordPress アプリ)、GitHub に 841★ の React Native ライブラリ | cask/formula とも 404 | .app/.dev は DNS 解決失敗、.com はスペインのクリーニングチェーン(実事業、稼働中)が保有 |
| Callkey | 複数の実在企業(CallKey International Inc. 等)、Sailfish OS 向け既存アプリ | cask/formula とも 404 | .app/.dev/.com すべて DNS 解決失敗(サイトなし) |
| Unmouse | 2008年 Microsoft Research のプロトタイプ「UnMouse Pad」がテック大手メディアで報道済み、GitHub に機能的に近い「マウス代替」系リポジトリ複数 | cask/formula とも 404 | .app/.dev は DNS 解決失敗、.com はオランダのホスティング会社のデフォルトページ(未構築) |
| Keyspot | macOS 対応の既存アプリ(コミュニティ系)、開発者向け CLI ツール(シークレット管理)、AI SaaS(keyspot.ai)が並立 | cask/formula とも 404 | .app/.dev は DNS 解決失敗、.com は HTTP 200 だがドメイン販売用パーキングページ |
| Hopmark | 直接の衝突は薄いが、音が近い著名 Mac アプリ「Hookmark」との混同リスク | cask/formula とも 404 | .app/.dev は DNS 解決失敗、.com は HugeDomains 経由の販売中ドメイン(第三者保有・未使用) |
| Jumptag | 実在の消費者向けブランド企業「JUMPTAG CLUB」(アプリ稼働中) | cask/formula とも 404 | .app は HTTP 200(JUMPTAG CLUB の稼働中サイト)、.dev は DNS 解決失敗、.com は HTTP 200 だが JS リダイレクトのみのランダーページ |
| Reticle | GitHub に 803★ (本日更新、アクティブ)の開発者向けツールを筆頭に、同名の macOS アプリ・OSS プロジェクトが複数乱立。企業商標(Reticle Labs LLC)も存在 | cask/formula とも 404 | .com は GoDaddy の販売中ページへリダイレクト、.dev は DNS 解決失敗、.app は接続確立できず内容未確認 |
| Deadeye | 辞書語(Merriam-Webster 掲載)、macOS 向け既存ユーティリティ(GitHub, 10★, アクティブ)、MITRE ATT&CK 記載のマルウェア名、Take-Two Interactive の登録商標「DEAD EYE」 | cask/formula とも 404 | .com は BrandBucket の販売中ブランド名ページへリダイレクト、.dev は HTTP 200(モバイルゲームのティザーサイト)、.app は HTTP 404(応答はあるがページなし) |
| Nockpoint | 商用 SaaS が 2 系統(データ分析 SaaS、アーチェリークラブ管理ソフト)で同名並立、実店舗チェーンも存在 | cask/formula とも 404 | .com は HTTP 200(データ分析 SaaS 企業の稼働中サイト)、.app/.dev は DNS 解決失敗 |
| Callsign | 一般英単語として非常に高頻度、かつ著名な ID 認証・不正検知企業「Callsign Inc.」(App Store 掲載、Gartner 掲載)が実在 | cask/formula とも 404 | .com は HTTP 200(Callsign Inc. の公式企業サイト)、.app/.dev は DNS 解決失敗 |
| Nock | GitHub に 13,126★(直近更新)の npm ライブラリ「nock」が突出、494★ のブロックチェーンプロジェクト「Nockchain」も活発、"Knock" との同音異義語で誤記実例が第三者記事(Grammarly)で確認済み、機能的に近い既存 Mac アプリ「Knock」も存在 | cask/formula とも 404 | .dev は HTTP 200(Urbit ホスティングサービスが稼働中)、.com は接続確立できず内容未確認、.app は DNS 解決失敗 |

### 第 2 弾(2026-09-21)

8 候補(Letterhop, Typick, Keyward, Hintjump, Keyhop, Hintkey, Letterjump, Typoint)いずれも Homebrew(cask/formula)・npm には未登録(全件 404)。GitHub・Google 検索・既存アプリ・企業名では候補ごとに程度の異なる衝突が見つかった。特に **Keyhop** は、今回のアプリと機能説明がほぼ一致する OSS プロジェクト(`rsaz/keyhop`、Windows 版が Microsoft Store/crates.io で配信中、README に将来の macOS/Linux 対応も言及)が存在し、単なる名前の衝突を超えて製品コンセプトそのものが重複している点で他候補と性質が異なる。順位付けは行わない。

| 名前 | 最大の衝突 | GitHub | Homebrew | npm | ドメイン(DNS のみ) |
|---|---|---|---|---|---|
| Letterhop | 既存の同名ワードゲーム(letterhop.io)、同名 GitHub Organization(2026-08-12 作成、blog=letterhop.eu) | 1 件(0★、無関係) + 同名 Organization(リポジトリ0) | cask/formula とも 404 | 404(未登録) | .com は A レコードあり、.app/.dev はなし |
| Typick | パリの実店舗カフェ「Typick Café」+ ネット通販「Typick Store」(typick.com稼働中)、App Store の類似綴りアプリ「Typic」(写真テキスト編集、2本) | 5 件(完全一致なし、休眠中心) + 同名ユーザー(2017年作成、休眠) | cask/formula とも 404 | 404(未登録) | .com は A レコードあり、.app/.dev はなし |
| Keyward | ベルリンの資金調達済み B2B SaaS 企業「Key Ward」(keyward.io、エンジニアリングデータ×AI基盤、Crunchbase/Dealroom掲載) | 75 件、最多は gateway-of-last-resort/keyward(48★、SSH鍵管理TUI、2026-08-20更新=アクティブ) + 同名ユーザー(2014年作成、休眠) | cask/formula とも 404 | 404(未登録) | .com/.app/.dev すべて A レコードあり |
| Hintjump | 明確な既存製品・企業なし(Second Life wiki の UI 通知名という断片的用例のみ) | 0 件 | cask/formula とも 404 | 404(未登録) | .com/.app/.dev すべて A レコードなし |
| Keyhop | 機能説明がほぼ同一の OSS「keyhop」(rsaz/keyhop, Rust, crates.io/docs.rs, MSIインストーラでMicrosoft Store配信、11★、2026-06-22更新=アクティブ)。他に macOS 向けランチャー「KeyHop」(kuniyoshi/KeyHop, Swift)、AIツールのアカウント切替ツール「keyhop」、iOS VPN「KeyHop VPN」等が乱立 | 10 件 | cask/formula とも 404 | 404(未登録) | .com/.app は A レコードあり、.dev はなし |
| Hintkey | 明確な製品・企業なし。Apple の API 定数名 `NSImageRep.HintKey` 等、技術的な語としての用例のみ。「hint key」自体が Vimium 系リンクヒントツールで一般的に使われる用語 | 0 件 | cask/formula とも 404 | 404(未登録) | .com/.app/.dev すべて A レコードなし |
| Letterjump | 明確な企業・著名製品なし。個人開発者のタイピングゲーム「LetterJump」(itch.io、小規模)、同名 GitHub リポジトリ(2020年で更新停止) | 1 件 | cask/formula とも 404 | 404(未登録) | .com は A レコードあり(keyhop.com と同一IPで応答)、.app/.dev はなし |
| Typoint | ベルリンのタイポグラフィ・デザイン事務所「typoint」(typoint.com、稼働中の実企業サイト) | 2 件(完全一致なし) | cask/formula とも 404 | 404(未登録) | .com は A レコードあり、.app/.dev はなし |

## 根拠

### Clavigate

- 事実: 「Clavigate」単独でのヒットはほぼなく、支配的な既存語・企業は見当たらない。類似語「Claviger」(中世の「鍵保持者」称号)、「Clavister」(スウェーデンのネットワークセキュリティ企業)、「Claviate」(風力タービン最適化AI企業)が混じる程度。
  - URL: https://en.wikipedia.org/wiki/Claviger_(title) , https://en.wikipedia.org/wiki/Clavister
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 「Clavigate mac app」「Clavigate software」で該当する製品は発見できず。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: GitHub 検索でヒットするのは `AmamDeus/clavigate-site`(スタートアップ用サイトテンプレート、0スター、7/18更新)1件のみ。「Clavigate」という名のユーザー/組織は見当たらない。
  - URL: https://github.com/search?q=Clavigate&type=repositories
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `formulae.brew.sh/api/cask/clavigate.json` および `/api/formula/clavigate.json`、また `formulae.brew.sh/cask/clavigate` `/formula/clavigate` のページはいずれも HTTP 404(未登録)。
  - URL: https://formulae.brew.sh/cask/clavigate , https://formulae.brew.sh/formula/clavigate
  - 出典日付: 記載なし
  - 確度: 高(メインで直接 HTTP ステータスを確認)
- 事実: 該当する既存アプリ・開発者ツールは見当たらない。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 明確に「Clavigate」を名乗る有名企業・商標は見当たらない。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `clavigate.app` `clavigate.dev` は DNS 解決失敗(A レコードなし)。`clavigate.com` は HTTP 200 で応答するが、GoDaddy のサイトビルダーで作られた「即将推出(Coming Soon)」中国語表記のプレースホルダーページで、実運用中の事業とは考えにくい。
  - URL: https://clavigate.com
  - 出典日付: 記載なし(ページ内コピーライト表示は2026年)
  - 確度: 高(メインで直接 DNS/HTTP を確認)
- 事実: 造語(clavier「鍵盤」+ navigate?)で、綴り・発音とも聞いただけでは再現しづらい可能性がある(「クラヴィゲイト」か「クラビゲート」か迷う)。ネガティブ・下品な意味は確認されず。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Pressto

- 事実: 「Pressto」は非常に多義的。スペインの洗濯・クリーニングのフランチャイズ企業(1994年創業、25カ国500店舗以上)、教育系ライティングプラットフォーム、Snellville(米ジョージア州)のバーガー店など複数の実在事業がヒットする。
  - URL: https://en.wikipedia.org/wiki/Pressto
  - 出典日付: 記載なし
  - 確度: 中
- 事実: macOS 向けだけで少なくとも2つの既存アプリが存在する——(1) LLMベースのテキスト変換Macアプリ「Pressto: LLM-powered text transforms for macOS」、(2) YouTube動画をWordPress記事に変換するAI Macアプリ(App Store)。さらにPR特化AIソフト「Pressto AI」、教育ライティングアプリも存在する。
  - URL: https://pressto.jdwilson.ca/ , https://apps.apple.com/us/app/pressto/id6745399059 , https://www.heypressto.ai/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: GitHub の `enzomanuelmangano/pressto` が841スター(React Native向けタップインタラクションライブラリ、2026/6/13更新)存在する。他に `netsensei/pressto`(44★)、`crocs-muni/pressto`(7★)もあり、GitHub検索全体で93件ヒットする。
  - URL: https://github.com/enzomanuelmangano/pressto
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `formulae.brew.sh/cask/pressto` `/formula/pressto` ともに404、未登録。
  - URL: https://formulae.brew.sh/cask/pressto
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: macOSアプリ・React Nativeライブラリ双方に既存の「Pressto」が存在し、特にmacOSアプリでの完全一致は大きな懸念。
  - URL: 上記に同じ
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Pressto(スペインのクリーニングチェーン)は500店舗超の実在フランチャイズブランドである。
  - URL: https://pressto.com
  - 出典日付: 記載なし
  - 確度: 中〜高
- 事実: `pressto.com` はHTTP 200で、実際に「Pressto franquicia internacional」というタイトルの稼働中の事業サイトである。`.app` `.dev` はDNS解決失敗。
  - URL: https://pressto.com
  - 出典日付: 記載なし
  - 確度: 高
- 事実: "Presto"(魔法の掛け声、National Presto Industries、トロントの交通系ICカード"Presto"、Operaのレンダリングエンジン"Presto"等)と発音がほぼ同一で、聞いた人が「Presto」と綴ってしまうリスクが指摘できる。
  - URL: なし(言語的推測+一般常識)
  - 出典日付: 記載なし
  - 確度: 低〜中

### Callkey

- 事実: 複数の異なる企業が「CallKey」を名乗る——CallKey International Inc.(バンクーバー拠点の電話サービス企業、Bloomberg/PitchBook/Crunchbaseにプロフィールあり)、CallKey(英国の元SIMカード企業、廃業)、Callkey Networks(ケニア、無線通信機器)。
  - URL: https://www.bloomberg.com/profile/company/CKYI:US , https://www.crunchbase.com/organization/callkey
  - 出典日付: 記載なし
  - 確度: 中
- 事実: Sailfish OS(Nokia系モバイルOS)向けのアプリ「CallKey」(SIPコールでゲート等を開閉するツール)が存在するが、macOS版は確認できず。
  - URL: https://openrepos.net/content/rikudousennin/callkey
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 完全一致の「Callkey」という単体リポジトリ・組織は見当たらないが、`RikudouSage/harbour-callkey`(Sailfish OS向け、0★、8日前更新=アクティブ)などが存在する。
  - URL: https://github.com/RikudouSage/harbour-callkey
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `formulae.brew.sh/cask/callkey` `/formula/callkey` ともに404、未登録。
  - URL: https://formulae.brew.sh/cask/callkey
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: Sailfish OS向けアプリ以外に目立った開発者ツールは無い。
  - URL: 上記に同じ
  - 出典日付: 記載なし
  - 確度: 中
- 事実: CallKey International Inc.(上場企業プロフィールあり)、Callkey Solutions LLP(インドのITソリューション企業)など複数の実在企業がある。
  - URL: http://www.callkey.in/
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `callkey.com` はDNS解決失敗(サイトなし)。`.app` `.dev` も同様。
  - URL: なし(DNS失敗のため対象ページなし)
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: 「Call key」という直訳的な組み合わせで、聞き間違い・綴り間違いのリスクは低い。ネガティブな意味は確認されず。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Unmouse

- 事実: 2008年にMicrosoft Researchが発表した圧力感知式マルチタッチパッドのプロトタイプ「UnMouse Pad」がTechCrunch・Gizmodo・Hackadayなど著名テックメディアで報じられており、検索結果の上位を占める。もう一つ、Carl Burch氏による2002年の手のジェスチャー認識ソフト「The Un-Mouse」も存在する。
  - URL: https://techcrunch.com/2008/07/31/microsofts-unmouse-pad-an-enormous-pressure-sensing-trackpad/ , https://hackaday.com/2008/07/31/unmouse-cheap-multitouch-prototype/
  - 出典日付: 記載なし(記事は2008年公開)
  - 確度: 高
- 事実: macOS向けの明確な既存アプリは見当たらないが、「The Un-Mouse」(webカメラで手を追跡しカーソルを操作するソフト、配布不可ライセンス)がヒットする。
  - URL: https://cburch.com/proj/unmouse/index.html
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `pdelfino/unmouse`(JavaScript、「キーボードでマウス操作を代替するテキスト選択ツール」、1★)、`tycheung/unmouse`(Python、「OSレベルの視線・ジェスチャー入力」、0★)など、機能的に今回のアプリと近い「マウス代替」系リポジトリが複数存在する。
  - URL: https://github.com/pdelfino/unmouse
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `formulae.brew.sh/cask/unmouse` `/formula/unmouse` ともに404、未登録。
  - URL: https://formulae.brew.sh/cask/unmouse
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: Microsoft研究プロトタイプ、Android版「UnMouse」(Wi-Fi/Bluetooth経由でPC遠隔操作)などが存在する。
  - URL: 上記に同じ
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 大手企業による商標としての「Unmouse」は確認されない(Microsoftのプロトタイプは製品化されていない研究発表)。
  - URL: なし
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `unmouse.com` はDNS自体は解決するがSSL証明書がオランダのホスティング会社(Hostnet)のものになっており、実際はホスティング会社のデフォルトページ(未構築ドメイン、タイトル「Hostnet: 最大手のドメイン・ホスティングプロバイダ」)。`.app` `.dev` はDNS解決失敗。
  - URL: http://unmouse.com
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 英語として「unmouse」は正式な単語ではないが意味は直感的("マウス無し"の意)。下品・ネガティブな意味は無い。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Keyspot

- 事実: 「Keyspot」は極めて多義的で複数の実在製品がヒットする——地域コミュニティ向けアプリ「Key Spot」(App Store/Google Play)、イタリアのソフトウェア販売会社「KeySpot」(keyspot.it)、AI提案書スクリーニングSaaS「keyspot」(keyspot.ai、ドイツのDAX上場企業からスピンオフ)、デイケアプログラム「Parkmead Keyspot」。
  - URL: https://www.keyspot.ai/ , https://apps.apple.com/us/app/keyspot/id1046238494
  - 出典日付: 記載なし
  - 確度: 高
- 事実: App Store上にmacOS対応の「KeySpot」アプリ(Quality SAP Inc.、コミュニティ向け取引情報アプリ)が実在する。さらに開発者向けの「KeySpot」(環境変数・シークレット管理CLIツール、keyspot.app)も存在し、今回のアプリと同じ開発者オーディエンス層に刺さる。
  - URL: https://apps.apple.com/us/app/keyspot/id1046238494 , https://www.keyspot.app/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 組織「KeySpot」(python-api, node-api, web-client, cli-tool-ppaなど複数リポジトリ、いずれも0★、2021-2022年更新で停滞)が存在する。別に `shrey-17bhardwaj/keyspot`(Flutter向けオンボーディング/ツアーライブラリ、18★、29日前更新=アクティブ)もある。
  - URL: https://github.com/KeySpot
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `formulae.brew.sh/cask/keyspot` `/formula/keyspot` ともに404、未登録。
  - URL: https://formulae.brew.sh/cask/keyspot
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: モバイルアプリ、CLIツール、SaaSと3系統で「Keyspot」ブランドが並立している。
  - URL: 上記に同じ
  - 出典日付: 記載なし
  - 確度: 高
- 事実: keyspot.ai(ドイツ企業からのスピンオフ、資金調達済みとみられるB2B SaaS)など複数の実在企業がある。
  - URL: なし(検索結果ベース)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `keyspot.com` はHTTP 200だが、iframeで`domainshop.com`を読み込むだけの販売用パーキングページ(実サイトなし)。`.app` `.dev` はDNS解決失敗。
  - URL: https://keyspot.com
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 発音・綴りは平易で問題なし。ネガティブな意味も無い。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Hopmark

- 事実: 支配的な単一の意味は無い——ノルウェーのサッカー選手Andreas Hopmark、ニュージーランドホップ業界の品質認証マーク「Hopmark™」、廃業した鉱業関連企業「Hopmarks」などが混在する。
  - URL: https://en.wikipedia.org/wiki/Andreas_Hopmark
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 「Hopmark」に該当する明確な既存製品は見つからない。検索結果は同音類似の「Hookmark」(著名なMac用ブックマーク/リンク管理アプリ、CogSci Apps社製、Setapp配信)に誘導される。
  - URL: https://hookproductivity.com/download/
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `rsbohn/hopmark`(Python、0★)、`Renaaa189/Hopmark`(JavaScript、学務管理システム、1★、6/8更新)などいずれも小規模。
  - URL: https://github.com/Renaaa189/Hopmark
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `formulae.brew.sh/cask/hopmark` `/formula/hopmark` ともに404、未登録。
  - URL: https://formulae.brew.sh/cask/hopmark
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: 目立った既存アプリ/開発者ツールは確認されない。
  - URL: なし
  - 出典日付: 記載なし
  - 確度: 中
- 事実: NZ Hops Ltd.の品質マーク「Hopmark™」がトレードマーク的に使用されている(Facebook投稿等で確認)。
  - URL: https://www.facebook.com/newzealandhops/
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `hopmark.com` はHugeDomains経由で「HopMark.com is for sale」という販売中ドメインページに302リダイレクトする(第三者が保有・未使用)。`.app` `.dev` はDNS解決失敗。
  - URL: http://hopmark.com
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 単体の意味は薄いが、音として著名な既存Macアプリ「Hookmark」(hook-mark)と非常に近く、開発者が音声やうろ覚えで検索した際に取り違える・誤変換するリスクが指摘できる。
  - URL: なし(言語的推測+Hookmarkの実在確認に基づく)
  - 出典日付: 記載なし
  - 確度: 低〜中

### Jumptag

- 事実: ウェアラブルテック+アプリのブランド「JUMPTAG CLUB」(実在の消費者向け企業、Instagram/Facebook等SNSも活発)が最も目立つ。ほかに2008年前後のソーシャルブックマークサービス「Jumptags.com」(現在は休眠ブログ状態)がある。
  - URL: https://www.jumptag.app/ , https://jumptags.wordpress.com/
  - 出典日付: 記載なし
  - 確度: 中〜高
- 事実: JUMPTAG CLUBの公式アプリ(jumptag.app)が実在する。Mac専用アプリではないがブランドの正式製品である。
  - URL: https://www.jumptag.app/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `KarnaTheGameDev/JumpTag`(0★)、組織`JumptagClub/Jumptag`(0★、2024/9更新)などいずれも小規模で活動が薄い。
  - URL: https://github.com/JumptagClub/Jumptag
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `formulae.brew.sh/cask/jumptag` `/formula/jumptag` ともに404、未登録。
  - URL: https://formulae.brew.sh/cask/jumptag
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: JUMPTAG CLUBアプリ以外に目立った開発者ツールは無い。
  - URL: なし
  - 出典日付: 記載なし
  - 確度: 中
- 事実: JUMPTAG CLUBは実在の消費者ブランド企業として運営中である。
  - URL: 上記に同じ
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `jumptag.app` はHTTP 200で、実際にJUMPTAG CLUBのサインイン/ダッシュボードのある稼働中サイトである。`jumptag.com` はHTTP 200だが、JavaScriptで`/lander`へ強制リダイレクトするだけの内容(ドメイン販売系ランダーの可能性)。`.dev` はDNS解決失敗。
  - URL: https://www.jumptag.app/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 綴り・発音とも平易。ネガティブな意味は無い。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Reticle

- 事実: 銃器用スコープ・光学機器の「レチクル(照準線)」という技術用語が辞書的に支配的(SIG Sauer、Thorlabs、Edmund Optics等の光学/銃器業界サイトが上位を占める)。
  - URL: https://www.sigsauer.com/glossary/reticle/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 少なくとも3つの独立したmacOSアプリ・ツールが「Reticle」を名乗る——LLM設計・デバッグ用デスクトップアプリ(reticle.run、macOS/Windows対応)、Apple SiliconのMLXモデル管理メニューバーアプリ「Reticle MLX」、ゲーム用クロスヘア表示アプリ「ReticleKit」(reticlekit.com)。
  - URL: https://reticle.run/ , https://reticlekit.com/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `reticlehq/reticle` が803★で2026/9/21(本日)も更新されているアクティブな開発者向けツール(AIエージェント検証)。他にも `soth-ai/mcp-reticle`(120★、2026/9/20更新)、`fwdai/reticle`(30★、「Postman for AI」)、`ussjoin/reticle`(90★)、`PsychoLlama/Reticle`(49★)、`vegaluisjose/reticle`(39★)など、開発者コミュニティ内で複数の中規模〜人気プロジェクトが同名で乱立している。
  - URL: https://github.com/reticlehq/reticle
  - 出典日付: 記載なし(更新日 2026-09-21 とAPIレスポンスに記載)
  - 確度: 高(メインで直接確認: 803★・アクティブ)
- 事実: `formulae.brew.sh/cask/reticle` `/formula/reticle` ともに404、未登録。
  - URL: https://formulae.brew.sh/cask/reticle
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: 対象読者である開発者層にとって「Reticle」は既に複数の人気OSSプロジェクト・商用AIツールで埋まっている。
  - URL: 上記に同じ
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「Reticle Labs LLC」という米シリコンバレーの企業が商標登録を保有している(不具合管理・データアーカイブ事業)。
  - URL: https://trademarks.justia.com/owners/reticle-labs-llc-2615666
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `reticle.com` はGoDaddyの販売中ページ(forsale.godaddy.com)に307リダイレクトする。`reticle.app` は複数回(WebFetch、curlの異なるプロトコル・タイムアウト設定)試行したが接続確立できず、内容確認不可。`.dev` はDNS解決失敗。
  - URL: https://forsale.godaddy.com/forsale/reticle.com
  - 出典日付: 記載なし
  - 確度: 高(.com)/低(.app、接続不能のため未確認)
- 事実: 発音・綴りは平易(reh-tih-kul)。銃器連想がやや強い単語だが、UI/光学分野では一般的な技術用語でもあり、ネガティブというより「既に技術用語として手垢がついている」ことが弱点として指摘できる。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Deadeye

- 事実: Merriam-Webster・Wikipediaに辞書項目がある一般英単語(元は帆船の索具部品、転じて「凄腕の射手」の意)。ゲーム(Red Dead Redemptionのゲームメカニクス)、バンド名、飲み物の名前など多義的である。
  - URL: https://www.merriam-webster.com/dictionary/deadeye
  - 出典日付: 記載なし
  - 確度: 高
- 事実: macOS向けに、ゲーム中のカーソル/クリック不具合を修正するユーティリティ「Deadeye」(GitHub: inulute/deadeye、10★、2026/9/14更新=アクティブ)が実在し、機能領域(メニューバー常駐のmacOSユーティリティ)が今回のアプリと近い。Windows向けの高速スクリーンショットツール「DeadEye」(SamusAranX/DeadEye)も別に存在する。
  - URL: https://github.com/inulute/deadeye
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 上記以外に `DEVILENMO/DeadEye-Auto-Aiming-System`(110★、ゲーム向け自動照準AI)、`strykeforce/deadeye`(6★、ロボット競技用ビジョンシステム)など、複数分野で使われている。
  - URL: https://github.com/DEVILENMO/DeadEye-Auto-Aiming-System
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `formulae.brew.sh/cask/deadeye` `/formula/deadeye` ともに404、未登録。
  - URL: https://formulae.brew.sh/cask/deadeye
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: MITRE ATT&CKに登録された実在のマルウェアファミリー名でもある(APT41が2021年以降使用する「DEADEYE」ローダー、正式ID: S1052)。セキュリティに詳しい開発者が検索すると混入する可能性がある。
  - URL: https://attack.mitre.org/software/S1052/
  - 出典日付: 記載なし
  - 確度: 中(検索スニペットで確認、直接ページは未fetch)
- 事実: Take-Two Interactive Software社が「DEAD EYE」を商標登録済みである(Red Dead Redemptionのゲームメカニクス名、登録番号4091120)。
  - URL: https://trademarks.justia.com/853/74/dead-eye-85374189.html
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `deadeye.com` はBrandBucket(ブランド名売買サイト)の「Deadeye」販売ページにリダイレクトする(直接アクセスは403で拒否されたが、リダイレクト先URLで確認)。`deadeye.dev` はHTTP 200で、実際にはモバイルゲーム(タップ式アクションゲーム)のティザーサイトが稼働中。`deadeye.app` はHTTP 404(ドメイン自体は応答するがページなし)。
  - URL: https://www.brandbucket.com/names/deadeye
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「Dead」という語頭が生産性ツールとしてはやや物騒・アグレッシブな印象を与えうる。マルウェア名との連想もマイナス要素になりうる。発音・綴りは平易。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Nockpoint

- 事実: アーチェリー用語(矢のノック=弦との接続部の位置)が語源に近いが、検索結果では実在のビジネス複数がヒットする——Mountlake Terrace(米ワシントン州)の実店舗アーチェリーショップ「The Nock Point」、データ分析SaaS「Nockpoint」(nockpoint.com)。
  - URL: https://thenockpoint.com/ , https://www.nockpoint.com/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: macOS専用アプリは見つからないが、Webベースの実在SaaS「Nockpoint」(nockpoint.com、Snowflakeベースのデータ分析プラットフォーム)と、別会社の「Nockpoint」(nockpoint.io、アーチェリークラブ管理ソフト)の2つの異なる商用ソフトウェア製品が同名で並立している。
  - URL: https://www.nockpoint.com/ , https://nockpoint.io/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `dapak/nockpoint`(0★、2013年)、`silah/nockpoint`(0★、2025/9/23更新)など小規模のみ。
  - URL: https://github.com/dapak/nockpoint
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `formulae.brew.sh/cask/nockpoint` `/formula/nockpoint` ともに404、未登録。
  - URL: https://formulae.brew.sh/cask/nockpoint
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: 上記データ分析SaaSが最も目立つ商用製品である。
  - URL: 上記に同じ
  - 出典日付: 記載なし
  - 確度: 高
- 事実: nockpoint.comの運営企業は資金調達済みとみられる本格的なB2B SaaS企業(統合、AIアシスタント等を謳う)である。
  - URL: https://www.nockpoint.com/
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `nockpoint.com` はHTTP 200で実際に稼働中のSaaS企業サイト(既存企業が保有)。`.app` `.dev` はDNS解決失敗。
  - URL: https://www.nockpoint.com/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「Nock」部分が「Knock」と同音のため聞き取り・綴りの取り違えリスクがある(詳細はNockの項参照)。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Callsign

- 事実: 「コールサイン(無線・航空・軍事の識別符号)」という非常に一般的な英単語で、Wikipediaに独立記事があるほど普及した語彙である。
  - URL: https://en.wikipedia.org/wiki/Call_sign
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 一般的な意味に加え、大手のID認証・不正検知ソフトウェア企業「Callsign」(callsign.com、英国拠点)が同名で存在し、App Store上にも企業向け認証アプリ「Callsign」を複数公開している。Gartner Peer Insights、Microsoft Azure Marketplaceにも製品掲載がある。
  - URL: https://www.callsign.com/ , https://apps.apple.com/us/developer/callsign-inc/id720208183
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `yaybu/callsign`(44★、ローカル開発用DNSサービス、2024/4更新で停滞)、`YuYanDev/callsign`(19★、無線局コールサイン検索ライブラリ)などがあるが、いずれも今回のアプリ用途とは無関係。
  - URL: https://github.com/yaybu/callsign
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `formulae.brew.sh/cask/callsign` `/formula/callsign` ともに404、未登録。
  - URL: https://formulae.brew.sh/cask/callsign
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: Callsign Inc.は認証/不正検知の分野で知名度のある企業(エンタープライズ向け)である。
  - URL: 上記に同じ
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Callsign Inc.(英国、Bloomberg企業プロフィールあり、金融機関を主要顧客とする)が明確に実在する。
  - URL: https://www.bloomberg.com/profile/company/1448599D:LN
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `callsign.com` はHTTP 200で、Callsign Inc.の公式企業サイトが稼働中。`.app` `.dev` はDNS解決失敗。
  - URL: https://www.callsign.com/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 一般語として非常に馴染み深く発音・綴りの問題は無いが、逆に「一般的すぎる語+実在の著名企業」の組み合わせで検索結果が埋まりやすい。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Nock

- 事実: 複数の意味が拮抗している——アーチェリー用語(矢の弦受け部)、銃工Henry Nock(18世紀の発明家、Wikipedia記事あり)、そしてNode.js向けHTTPモッキングライブラリ「nock」(npm)。「Knock」との同音異義語であるため、Grammarlyに専用の「Knock vs. Nock」解説記事があるほど混同が実例として起きている。
  - URL: https://www.grammarly.com/commonly-confused-words/knock-vs-nock , https://en.wikipedia.org/wiki/Henry_Nock
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 直接の完全一致Macアプリは無いが、非常に近い競合として「Knock」(tryknock.app)というMacアプリが実在する——「タップでMacを操作する」ショートカットアプリで、対象ユーザー層・利用シーンが今回のアプリと極めて近い。
  - URL: https://www.tryknock.app/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `nock/nock` が13,126スター、2026/9/20更新(最新)という、Node.jsエコシステムで非常に有名なHTTPモッキングライブラリである(npm週間ダウンロード数も多く、依存プロジェクト1,100件超)。さらに `nockchain/nockchain`(494★、2026/9/21更新=本日、$NOCKトークンのL1ブロックチェーンプロジェクト)も活発に動いている。開発者が「nock」でGitHub検索すると、これら2つの大型プロジェクトに実質的に埋もれる。
  - URL: https://github.com/nock/nock , https://www.npmjs.com/package/nock , https://github.com/nockchain/nockchain
  - 出典日付: 記載なし(GitHub API上の更新日は2026-09-20/2026-09-21)
  - 確度: 高(メインで直接確認: nock/nock が13,126★で活発)
- 事実: `formulae.brew.sh/cask/nock` `/formula/nock` ともに404、未登録。
  - URL: https://formulae.brew.sh/cask/nock
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: 上記npmライブラリ(nock)は開発者オーディエンスに広く知られたツールであり、今回のアプリの想定読者(英語圏の開発者)と完全に重複する。
  - URL: 上記に同じ
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 明確な単一企業商標は無いが、Urbitエコシステムにおける低レベル関数型言語「Nock」の名称でもある(nock.devがUrbitのホスティングサービスとして稼働している)。
  - URL: https://nock.dev/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `nock.dev` はHTTP 200で、実際にUrbitのshipホスティングサービス「urbit.sh」が稼働中(第三者運営)。`nock.com` は複数回試行(https/http、タイムアウト延長)したが接続確立できず、内容確認不可。`.app` はDNS解決失敗。
  - URL: https://nock.dev/
  - 出典日付: 記載なし
  - 確度: 高(.dev)/低(.com、未確認)
- 事実: 「Knock」との同音異義語で、耳で聞いた際に綴りを誤る可能性が非常に高い(Grammarlyが専用記事を書くほど実例のある混同)。さらにアーチェリー用語自体が一般の英語話者には馴染みが薄く、単語の意味を説明する必要がある。
  - URL: https://www.grammarly.com/commonly-confused-words/knock-vs-nock
  - 出典日付: 記載なし
  - 確度: 中

### Letterhop

- 事実: 「Letterhop」単独では、単語を1文字ずつ変化させて別の単語に到達するワードゲーム「LetterHop」(letterhop.io)、および読み書き練習用の「跳びながら文字を覚える」フォニックス教材が上位を占める。ベルギーの非営利団体「Vzw Letterhop」(障がい者支援)もヒットする。
  - URL: https://letterhop.io/ , https://kbs-frb.be/en/vzw-letterhop
  - 出典日付: 記載なし
  - 確度: 中(検索スニペットのみ、未取得)
- 事実: 「Letterhop mac app」「Letterhop software」で該当する Mac アプリ・開発者ツールは見つからない。上記ワードゲーム「LetterHop」が引き続き最上位。
  - URL: https://letterhop.io/
  - 出典日付: 記載なし
  - 確度: 中
- 事実: GitHub のリポジトリ検索では `theboffin/letterhop-privacy`(0★、2026-09-17更新)1件のみヒットする。さらに「letterhop」という名前の Organization(2026-08-12作成、blog=letterhop.eu、リポジトリ0件、説明欄は空)が存在する。
  - URL: https://github.com/letterhop
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `formulae.brew.sh/cask/letterhop` `/formula/letterhop` はいずれも HTTP 404(未登録)。
  - URL: https://formulae.brew.sh/cask/letterhop
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `registry.npmjs.org/letterhop` は HTTP 404(未登録)。
  - URL: https://registry.npmjs.org/letterhop
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: App Store 検索(`site:apps.apple.com "Letterhop"`)では完全一致するアプリは見つからない(LetterHUB、LetterBoom!等の類似名のみ)。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 「Letterhop」を名乗る著名企業・商標は見当たらない。上記の GitHub Organization(letterhop.eu)は新しく作成されたばかりで、実体・事業内容は確認できない。
  - URL: https://github.com/letterhop
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `letterhop.com` は A レコードあり(3つのIP)。DNS のみの確認で、内容は未取得。`letterhop.app` `letterhop.dev` は A レコードなし。
  - URL: なし(DNS照会のみ、`dig +short letterhop.com`)
  - 出典日付: 記載なし
  - 確度: 高(メインで直接 DNS を確認、内容は未取得)
- 事実: 造語として意味は直感的(文字の間を跳ぶ)だが、既存のワードゲーム「LetterHop」と概念が近い(文字を1つずつ変えて単語を作るゲーム)ため、思わぬ意味的な重なりがある。郵便業界用語「lettershop」(ダイレクトメール発送代行)と発音がやや近く、聞き間違いの余地がわずかにある。ネガティブな意味は確認されず。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Typick

- 事実: 「Typick」はパリの実店舗カフェ「Typick Café」(Instagram/Facebook/Yelp掲載、運営中)、およびネット通販サイト「Typick Store」(typick.com)が上位を占める。
  - URL: https://www.yelp.com/biz/typick-caf%C3%A9-paris , https://typick.com/
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 「Typick mac app」では完全一致するアプリは見つからず、綴りの近い「Typist」(タイピング練習)、「Cotypist」(AI自動補完)、「Typix」(文章校正)が上位に出る。
  - URL: https://apps.apple.com/us/app/typist/id415166115 , https://cotypist.app/
  - 出典日付: 記載なし
  - 確度: 中
- 事実: GitHub のリポジトリ検索は5件ヒットするが完全一致はなく、いずれも無関係(`therladbsgh/typicka`、トイレ判定アプリ「PotTYpicker」の複数フォーク、`Typickal/Typickal.github.io`)。同名ユーザー「Typick」は2017年作成、リポジトリ0件で休眠している。
  - URL: https://github.com/search?q=Typick&type=repositories
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `formulae.brew.sh/cask/typick` `/formula/typick` はいずれも HTTP 404(未登録)。
  - URL: https://formulae.brew.sh/cask/typick
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `registry.npmjs.org/typick` は HTTP 404(未登録)。
  - URL: https://registry.npmjs.org/typick
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: App Store 検索(`site:apps.apple.com "Typick"`)では完全一致は見つからず、「Typic」「Typik」「Typicon」等の近縁名アプリのみヒットする。
  - URL: https://apps.apple.com/us/app/typic-text-on-photos/id601467470
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 「Typick」を名乗る著名企業・商標は見当たらないが、Typick Café/Store という小規模ながら実在するブランドがある。
  - URL: https://typick.com/
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `typick.com` は A レコードあり(Cloudflare経由とみられる)。DNS のみの確認で内容は未取得(上記検索でTypick Storeが稼働中と推測されるのみ)。`typick.app` `typick.dev` は A レコードなし。
  - URL: なし(DNS照会のみ、`dig +short typick.com`)
  - 出典日付: 記載なし
  - 確度: 高(DNSのみ確認)/中(内容は検索スニペット由来で未取得)
- 事実: 発音が "typic"(Merriam-Websterに項目あり、"typical" の文語形)とほぼ同一で、耳で聞いた際に "Typic" や "typical" と誤解・誤記される可能性がある。App Store の「Typic」アプリと発音上ほぼ区別がつかない点はリスク。
  - URL: https://www.merriam-webster.com/dictionary/typic
  - 出典日付: 記載なし
  - 確度: 中

### Keyward

- 事実: 「Keyward」で検索すると、ベルリン拠点の資金調達済み B2B SaaS 企業「Key Ward」(2021年創業、エンジニアリングデータ×AI基盤、CAEフォーマットを解析するプラットフォーム)が支配的にヒットする。Crunchbase・Dealroom・Caplight 等の企業データベースにプロフィールがある。
  - URL: https://www.keyward.io/ , https://www.crunchbase.com/organization/keyward , https://app.dealroom.co/companies/keyward
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「Keyward mac app」では、SSH エージェント兼 SwiftUI アプリ「keyward」(GitHub: SolAstrius/keyward、macOS 14+/Apple Silicon対応、Secure Enclave 利用、DMG配布・非公証)がヒットする。macOS 向けの実在するオープンソースアプリという点で、今回の対象と開発者層が重なる。
  - URL: https://github.com/SolAstrius/keyward
  - 出典日付: 記載なし
  - 確度: 高
- 事実: GitHub リポジトリ検索は75件ヒットし、最多は `gateway-of-last-resort/keyward`(48★、SSH鍵管理TUI、2026-08-20更新=アクティブ)。同名の完全一致リポジトリ("keyward"という名前)は18件確認でき、SSH/シークレット管理系のツールが多い(`arturayupov/keyward`, `klarlabs-studio/keyward`, `SolAstrius/keyward` 等、いずれも2026年に活発更新)。同名ユーザー「keyward」(2014年作成、休眠、リポジトリ3件)も存在する。
  - URL: https://github.com/gateway-of-last-resort/keyward
  - 出典日付: 記載なし(更新日はAPIレスポンスの pushed_at)
  - 確度: 高(メインで直接確認)
- 事実: `formulae.brew.sh/cask/keyward` `/formula/keyward` はいずれも HTTP 404(未登録)。
  - URL: https://formulae.brew.sh/cask/keyward
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `registry.npmjs.org/keyward` は HTTP 404(未登録)。
  - URL: https://registry.npmjs.org/keyward
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: App Store 検索(`site:apps.apple.com "Keyward"`)では完全一致するアプリは見つからない。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: Key Ward(keyward.io)は資金調達済みの実在企業であり、自動車・航空宇宙業界向けにエンジニアリングデータ基盤を提供している。
  - URL: https://www.keyward.io/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: `keyward.com` `keyward.app` `keyward.dev` はいずれも A レコードあり(DNSのみの確認で内容は未取得。`.io` が Key Ward 社の公式ドメインであることは検索結果から確認済み)。
  - URL: なし(DNS照会のみ、`dig +short keyward.com/.app/.dev`)
  - 出典日付: 記載なし
  - 確度: 高(DNSのみ確認)
- 事実: 一般語「keyword」とスペルが1文字違い・発音もほぼ同一で、聞き間違い・タイプミスのリスクが非常に高い(オーナー自身が却下理由として明示的に挙げている組み合わせ)。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 中

### Hintjump

- 事実: 「Hintjump」単独でのヒットはほぼなく、支配的な既存語・企業・製品は見当たらない。断片的に Second Life Wiki の UI 通知システムで「HintJump」という内部名(ジャンプ操作時のヒント表示のオンオフ設定)が使われている程度。
  - URL: https://wiki.secondlife.com/wiki/Adding_UI_Hints
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 「Hintjump mac app」「Hintjump software」で該当する製品は発見できない。検索結果は無関係な「Hint」系アプリ(占星術アプリ、HINTファイルビューア等)に分散する。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: GitHub のリポジトリ検索は0件。同名ユーザー/組織も存在しない(`gh api users/hintjump` は404)。
  - URL: https://github.com/search?q=Hintjump&type=repositories
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `formulae.brew.sh/cask/hintjump` `/formula/hintjump` はいずれも HTTP 404(未登録)。
  - URL: https://formulae.brew.sh/cask/hintjump
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `registry.npmjs.org/hintjump` は HTTP 404(未登録)。
  - URL: https://registry.npmjs.org/hintjump
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: App Store 検索(`site:apps.apple.com "Hintjump"`)では完全一致するアプリは見つからない。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 「Hintjump」を名乗る著名企業・商標は見当たらない。
  - URL: なし
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `hintjump.com` `hintjump.app` `hintjump.dev` はいずれも A レコードなし。
  - URL: なし(DNS照会のみ、`dig +short hintjump.com/.app/.dev`)
  - 出典日付: 記載なし
  - 確度: 高(メインで直接 DNS を確認)
- 事実: 造語として意味は直感的(ヒントが出てジャンプする)。同音異義語・誤記リスクは低い。ネガティブな意味は確認されず。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Keyhop

- 事実: 「Keyhop」で最も目立つのは、今回のアプリと機能説明がほぼ一致するオープンソースの Rust プロジェクト「keyhop」(GitHub: `rsaz/keyhop`)である。README には「Drive your entire desktop from the keyboard. Press a leader chord, see hint labels on every clickable thing on screen, type the hint, done.」とあり、リーダーキー押下→クリック可能要素にヒントラベル表示→ヒント入力で操作、という今回のアプリと同一のコンセプトを謳っている。crates.io・docs.rs で配信され、MSI インストーラで Windows 版が配布されており、README には将来的な Linux/macOS バックエンド追加の言及もある。
  - URL: https://github.com/rsaz/keyhop , https://docs.rs/keyhop/latest/keyhop/ , https://crates.io/crates/keyhop
  - 出典日付: 記載なし(pushed_at 2026-06-22、README記載バージョン v0.4.0)
  - 確度: 高(メインで直接 README とリポジトリ情報を確認)
- 事実: 「Keyhop mac app」で検索すると、Claude Code/Cursor/Codex のアカウント切替ツール「Keyhop」(macOS メニューバーアプリ、GitHub: `dominikzabcik/keyhop`)がヒットする。今回のアプリと同じ開発者オーディエンス(AIコーディングツールを使うエンジニア)向けの macOS アプリという点で重なりがある。
  - URL: https://github.com/dominikzabcik/keyhop
  - 出典日付: 記載なし(pushed_at 2026-09-21=本日)
  - 確度: 高
- 事実: GitHub リポジトリ検索は10件ヒットし、完全一致名("keyhop"/"KeyHop")のみでも8件ある。macOS 向けアプリランチャー「KeyHop」(`kuniyoshi/KeyHop`, Swift, 1★)、ブラウザ拡張「KeyHop」(`JdonAi/KeyHop`, 1★, 2026-09-11更新)、上記アカウント切替ツール、上記 Rust ライブラリなど、少なくとも4つの独立した"Keyhop"プロジェクトが並立している。
  - URL: https://github.com/kuniyoshi/KeyHop , https://github.com/JdonAi/KeyHop
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `formulae.brew.sh/cask/keyhop` `/formula/keyhop` はいずれも HTTP 404(未登録)。
  - URL: https://formulae.brew.sh/cask/keyhop
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `registry.npmjs.org/keyhop` は HTTP 404(未登録)。
  - URL: https://registry.npmjs.org/keyhop
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: App Store 検索(`site:apps.apple.com "Keyhop"`)では完全一致は見つからず、無関係の「KeyHop VPN – Fast & Secure」(iOS、VPNアプリ)がヒットする。
  - URL: https://apps.apple.com/us/app/keyhop-vpn-fast-secure/id6761395171
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 単一の著名企業・商標としての「Keyhop」は見当たらないが、Google Play 上に Android アプリ「KeyHop - App cloner & VPN」(開発元 grape.products.keyhop)が実在する。
  - URL: https://play.google.com/store/apps/details?id=grape.products.keyhop
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `keyhop.com` `keyhop.app` は A レコードあり(DNSのみの確認、内容未取得)。`keyhop.dev` は A レコードなし。
  - URL: なし(DNS照会のみ、`dig +short keyhop.com/.app/.dev`)
  - 出典日付: 記載なし
  - 確度: 高(DNSのみ確認)
- 事実: 発音・綴りは平易で誤記リスクは低い。ただし前項の通り、名前の衝突以前に「押すとヒントラベルが出て入力すると操作できる」という製品コンセプト自体がオープンソースの `rsaz/keyhop` と実質的に重複しており、8候補の中で最も深刻な衝突である。
  - URL: https://github.com/rsaz/keyhop
  - 出典日付: 記載なし
  - 確度: 高

### Hintkey

- 事実: 「Hintkey」は一般的な独立製品・企業としてはヒットせず、Apple の開発者向けドキュメントにある API 定数 `NSImageRep.HintKey`(画像描画時のヒント辞書キー)、Go言語の nostr SDK における型 `HintKey` など、技術文書内の識別子として散発的にヒットする。
  - URL: https://developer.apple.com/documentation/appkit/nsimagerep/hintkey , https://pkg.go.dev/github.com/nbd-wtf/go-nostr/sdk/hints
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「Hintkey mac app」「Hintkey software」いずれでも該当する製品・企業は見つからない。検索結果は無関係な「Hint」「Hotkey」系アプリ(HintView、HotKeys、HotKey、AutoHotkey等)に分散する。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: GitHub のリポジトリ検索は0件。同名ユーザー/組織も存在しない(`gh api users/hintkey` は404)。
  - URL: https://github.com/search?q=Hintkey&type=repositories
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `formulae.brew.sh/cask/hintkey` `/formula/hintkey` はいずれも HTTP 404(未登録)。
  - URL: https://formulae.brew.sh/cask/hintkey
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `registry.npmjs.org/hintkey` は HTTP 404(未登録)。
  - URL: https://registry.npmjs.org/hintkey
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: App Store 検索(`site:apps.apple.com "Hintkey"`)では完全一致するアプリは見つからない。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 「Hintkey」を名乗る著名企業・商標は見当たらない。
  - URL: なし
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `hintkey.com` `hintkey.app` `hintkey.dev` はいずれも A レコードなし。
  - URL: なし(DNS照会のみ、`dig +short hintkey.com/.app/.dev`)
  - 出典日付: 記載なし
  - 確度: 高(メインで直接 DNS を確認)
- 事実: 「hint key(ヒントキー)」自体は Vimium 等のキーボード操作型リンクヒント系ツールで一般的に使われてきた用語であり(GitHub上の `mousemaster` のIssueでも "hint keys" という一般名詞的表現が使われている)、固有名詞としての独自性がやや薄い可能性がある。発音・綴りに問題はなく、ネガティブな意味も確認されない。
  - URL: https://github.com/petoncle/mousemaster/issues/104
  - 出典日付: 記載なし
  - 確度: 低〜中

### Letterjump

- 事実: 「Letterjump」で最も目立つのは、個人開発者 Pugsly191 による itch.io 配信のタイピングゲーム「LetterJump」(素早く文字を打ち続けて生き残るブラウザゲーム、小規模)である。
  - URL: https://pugsly191.itch.io/letterjump
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「Letterjump mac app」「Letterjump software」では該当する Mac アプリ・開発者ツールは見つからない。検索結果は無関係な文字関連アプリ(Letterpress、Letterly、Letter Opener Pro等)に分散する。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: GitHub のリポジトリ検索は `lgauthier1/letterjump`(0★、2020-04-19が最終更新で以降停滞)1件のみ。同名ユーザー/組織は存在しない(404)。
  - URL: https://github.com/lgauthier1/letterjump
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `formulae.brew.sh/cask/letterjump` `/formula/letterjump` はいずれも HTTP 404(未登録)。
  - URL: https://formulae.brew.sh/cask/letterjump
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `registry.npmjs.org/letterjump` は HTTP 404(未登録)。
  - URL: https://registry.npmjs.org/letterjump
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: App Store 検索(`site:apps.apple.com "Letterjump"`)では完全一致するアプリは見つからない。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: 「Letterjump」を名乗る著名企業・商標は見当たらない。
  - URL: なし
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `letterjump.com` は A レコードあり、IP アドレスが `keyhop.com` と完全に一致する(13.223.25.84 / 54.243.117.197)。同一のドメイン販売・駐車サービスにホストされている可能性が高いが、DNSのみの確認で内容は未取得。`letterjump.app` `letterjump.dev` は A レコードなし。
  - URL: なし(DNS照会のみ、`dig +short letterjump.com/.app/.dev`)
  - 出典日付: 記載なし
  - 確度: 高(DNSのみ確認)/低(同一ホスティングという解釈は推測)
- 事実: 造語として意味は直感的(文字がジャンプする)。同音異義語・誤記リスクは低い。ネガティブな意味は確認されず。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

### Typoint

- 事実: 「Typoint」で最も目立つのは、ベルリン拠点のタイポグラフィ・デザイン事務所「typoint」(創業者 Patrick Marc Sommer、typoint.com で稼働中、LinkedIn・Instagram・Facebook・SoundCloud・YouTubeにも展開)である。
  - URL: https://www.typoint.com/en , https://www.linkedin.com/company/typoint
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 「Typoint mac app」では該当する製品は見つからず、綴りの近い「Timepoint」(勤怠管理)、「Typist」(タイピング練習)、「TypiMage」(タイポグラフィエディタ)等が上位に出る。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: GitHub のリポジトリ検索は2件ヒットするが完全一致はなく、いずれも無関係(`smwhr/Typointnclick`、2012年で停止、`p2ppsr/typoints-frontend`)。同名ユーザー/組織は存在しない(404)。
  - URL: https://github.com/search?q=Typoint&type=repositories
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `formulae.brew.sh/cask/typoint` `/formula/typoint` はいずれも HTTP 404(未登録)。
  - URL: https://formulae.brew.sh/cask/typoint
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: `registry.npmjs.org/typoint` は HTTP 404(未登録)。
  - URL: https://registry.npmjs.org/typoint
  - 出典日付: 記載なし
  - 確度: 高(メインで直接確認)
- 事実: App Store 検索(`site:apps.apple.com "Typoint"`)では完全一致するアプリは見つからない。
  - URL: 検索結果ベース(個別URLなし)
  - 出典日付: 記載なし
  - 確度: 中
- 事実: typoint(Patrick Marc Sommer 氏のデザイン事務所)は小規模ながら実在し稼働中のブランドである。USPTOなど公式商標データベースでの正式登録有無までは確認していない。
  - URL: https://www.typoint.com/en
  - 出典日付: 記載なし
  - 確度: 中
- 事実: `typoint.com` は A レコードあり(DNSのみの確認。上記検索結果から typoint 社のサイトである可能性が高いが未取得)。`typoint.app` `typoint.dev` は A レコードなし。
  - URL: なし(DNS照会のみ、`dig +short typoint.com/.app/.dev`)
  - 出典日付: 記載なし
  - 確度: 高(DNSのみ確認)/中(内容は検索スニペット由来で未取得)
- 事実: 「Typoint」は "typo"(誤字・打ち間違い)+ "point" の組み合わせに読めてしまい、キーボード操作アプリとしてはやや皮肉な・ネガティブな連想(誤入力)を招く可能性がある。発音・綴り自体に混乱のリスクは低い。
  - URL: なし(言語的推測)
  - 出典日付: 記載なし
  - 確度: 低

## グレーゾーン・未確認

- **reticle.app**: 複数回(WebFetch、curl経由の異なるプロトコル・タイムアウト設定)試行したが、接続確立できず(タイムアウト/ECONNREFUSED)。ライブサイトかどうか確認不能。
- **nock.com**: DNS自体は解決する(IPアドレスが返る)が、http/https両方で接続タイムアウトし、内容を確認できなかった。ファイアウォールによる自動アクセスのブロックの可能性もあり、確度は低い。
- **Product Hunt個別チェック**: 時間の制約上、12名称それぞれについてProduct Hunt上の直接検索は実施していない。App Store/GitHub/Google検索で得られた情報を優先した。
- **npmレジストリの網羅チェック**: 「Nock」については直接npmjs.comを確認したが、他11名称についてはnpmパッケージ名としての衝突は個別にnpm検索していない(Google検索・GitHub検索の結果に付随して見つかったもののみ報告)。
- **VS Code拡張機能マーケットプレイスの網羅チェック**: 「Reticle」についてOpen VSX上の拡張機能(roboalchemist/reticle)がヒットしたことは確認したが、他11名称については個別にVS Code Marketplaceを検索していない。
- **米国商標庁(USPTO)などの公式商標データベースへの直接照会**: 実施していない。Justia Trademarksなど第三者データベースの検索スニペットに基づく情報のみ(Deadeye/DEAD EYE、Reticle Labs LLCなど)。
- **clavigate.com / pressto.com の詳細な事業実態**: サイトのタイトル・トップページの表面的な内容は確認したが、実際の事業規模(トラフィック量、検索順位での強さ)までは測定していない。
- **GitHub検索結果の総件数**: 一部(Pressto=93件など)は総件数が判明したが、他の名称についてはper_page制限(上位8〜9件)内での確認にとどまり、全体件数は不明。

### 第 2 弾で追加で未確認・グレーゾーンになった点

- **候補ドメイン(letterhop.com / typick.com / keyward.com/.app/.dev / keyhop.com/.app / letterjump.com / typoint.com)の内容**: 安全確認手順(safe-fetching.md)に従い、A レコードの有無のみを `dig +short` で確認した。curl や WebFetch、ブラウザでの中身の確認は一切行っていない。稼働中サイトか、駐車・販売中ページか、未構築のデフォルトページかは不明であり、検索結果のスニペットから推測できる範囲(typick.com=Typick Store、keyward.io公式=Key Ward社、typoint.com=typoint社)を除き、確度は「DNSのみ確認・内容未取得」にとどまる。
- **letterjump.com と keyhop.com が同一IP(13.223.25.84 / 54.243.117.197)で応答した点**: 同一のドメイン販売・駐車サービスに乗っているのではという推測に留まり、確認していない。
- **`.eu`・`.io`・`.tech`・`.ai` など、指定の3TLD(.com/.app/.dev)以外のドメイン**: letterhop.eu(GitHub Organizationのblogリンク)、keyward.io(Key Ward社)、keyhop.tech(モバイルアプリ)など、検索で見つかった他TLDのドメインは存在を把握したのみで、DNS照会・内容確認とも行っていない。
- **USPTO等の公式商標データベースへの直接照会**: 実施していない。Keyward(Key Ward社、資金調達済み)、Typoint(typoint社)について、正式な商標登録の有無までは確認できていない。
- **rsaz/keyhop の実際の macOS 対応状況**: README は「Linux backend planned」「macOS backendsも将来追加予定」と書いているのみで、現時点で実際にmacOSで動作するかどうかは未検証(コード自体は読んでいない)。
- **Product Hunt個別チェック**: 第2弾でも8名称それぞれのProduct Hunt検索は実施していない。
- **npm・Homebrewの結果は全件404**だが、パッケージ名のスコープ付き(`@scope/keyhop`等)やHomebrewのtapリポジトリ(brew未公式化のtap)までは確認していない。

## 影響する論点

open-questions.md の「アプリ名」に効く
