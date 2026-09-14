# 個人開発者が英語学習アプリのユーザーを獲得する現実的な流入経路

- 調査日: 2026-09-14
- 調査手段: メインセッションによる WebSearch / WebFetch 実施（デスクリサーチのみ、サブエージェント委譲なし）
- 問い: 個人開発者が英語学習アプリのユーザーを獲得するとき、現実的に機能する流入経路はどれか。SEO は本当に無理か。グローバル市場と日本市場で何が違うか。

## 結論

SEO（コンテンツ SEO によるオーガニック検索流入）は「完全に無理」ではないが、2024〜2026 年にかけて期待値が構造的に下がっており、新規個人が今からゼロベースで勝負するには分が悪い。ビッグキーワード（"learn english" "english grammar" 等）は政府機関・大手メディア・大手 EdTech（British Council, VOA, EF, Grammarly, Duolingo, Cambridge 等）と、10 年単位でコンテンツを積んできた中堅特化サイト（IELTS Liz, Espresso English, 7ESL 等）でほぼ占有されている。ロングテール（"how to say X in english" 系、特定の文法点）には個人・小規模サイトが入り込む余地が実際の SERP で確認できたが、そこですら YouTube 動画が並び立ち、かつ AI Overviews / AI Mode によってクリックそのものが構造的に減っている（後述）。SEO 以外では、Reddit（サブ全体で確認できたのは数十万〜300 万人規模のコミュニティ）、TikTok/YouTube Shorts（個人が数百万フォロワーに到達した実例が複数）、ASO ロングテールキーワード、日本ではエンジニア界隈のバズ（Qiita/Twitter/はてブ）が、実例つきで確認できた現実的な経路である。

## SERP 実測

### グローバル（英語圏、Google 検索、2026-09-14 実施）

| クエリ | 上位に出たドメイン（種別） |
|---|---|
| "learn english" | Wikipedia、Duolingo（公式）、usa.gov（米政府）、Google Play アプリ一覧、VOA Learning English（米国政府系メディア）、British Council、YouTube チャンネル、EnglishClass101（中堅企業）、USA Learns（非営利）、YouTube チャンネル |
| "english grammar" | British Council、Wikipedia、EnglishClub（老舗中堅サイト）、EnglishGrammar.org（老舗個人〜小規模サイト）、Grammarly（大手 SaaS）、EF（大手語学スクール）×2 |
| "ielts writing task 2" | Magoosh（中堅 EdTech）、IELTS Advantage（個人発の中堅ブランド）、IELTSPodcast（個人発）、IELTS Liz（個人教師発ブランド）、ielts.org（IELTS 公式）、Western Overseas（予備校）、engnovate（UGC型サービス） |
| "english speaking practice app" | App Store/Google Play の直接掲載、EnglishSpeaking.app（プロダクト自体）、PracticeMe.app のまとめ記事 |
| "improve english vocabulary" | Medium個人記事、Oxford Learning（中小企業）、British Council、Vocabulary.com（プロダクト）、大学ブログ複数、LanGeek（プロダクト）、非営利団体、Goodreads |
| "how to say excited in english"（ロングテール例） | Facebook投稿、YouTube動画×2、AwalEnglish.com（小規模個人サイト）、Thesaurus.com、Cambridge Dictionary、SydneyEnglishTeacher.com.au（個人教師サイト）、Merriam-Webster、Substack記事 |
| "present perfect vs past simple explained"（文法ロングテール） | FluentU、EF、Cambridge、Espresso English（小〜中規模個人発サイト）、Wikipedia、Test-English×2、Britannica、7ESL（小〜中規模サイト） |

**読み取れる傾向**: ビッグキーワードほど政府機関・大手メディア・大手 SaaS が占有し、個人が新規参入できる隙はほぼない。ロングテール（"how to say X" 系、個別の文法点）では、10 年前後の運営実績を持つ個人〜小規模サイト（AwalEnglish, Sydney English Teacher, Espresso English, 7ESL, IELTS Liz 等）が今も上位を維持しているのが確認できたが、これは「今日から始めた新規個人サイト」がすぐ入れる隙ではなく、「長年ロングテールを積み上げた小規模プレイヤーが生き残っている」状態。加えて YouTube 動画がテキスト記事と並んで上位に出るため、記事だけでなく動画も競合になる。

### 日本市場（Google 検索、日本語クエリ、2026-09-14 実施）

| クエリ | 上位に出たドメイン（種別） |
|---|---|
| "英語 学習 アプリ おすすめ" | eikaiwa.weblio.jp（メディア）、my-best.com（比較メディア）、migaku.com（プロダクト系ブログ）、walkerplus.com（大手メディア）、notta.ai（プロダクト系ブログ）、app-liv.jp（アプリ比較メディア） |
| "英語 勉強法" | eigosapuri.jp（スタディサプリENGLISH、リクルート系）、bizmates.jp（オンライン英会話事業者）、note.com個人記事、アメブロ塾探し（メディア） |
| "英会話 独学 ブログ note" | note.com個人記事複数、アメブロ、英語ブログ村（個人ブログランキングサイト）、個人ブログ多数、QQEnglish（オンライン英会話事業者のブログ） |
| "TOEIC 勉強法 個人ブログ" | eigosapuri.jp、TAC（予備校）、忍者英会話（メディア）、note.com個人記事（TOEIC満点体験記）、英語ブログ村 |

**読み取れる傾向**: 日本語 SERP は「比較メディア（app-liv, my-best 等）」「大手オンライン英会話事業者のオウンドメディア（スタディサプリENGLISH, bizmates, QQEnglish）」がビッグキーワードを占有する点はグローバルと同じ構図だが、note.com 個人記事や個人ブログが比較的上位に食い込みやすい（特に体験記・学習法の一次情報系）。これは Google がnoteドメインの権威性をある程度評価している可能性と、個人の実体験コンテンツが「学習法」「独学」系の意図に合っている可能性の両方が考えられる（未検証）。

## 経路別の評価表

| 経路 | 個人にとっての現実性 | 必要な継続労力 | 根拠 URL | 確度 |
|---|---|---|---|---|
| コンテンツ SEO（ビッグキーワード） | 低 | 極めて高い（数年単位） | 上記 SERP 実測 | 高 |
| コンテンツ SEO（ロングテール："how to say X"、個別文法点） | 中〜低 | 高（継続的な記事量産、数年） | 上記 SERP 実測 | 高 |
| Reddit（r/EnglishLearning 等での自然な言及・投稿） | 中 | 中（コミュニティ活動の継続、宣伝色を抑える必要） | r/EnglishLearning 約70.7万〜72万人 [reddapi](https://reddapi.dev/subreddits/englishlearning/insights) / [gummysearch](https://gummysearch.com/r/EnglishLearning/)、r/languagelearning 約340万人 [reddapi](https://reddapi.dev/subreddits/languagelearning/insights)、r/Anki 約20.5万人 [reddapi](https://reddapi.dev/subreddits/anki/insights)、r/IELTS 約13万人〜80万人超（出典間で食い違い、後述グレーゾーン） | 中（サブ固有の自己宣伝ルールは未確認） |
| Reddit（r/SideProject 等での「作った話」投稿） | 中 | 低〜中（単発の投稿で数千リーチの実例あり） | [Reddit Growth Strategy for Indie Hackers](https://www.redditmaster.com/reddit-growth-for/indie-hackers) | 中 |
| TikTok / YouTube Shorts（コンテンツ主導の個人ブランド構築） | 中 | 極めて高い（数年かけて動画を量産し続ける必要） | Antonio Parlati 580万、Speak English with Zach 500万、Englishwithgeet 640万、English with Lucy 170万（TikTok）、Claudine James 440万フォロワー／2460万いいね [Promova まとめ記事](https://promova.com/blog/top-tik-tok-and-instagram-accounts-to-learn-english) | 中（個々の一次データではなくまとめ記事経由） |
| TikTok（企業規模のバイラル運用、参考値） | 低（個人には再現困難） | Duolingo規模の専属チームが必要 | Duolingo TikTok 1600万+フォロワー、ハッシュタグ施策CTR 39% [Case Studied](https://newsletter.casestudied.com/p/vol-44-duolingo-tiktoks-favorite-mascot) / [Influencers Time](https://www.influencers-time.com/duolingo-tiktok-owl-how-zero-paid-media-won-app-growth/) | 中 |
| ASO（ロングテールキーワードでの App Store/Google Play 上位表示） | 中 | 中（初月に10〜15個のロングテール語で上位を狙う戦術が定石） | 市場全体：2025年ダウンロード3.27億件、売上15.4億ドル（前年比+18.8%）、Duolingo単独売上10.3億ドル [Business of Apps 言語学習市場データ](https://www.businessofapps.com/data/language-learning-app-market/)（検索エンジンの要約経由での確認、直接フェッチは403で失敗） | 中（一次ページを直接確認できず） |
| Product Hunt ローンチ | 低〜中（単発の可視化スパイクのみ、持続的流入にはならない） | 低（単発イベント） | 一般に「登録増加を実感」50%、「大幅増加」30%、「変化なし」16% [shno.co統計](https://www.shno.co/marketing-statistics/product-hunt-launch-statistics)。語学学習アプリ特有の直接コンバージョンは低いとする言及あり | 中（語学カテゴリ特化の一次データではなく一般ローンチ統計の援用） |
| 既存コミュニティへの相乗り（Discord語学交換サーバー、italki コミュニティ） | 低〜中 | 中 | Discord上に50言語以上対応の語学交換サーバーが存在する旨の言及あり [italki フォーラム](https://www.italki.com/en/post/discussion-165188) | 低（規模・宣伝可否の具体データなし） |
| 日本：エンジニア界隈でのバズ（Qiita/Twitter/はてなブックマーク） | 中（エンジニア向けプロダクトに限れば高い） | 低〜中（単発のバズだが技術記事の継続執筆が前提） | 実例：Qiita「1000 LGTM」、はてブ「1543」、Twitterフォロワー20→720人、サービスアクセス「2.2万UU/12万PV」、事前登録800名、3週間で有料機能から売上発生 [Zenn記事](https://zenn.dev/yuno_miyako/articles/01eaad61140567) | 高（一次記事を直接確認） |
| 日本：note.com での学習体験記コンテンツ | 中 | 中（継続的な体験記投稿） | 「英会話 独学」「TOEIC 勉強法」等のSERPでnote個人記事が複数上位表示（上記SERP実測） | 中 |
| 多言語展開（中国語・韓国語・スペイン語などへのAI翻訳展開） | 中（市場規模は大きいが検証コスト・言語別チャネル習熟コストも大きい） | 高（言語ごとに異なるSNS・検索エコシステムへの適応が必要） | 中国：英語学習者3〜4億人規模、Xiaohongshu上「英語学習」関連投稿500万件超 [36kr](https://36kr.com/p/3646141794193029) / [知乎まとめ](https://zhuanlan.zhihu.com/p/507226209)。韓国：韓国発の英語学習アプリ「말해보카（Malhae Voca）」が韓国・日本・スペイン語圏で展開し全世界累計1000万DL突破、台湾進出後6ヶ月で教育カテゴリ1位 [Sensor Tower](https://sensortower.com/ko/blog/revenue-of-the-korean-market-education-app-and-MalhaeVoca-reached-all-time-highs) / [Unicornfactory](https://www.unicornfactory.co.kr/article/2025123109451596216) | 中 |

## AI 検索による前提の変化

SEO 戦略の前提そのものを揺るがすデータが複数確認できた。

- Google 検索全体で、クリックにつながらない検索（zero-click）の割合が 2026年1〜4月時点で **68.01%**（2024年の60.45%から上昇、2016年時点の約45%から10年で+23ポイント）。データはSimilarweb集計。[SparkToro（2026-06-09公開）](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/) — 確度：高（サブエージェントに加え、メインセッションでも 2026-09-14 に一次記事を直接確認。原文: "In the first four months of 2026, a whopping 68.01% of Google searches ended without a click" / "In 2024, US zero click searches on Google stood at 60.45%"。**データ元は Similarweb の US パネル（2026年1〜4月、デスクトップ+モバイル）であり、US 限定である点に注意**）
- AI Overviews が表示されるクエリでは、オーガニックCTRが**約58〜61%低下**（Ahrefs／Seer Interactiveの分析、5.47万クエリ規模）。日本語圏でもAhrefsの調査で「1位ページのCTRが日本で約38%、グローバルで約58%低下」という報告がある。[ALM Corp](https://almcorp.com/blog/google-ai-overviews-organic-ctr-2026/) / [SEJ](https://www.searchenginejournal.com/impact-of-ai-overviews-how-publishers-need-to-adapt/556843/) — 確度：中（検索エンジン要約経由、複数ソースで数値が一部food違うため）
- 大手パブリッシャーでは2025年6月〜2026年6月のYoYで、USA Today -50%、CNN -25%、Business Insider -85%超という報告（WSJ報道、Semrushデータ）。[SEJ経由](https://www.searchenginejournal.com/impact-of-ai-overviews-how-publishers-need-to-adapt/556843/) — 確度：中（孫引き）
- Google AI Mode は93%のクエリでクリックゼロ（Seer Interactive、2510万インプレッション分析）。[SEJ関連まとめ](https://searchengineland.com/google-zero-click-searches-2026-study-479717) — 確度：中
- 日本国内でもマーケター33.9%が「AI検索導入後の自然検索流入減少」を実感（PRIZMA調査、2026年）。[PR TIMES](https://prtimes.jp/main/html/rd/p/000000155.000149156.000149156.html) — 確度：中
- 一方で、AI Overview表示クエリにおけるオーガニックCTRは2025年12月の1.3%から2026年2月には2.4%へやや回復したとの報告もあり、下落が単調ではない可能性がある。[ALM Corp](https://almcorp.com/blog/google-ai-overviews-organic-ctr-2026/) — 確度：低（単一ソースのみ、回復トレンドの継続性は未確認）

**含意**: 「上位表示されればトラフィックが来る」という従来のSEOの前提が壊れつつある。教育・ハウツー系コンテンツ（英語学習の「〜のやり方」「文法の違い」系）は、AI Overviewsが最も直接的に答えを出しやすいカテゴリの一つであり、個人が検索順位を取れたとしても、クリックが取れない構造的リスクが年々高まっている。

## グローバル vs 日本

- **市場占有構造は同型**：どちらの言語圏でも、ビッグキーワードは大手メディア・大手事業者のオウンドメディアが占有する。グローバルでは政府機関系（VOA, British Council）や大手SaaS（Grammarly, Duolingo）、日本ではリクルート系（スタディサプリENGLISH）やオンライン英会話事業者（bizmates, QQEnglish）が強い。
- **個人コンテンツの入り込みやすさに差**：日本語SERPでは note.com 個人記事や個人ブログが、学習体験記・独学法・TOEIC体験記といったクエリで比較的上位に出やすい傾向が実測で確認できた。英語圏でも個人〜小規模サイトはロングテールで生き残っているが、それは長年の蓄積の結果であり、今日から始めて短期間で入り込める隙としてはグローバルの方が狭いと見られる（ただし両市場とも定量比較データは見つからず、SERP実測からの推測にとどまる）。
- **エンジニア発コミュニティ経由のバズは日本で実例が濃い**：Qiita/Zenn/Twitter/はてなブックマークという日本特有のエンジニアコミュニティの連鎖が、個人開発の英語学習系サービスに具体的な数字（数千UU〜数万PV、数百件の事前登録）をもたらした実例が確認できた。英語圏でこれに相当する明確な個人開発バズ実例（同等の定量データ付き）は今回の調査では見つからなかった（Indie Hackers上の一般的な記述はあるが、具体的な流入数値を伴う実例は未確認）。
- **市場規模そのものは日本より海外の方がはるかに大きい**：中国だけで英語学習者3〜4億人規模、韓国も含めAPAC全体で8億人超の学習者規模という報告がある一方、日本市場は成長しているものの規模としては相対的に小さい（具体的な日本市場規模の一次データは今回未取得、韓国の教育カテゴリ売上ランキングは取得できたが日本の同等データは未確認）。

## グレーゾーン・未確認

- **r/EnglishLearning の自己宣伝ルールの具体的な文言**：subredditのサイドバー/wikiを直接確認できなかった（`reddit.com` へのWebFetchがツール制限でブロックされた）。検索結果は一般的なReddit全体の「90/10ルール」しか拾えておらず、このサブ固有のルールは未確認。実際に投稿する前に、サブレディット内で直接確認する必要がある。
- **r/IELTS の登録者数が出典間で大きく食い違う**：一方は「129,637人」（reddapi、取得日不明）、もう一方は「80万人超」（2026年7月時点とする二次情報）。どちらが正確か、または対象が異なるサブ（r/IELTS vs 類似名の別サブ）を指しているのか切り分けられなかった。
- **Business of Apps の言語学習市場データを一次ページで直接確認できなかった**：`businessofapps.com` への直接フェッチが403エラーで失敗したため、検索エンジンが返した要約文のみに依拠している。ダウンロード数・売上額の数字は検索結果の要約経由であり、一次ページのグラフや脚注（データ取得方法、対象アプリの定義）までは検証できていない。
- **ASO ロングテール戦術の効果を定量化した実例が見つからなかった**：「初月に10〜15個のロングテールキーワードを狙う」という戦術論は複数のASOブログで語られているが、個人開発の英語学習アプリがこの戦術で実際に何ダウンロード獲得したかという定量的な事例研究は見つからなかった。
- **Product Hunt の語学学習カテゴリ特化の定量データはほぼ見つからなかった**：一般的なローンチ統計（50%が登録増を実感等）はSaaS全体の数字であり、語学学習カテゴリに絞った定量データは確認できなかった。
- **多言語展開の「獲得効果」を直接示す定量データは限定的**：中国のXiaohongshuでの英語学習投稿規模やマネタイズ事例は確認できたが、「アプリを中国語UIに翻訳して展開したら実際にどれだけ獲得が伸びたか」という個人開発者〜小規模事業者の一次事例は見つからなかった。韓国発の말해보카の多言語展開実績は確認できたが、これは韓国の資金力ある企業の事例であり、個人開発者が同じ戦略を取った場合の再現性は未検証。
- **TikTok/YouTube Shorts個人クリエイターの「アプリダウンロードへの転換率」**：数百万フォロワーを獲得した英語学習系クリエイターの実例は複数確認できたが、彼らがそのオーディエンスを自社アプリ・プロダクトのユーザーにどれだけ転換できたかという定量データは見つからなかった。フォロワー数＝広告的リーチであり、アプリ獲得への直接的な転換率は別の問題として未検証のまま残る。

## 影響する論点

この調査結果は、english-saas-venture の `open-questions.md` にある「ユーザー獲得チャネルをどう見積もるか」「SEOに投資する価値があるか」に直接関わる。決定を行う際は、①SEOをビッグキーワードで狙う想定を外すこと、②Reddit/TikTok/日本ならエンジニアコミュニティ経由のバズなど、コンテンツ量産より「一度作って当てにいく」型の経路を優先候補として検討すること、③多言語展開は市場規模の魅力はあるが個人開発者の一次成功事例が薄く、賭けとしては後回しが妥当であること、の3点を反映すべきである。

---

## 個人が現実的に賭けるべき経路は何か（確度つき判定）

**推奨: 「SEOを主軸に据えない」ことを前提に、(1) ロングテールASO×アプリストア最適化、(2) Reddit/コミュニティでの誠実な"作った話"投稿、(3)（日本語プロダクトなら）Qiita/Zenn/Twitter/はてなブックマークを通じたエンジニアコミュニティ発のバズ、の3つを組み合わせるのが最も現実的な賭けである（確度：中）。** 根拠は次の通り——SEOのビッグキーワードは実測SERPで大手が占有しており（確度：高）、AI OverviewsによるCTR低下が英語学習という「答えが一発で出せる」カテゴリを直撃する構造的トレンドが複数ソースで裏付けられている（確度：中〜高）。対してASOのロングテール戦術は市場全体のダウンロード数の大きさ（2025年に3.27億件）を考えると小さくても現実的な流入経路になり得る一方、個人開発者の定量的な成功事例は今回見つけられていない（確度：中、戦術の存在は確からしいが効果の実証は弱い）。Reddit・TikTok・YouTube Shortsは個人が数十万〜数百万規模のリーチに到達した実例が複数あるが、いずれも「コンテンツクリエイターとして数年かけて育てた個人ブランド」の実例であり、アプリのユーザー獲得チャネルというよりは並行して育てるべき別事業に近い（確度：中）。最も再現性高く・低コストで確認できたのは日本のエンジニア発バズ実例（Zenn記事で数字まで追えた）であり、対象プロダクトが英語学習を必要とするエンジニア層と重なるなら、この経路への投資対効果が最も具体的な裏付けを持つ（確度：高、ただし単一事例からの一般化である点は留意）。多言語展開はマーケット規模としては魅力的だが、個人開発者の一次成功事例が薄いため、初期の賭けとしてではなく、初期チャネルで一定の牽引力が出た後の第二段階の拡張策と位置づけるのが妥当である（確度：中）。
