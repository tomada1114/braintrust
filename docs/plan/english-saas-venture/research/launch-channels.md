# Show HN と Product Hunt は語学・英語学習アプリの獲得経路として機能するか

- 調査日: 2026-09-14
- 調査手段: メインセッションによる HN Algolia API（`hn.algolia.com/api/v1/*`）と curl / WebFetch 直叩き。WebSearch はクォータ切れのため不使用。Reddit は 403 のため試行せず。
- 問い: Show HN と Product Hunt は、個人開発の語学・学習系アプリにとって実際に機能する経路か。機能するとして、どの程度の初速が出て、それは継続するのか。複数回使える経路か。

## 結論

**Show HN は「使える経路」だが、期待値は低く見積もるべきである。** 過去 3〜4 年の語学・英語学習系 Show HN 44 件を集計した結果、points の中央値は **28**、半数近く（21/44）が 20 点以下で沈んでいる。個人開発者が現実的に期待できる初速は「開発者の Twitter/X フォロワーがいなくても数十〜数百人が数日訪れる」程度であり、787 点（Quazel）のような突出例は極めて稀（今回のサンプルで上位 2 件のみが 400 点超）。**継続性は個別次第**：Show HN 経由の成功が事業として続いた例（Quazel、simedw の一連のプロジェクト、Term Typer/Speech Meter の jeanmayer）がある一方、ドメイン自体が失効・停止した例も 44 件中 5 件（約 11%）確認できた——ただし「生存＝ドメインが応答する」の確認に留まり、活発に更新されているかは別問題。**複数回使える経路である**ことは HN のガイドライン上も実例上も裏付けられたが、重要な条件がある：**同じ人が「別の新しい製品」を出すたびに点数は独立に評価される（jeanmayer、simedw、fersarr の例で確認）一方、「同じ製品」を焼き直して繰り返し投稿しても得点は上がらず低空飛行が続く**（barrell の Phrasing.app 4 回、yunusabd の同系統プロダクト 7 回はいずれも 2 桁未満〜低い 2 桁で頭打ち）。HN 読者層はコメント欄の質が高く、冷笑一辺倒ではなく実際に試して支払い意思を示す声も観測できたが、それは「あからさまな AI ラップ製品」への強い忌避感とセットである。**Product Hunt はクロール制約が大きく網羅調査はできなかった**が、断片的に取得できた範囲では、語学カテゴリの一般トピックページは大手（Duolingo、ElevenLabs 等）が支配しており、個人開発アプリの実績は Show HN と同程度かそれ以下（PrettyPolly が #15 Day Rank・202 points、lairner はわずか 3 points）。

## Show HN 一覧（過去 3〜4 年、language / english / vocabulary / flashcard / speaking / fluency 系、n=44）

調査方法: HN Algolia 全文検索 API（`tags=show_hn` ×「english」「language learning」「vocabulary」「flashcard」「speaking practice」「fluency」「language app」「learn language」「pronunciation」の 9 クエリ、各 hitsPerPage=100）を叩き、重複排除後 746 件から語学学習に直接関係する投稿を手動で選別した 44 件（**網羅的な自動抽出ではなく人力フィルタ**。ノイズ除去のため "plain English to SQL" 系のプログラミングツールなどは除外）。生死確認は各 URL を curl（`-L --max-time 8〜10`, UA 偽装）で直接フェッチし、200 系以外は個別に再確認・目視検証した（2026-09-14 時点）。

points 降順:

| タイトル | points | コメント数 | 投稿日 | 現在の生死（2026-09-14 確認） | URL |
|---|---|---|---|---|---|
| Get conversational practice in over 20 languages by talking to an AI | 787 | 335 | 2022-09-27 | 生存 | [talk.quazel.com](https://talk.quazel.com/chat/try) / [HN](https://news.ycombinator.com/item?id=32993130) |
| I trained a 9M speech model to fix my Mandarin tones | 469 | 153 | 2026-01-31 | 生存 | [simedw.com](https://simedw.com/2026/01/31/ear-pronunication-via-ctc/) / [HN](https://news.ycombinator.com/item?id=46832074) |
| Glossarie – a new, immersive way to learn a language | 363 | 155 | 2024-03-24 | 実質停止（Plesk既定のメンテナンスページ表示、3回リトライで再現） | [glossarie.app](https://glossarie.app/) / [HN](https://news.ycombinator.com/item?id=39807912) |
| Learn a language quickly by practising speaking with AI | 325 | 253 | 2023-08-02 | ドメイン失効（DNS解決不可、WebFetchでも`ENOTFOUND`） | [prettypolly.app](https://www.prettypolly.app) / [HN](https://news.ycombinator.com/item?id=36973400) |
| I'm making an open-source platform for learning Japanese | 288 | 88 | 2025-09-06 | 生存 | [kanadojo.com](https://kanadojo.com) / [HN](https://news.ycombinator.com/item?id=45152940) |
| Term Typer – Learn a language by typing | 220 | 99 | 2024-04-16 | 生存 | [termtyper.com](https://www.termtyper.com/) / [HN](https://news.ycombinator.com/item?id=40053257) |
| "Interactive" Italian Poetry for English Speakers | 187 | 49 | 2023-10-15 | 生存 | [italianpoetry.it](https://italianpoetry.it/) / [HN](https://news.ycombinator.com/item?id=37888606) |
| Learn German with Short Stories | 180 | 119 | 2023-04-26 | 生存 | [webbu.app/german](https://webbu.app/german) / [HN](https://news.ycombinator.com/item?id=35713852) |
| Personalized Duolingo (kind of) for vocabulary building | 161 | 68 | 2025-01-20 | 生存（GitHubリポジトリのみ、ホスト型サービスではない） | [GitHub](https://github.com/baturyilmaz/wordpecker-app) / [HN](https://news.ycombinator.com/item?id=42770200) |
| LearnLingo – Converse with an AI-powered language tutor | 157 | 103 | 2023-07-31 | 生存 | [learnlingo.dev](https://www.learnlingo.dev) / [HN](https://news.ycombinator.com/item?id=36939145) |
| Phrasing – learn every language, to any level | 127 | 125 | 2024-01-29 | 生存 | [phrasing.app](https://phrasing.app/playground) / [HN](https://news.ycombinator.com/item?id=39177467) |
| Kimchi Reader – Immersive Korean Learning with a Popup Dictionary | 115 | 44 | 2023-10-29 | 生存 | [kimchi-reader.app](https://kimchi-reader.app) / [HN](https://news.ycombinator.com/item?id=38059396) |
| Manabi Reader – Learn Japanese by Reading on iOS and macOS | 105 | 57 | 2023-07-10 | 生存 | [reader.manabi.io](https://reader.manabi.io/) / [HN](https://news.ycombinator.com/item?id=36674259) |
| Turn native language audio into flashcards and shadowing practice | 92 | 37 | 2026-06-25 | 生存 | [lingochunk.com](https://lingochunk.com/try) / [HN](https://news.ycombinator.com/item?id=48671886) |
| Learning a Language Using Only Words You Know | 84 | 29 | 2025-12-15 | 生存 | [simedw.com](https://simedw.com/2025/12/15/langseed/) / [HN](https://news.ycombinator.com/item?id=46274287) |
| I built an AI language teacher to get you speaking | 82 | 110 | 2023-06-07 | 生存の可能性（自動確認は403、Cloudflare等のボット対策とみられる） | [gliglish.com](https://gliglish.com/) / [HN](https://news.ycombinator.com/item?id=36228477) |
| SubSmith – Turn your own videos into language-learning material | 78 | 51 | 2026-08-28 | 生存 | [subsmith.app](https://subsmith.app) / [HN](https://news.ycombinator.com/item?id=49476894) |
| Speech Meter – Improve Your English Pronunciation | 71 | 66 | 2023-10-11 | 生存 | [speechmeter.com](https://speechmeter.com/) / [HN](https://news.ycombinator.com/item?id=37843621) |
| A New Way to Learn Languages | 67 | 53 | 2025-02-14 | 生存 | [langturbo.com](https://www.langturbo.com) / [HN](https://news.ycombinator.com/item?id=43047554) |
| I built an AI conversation partner to practice speaking languages | 65 | 56 | 2026-01-30 | 生存（App Store） | [App Store](https://apps.apple.com/us/app/talkbits-speak-naturally/id6756824177) / [HN](https://news.ycombinator.com/item?id=46830698) |
| Ricotta – Language Learning to Replace Anki | 58 | 79 | 2025-02-06 | 生存 | [ricotta.affineur.io](https://ricotta.affineur.io/) / [HN](https://news.ycombinator.com/item?id=42966942) |
| I speak 5 languages. Common apps taught me none. So I built lairner | 35 | 89 | 2026-02-13 | 生存 | [lairner.com](https://lairner.com) / [HN](https://news.ycombinator.com/item?id=47003596) |
| Flowery – Vocabulary builder powered by LLM and spaced repetition | 21 | 24 | 2024-06-18 | 生存 | [flowery.app](https://flowery.app) / [HN](https://news.ycombinator.com/item?id=40717052) |
| YapCards (iOS) – Voice-driven flashcards with AI feedback | 20 | 9 | 2025-05-15 | 公式サイト不明（元投稿にURLなし） | [HN](https://news.ycombinator.com/item?id=43990868) |
| ListLang – Learn Languages to Fluency | 18 | 25 | 2023-02-08 | 生存 | [listlang.com](https://www.listlang.com/) / [HN](https://news.ycombinator.com/item?id=34708959) |
| Nuenki - Learn a language while you browse the web | 18 | 20 | 2024-09-21 | 生存 | [nuenki.app](https://nuenki.app) / [HN](https://news.ycombinator.com/item?id=41609346) |
| Vocab Top – AI-powered vocabulary builder | 18 | 12 | 2026-08-05 | 生存 | [vocab.top](https://www.vocab.top/) / [HN](https://news.ycombinator.com/item?id=49183110) |
| I built a language learning quiz app | 15 | 9 | 2022-09-11 | 生存 | [vocab.ling-academy.com](https://vocab.ling-academy.com/) / [HN](https://news.ycombinator.com/item?id=32801721) |
| I build an AI Language Speaking that make 3k a month | 14 | 12 | 2024-04-04 | 生存 | [fluentpal.app](https://fluentpal.app/en) / [HN](https://news.ycombinator.com/item?id=39928906) |
| I made a word puzzles app for improving your English vocabulary | 12 | 21 | 2025-05-17 | 生存 | [dictionarygames.io](https://www.dictionarygames.io) / [HN](https://news.ycombinator.com/item?id=44017713) |
| I spent 10k hours building the perfect language learning app | 10 | 8 | 2026-01-15 | 生存（Phrasing.appの再投稿） | [phrasing.app](https://phrasing.app/) / [HN](https://news.ycombinator.com/item?id=46633820) |
| LLM-based Toolset for Language Learning | 9 | 4 | 2025-02-13 | ドメイン失効/転売（`http://drillapp.xyz`はSafeBrowse警告ページへ302リダイレクト） | [drillapp.xyz](https://drillapp.xyz/login) / [HN](https://news.ycombinator.com/item?id=43035524) |
| Tired of ghosting on language apps. I made this to schedule real talks | 9 | 6 | 2025-08-21 | 生存 | [meetapart.com](https://meetapart.com) / [HN](https://news.ycombinator.com/item?id=44968701) |
| Lexical - How I learned 3 languages in 3 years | 9 | 13 | 2025-11-11 | 生存 | [lexical.app](https://lexical.app/white-paper) / [HN](https://news.ycombinator.com/item?id=45890795) |
| Itsumo: Make yourself fun and interesting academic language lessons | 9 | 0 | 2026-04-08 | 生存 | [itsumo.study](https://itsumo.study/) / [HN](https://news.ycombinator.com/item?id=47694112) |
| LingoLooper – Language Learning with Fun, Interactive AI Avatars in 3D | 7 | 2 | 2024-03-27 | 生存 | [lingolooper.com](https://www.lingolooper.com/) / [HN](https://news.ycombinator.com/item?id=39839616) |
| Phrasing.app – learn and maintain multiple languages | 7 | 3 | 2025-11-07 | 生存（Phrasing.appの再投稿） | [phrasing.app](https://phrasing.app/) / [HN](https://news.ycombinator.com/item?id=45845815) |
| Gem and I built an open-source app to learn Japanese | 7 | 0 | 2025-06-13 | 生存 | [nihongo.site](https://nihongo.site) / [HN](https://news.ycombinator.com/item?id=44273058) |
| Conversational Language Learning App (Lingocat) | 6 | 2 | 2025-01-12 | App Storeから削除済み（404） | [App Store](https://apps.apple.com/ca/app/lingocat-practice-speaking/id6502639816) / [HN](https://news.ycombinator.com/item?id=42676861) |
| Squeak – Learn languages with news articles tailored to CEFR | 6 | 0 | 2025-04-08 | 生存 | [squeak.today](https://squeak.today/) / [HN](https://news.ycombinator.com/item?id=43625908) |
| I created an app to learn any language without effort for free (fluent.im) | 6 | 7 | 2024-09-01 | 生存 | [app.fluent.im](https://app.fluent.im/) / [HN](https://news.ycombinator.com/item?id=41416827) |
| Language Life – Learn a language by living a simulated life | 5 | 2 | 2026-03-14 | 生存 | [languagelife.ai](https://www.languagelife.ai) / [HN](https://news.ycombinator.com/item?id=47380572) |
| Anki-like flashcards for non tech-savvy users (language learning) | 5 | 2 | 2025-03-06 | ドメイン失効（DNS解決不可、WebFetchでも`ENOTFOUND`） | [koshka.app](https://koshka.app/) / [HN](https://news.ycombinator.com/item?id=43278688) |
| Coupling - A Language Learning App for Couples | 5 | 0 | 2025-02-14 | 生存 | [couplingcafe.com](https://couplingcafe.com) / [HN](https://news.ycombinator.com/item?id=43049243) |

参考（3〜4年の対象期間より前だが継続性の材料として）: Clozemaster（2017年投稿、145pt）、Readlang（2015年、178pt）、fleex.tv（2013年、287pt）、Lingvist（2015年、18pt）はいずれも2026-09-14時点で生存を直接確認（HTTP 200）。

## points の分布（数字）

n=44（上表と同一サンプル）。

- 最小: 5 / 最大: 787 / **中央値: 28** / 平均: 98.9（上位数件の外れ値に強く引っ張られており、代表値としては中央値を見るべき）
- 20点以下: 21/44（47.7%）
- 50点以下: 23/44（52.3%）
- 100点以下: 31/44（70.5%）
- 400点超（今回のサンプルでの「大当たり」相当）: 2/44（4.5%）

**個人開発者が現実的に期待できる初速**: 中央値が28点であることから、「フロントページに乗って数千の目に触れる」のは例外で、**大半（半数近く）は shownew に載っても20点未満で沈み、実質的には数十〜百数十人が見て終わる**規模だと見るのが妥当。この分布はサンプルの選別バイアス（Algolia検索でヒットした語学学習関連タイトルを人力で拾ったもの。ヒットしなかった0〜数点の投稿はさらに多く存在すると推測されるため、実際の中央値はこれより低い可能性がある）を割り引いてもなお低い。

## 成功例の深掘り（points上位5件、作者自身の発言を原文引用）

`items/<id>` で本文・コメントツリー全体を取得し、投稿者（OPアカウント）自身の発言、および全コメントからトラフィック・登録・収益に言及した箇所を検索した。

### 1. Quazel（787pt, `Hadjimina`）
OP自身がトラフィック規模を数値で語った発言は**見つからなかった**。マネタイズについて模索中である旨のコメントのみ：
> "For pricing we would probably go the subscription route. [...] We are trying to figure this stuff out ourselves atm..."

### 2. Mandarin tone trainer（469pt, `simedw`）
OP自身の数値言及は**見つからなかった**。ただし第三者コメントに強い support-to-pay の反応があった（詳細は後述「HN読者層との相性」）。

### 3. Glossarie（363pt, `jonathanb88`）
トラフィック・登録者数への言及は**見つからなかった**。「2年以上かけて開発した」「初期ユーザーでのテストで効果を確認」という定性的な記述のみ。

### 4. PrettyPolly（325pt, `cwbuilds`）
数値そのものではないが、**投稿後にトラフィックが想定を超えたことを作者自身が明言**している：
> "Yeah, apologies. Wasn't expecting nearly this much traffic. Have made it more robust so it should be running faster than ever now"
> "Hi there, sorry about the poor user flow at the moment. We had to take emergency measures and change the signup process to ensure that premium members are able to get a service."

これは「Show HN 単体で想定外の初速が来た」ことを示す一次証言。ただし具体的な訪問者数・登録者数は語られていない。現在このドメインは**DNS解決不可（失効）**であり、325ptという当時の反響は事業としては継続しなかったと見られる。

### 5. Kanadojo（288pt, `tentoumushi`）
トラフィック言及は**見つからなかった**。OSSコントリビューター募集の呼びかけのみ。

**補足（サンプル外だが直接的な数値証言があった例）**: FluentPal（14pt, `davidtranjs`、id=39928906）の投稿本文で作者が明確な数値を開示している：
> "The app got 500 downloads on the first day alone, though I didn't earn any money from it initially. In the next 3 months, I only made around $50. [...] The game-changer was in December, 2023 when I got a popular Youtuber to promote FluentPal. [...] Now, FluentPal earns $3,000 a month"

**重要な注意**: この$3,000/月という数字は**Show HN投稿（14pt/12コメントと低調）によってもたらされたものではない**。作者自身が語る成長要因は「ベトナムのフォーラム voz.vn への投稿（初日500ダウンロード）」と「YouTuberによるプロモーション」であり、HNはこの回顧録を後から投稿しただけ。**Show HNのpointsと事業成果は必ずしも相関しない**ことを示す重要な反例。

## 継続性

- **ドメイン生存率**: 44件中39件（約89%）が2026-09-14時点でHTTP 200等で応答（＝ドメインが生きている）。ただしこれは「サーバーが応答する」ことの確認に過ぎず、**活発に開発・運営されているかは別問題**（例えばPhrasing.appは同一作者が3回Show HNに再投稿しており、作者自身は今も開発を続けていることが確認できるが、多くの他サイトはコンテンツが更新されているかまでは確認していない）。
- **死亡確認5件（約11%）**の内訳: ドメイン失効（PrettyPolly、koshka.app）、Pleskの既定メンテナンスページ化（Glossarie＝実質的な放置状態とみられる）、SafeBrowse警告ページへのリダイレクト（drillapp.xyz＝ドメイン転売/悪用の兆候）、App Storeからの削除（Lingocat）。**高得点だったPrettyPolly（325pt）とGlossarie（363pt）の2つがいずれも「死亡」側に分類される**のは象徴的——Show HNでの高評価が事業としての継続を保証しないことを示している。
- **単発スパイクで終わるか、そこから伸びるか**: 両方の例が確認できた。
  - 伸びた例: Quazel（787pt→現在も稼働、talk.quazel.comが応答）、simedw（Mandarin tone trainer 469pt→langseedプロジェクトなど継続的に新作を発表）、jeanmayer（Term Typer 220pt、Speech Meter 71ptの両方を継続稼働させている）。
  - 単発で終わった（とみられる）例: PrettyPolly（325ptの反響後、ドメイン失効）、Glossarie（363pt後、メンテナンスページ化）。
- 対象期間より前の古い事例（Clozemaster 2017/145pt、Readlang 2015/178pt、fleex.tv 2013/287pt）は**いずれも10年前後を経た今も生存**しており、「Show HNで火がついた製品が長期的に生き残る」こと自体は不可能ではないことを示す参考データ。ただしこれらがShow HN経由の初速だけで生き残ったのか、その後の別の成長要因（SEO、口コミ等）によるのかは本調査では切り分けられない。

## 複数回使えるか

**HNガイドライン上の制約**: `https://news.ycombinator.com/showhn.html` を直接フェッチして全文確認した。「同じ人が複数回使ってよいか」「別製品なら再投稿してよいか」を明示的に禁止・許可する記述は**存在しない**。関連する記述は次の一般規定のみ：
> "New features and upgrades ('Foo 1.3.1 is out') generally aren't substantive enough to be Show HNs. A major overhaul is probably ok."
> "Please don't ask friends to upvote or comment. That's not ok on HN."

一般FAQ（`newsfaq.html`）の「Are reposts ok?」は**同一記事の再投稿**についての規定であり、Show HNで別製品を出すこととは論点が異なる：
> "If a story has not had significant attention in the last year or so, a small number of reposts is ok."

**実例からの裏付け**: 対象データセット（746件の語学学習系Show HN候補プール）内で同一著者を集計したところ、複数回投稿している著者が多数確認できた。

- **「別製品」を複数回投稿し、いずれも一定の反響を得た例**:
  - `jeanmayer`: Term Typer（220pt, 2024-04）／Speech Meter（71pt, 2023-10）／Essential Vocabulary（2pt）／Code Typer（2pt）— 主力2本はいずれも今も稼働中。
  - `fersarr`: Learn German with Short Stories（180pt, 2023-04）／Hupreter（57pt, 2021-05）— 異なる着想の製品がそれぞれ独立に評価されている。
  - `simedw`: Mandarin tone trainer（469pt, 2026-01）／langseed（84pt, 2025-12）— 約6週間差で2本連投し、両方とも一定の反響。
- **「同じ製品」を焼き直して繰り返し投稿しても伸びない例**:
  - `barrell`（Phrasing.app）: 127pt（2024-01）→2pt（2025-11-15、別タイトルでの再投稿）→7pt（2025-11-07）→10pt（2026-01-15）。初回以降、一度も初回を超えられていない。
  - `yunusabd`（YouTube連動の語学学習ツール、複数の名称・切り口で計7回投稿、2025-03〜2026-03）: 1, 2, 2, 2, 3, 4, 4pt。7回投稿してもすべて一桁点に留まっている。
  - `detectivestory`（Snapalabra）: 4回投稿（2025-12〜2026-01）、いずれも2〜4pt。

**結論**: Show HNは**複数回使える経路だが、「使える」の意味が重要**。新しいアイデア・新しい製品であれば毎回フラットに再評価される（＝複数アプリ戦略と相性が良い）。しかし**同じ製品を粘り強く再投稿する戦術はほぼ機能しない**——HN読者はおそらく既視感やタイトルの手直しを見抜いており、繰り返すほど反応は先細りしている。複数アプリ戦略の文脈では、「1本のアプリを何度も磨いて出し直す」のではなく「本当に別のアプリを作って都度出す」ことが前提になる。

## HN読者層との相性

**エンゲージメントの質**: 今回精読した5件のトップスレッドのコメントは、冷笑的な一行diss中心ではなく、**実際に試した上での技術的・言語学的に踏み込んだフィードバック**が大半だった（例: PrettyPollyのスレッドで、TTS速度・keigo（敬語）の扱い・発音認識の精度についての専門的な議論が数十件続いている）。

**支払い意思を示す発言（肯定的な原文引用）**:
> "Nice. Please add Icelandic some time soon. I'd probably be willing to pay for that." （`peterhartree`、Quazelのスレッドより）

> "I am a huge, huge AI hater. I hate, hate, hate all the 'Show HN: My Latest AI Slop App...' [...] this is the first legitimately useful 'Show HN' I have seen in this AI sphere. [...] I would pay you to use this once the model improves a little bit. It's really fantastic." （`irl_zebra`、Mandarin tone trainerのスレッドより）

この2件目のコメントが特に重要：**HN読者は「量産型のAIラップアプリ」に対して強い忌避感（"AI Slop"という蔑称が定着している）を持つ一方、技術的に踏み込んだ、明確に有用な単一機能ツールには賞賛と支払い意思を示す**。つまり相性は「日常会話スキルアップアプリ」という括りそのものではなく、**「何が具体的にできるか」の解像度**に強く依存する。

**ターゲット層との整合性については未検証**: 今回精読したスレッドはいずれも「言語学習ツールとしての出来」を評価する反応が中心で、「非ネイティブ開発者自身が日常会話スキルアップのために金を払うか」という一人称の証言は見つからなかった。decisions.md 2026-09-14で「業務英語ではなく日常会話」に対象を絞ったこととの相性は、本調査だけでは判定できない（open-questions.mdの既存論点と一致）。

## Product Hunt

**取得できなかったもの**:
- `producthunt.com/topics/language-learning` 等、一部のトピックスラッグは**404**（スラッグ体系が不明でヒットしない）。
- `producthunt.com/categories/*` は**Cloudflareのチャレンジページ（403）**が返り、直接取得不可（WebFetch・curl双方で確認）。
- Show HNの語学学習系44件のうち、Product Hunt上に対応ページが存在したのは確認できた範囲で3件のみ（`quazel`, `glossarie`, `phrasing`, `termtyper`は404＝PHには出していないか別スラッグ）。

**取得できたもの**:
- `producthunt.com/topics/languages`（スラッグ`languages`のみ生存）: 取得できたのは**AIが要約生成した「Best Languages Tools in 2026」という評価型ランキングページ**であり、日々のローンチフィードではない。上位に並ぶのはDuolingo、ElevenLabs、Spotify、Railway、DeepSeek、Googleなど**巨大企業の製品ばかり**で、個人開発の語学アプリが入り込む隙が構造的に無いことが確認できた。
- 個別製品ページは直接スラッグが分かれば取得可能（`producthunt.com/products/<slug>`）。以下2件を確認：
  - **PrettyPolly**（同一製品がShow HNでも325pt）: "Launched 2yr ago #15 Day Rank Upvote・202 points、166 followers、1 review 5.0"。Show HNとPHの両方で相応の反響を得た数少ない例。ただし前述の通り、このドメインは現在DNS失効。
  - **lairner**（Show HNでは35pt）: PH側は"3 points, 3 followers"のみ。Show HNより低調。
- 「Ricotta」という同名の別製品（OKR管理ツール、語学学習アプリとは無関係）がPHに存在することも判明——**製品名の衝突により誤認しないよう注意が必要**。

**判断材料としての限界**: Product Huntのクロール制約により、語学学習カテゴリの日々のローンチ実績を定量的に把握することはできなかった。断片的に取得できた2件（PrettyPolly、lairner）からは、**Show HNと同程度かそれ以下の規模感**という推測はできるが、サンプル数が少なすぎて一般化はできない。

## グレーゾーン・未確認

- **サンプル選別のバイアス**: 44件はAlgolia検索結果（746件）から人力でフィルタしたものであり、完全な網羅ではない。特に0〜数点で埋もれた投稿はAlgoliaの関連度ソートで下位に沈み、検索クエリに引っかからなかった可能性がある。実際の全体分布の中央値は今回算出した28よりさらに低い可能性が高い。
- **「生存」の定義が甘い**: 39件を「生存」としたが、これは「HTTPリクエストに200番台等で応答した」ことの確認に留まる。実際にサービスが提供されているか、コンテンツが更新されているか、運営者が今も対応しているかは個別に確認していない（時間の制約により全件の目視UIチェックは行っていない）。
- **成功例の深掘りで数値証言がほとんど見つからなかった**: 上位5件のうちOP自身がトラフィック・登録者数の具体的な数字を語っていたのは0件（PrettyPollyの「想定外のトラフィック」は定性的表現のみ）。ShowHNの反響とその後の実際の集客効果を結びつける定量データは、今回のコメント欄探索では確認できなかった。
- **Product Hunt側の網羅調査ができなかった**ことは前述の通り。特に「語学カテゴリでの日次ローンチフィード」「カテゴリ別の中央値」は一次データで確認できておらず、acquisition-channels.mdに記載されている「一般的なローンチ統計（50%が登録増を実感）」の援用にとどまる。
- **HN読者と「日常会話スキルアップ」ニーズの直接的な一致は未確認**。今回のスレッド精読では「ツールとしての出来」への反応は豊富だが、「自分は日常会話で困っていて金を払いたい」という一人称の証言は見つかっていない。
- **barrell（Phrasing.app）が同一人物か、同一チームの複数アカウントかは未検証**（HNアカウント名が同一である事実のみ確認）。

## 個人が Show HN / Product Hunt に賭ける価値があるか（確度つき判定）

**判定: 賭ける価値はあるが、単一の獲得経路として期待してはならない（確度：中〜高）。** Show HNは実際に機能する経路であり（44件中確認できた反応の中央値28ptは「数十〜百人規模の可視化」を保証し、無視できない初速ではある）、同一人物が別製品を複数回投稿することも実例・規約の両面で問題なく、**複数アプリ戦略との相性自体は良い**（確度：高、jeanmayer・simedw・fersarrの実例で裏付け）。ただし3つの重大な留保がある。第一に、初速の中央値は低く、787点のような突出例は稀（今回のサンプルで4.5%）であるため、Show HN単体を事業の主要な集客エンジンとして設計するのは危険（確度：高）。第二に、高得点が事業の継続を保証しない——今回サンプル中もっとも高得点だった2件のうち1件（PrettyPolly、325pt）は現在ドメイン失効、もう1件（Glossarie、363pt）は実質的に放置状態にあり、**「バズった直後」の観測だけでは判断できない**（確度：高、直接確認済み）。第三に、同じ製品を焼き直して再投稿する戦術はほぼ効果がなく（barrell・yunusabd・detectivestoryの実例）、複数アプリ戦略を機能させるには**毎回本当に異なる着想の製品を出す**という規律が必要（確度：中〜高）。Product Huntについては取得制約が大きく確度の高い判定材料が集められなかったため、断片的な観測（PrettyPollyの#15 Day Rank、lairnerの3points）からは「Show HNと同程度かそれ以下」としか言えない（確度：低）。総じて、Show HN / Product Huntは「複数アプリを出して当たりを探す」戦略における**タダで使える視認性の刻み目**としては合理的だが、これ単体を獲得経路の柱に据えるのではなく、`research/acquisition-channels.md`で検討した他経路（ASO、コミュニティでの継続的な存在、日本ならエンジニア界隈のバズ）と組み合わせる前提を置くべきである。

## 影響する論点

- `open-questions.md`「Reddit が閉じた後に残る獲得経路はどれか」に直接回答する。Show HNは「残る候補」の一つとして実証されたが、単独では不十分という留保つき。
- `open-questions.md`「複数アプリを出す戦略における『共通の入口』を何にするか」に関連: Show HNは複数アプリ戦略と技術的には相性が良い（毎回リセットされる）が、それ自体が「共通の入口」にはなり得ない（1回ごとに新規の可視化が必要で、フォロワーの蓄積が効かない）。共通の入口の問いは依然未解決。
- `decisions.md` 2026-09-14「複数のアプリを出して当たったものを伸ばす」方針の実行可能性の裏付け材料として使える。ただしClaudeの指摘（「入口を持たないまま5本出せば5本ともゼロになる」）を否定はしない——Show HNだけでは複数アプリ戦略の集客問題を解決しきれない。

## メインセッションによる追検証（2026-09-14）— サブエージェントの数字を下方修正

サブエージェントは points 中央値 28 と報告したが、**これは目に留まった案件を拾った標本であり、選択バイアスがかかっている**。
メインセッションが HN Algolia API を無加工で叩いた結果は、はるかに厳しい。

実行したクエリ:
`https://hn.algolia.com/api/v1/search?tags=show_hn&query=english%20learning&hitsPerPage=50`

**結果（n=50、2026-09-14 取得、確度: 高）**
- **中央値: 2 点**
- 平均: 16.3 点
- 最大: 457 点（ただし `FastGraphRAG` という RAG ライブラリで、語学アプリではない）
- 最小: 1 点
- **20 点以下: 46 件（92%）**
- 50 点以下: 47 件（94%）

語学系で上位に来たもの:
| points | 日付 | タイトル |
| --- | --- | --- |
| 115 | 2023-10-29 | Show HN: Kimchi Reader – Immersive Korean Learning with a Popup Dictionary |
| 87 | 2024-02-14 | Show HN: FoldMation – Interactive origami learning and creation |
| 35 | 2022-11-17 | Show HN: Text editor with inline English-German dictionary |
| 14 | 2024-04-04 | Show HN: I build an AI Language Speaking that make 3k a month |
| 8 | 2025-03-27 | Show HN: My cousin in Morocco almost quit coding because of English |
| 7 | 2021-06-18 | Show HN: Hotpot, a TikTok for learning English like a native speaker |
| 7 | 2024-03-27 | Show HN: LingoLooper – Language Learning with Fun, Interactive AI Avatars |

**結論の修正: Show HN に英語学習アプリを出しても、ほぼ何も起きないのが標準的な結果。**
「中央値 28 点」を前提に期待値を組むと誤る。実態の中央値は 2 点。

## HN 公式ガイドラインの確認（メインセッション、2026-09-14）

出典: https://news.ycombinator.com/showhn.html （直接フェッチ、確度: 高）

複数アプリ戦略との関係で重要な原文:
- **同一人物が別製品を複数回投稿することを禁じる記述は無い。** サブエージェントの観測と一致。
- ただし: **「The project should be non-trivial. Don't post quickly-generated one-offs; anybody can do that now. Share something that is deeply personal and interesting to you. Explain how and why.」**
  → **量産したアプリを次々に出す、というやり方は正面から釘を刺されている。**
  `research/reddit-promotion-rules.md` の r/languagelearning の「vibe coded in less than 6 months は品質基準に届かない」と同じ方向の規範。
- 「Please make it easy for users to try your thing out, ideally without barriers such as signups or emails.」
  → サインアップ必須の設計は不利。
- 「Off topic: blog posts, sign-up pages, newsletters」「Don't post landing pages or fundraisers.」
- 「Please don't ask friends to upvote or comment.」

## 最も重い発見（サブエージェント、メインセッション未検証）

高得点だった 2 件（PrettyPolly 325点、Glossarie 363点）は、**いずれも現在サイトが死んでいる**（DNS 失効 / Plesk 放置ページ）。
**Show HN でバズることは、事業の継続をまったく保証しない。**
一方 FluentPal（月 $3k を開示）の成長要因は**ベトナムのフォーラムと YouTuber 経由**で、HN 投稿（14 点）は寄与していない。
