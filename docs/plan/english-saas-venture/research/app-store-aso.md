# アプリストア(ASO)は個人開発の英語学習アプリにとって流入経路になるか

- 調査日: 2026-09-14
- 調査手段: iTunes Search API（curl + jq）による定量集計、Google Play ストアページの直接取得（curl、埋め込みJSONのdownloads表記を抽出）、公式サイトの WebFetch。WebSearch は使用不可（クォータ枯渇）、Reddit は 403 のため未使用。すべて本セッションが直接叩いた一次データ。
- 問い: アプリストアは、個人開発の英語学習アプリにとって実際に流入を生む経路か。新規の無名アプリが露出する余地はどこにあるか。

## 結論

**主要クエリ（`english speaking` 等）はほぼ寡占状態で、個人開発の新規アプリが露出する余地はほぼない。** 上位20件のレビュー数合計に対する上位3社のシェアは80〜96%に達し、Duolingo・ELSA Speak・Learna・Babbel・British Council など資金力のある事業者が常連で並ぶ。

**一方、より狭いロングテールクエリ（`english collocations` / `english idioms` / `phrasal verbs` / `shadowing english` など）では、上位が個人開発者・小規模チームで占められているクエリが実在する。** 特に `phrasal verbs`・`english idioms`・`english collocations` は上位20件中に大手が1〜2社しか入らず、残りはレビュー数0〜数百件の個人アプリ（多くがベトナム人個人開発者と見られる名義）が並ぶ。これが今回確認できた唯一の隙であり、詳細はロングテール節に記す。

**新規参入アプリ（直近2年以内リリース）の現実的な到達点はかなり低い。** 収集した59件の新規アプリのうち66%（39件）がレビュー数100件未満、20%（12件）が0件。1万件以上に到達したのは3件のみで、いずれもAI英会話系の資金力あるスタートアップ（Learna、LangLearn、Gleam）だった。個人開発者が単独アプリで大きな数字に到達した例は今回のデータからは見つからなかったが、**個人名義の開発者が複数アプリを並行してリリースし、その中の1〜2本が数千〜1万件規模のレビューに到達している例は複数確認できた**（Nguyen Thi Hoai Thu、Loc Nguyen、Xung Le など）。これは「複数アプリを出して当たったものを伸ばす」という依頼者の戦略と整合する実例である。

日本市場（`country=jp`）は英語文字列のクエリでも日本語ローカライズされた資金力のあるアプリ（AI英会話スピーク、スピークバディ）が上位を占め、米国市場より参入がむしろ難しい可能性がある。

ウェブのみで英語学習の有料プロダクトを運営する例（WaniKani）は実在が確認できた。詳細は該当節。

## 1. 主要クエリの占有状況

iTunes Search API、`country=us`、`entity=software`、`limit=20`で取得。各クエリの上位から抜粋（全20件中の上位10件、レビュー数順ではなく検索順位順）。

### english speaking

| 順位 | アプリ名 | 提供者 | レビュー数 | 評価 | 価格 |
|---|---|---|---|---|---|
| 1 | English Speaking: SpeakFluent | Nguyen Thi Hoai Thu | 318 | 4.66 | 無料 |
| 2 | ELSA Speak - English Learning | ELSA, Corp. | 112,613 | 4.75 | 無料 |
| 3 | Learna: Speak & Learn English | DEEP FLOW SOFTWARE SERVICES | 400,966 | 4.64 | 無料 |
| 4 | English Speaking for Beginners | Xung Le | 6,474 | 4.69 | 無料 |
| 5 | Speak English with Loora AI | Loora A.I LTD | 38,645 | 4.90 | 無料 |
| 6 | HelloTalk | HELLOTALK... | 43,762 | 4.58 | 無料 |
| 7 | Duolingo | Duolingo, Inc | 5,445,732 | 4.72 | 無料 |
| 9 | Stimuler | STIMULER PRIVATE LIMITED | 7,946 | 4.82 | 無料 |
| 12 | LearnEnglish Grammar (UK) | British Council | 40,077 | 4.69 | 無料 |
| 15 | Speak: Language Learning | Speakeasy Labs, Inc | 60,143 | 4.83 | 無料 |
| 17 | EWA: Learn Languages | Lithium Lab Pte Ltd | 195,275 | 4.73 | 無料 |

### learn english

上位: Learna(400,966) / Duolingo(5,445,732) / EWA(195,275) / Babbel(753,289) / Busuu(100,711) / Falou(96,354) / British Council系 / HelloTalk(43,762) / LangLearn: AI English Tutor(20,423, 2025-04-22リリースの新規)。個人開発は上位20件中「Learn English US for Beginners」(Hector Gonzalez Linan, 1,224件)のみ。

### english conversation

「English Conversation: Episoden」(Episoden Inc., 32件, 2025-01-14リリース)のような小規模アプリが下位に入るが、上位はELSA(112,613)・British Council LearnEnglish Podcast(8,177)・Cambly(9,324)など。

### english vocabulary

Vocabulary by Monkey Taps(217,000) / Dictionary.com(327,810) / Duolingo(5,445,732) / EWA(195,275) が上位。British Council系も強い。

### speaking practice

ELSA(112,613)がトップ。Duolingo(5,445,732)、Speak(60,143)、BoldVoice(53,522)。個人開発では「Speaking Coach: Speaksure」(Muiz Redjepi, 1件, 2026-05-06)、「Orate: Practice Speaking」(James Yun, 2件, 2026-04-09)が最下位に見えるが、レビュー1桁は事実上圏外。

### english fluency

Duolingo(5,445,732)がトップ。ELSA(112,613)、Learna(400,966)、Loora AI(38,645)、Speak(60,143)が続く。

### talk english ai

Learna(400,966)、Loora AI(38,645)、ELSA(112,613)、Praktika(163,228)、Hablo(23,378)など「AI英会話」系スタートアップの密集地帯。個人開発の「English Ai - AI Learn English」(HELLOTALK名義、レビュー2件）のように、開発者名とアプリの実態が一致しない/流用アカウントと見られるものも混在。

### 占有率のまとめ（上位20件中の上位3社シェア、レビュー数ベース）

| クエリ | 収集件数 | レビュー合計 | 上位3社シェア | 100件未満 | 10万件以上 |
|---|---|---|---|---|---|
| english conversation | 18 | 203,942 | 80% | 5 | 1 |
| english fluency | 20 | 6,161,466 | 96% | 4 | 3 |
| english speaking | 18 | 6,415,577 | 94% | 1 | 4 |
| english vocabulary | 18 | 6,334,036 | 94% | 3 | 4 |
| learn english | 18 | 7,289,561 | 90% | 1 | 6 |
| speaking practice | 20 | 6,358,644 | 95% | 5 | 4 |
| talk english ai | 20 | 818,141 | 82% | 2 | 3 |

**主要7クエリの平均上位3社シェアは約90%。** これは「検索結果の質」というより、App Storeのランキングアルゴリズム自体がレビュー数・エンゲージメント・課金実績を強く重み付けしていることの帰結で、無名の新規アプリが広告なしで主要クエリの1ページ目に載る可能性は極めて低いと判断できる。

## 2. ロングテールの余地（試したクエリ全部）

`country=us`、上位20件で確認。**レビュー数100件未満のアプリが上位に多数出るクエリ**を中心に記載。

| クエリ | 収集件数 | 100件未満 | 先頭3件のレビュー数 | 所見 |
|---|---|---|---|---|
| shadowing english | 20 | 9 | 41 / 796 / 651 | **隙あり**。1位が41件。上位10件中6件が800件未満で個人・小規模開発者。ELSA(112,613)が6位に混入するが支配的ではない |
| english collocations | 18 | 11 | 0 / 7 / 276 | **隙あり**。1位が0件（未評価）。大手はDictionary.com(327,810)とOxford Dictionary(28,871)のみで、他は個人名義の0〜数百件アプリ |
| english idioms | 18 | 14 | 0 / 37 / 917 | **隙あり**。1位が0件。18件中14件が100件未満。大手の混入はSMERTRIOS社の1本のみ |
| phrasal verbs | 20 | 16 | 1,173 / 17 / 1,066 | **隙あり**。20件中16件が100件未満。大手は「Promova」(62,899件)が1本混じるのみで、残りはほぼ全て個人開発者（Vladimir Bayatov、Timofei Savin、Artem Taranukha等が複数アプリを出している） |
| business english speaking | 20 | 7 | 11 / 2 / 112,613 | 部分的に隙あり。1〜2位はレビュー1桁〜十数件の個人アプリだが、3位にELSAが入り以降も大手が混在 |
| ielts speaking practice | 20 | 5 | 342 / 1,192 / 517 | 部分的に隙あり。上位は数百件規模の専門アプリで大手ではないが、「無名」というほど新規でもない（2014〜2023年リリースが中心） |
| speaking anxiety | 20 | 9 | 6,730 / 4,888 / 10 | 隙は限定的。上位は不安症全般のアプリ（英語学習と無関係）が占め、英語特化の新規アプリ（ComposedAI等）は3位以降に低レビューで顔を出す程度 |
| english listening practice | 20 | 6 | 389 / 85 / 313 | 部分的に隙あり。上位が数百件規模の小規模アプリ中心だが、下位にLearnEnglish Podcast(8,177)等が控える |
| workplace english | 20 | 3 | 12,297 / 6 / 5,816 | 隙は薄い。1位はCLEVER APPSの汎用アプリ(12,297件)で、ニッチ専用アプリ(「English for Jobs」6件など)は2位止まり |
| english debate practice | 20 | 1 | 6,474 / 6,477 / 12,297 | 隙なし。専用アプリが存在せず、汎用の大手・準大手英会話アプリが「フォールバック」として表示されるだけ |
| english for introverts | 20 | 1 | 12,297 / 10,469 / 10,252 | 隙なし。同上、専用アプリが存在しない |
| english for parties | 19 | 4 | 6,477 / 6,647 / 3,216 | 隙なし。「party」に反応してPicoloのようなパーティゲームアプリが混入するなど、検索意図とズレる |
| english pronunciation practice | 19 | 2 | 112,613 / 4,693 / 18,631 | 隙なし。ELSAが完全に支配 |
| english small talk | 19 | 2 | 6,474 / 12,297 / 7,633 | 隙なし。専用アプリが存在せず汎用アプリのフォールバック |
| english storytelling practice | 20 | 1 | 6,474 / 12,297 / 6,477 | 隙なし。同上 |

**成果があった（隙が確認できた）クエリ: `shadowing english`、`english collocations`、`english idioms`、`phrasal verbs`。** いずれも「英語学習の中の特定の学習法・文法トピック」に対応するクエリで、大手汎用アプリがこの語で最適化していないためと考えられる。

**成果がなかった（隙が確認できなかった）クエリ: `english debate practice`、`english for introverts`、`english for parties`、`english pronunciation practice`、`english small talk`、`english storytelling practice`、`workplace english`。** これらは共通して「専用アプリが存在しない」ため、App Store側が関連性の低い汎用大手アプリをフォールバック表示している（＝需要はあってもニッチアプリの供給がない、または検索意図とマッチする語ではない）。

**部分的（大手が1〜2社だけ混入）: `business english speaking`、`ielts speaking practice`、`speaking anxiety`、`english listening practice`。**

## 3. 新規アプリの生存（直近2年以内リリースの分布）

上記の全22クエリ（主要7＋ロングテール15）で収集した結果を`trackId`で重複排除し、`releaseDate >= 2024-09-14`（今日から2年以内）で絞り込んだ59件のレビュー数分布。

| レビュー数帯 | 件数 | 割合 |
|---|---|---|
| 0件 | 12 | 20% |
| 1〜9件 | 15 | 25% |
| 10〜99件 | 12 | 20% |
| 100〜999件 | 10 | 17% |
| 1,000〜9,999件 | 7 | 12% |
| 1万件以上 | 3 | 5% |

**66%（39/59件）が100件未満。1万件以上に到達したのは3件のみ**（Learna 400,966件、LangLearn: AI English Tutor 20,423件、Gleam: Social Intelligence 10,204件）。いずれも資金調達を受けたAI系スタートアップの製品であり、個人開発者の単独プロジェクトが2年以内に1万件規模へ到達した例はこの調査では見つからなかった。

100〜999件に到達した新規アプリの例: Fluently(5,659件、法人)、Speak English: Lingo AI(4,555件)、Learning English with AI Tutor(4,938件)、Talko: Learn English with AI(1,420件、Soly Limited）、Daily Dictation English(1,530件、Huy Nguyen名義の個人)。個人名義で新規に1,000件前後まで到達した例としては Huy Nguyen の Daily Dictation English (1,530件、2024-07-03リリース) が該当する。

## 4. 個人開発者の例

セラー名が個人名（会社形態の記載がない）と推測できるものを抽出。特に**同一人物が複数の英語学習アプリを並行運営しているケース**が多数確認でき、依頼者の「複数アプリを出して当たったものを伸ばす」戦略と近い実例になっている。

| 開発者名（推定個人） | アプリ数（今回の収集内） | 最大レビュー数のアプリ | 備考 |
|---|---|---|---|
| Nguyen Thi Hoai Thu | 8本 | English Listening - 6mins (10,469件) | リスニング・発音・語彙・IELTS等、細分化された複数アプリを展開。レビュー数は58〜10,469件と幅広い |
| Loc Nguyen | 2本 | Pronuncian - English Pronounce (4,693件) | 発音とPhrasal Verbsの2本 |
| Timofei Savin | 2本 | IVERBS Irregular Verbs (3,279件) | 不規則動詞とPhrasal Verbsの2本、後者は2025年末リリースでまだ8件 |
| Xung Le | 1本（確認内） | English Speaking for Beginners (6,474件) | 単独アプリでも6千件規模に到達した数少ない例 |
| Steve Kim | 3本 | Speak English Conversation (522件) | いずれも数百件規模で頭打ち |
| Vladimir Bayatov | 4本 | English Phrasal Verbs Cards (1,066件) | Idioms/Phrasal Verbsのカード型アプリを複数展開 |
| Andie Nguyen | 3本 | Accent Training (11,059件) | アクセント訓練で1万件超えの例 |
| Phan Phuoc Luong | 2本 | English Collocations Master (157件) | Business English/Collocationsの2本、いずれも小規模 |
| Artem Taranukha | 2本 | Phrasal Verbs in Action (14件) | 2025年後半リリースの新規、まだ低レビュー |
| Bui Hoai Trang | 3本 | Dictionary of Collocations (3件) | Collocations関連を複数出すも全て0〜3件、伸びていない例 |

**示唆:** 個人開発者が英語学習アプリで一定規模（数千〜1万件のレビュー）に到達した例は実在するが、いずれも「文法・発音・語彙の特定トピックに特化したニッチアプリ」であり、主要クエリで競合する汎用アプリではない。また同一人物の複数アプリでも当たり外れの差が大きく（Nguyen Thi Hoai Thuの58件〜10,469件、Bui Hoai Trangの全滅など）、「数を出して当たりを伸ばす」戦略は成立し得るが再現性は高くない。

## 5. 国別の差

`english speaking`と`learn english`をUS/JP/INで比較（IN/JPは上位10件のみ取得）。

**JP（`english speaking`）:** 上位を日本語ローカライズされた資金力のあるアプリが占める。1位「AI英会話スピーク」(Speakeasy Labs, 77,082件)、2位「AI英会話スピークバディ」(SpeakBUDDY Ltd., 63,335件)、3位Duolingo(752,522件)、4位ELSA(62,755件)。個人開発の「English Speaking: SpeakFluent」(Nguyen Thi Hoai Thu)はUS版では318件だが、JP版では8件と極端に低く、日本語話者向けにローカライズされていない英語タイトルの英語学習アプリはJPストアでほぼ露出していないことが分かる。

**IN（`english speaking`）:** Learna(11,643)、Duolingo(205,133)、Stimuler(8,075、インド発のスタートアップ)、ELSA(15,486)、MySivi(18,906、インド発)など、US版よりレビュー絶対数は小さいが、インド発のAI英会話スタートアップが強く食い込んでいる。US版で318件だった「English Speaking: SpeakFluent」はIN版のトップ10には現れなかった（確認できず）。

**所見:** JPは「日本語ローカライズ＋資金力」の組み合わせが必須になっており、英語圏で戦うより参入障壁が高い可能性がある。INは絶対的なレビュー数が小さい分、相対的に新興プレイヤーが上位に来やすいが、それでもDuolingo・Learna・ELSAという同じ大手が必ず上位に入る点はUS/JPと共通していた。3カ国とも「無名の個人開発アプリが英語圏向け主要クエリの上位に出る」ケースは確認できなかった。

## 6. Google Play

Google Playストアページを直接curlで取得し、埋め込みJSON内の`"downloads"`表記（`ClM7O">値</div><div class="g1rdde">Downloads`パターン）を抽出。

| アプリ | パッケージ | インストール数 |
|---|---|---|
| Duolingo | com.duolingo | 500,000,000+ |
| Babbel | com.babbel.mobile.android.en | 50,000,000+ |
| Busuu | com.busuu.android.enc | 50,000,000+ |
| Codeway AI Tutor系 | com.codeway.aitutor | 10,000,000+ |
| HelloTalk | com.hellotalk | 10,000,000+ |
| Praktika | ai.praktika.android | 10,000,000+ |
| EWA | com.ewa.ewaapp | 10,000,000+ |
| Loora AI | com.loora.app | 10,000,000+ |
| TalkPal | ai.talkpal | 5,000,000+ |
| Lola Speak | com.lolaspeak.lolaspeak | 1,000,000+ |
| ELSA Coach（※別アプリの可能性） | com.fndworldllc.elsacoach | 500+ |

**所見:** App Storeのレビュー数ランキングと同様、Google Playでも主要アプリは数百万〜数億インストール規模。App StoreよりGoogle Playの方が母数が大きい（Androidの世界シェアが高いため）ぶん、絶対数の差はさらに開いている。ASOで戦うにはiOS/Android問わず同じ寡占構造に直面する。

なお「ELSA Speak」本体の正式なGoogle Playパッケージ名の特定は本調査では完了できなかった（`com.innovationbros.elsaspeak`は404）。`com.fndworldllc.elsacoach`（500+インストール）はELSA社とは無関係の別アプリの可能性が高く、参考値として扱う（グレーゾーン参照）。

## 7. ウェブのみで成立するか

- **WaniKani（日本語の漢字学習、月額課金SaaS型）**: iTunes Search APIで`term=wanikani`を検索した結果、44件がヒットしたが、いずれも"Tsurukame - For WaniKani"（David Sansome）、"Kakehashi - For WaniKani"（Pedro Ortego）、"Gakugame - WaniKani Companion"（Bold Flight LLC）、"KanjiMado for WaniKani"、"WK Stats"のような**サードパーティ製の非公式コンパニオンアプリのみ**で、WaniKani運営元（Tofugu）による公式アプリは存在しなかった。`term=tofugu`で検索しても同様に自社アプリはヒットしなかった。knowledge.wanikani.com のトップページには"The WaniKani Android App"「The WaniKani iOS App」というヘルプ記事タイトルが見えたが、記事本文までは確認できておらず、これが公式アプリなのかサードパーティアプリの紹介記事なのかは未確認（グレーゾーン）。**ただし少なくともApple/Tofugu名義の公式アプリがストアに存在しないことは一次データ（iTunes Search API）で確認できた。** WaniKaniはウェブブラウザ＋ユーザーコミュニティ製の非公式アプリのエコシステムのみで、月額課金のSaaS的英語（日本語）学習プロダクトとして長年運営されている実例と言える。
- **Clozemaster（多言語のCloze/穴埋め学習、Freemium）**: 公式サイト(WebFetch確認)に「Available on iOS and Android」の記載とストアバッジがあり、ウェブ版とネイティブアプリ版を両方公式に提供している。iTunes Search APIでも「Clozemaster－Vocabulary Builder」(Language Innovation LLC, 2,003件)がヒットした。課金は「基本無料＋Proプランで高度機能」のFreemium。**Clozemasterはウェブのみではなく、ウェブ+アプリのハイブリッド展開である**（依頼者の認識通り）。

**示唆:** 「アプリストアに依存しない」という選択は、WaniKaniのように強いコミュニティ・口コミ経路（Reddit、YouTube等の学習者コミュニティでの言及）を持つニッチな学習SaaSでは成立し得る。ただし WaniKani は日本語学習という、英会話よりもさらに専門性の高い・競合の少ない領域であり、かつ10年以上の運営実績とコミュニティの厚みを前提にしている点には注意が必要（英語学習という一般性の高い領域で同じことが再現できるかは未検証）。

## グレーゾーン・未確認

- ELSA Speak本体の正式なGoogle Playパッケージ名を特定できず、Google Play側のインストール数を直接確認できなかった。`com.fndworldllc.elsacoach`（500+）は別アプリの可能性が高く参考値にとどめる。
- 「新規アプリ」の判定に使った`releaseDate`はストア初回登録日であり、実際のマーケティング開始時期やリブランド・大型アップデートのタイミングとは一致しない可能性がある（例: 大幅リニューアルで実質的に「新規扱い」になったアプリを古い`releaseDate`のまま集計している可能性）。
- iTunes Search APIの`term`検索結果は、必ずしも実際にユーザーがApp Store内検索窓に入力した際の検索結果ランキングと完全に一致するとは限らない（検索APIとストア内検索アルゴリズムは異なる可能性がある）。本調査はAPI経由の結果を代理指標として扱っている。
- WaniKaniのiOS/Androidアプリに関するknowledge.wanikani.comの記事本文（"The WaniKani iOS App"等）は未読了で、公式アプリの有無について確定的な一次情報は得られていない。iTunes Search APIでの非公式アプリのみのヒットは強い傍証だが、100%の確証ではない。
- Google Playの`downloads`表記はレンジ表示（例: `10,000,000+`）であり、実数ではない。App Storeのレビュー数と単純比較できない（レビュー率は通常インストール数の1〜数%程度とされるが、本調査では検証していない）。
- 個人開発者と推定した名義（例: Nguyen Thi Hoai Thu、Loc Nguyen等）が実際に単独個人か、小規模スタジオ/外注チームかは、セラー名からの推測であり確認していない。ベトナム語圏の個人名パターンが多いことから小規模開発者である可能性は高いと考えるが、法人登記の確認はしていない。
- 広告費（Apple Search Ads等）をかけた場合の露出可能性は本調査の範囲外（オーガニック検索結果のみを調査した）。

## 影響する論点

- `docs/plan/english-saas-venture/open-questions.md` の「ウェブアプリかモバイルアプリか」の論点に対し、ASO単独でのオーガニック流入は主要クエリでは期待薄、ロングテール（文法・語彙トピック特化）でのみ現実的な余地があるという材料を提供する。
- 「複数アプリを出して当たったものを伸ばす」戦略の実例（個人開発者の複数アプリ展開）と、その再現性の低さ（当たり外れの差が大きい）を示す材料になる。
- ウェブオンリー運営の選択肢について、WaniKani・Clozemasterの実例を判断材料として提供する。ただし英語学習という一般性の高い領域での再現性は未検証。

## メインセッションによる追検証（2026-09-14）

サブエージェントが「隙がある」と判定した `english collocations` を、メインセッションが iTunes Search API
（`https://itunes.apple.com/search?term=english%20collocations&entity=software&country=us&limit=20`）で直接叩いて確認した。

**結果: サブエージェントの観測は正しい。** 上位 18 件（全結果が 18 件）のレビュー数は次の通り。

| レビュー数 | 評価 | アプリ名 | 提供者 |
| --- | --- | --- | --- |
| 0 | - | English Collocation In Use | Hoa Nguyen Quang |
| 7 | 4.7 | English Collocation Dictionary | Trung Huynh |
| 276 | 4.8 | English Collocations for IELTS | Nguyen Thi Hoai Thu |
| 157 | 4.8 | English Collocations Master | Phan Phuoc Luong |
| 0 | - | English Collocation Sentence | Bui Hoai Trang |
| 0 | - | English Collocations By Topics | Huong Nguyen |
| 0 | - | Lexiglu: English Collocations | Andrea Quadrelli |
| 661 | 4.8 | IELTS Collocation PRO | Nguyen Thi Hoai Thu |
| 2208 | 4.7 | English Dictionary - LDOCE PRO | Nguyen Thi Hoai Thu |
| 327810 | 4.8 | Dictionary.com: English Words | Curiosity Media, Inc. |

確度: 高（メインセッションが API を直接実行。2026-09-14 取得）

### ただし解釈に重大な留保（メインセッションの指摘）

**「大手がいない」ことは「隙がある」ことを意味しない。** 同じデータは次のようにも読める。

- **全結果が 18 件しかない。** 大手が最適化していないのではなく、**そもそも検索されていない語**である可能性が高い。
- 個人開発アプリの最高到達点が 276 レビュー（コロケーション専用アプリとして）。これは
  「参入すればここまで行ける」ではなく「**このニッチの天井がここ**」と読むほうが自然。
- 需要のない場所に空きがあるのは当然であり、それは参入余地ではない。
- **本調査では検索ボリュームを一切測っていない。** iTunes Search API はボリュームを返さない。
  「隙があった」と判定した 4 クエリ（`shadowing english` / `english collocations` /
  `english idioms` / `phrasal verbs`）すべてに同じ留保がかかる。**これは未解決の穴。**

### 副次的な発見: 複数アプリ戦略の実在例

`Nguyen Thi Hoai Thu` は同一提供者名で複数アプリを出しており、上記クエリだけで 3 本
（276 / 661 / 2208 レビュー）が確認できた。`decisions.md` 2026-09-14「複数アプリを出して
当たったものを伸ばす」と同じ戦略を実行している例。ただしこの提供者の総本数・収益は未確認。
