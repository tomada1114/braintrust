# 非ネイティブエンジニアの「英語で困っている」痛みと、既存プロダクト・課金実態の調査

- 調査日: 2026-09-14
- 調査手段: Hacker News Algolia 全文検索 API（コメント・Show HN 横断）+ dev.to API + 各社公式サイト・アプリストアの WebFetch + Wikipedia（Grammarly の数字確認用）+ GitHub Octoverse / Stack Overflow Developer Survey の一次データ。Reddit（r/cscareerquestions 等）は本セッションでは全面的にアクセス不可（後述）。WebSearch はセッション開始時点でクォータ切れ（0/200 残）で一度も使えなかった。
- 問い: 非ネイティブのエンジニア／技術職が「仕事で英語に困っている」という痛みは実在するか。実在するとして、その層向けの英語学習プロダクトは既にあるか、人は金を払っているか。
- 対象セグメント: Hacker News・dev.to に投稿する非ネイティブ英語話者のエンジニア／技術職（自己申告ベース）。国籍は本文中に明記されている場合のみ記録（ブラジル、日本、中国、ドイツなど散発的）。Reddit の r/developersIndia / r/brdev など特定国コミュニティの声は取得できなかった。
- 情報源: Hacker News（コメント・Show HN、英語）、dev.to 記事（英語、一部 AI 生成の疑いあり）、製品公式サイト・App Store（英語）、Wikipedia（英語）、GitHub Octoverse・Stack Overflow Developer Survey（英語、一次統計）。すべて英語圏の情報源のみで、日本語・ポルトガル語・ヒンディー語などの一次情報は取れていない。

## 調査手段の内訳（正直な報告）

**使えた:**
- Hacker News Algolia 検索 API（`hn.algolia.com/api/v1/search`）— コメント全文検索、Show HN 検索とも問題なく使用できた。今回の生の声・indie プロダクト発見の主力。
- 個別 HN アイテムの子コメント取得（`hn.algolia.com/api/v1/items/<id>`）— スレッド全体を読んで文脈を確認するのに使用。
- dev.to API（`/api/articles?tag=english`）— 使えたが、ヒットしたのはほぼ全て content-farm 的な AI 生成疑いの記事（同一アカウントが1日に何本も「AI-Powered X」を量産）。信号として弱い。
- WebFetch — 製品公式サイト、App Store、Wikipedia、GitHub Octoverse、Stack Overflow Survey ページの取得に使用。おおむね機能したが、Udemy（トピックページ・検索ページとも 403）、reddit.com（全パターンで 403 またはブロックページ）、pushshift.io（403 Not authenticated）、italki の teachers 検索の一部、goodcharacters.com（DNS 消滅＝リンク切れ）は取得できなかった。

**使えなかった:**
- WebSearch — セッション開始時点で 200/200 クォータを使い切っており、一度も実行できなかった（最初の1回だけ試して確認）。
- Reddit JSON API（`www.reddit.com/r/.../search.json`）— 複数の User-Agent、`old.reddit.com`、Googlebot UA、いずれも 403 または "Blocked" ページ。r/cscareerquestions、r/ExperiencedDevs、r/developersIndia、r/brdev、r/csMajors の声は**一件も取得できなかった**。
- Pushshift API — 403 "Not authenticated"（旧無料枠は廃止されている）。
- Udemy のトピックページ・検索ページ — 403。「English for IT」系コースの受講者数・価格は確認できなかった。
- goodcharacters.com（HN で106ポイントを集めた "Things I did to improve my English and reduce my accent" のブログ本体）— ドメインが消滅（DNS 解決不可）。HN 側のコメントスレッドは読めた。

この結果、**生の声はほぼ Hacker News 発（英語圏のエンジニアコミュニティの中でも技術寄り・シニア寄りに偏る媒体）に偏っている。** r/developersIndia や r/brdev のような、まさに問いが想定する層に近いコミュニティの声は今回取れていない。これは重大な制約として以下で明示する。

## 生の引用（16件）

### クラスタ A: 会議・発言（standup / ミーティングで話せない）

1. 「It is a sad state of affairs that reducing your accent can increase your chances of success, though I guess everyone has a bias towards hiring people like them... I think that would do a good job of eliminating bias, however the bias would still exist for things like promotions.」
   - URL: https://news.ycombinator.com/item?id=6314189（元スレッド https://news.ycombinator.com/item?id=6313591 内、著者 codygman）
   - 出典日付: 2013-09-02
   - 言語/情報源: 英語 / Hacker News コメント
   - セグメント: 自称なし（文脈上、非ネイティブ話者を擁護する立場のコメント）
   - 確度: 中（1件のみ、個人の意見）

2. 「Lots of professionals pay for accent coaching / accent modification, which can be accomplished by someone with patience, a good ear, good rapport, and no expensive degree. This is a good part-time job for people with an "in" in a particular foreign [community]...」
   - URL: https://news.ycombinator.com/item?id=6313843（コメント者: patio11 / Patrick McKenzie、元スレッド https://news.ycombinator.com/item?id=6313591）
   - 出典日付: 2013-09-02
   - 言語/情報源: 英語 / Hacker News コメント
   - セグメント: 業界観察者（本人はネイティブ話者、アクセント矯正市場の観察）
   - 確度: 中（金が動いている市場があるという傍証。売上規模の数字は無い）

3. 「I have taken the classes and it really isn't as hard...」は除外（無関係）。代わりに、面接での接続不良的アクセント問題:
   「I had a phone interview with Amazon. It too, was with someone with a heavy accent I had trouble understanding... To make things even worse, the interviewer had trouble understanding my english.」
   - URL: https://news.ycombinator.com/item?id=7041965
   - 出典日付: 2014-01-11
   - 言語/情報源: 英語 / Hacker News コメント
   - セグメント: エンジニア（求職者側、双方が非ネイティブ／訛りのある英語話者だった可能性）
   - 確度: 中

### クラスタ B: 書き言葉（PR・Slack・ドキュメント）

4. 「I remember the night after I joined my first American company. I sent a Slack message to my manager — and realized hours later I'd written something with awkward grammar. It wasn't a big deal… but I couldn't sleep (literally). I'd often rewrite messages 2–3 times before sending them... It felt so embarrassing. English isn't my first language. But I care deeply about how I come across, especially at work. So I built a Chrome extension for people like me.」
   - URL: https://news.ycombinator.com/item?id=43771934
   - 出典日付: 2025-04-23
   - 言語/情報源: 英語 / Hacker News（Show HN 投稿本文、著者 Bikashhh）
   - セグメント: エンジニア（自作の Chrome 拡張 "Typemate" のローンチ投稿）
   - 確度: 高（本人の一人称の体験談かつ、それを解決するために製品を作ったという強い証拠）

5. 「English is my second language and posting a comment on HN takes me five rewrites before clicking "add comment" and two+ edits after. Even then they don't necessarily come out all that clear judging by some of the responses I get.」
   - URL: https://news.ycombinator.com/item?id=8533876
   - 出典日付: 2014-10-30
   - 言語/情報源: 英語 / Hacker News コメント
   - セグメント: エンジニア（HN 常連と推定）
   - 確度: 高

6. 「Exactly. My team's technical documentation is written (in English) by people who don't speak English natively, and it's awful, barely comprehensible many times because these people don't understand articles ("the" and "a") very well and constantly omit them or use the wrong ones. And aside from the poor English, the documentation itself is just bad. AI w[ould help]...」
   - URL: https://news.ycombinator.com/item?id=46641802
   - 出典日付: 2026-01-16
   - 言語/情報源: 英語 / Hacker News コメント
   - セグメント: ネイティブ話者の同僚視点（非ネイティブエンジニアが書いたドキュメントのコスト・摩擦を証言）
   - 確度: 高（一人称の痛みではないが、非ネイティブの英語がチームに実害を与えている一次証言）

7. 「it got rejected right away because of poor grammar or something similar. the conference was in Brazil, b[ut written in English]...」
   - URL: https://news.ycombinator.com/item?id=38687156
   - 出典日付: 2023-12-18
   - 言語/情報源: 英語 / Hacker News コメント
   - セグメント: 学生／エンジニア（ブラジル）
   - 確度: 高（文法を理由に論文が一発却下されたという具体的な不利益）

8. 「Sorry, English is not my primary language, so the grammar constructions might get odd from time to time, this might have been the cause. ... When engineer becomes tech lead or engineering manager, be[tter soft skills matter more]...」
   - URL: https://news.ycombinator.com/item?id=15465084
   - 出典日付: 2017-10-13
   - 言語/情報源: 英語 / Hacker News コメント
   - セグメント: エンジニア（キャリア論のコメントの中で自分の英語を予防線として断っている）
   - 確度: 中

9. （dev.to、確度低・注意書き付き）「every PR description and README costs you more effort than it costs your native-speaking teammates」「Correction, not rewriting. You know what you mean; you need articles, prepositions, and tense fixed」「Affordable or free. Regional pricing is real; $12/month for grammar is steep in many markets」
   - URL: https://dev.to/yanlong_wang/best-grammar-checkers-for-non-native-english-developers-2026-172c
   - 出典日付: 2026-09-13
   - 言語/情報源: 英語 / dev.to 記事
   - セグメント: 不明（記事著者。プロフィールや投稿頻度から AI 生成コンテンツの可能性がある。他の同著者記事も似た構成の量産的リストブログ）
   - 確度: 低（内容自体はもっともらしく他の一次証言と整合するが、実在の非ネイティブ開発者の発言という保証がない。地域別プライシングへの言及など具体性はある）

### クラスタ C: 面接・採用

10. 「I can tell you that sadly accent can have more weight than we all wish it would have. It's a double issue, even if you are interviewing with the most liberal and ethical person who loves you and think you're a great fit but had problem understanding due to heavy accent, it's not in your favor.」
    - URL: https://news.ycombinator.com/item?id=7373743
    - 出典日付: 2014-03-10
    - 言語/情報源: 英語 / Hacker News コメント
    - セグメント: エンジニア（採用プロセスを語る文脈）
    - 確度: 高

11. 「Heaven forbid that a good communicator get promoted to deal with people, or that people be proficient in the language of the land.」（元発言への反論として引用される形での原発言）「management didn't want to talk to those foreginers who acted and spoke English funny, so he became the Western face of the team, and took all the credit.」
    - URL: https://news.ycombinator.com/item?id=42573392
    - 出典日付: 2025-01-02
    - 言語/情報源: 英語 / Hacker News コメント
    - セグメント: エンジニア（マネジメント・キャリアの議論の中で語られる、非ネイティブが対外窓口役から外される構造の証言）
    - 確度: 中（他者の体験の要約引用であり、一次証言としての確度はやや落ちる）

### クラスタ D: アクセント・発音への自己不安

12. 「I'm hearing impaired (not deaf) and I'm also a very experienced software engineer... I work with a number of people whose first language is not English, and some of them have very, very strong accents. It's nearly impossible for me to carry a conversation with them because of it. It gets better over time, but the first few weeks/month...」
    - URL: https://news.ycombinator.com/item?id=7908415 (story_id 7890255)
    - 出典日付: 2014-06-18
    - 言語/情報源: 英語 / Hacker News コメント
    - セグメント: 同僚視点（聴覚障害のある同僚から見た、強いアクセントによるコミュニケーション困難）
    - 確度: 中

13. 「Accents are part of people's identity because of the nature of their mother tongue... They are fine - they are not a deficiency.」（反証寄りの意見。Ban Ki-moon を例に、アクセントは仕事の支障にならないと主張）
    - URL: https://news.ycombinator.com/item?id=6315310（元スレッド https://news.ycombinator.com/item?id=6313591 内、著者 dodyg）
    - 出典日付: 2013-09-02
    - 言語/情報源: 英語 / Hacker News コメント
    - セグメント: 業界観察者
    - 確度: 中（反証として後段のセクションでも使用）

### クラスタ E: キャリア全体・給与・昇進

14. 「The level of English varies, and salaries usually correlate with English proficiency just as well as with technical ability. I believe this is because devs with strong English can compete as remote workers on the global market, whereas those who are not professionally competent in English are relegated to work in firms that speak their language, or at least to have a bilingual management layer abo[ve them]...」
    - URL: https://news.ycombinator.com/item?id=38583343
    - 出典日付: 2023-12-09
    - 言語/情報源: 英語 / Hacker News コメント
    - セグメント: エンジニア（給与とリモート市場アクセスの相関について）
    - 確度: 高（本調査で見つかった中で最も直接的な「英語＝金銭的機会」の証言）

15. x264（動画コーデック OSS）の日本人コミュニティについて：「Japan has long had a community of x264 developers and users, but for a long time they largely remained insular and didn't make much active effort to push their patches upstream... The language barrier was a big problem -- less so that they didn't [know English]...」
    - URL: https://news.ycombinator.com/item?id=3199748 (story_id 3198628 内、著者 bane)
    - 出典日付: 2012-02-29
    - 言語/情報源: 英語 / Hacker News コメント
    - セグメント: OSS コミュニティ観察者（日本の開発者コミュニティが言語の壁で世界に成果を還元できなかった事例）
    - 確度: 中

16. 「4. If you don't have functional English, learn it. As an American and native English-speaker myself, I have previously been reluctant to suggest this, lest it be taken as a sort of cultural imperialism. But several native speakers of other languages have urged me to point out that English is the working language of the hacker culture and the Internet, and that you will need to know it to funct[ion]...」（Eric S. Raymond "How To Become A Hacker" からの引用）
    - URL: https://news.ycombinator.com/item?id=8534547
    - 出典日付: 2014-10-30（HN 引用日。元エッセイ自体はさらに古い）
    - 言語/情報源: 英語 / Hacker News コメント内の引用
    - セグメント: ハッカー文化の規範的言説（本人の痛みの証言ではなく、コミュニティの共通認識としての「英語は必須」という規範）
    - 確度: 高（引用元の実在は確認できるが、これは当事者の痛みの声ではなく規範の表明）

## 困りごとのクラスタ（まとめ）

| クラスタ | 典型的な場面 | 強さの根拠 | 出典数 |
|---|---|---|---|
| 会議・発言 | 電話/ビデオ面接、standup | アクセントが採用判断に不利に働くという複数証言、accent coaching が実在の有料市場（patio11） | 3 |
| 書き言葉（PR/Slack/ドキュメント） | Slack でのメッセージ送信前に2-3回書き直す、PR description・README、カンファレンス論文投稿 | 「送信前に眠れなかった」という強い情動表現、論文が文法理由で即却下、同僚が書いたドキュメントが「barely comprehensible」という実害証言 | 5〜6（dev.to 込み） |
| 面接・採用 | 電話/リモート面接 | 「アクセントが好意的な面接官にすら不利に働く」「英語が下手な人は西洋の顔役に置き換えられる」 | 2 |
| アクセント・発音 | 日常の会話・同僚とのやり取り | 同僚が「ほぼ会話が成立しない」と証言する一方、「アクセントは欠陥ではない」という反証意見も同スレッドに存在 | 2（うち1件は反証） |
| キャリア・給与 | リモート市場への参入、昇進、OSS への貢献 | 「給与は英語力と技術力にほぼ同じくらい相関する」という直接証言、日本の OSS コミュニティが言語の壁で世界に還元できなかった事例、ハッカー文化の規範として「英語必須」という共通認識 | 3 |

## 既存プロダクト一覧

| プロダクト | URL | 対象 | 個人向けセルフサーブ課金か | 価格 | エンジニア/テック明示か | 生存確認 | 規模の数字（確度） |
|---|---|---|---|---|---|---|---|
| Voxy | voxy.com | 企業（B2B） | いいえ（デモ予約制、企業契約） | 非公開 | Yes（「Software Engineering」が明示的なユースケース、Tech 業界のケーススタディあり） | 生存（2026-09-14 WebFetch確認） | 非公開 |
| Preply Business | preply.com/en/business | 企業（B2B） | いいえ（デモ予約制） | 非公開 | Yes（「Language training for engineering & tech teams」を明示） | 生存 | 非公開 |
| ELSA Speak | elsaspeak.com | 個人＋企業 | 個人向けは Yes（無料+有料）、企業向けはカスタム見積り | 個人向け価格非公開、企業は要問合せ | いいえ（「working professionals」全般。エンジニア限定ではない） | 生存 | 「92M+ downloads」「90M+ learners」「1,300+ organizations」（すべて自己申告、確度低） |
| Speak | speak.com | 個人（一般消費者） | Yes | 地域・プロモーションで変動、非公開 | いいえ（対象は一般学習者） | 生存 | 「15M+ downloads」「4.8星」、OpenAI Startup Fund 出資（自己申告部分は確度低、出資自体は他媒体でも報道あり） |
| Coursera「English Communication for Tech Professionals」（Arizona State University） | coursera.org | 個人 | Yes（Coursera サブスクの一部として） | Coursera 標準の月額/コース単位課金（本セッションでは金額未確認） | Yes（コース名にテック専門家向けと明示） | 生存 | 評価4.7（84件のレビュー）。受講者数は未確認 |
| Typemate（Chrome拡張） | Chrome Web Store（chromewebstore.google.com） | 個人 | 不明（Show HN 時点で価格情報なし、WebFetch でも詳細取得できず） | 不明 | Yes（非ネイティブ開発者が自分のために作った、と明言） | Show HN 投稿は2025-04-23。継続運営か未確認 | HN 1ポイント、コメント1件。極めて小規模 |
| Orratio | orratio.com | 個人（一般） | Yes（無料+プレミアム、金額非公開） | 非公開 | いいえ（営業・面接・スピーチなど汎用） | 生存（2026-09-14 WebFetch確認） | 「952人のユーザー」（自己申告、確度低） |
| SayItRight（accent training） | App Store | 個人 | Yes（アプリ内課金） | 12.99 / 59.99 / 99.99 SAR（約 3.5〜27 USD） | 「初心者から上級者」で汎用、エンジニア限定ではない | Show HN 2025-06-12。生存は未確認 | レビュー8件、評価4.9。極めて小規模 |
| Accent AI（pronunciation coach） | App Store | 個人 | 不明 | 不明 | いいえ（汎用） | Show HN 2026-01-22 | HN 1ポイント |
| getpronounce.com | getpronounce.com | 個人 | 不明（WebFetch 403 で確認不可） | 不明 | 不明 | Show HN 2023-09-15。サイト生存は今回未確認（403） | HN 1ポイント |
| Grammarly（参考・英語学習ではなく校正ツール） | grammarly.com | 個人＋企業 | Yes | 非公開（今回未確認） | いいえ（全ライター対象） | 生存（サイトはSuperhumanブランドへリダイレクト、2026年時点でブランド統合が進行中と推測） | 評価額 $13B（2021年、Wikipedia）、$1B 非希薄化資金調達（2025年5月、General Catalyst）、100万人日次アクティブ（2015年時点、古い数字） |
| Udemy「English for IT」系コース | udemy.com | 個人 | Yes（Udemy の性質上） | 不明 | 不明 | 未確認（403でアクセス不可） | **未確認**。受講者数・具体的コース名は今回のセッションでは一切確認できなかった |

**「エンジニア／技術職向け英語学習」を名乗り、かつ個人が Stripe 的にセルフサーブで課金でき、かつ一定の規模（レビュー数・ユーザー数）を持つプロダクトは、今回の調査では見つからなかった。** 見つかった中で最も近いのは、B2B 専業（Voxy、Preply Business＝企業が契約してデモを予約する形。個人課金の窓口が無い）と、個人向けだが汎用（ELSA、Speak、Orratio＝エンジニアに限定しない一般英語/発音アプリ）、そして個人が作ったが規模がほぼゼロのインディー製品（Typemate、SayItRight、Accent AI、getpronounce）に二極化している。

## 金が動いている形跡

| 項目 | 数字 | 出典 | 出典日付 | 確度 |
|---|---|---|---|---|
| italki のビジネス英語講師の時給目安 | 30分レッスンで概ね $4〜$10、講師により $5〜$68/時間 | italki.com（teachers ページ、WebFetch） | 2026-09-14取得 | 中（ページの記載を直接確認したが、IT/テック特化の講師は今回の閲覧範囲では明示的に見つからなかった） |
| accent coaching / speech therapy が実在の有料副業市場である | 金額不明。「Lots of professionals pay for accent coaching」との証言 | patio11 (Patrick McKenzie) の HN コメント | 2013-09-02 | 中（信頼できる観察者だが数字を伴わない） |
| Grammarly の評価額・資金調達 | $13B（2021年11月）、$1B 非希薄化資金調達（2025年5月、General Catalyst） | Wikipedia「Grammarly」項 | 記事内の各年表記 | 中（Wikipedia は二次情報だが出典明記あり） |
| ELSA Speak の利用者数・法人数 | 「92M+ downloads」「90M+ learners」「1,300+ organizations」 | elsaspeak.com（自社サイト） | 2026-09-14取得 | 低（自己申告） |
| Speak の利用者数 | 「15M+ downloads」、OpenAI Startup Fund 出資 | speak.com（自社サイト） | 2026-09-14取得 | 低（自己申告） |
| SayItRight のアプリ内課金額 | 12.99 / 59.99 / 99.99 SAR | App Store（WebFetch） | 2026-09-14取得 | 高（アプリストアの表示価格そのもの。ただし実売実績は不明） |
| Udemy「English for IT」系の受講者数・価格 | **未確認** | — | — | — |

**総括:** 「非ネイティブエンジニアが英語のために直接金を払っている」ことを裏付ける一次的な金額データは、今回のセッションでは薄い。individually 課金しているという確度の高い数字は SayItRight のアプリ内課金額くらいで、それも実売実績（何人が買ったか）が分からない。ELSA・Speak の利用者数は自己申告であり、しかもエンジニア限定ではない全ユーザー数。「英語コーチングに金を払う人はいる」という定性的な証言（patio11）はあるが、規模の裏付けがない。B2B（Voxy、Preply Business）は「企業が」エンジニアチームの英語研修に金を払っている実例として存在が確認できるが、これは個人課金モデルの傍証にはならない。

## 反証

- 「But for many people and in many situations, translation---including MT---is good enough. And that overcomes any perceived need to learn another language (which learning may be in opposition to learning something else, something perceived as more important).」
  - URL: https://news.ycombinator.com/item?id=48808787
  - 出典日付: 2026-07-06
  - 確度: 中（一般論としての機械翻訳十分論。エンジニア限定の文脈ではないが、直接的に「学習の必要性を消す」と主張している）

- 「Accents are part of people's identity because of the nature of their mother tongue... They are fine - they are not a deficiency.」（Ban Ki-moon を例に、アクセントは仕事の障害にならないと明言）
  - URL: https://news.ycombinator.com/item?id=6315310（元スレッド https://news.ycombinator.com/item?id=6313591、著者 dodyg）
  - 出典日付: 2013-09-02
  - 確度: 中

- 「salaries usually correlate with English proficiency... those who are not professionally competent in English are relegated to work in firms that speak their language」（HN 38583343、前掲）は、裏を返せば**英語ができなくても、自国語で完結する企業で働くキャリアパスは現に存在する**ことを示している。全員が英語を必要としているわけではないという反証としても読める。
- 既存インディープロダクト（Typemate、SayItRight、Accent AI、getpronounce）はいずれも HN で1〜数ポイント、App Store レビューが1桁という極めて低い反応しか得ていない。これは「作ってもニーズに刺さらない」ことの傍証にもなり得るし、単に「配信力・マーケティングが弱かっただけ」の可能性もあり、どちらとも断定できない（グレーゾーンとして扱う）。
- 本調査ではエンジニアが「英語ができないことを理由に明示的にクビになった／内定を取り消された」という一次証言は見つからなかった。見つかったのは「不利に働く」「相関する」という間接的な証言のみで、直接的な金銭的損失の証言としては弱い。

## 層の広さ

| 国 | GitHub 上の開発者数（推定） | 前年比成長率 | 出典 |
|---|---|---|---|
| インド | 1,700万人以上 | +28% | GitHub Octoverse 2024（対象期間 2023-10-01〜2024-09-30） |
| 中国 | 900万人以上 | +10% | 同上 |
| ブラジル | 540万人以上 | +27% | 同上 |
| 日本 | 350万人以上 | +23% | 同上 |
| インドネシア | 350万人以上 | +23% | 同上 |
| ナイジェリア | 110万人以上 | +28% | 同上 |

GitHub Octoverse 2024 は「インドは2028年までに米国を上回り、世界最大の開発者人口を持つ国になる見込み」とも予測している（出典日付: 2024-10-29公開のレポート、確度: 高、一次情報源）。

Stack Overflow Developer Survey 2024（回答者65,437人、185カ国）では、国別回答比率が米国18.9%、ドイツ8.4%、インド7.2%、英国5.5%、ウクライナ4.6%、カナダ3.6%、フランス3.6%、ポーランド2.6%、オランダ2.5%、ブラジル2.3%となっている（出典: survey.stackoverflow.co/2024/、確度: 高、ただし注意点あり）。**注意**: この調査自体が英語で実施・告知されているため、英語が苦手な層ほど回答者に含まれにくいという選択バイアスがかかっている可能性が高い。つまりこの数字は「非ネイティブ英語話者エンジニアの母集団」を過小評価している可能性がある。

これらを合わせると、英語を母語としない主要な開発者人口だけでインド・中国・ブラジル・日本・インドネシアの上位5カ国で合計3,000万人規模（GitHub アカウントベース、重複・非アクティブアカウントを含む可能性あり）というオーダー感が一次資料から得られる。東欧（ポーランド、ウクライナ）や韓国については今回信頼できる一次数字を確認できなかった（グレーゾーン）。

## グレーゾーン・未確認

- **Reddit（r/cscareerquestions、r/ExperiencedDevs、r/developersIndia、r/brdev、r/csMajors）は本セッションでは一切アクセスできなかった。** 依頼で名指しされたコミュニティの声を全く反映できていない。特に r/developersIndia・r/brdev はまさに本調査が対象とする層（インド・ブラジルのエンジニア）の一次コミュニティであり、この欠落は調査の信頼性に対する最も大きな制約である。
- WebSearch がセッション開始時点で完全にクォータ切れだったため、Google 経由での網羅的な確認は一切行えていない。HN Algolia と dev.to、個別サイトの WebFetch だけに依存した調査であり、母集団は「HN に英語で書き込む層」に強くバイアスしている。HN は元々シニア寄り・すでに英語で発信できる層に偏っており、「本当に英語で困っていて声を上げられない人」はそもそも HN に出てこない可能性がある（生存者バイアス）。
- Udemy の「English for IT」系コースの受講者数・価格は 403 エラーで一切確認できなかった。この種のコースの受講規模は「英語学習に金が動いているか」を測る上で重要な指標のはずだが、今回は欠落している。
- dev.to のクラスタB引用9は、記事自体が AI 生成コンテンツファームの可能性がある媒体からのものであり、確度を「低」としている。内容は他の一次証言と整合するが、実在の開発者の言葉である保証はない。
- ELSA・Speak・Orratio の利用者数はすべて自己申告であり、第三者による検証はできていない。
- goodcharacters.com のブログ本体（HNで106ポイントを集めた元記事）はドメインが消滅しており、一次テキストを確認できなかった。HN 側のコメントスレッドから間接的に内容を推測している。
- 「英語ができないことが理由で明示的に不採用・降格・解雇になった」という一次証言（金銭的インパクトの直接証拠）は見つからなかった。存在しないと断定はできないが、少なくとも今回の検索範囲（HN 中心）では出てこなかった。
- 東欧・韓国の開発者人口についての信頼できる出典は見つけられなかった。
- 既存プロダクトのうち Voxy・Preply Business の実売規模（契約企業数、ARR）は非公開で確認できなかった。「エンジニア向け英語研修に企業が金を払っている」という事実の存在は確認できたが、規模は不明。

## この仮説は生きているか死んでいるか

**判定: 生きている（確度: 中）。ただし「個人が Stripe でセルフサーブ課金する、月30万円以上、営業なし、SEO なし」という前提の実現性については、判定材料が弱い。**

痛み自体の実在は、HN だけからでも複数クラスタ（会議・書き言葉・面接・アクセント・給与相関)にわたる一人称の証言（特に Typemate 作者の「Slack メッセージの文法で眠れなかった」という話、Brazil のカンファレンス論文が文法理由で即却下された話、給与と英語力の相関を語る証言）で相応に裏付けられており、これを「痛みが存在しない」と結論づける根拠は見つからなかった。GitHub Octoverse の数字も、対象になりうる母集団が最低でも数千万人オーダーで存在することを示している。一方で、既存プロダクトを見る限り、この層に対する商業的な解答は「企業が金を払う B2B 研修」(Voxy、Preply Business が明示的にエンジニアリングチームを標的にしている）に強く寄っており、「個人が自分の財布からセルフサーブで課金する、エンジニア専用の英語学習プロダクト」という形態で成功している事例は見つからなかった。存在するインディーの個人向け試みは軒並み反応が薄い(HN 1〜数ポイント、レビュー1桁)。これが「個人課金モデルがこの層に刺さらない」ことの証拠なのか、単に「まだ誰も本気でマーケティングしていないだけ」なのかは、今回のデスクリサーチだけでは判定できない。また、Reddit という最も重要な一次コミュニティ（r/developersIndia、r/brdev を含む）に一切アクセスできなかったこと、Udemy のコース実績が確認できなかったことは、この判定の確度を大きく下げている。次にやるべきは、Reddit へのアクセス手段の確保(別セッションでの WebSearch 再開、または API 経由)と、Udemy/Coursera の実際の受講者数の確認、そして可能であれば r/developersIndia・r/brdev の生の声を直接読むことだと考える。
