# 汎用AI時代に英語学習プロダクトへ課金が発生し続けている理由 ―「代替されない線」の検証

- 調査日: 2026-09-14
- 調査手段: Sonnet サブエージェント4体（並列・WebSearch枯渇のためWebFetch中心） + メインセッションによる原典確認（ELSA Speak公式サイトを直接WebFetch）
- 問い: ChatGPT / Claude のような汎用AIが誰でも無料〜安価に使える2026年に、それでも人が別途金を払っている英語学習プロダクトは何か。そこにある「代替されない線」は何か。

このファイルは「汎用AIに何ができるか」の調査ではなく、**「汎用AIがあってもなお課金が発生している事実」を集める調査**である。個人開発・少人数開発の収益化事例そのものについては、同じアイデアディレクトリの既存調査 [`research/indie-saas-track-record.md`](./indie-saas-track-record.md) がすでに13件のケースを扱っているため、本ファイルでは重複を避け、必要な範囲でのみ参照する。

---

## 結論（15行以内サマリー）

1. 「なぜChatGPTではなくこのアプリか」を**製品側が明示的な比較文言で答えているケースはほぼ皆無**だった。調査した13製品の公式サイト・ブログのうち、ChatGPTを名指しして比較した文言は1件も見つからなかった。
2. 差分は「言葉で主張する」のではなく「**事業構造として体現する**」形で存在する。もっとも強く裏付けられたのは、人間講師・添削者を仲介するマーケットプレイス型（italki, Preply, Cambly, Lingoda）と、コーチング特化AI（Yoodli）が「AIは人を置き換えず支援する」と明言し、資金調達・黒字化で生存を続けている事実。
3. 反対に、汎用チャットに近いポジショニングの製品（Duolingo Max）はユーザーから「Duolingoは実質ChatGPTの中間業者」という辛辣な評価を受け、実際に解約者の声が複数見つかった。
4. SRS（間隔反復）・記憶管理を軸にした小規模プロダクト（Anki, WaniKani, Bunpro）は、ChatGPT時代でも生存を続けている（indie-saas-track-record.mdで確認済み）。ユーザー自身が「チューターの不足点は指導の質ではなくスケジュール管理と誤り追跡だった」と語る一次証言もあり、この線は個人開発でも狙える規模感で裏付けが取れた。
5. 発音評価AI（ELSA等）は「あなたの声に合わせたリアルタイムAIフィードバック」を主張するが、ChatGPTとの直接比較や第三者検証は見つからず、支持材料は弱い。
6. 解約・衰退の証拠は主にDuolingoに集中している。「AI-first」方針発表後の解約表明が複数のHNコメントで一次証言として確認でき、10-K（有価証券報告書）自体がAIを競合リスクとして明記している。他社（Babbel, Rosetta Stone, Mondly等）の同種の証拠は見つからなかった。
7. 反証（差は幻想で惰性とマーケ予算で生きているだけ）を支持する声もHN上に複数見つかった。「Duolingoは千個のChatGPTラッパーに置き換え可能」「Grammarlyの差別化はブラウザ拡張で模倣できるUX問題に過ぎない」という主張である。
8. ただし同時に、Preply（2026年1月ユニコーン到達）、Yoodli（評価額半年で3倍・$300M超）、Speak（$1B評価額）のように**ChatGPT/Claude普及後も大型資金調達・黒字化を続けている企業が複数存在**しており、「全て惰性」という反証を無条件には支持できない。
9. ユーザーの生の声は課金継続側5件、解約側8件の計13件を一次引用で確認。解約側の多くはDuolingoに集中し、課金継続側は人間講師サービス（italki等）とハイブリッド利用（人間+ChatGPT併用）に集中していた。
10. 個人開発者が賭けるべき線は「人間が絡む」（最も強く裏付けられたが個人には運用負荷が高い）ではなく、**「学習スケジュールと記憶の管理（SRS/継続の仕組み）」**である（確度: 中）。詳細は末尾参照。

---

## 製品一覧

自己申告の価格・ユーザー数は各社発表。第三者検証があるものは確度を「高」寄りにしている。

| 製品 | 価格 | 主張する差分（原文引用） | 出典URL | 出典日付 | 確度 |
|---|---|---|---|---|---|
| Speak | 月$17.99〜$39.99、年$83.99〜$164.99（App Store実価格、地域差あり） | "Structure vs. open-ended chat," "Feedback built for language learners," "Personalization over time"。ChatGPTとの直接比較はなく「OpenAI Startup Fund出資・正式提携」を強調 | https://www.speak.com | 2026-09-14 | 中〜高 |
| ELSA Speak | 月$19.99、年$99.99〜$129.99（App Store実価格） | "Get real-time, AI-powered feedback tuned to your voice - so you know exactly what to improve and how" | https://elsaspeak.com/en | 2026-09-14 | 中（メインセッションが直接WebFetch確認） |
| Praktika | 月$9.99〜、年$39.99〜$139.99（App Store実価格）。公式は「月$8程度 vs 人間チューター月$400」と比較訴求 | "Private language tutor quality. App convenience." "Private-tutor results without the private-tutor price" | https://praktika.ai | 2026-09-14 | 中 |
| TalkPal | 月$19.99、3ヶ月$49.99、年$119.99（App Store実価格） | "Unlike other language learning apps, Talkpal uses the most advanced AI..."。自己記述は「a GPT-powered AI language tutor」 | https://www.talkpal.ai | 2026-09-14 | 中 |
| Loora | 月$14.99〜$19.99、年$59.99〜$119.99（App Store実価格） | "Unlock your full potential with your very own AI English tutor"。人間チューター1時間より安いと訴求するのみで具体額なし | https://loora.com | 2026-09-14 | 低〜中 |
| Duolingo Max | Super系サブスク月$9.99〜$12.99、年$79.99〜$119.99（Max単独SKUはApp Storeで特定できず） | "we've spent months collaborating closely with OpenAI to test and train this technology"。人間監修を強調するが差別化文言としては弱い | https://blog.duolingo.com/duolingo-max/ | 2026-09-14 | 中 |
| Pimsleur | Premium月$19.95、All Access月$20.95（非公式ソース経由、直接確認できず） | "No other language learning app puts as many possibilities in play as Pimsleur!"（Pimsleur Method™という独自メソッドを訴求。他アプリとの比較のみでChatGPT比較なし） | https://www.pimsleur.com/how-it-works | 2026-09-14 | 低〜中 |
| Lingoda | グループ5コマ€169.99〜、プライベート5コマ€11.99/コマ〜（ユーロ建て） | "Every small-group and private class is led by a native-level teacher who...uses AI insights to deliver a tailored learning experience."（AIは自習教材の補助のみ、人間講師が主役） | https://www.lingoda.com/en/prices | 2026-09-14 | 高 |
| italki | 固定サブスクなし。講師単価$4〜$60/時間 | **"Tired of app learning? Speak with a native teacher"**（アプリ学習疲れを想起させ人間講師へ誘導する、本調査で最もChatGPT差別化に近い文言） | https://www.italki.com/en | 2026-09-14 | 高 |
| Preply | 具体額は確認できず（見つからなかった） | "Receive immediate, personalized feedback from an experienced tutor"。AIはレッスン間の復習補助として併用する位置づけ | https://preply.com/en/ | 2026-09-14 | 中 |
| Cambly | Small Groups月$17〜$24、Private+月$39〜$56、Pro月$56〜$80 | "100% native English speaking tutors"。ChatGPT等との明示比較なし | https://www.cambly.com/english | 2026-09-14 | 高 |
| Yoodli | Pro月$8、Advanced月$20（年払い時） | "Improve your communication skills with private, real-time, and judgment-free roleplay coaching — powered by AI."　CEO発言: "AI built to assist, not replace, people" | https://yoodli.ai/pricing、https://techcrunch.com/2025/12/05/... | 2026-09-14 | 高 |
| Grammarly（→Superhuman） | Free $0、Pro 月$12 | "The name Superhuman reflects our belief that AI should amplify human capability, not replace it or force people to adapt to its limitations."（CEO Shishir Mehrotra、社名変更発表） | https://www.grammarly.com/plans、https://www.grammarly.com/blog/company/announcing-company-rebrand-to-superhuman/ | 2025-10-29 | 高 |

補足: 個人開発の小規模プロダクト（Anki, WaniKani, Bunpro, Gliglish, Englister等）は [`indie-saas-track-record.md`](./indie-saas-track-record.md) にすでに一覧化されているためここでは重複掲載しない。特にAnkiMobile（"唯一の収入源"）、WaniKani（約10人チーム）、Bunpro（約21人）はSRS/記憶管理を軸にChatGPT時代でも生存を続けている点が本調査の仮説検証（下記）に直接関係する。

---

## 「代替されない線」の仮説別の検証結果

### 1. 発音・音声の評価（ELSA等）
**判定: 未確認**
ELSA Speakは「あなたの声に合わせたリアルタイムAIフィードバック」を公式サイトで主張するが、ChatGPTの音声モードとの直接比較文言（FAQ・ブログ含む）は見つからなかった。ユーザーの生の声でも発音評価そのものを主題にした課金継続/解約の発言は見つからなかった（見つかったのは主に文法説明・会話練習に関する発言）。「ChatGPTは構造化された発音スコアリングをしない」という技術的な妥当性はある仮説だが、それを裏付ける一次資料（ユーザー比較レビュー、第三者ベンチマーク）は本調査の範囲では発見できなかった。

### 2. 学習スケジュールと記憶の管理（SRS、進捗、継続の仕組み）
**判定: 支持**
- indie-saas-track-record.mdで確認済みの通り、Anki（"Ankiデスクトップ版込みで唯一の収入源"）、WaniKani（約10人チーム）、Bunpro（約21人）はSRSを軸にした製品として、ChatGPT時代でも有料課金を維持し続けている。
- 個人開発者Alex Shelaevの実名ブログ（2026年、[alshe.substack.com](https://alshe.substack.com/p/i-canceled-my-french-tutor-and-built)）は、月$200の人間チューターを解約した理由として「指導の質」ではなく「復習スケジュールの甘さと誤り追跡の欠如」という**構造的な2点**を明言し、自作のLLM+SRSシステム（1セッション約$0.04）に切り替えたと書いている。これは「スケジュール管理・記憶の仕組み」こそが単発のChatGPT対話にはない付加価値であることを、実例として裏付けている。
- ただし本人はこのニーズを「アプリへの課金」ではなく「自作」で解決しており、"だから個人開発者に課金機会がある"と単純に読み替えるにはグレーゾーンが残る（下記参照）。

### 3. 人間が絡む（講師・コミュニティ・添削者）
**判定: 支持（最も強い裏付け）**
- italki公式の "Tired of app learning? Speak with a native teacher" は、アプリ的な学習（AI含む）への疲労感を逆手に取る、本調査で見つかった中で最もChatGPTへの間接的対抗軸が明確な文言。
- Preplyは2026年1月にユニコーン到達（Series D $150M、TechCrunch確認）、12ヶ月連続EBITDA黒字化。
- Yoodli CEO: "AI built to assist, not replace, people"（2025年12月、評価額$300M超・半年で3倍）。
- ユーザーの生の声: emursebrian「人間的・感情的つながりはAIには簡単には再現されない」、bricee98「iTalkiの人間講師と同水準の正確性・信頼性がなければ乗り換えない」、dragontamer「ドイツ語学習コミュニティではLLMのハルシネーションに苛立ち、教師の方が教えるのが上手いという意見が大勢」、bidder33「ChatGPTは会話練習には良いが基礎固めには人間チューターが必要」。
- 反証: zkid18は「Italki/Preplyのような講師仲介プラットフォームは構造化された学習パスがなく、ChatGPTの方が自分でプログラムを組める」と述べ、**人間講師であること自体は十分条件ではない**ことも示している（構造化の欠如が不満の核）。

### 4. 教材そのものの品質・体系（カリキュラム、レベル設計）
**判定: 混在（未確認寄り）**
- 支持材料: Pimsleurは独自メソッド（Pimsleur Method™）を訴求し、他アプリとの比較で優位性を主張（ChatGPTとの比較ではない）。dragontamer「30ユーロ・40ドルの体系立ったリスニング/スピーキングテスト付き教科書の方がどんなLLMサブスクよりずっと良い」という一次証言あり。
- 反証材料: zkid18は逆に「ChatGPTの方が自分の学習プログラムを組み立てやすい」と述べており、体系化された教材がChatGPT側にも作れてしまうケースがあることを示す。
- 総じて「教材の体系」単体が独立した差別化線として機能しているかは、証拠が両方向に分かれておりはっきりしない。

### 5. 摩擦の無さ（開くだけで始まる、設定が要らない、プロンプトを書かなくていい）
**判定: 未確認（むしろ弱い反証あり）**
この仮説を直接支持する一次証言は見つからなかった。逆にDuolingo Maxに関するTrustpilotレビュー（Jonathan、2025-05-14）は "Pro tip: ChatGPT (their AI) is free, so you can get around Max by having both open and being willing to type a little." と述べており、**ユーザーは多少の摩擦（タイピングの手間）を許容してでも無料のChatGPTを選ぶ**行動が確認できた。摩擦の少なさだけでは課金継続の決め手にならない可能性を示唆する（確定的な反証ではないため「未確認」寄りの判定とする）。

### 6. 責任・保証（試験スコア保証など）
**判定: 見つからなかった**
調査した13製品のいずれについても、スコア保証・返金保証等の「責任・保証」を差別化軸として掲げる文言は公式サイト上で見つからなかった。この仮説を積極的に支持する証拠も反証する証拠も本調査の範囲では得られなかった。

### 7. 記録が溜まって資産になる
**判定: 不支持寄り（反証あり）**
Duolingoの「AI-first」方針発表（2025年4月）への反発を示すHNコメントの中に、ユーザーkrowekの一次発言がある: "I've just uninstalled the app and deleted the account... after having used Duolingo for years (almost 2000 days streak)"。約2000日（5年超）分のストリーク（学習継続記録という蓄積資産）を持つユーザーが、それでも方針への不満を理由にアカウントごと削除している。これは「記録の蓄積」が強力な解約防止バリアとして機能しなかった具体例であり、この仮説への反証として扱う。他に「記録の蓄積を理由に課金継続している」という一次証言は見つからなかった。

---

## ユーザーの生の声

原文はサブエージェントが実際にHacker News全文検索API・Trustpilotから取得したもの。合計13件（課金継続5件・解約側8件）。

### 課金継続側（抜粋、詳細は上記仮説検証内でも引用）

> "i still think a human tutor is required for foundations but gpt is very helpful for practice."
— bidder33, Hacker News (2024-01-09) https://news.ycombinator.com/item?id=38920768 ／確度: 高

> "replacing the human and emotional connection with a person isn't something that will be easily replicated (or at all!) with AI."
— emursebrian, Hacker News (2024-01-30) https://news.ycombinator.com/item?id=39194764 ／確度: 高（ただし本人は語学学習スタートアップ創業者でバイアスあり）

> "Most of the German discord group is mostly annoyed at how awful LLM explanations and hallucinations are... most seem to agree that the 30EUR or $40 textbooks with well organized listening/speaking tests are leagues better than any LLM subscription."
— dragontamer, Hacker News (2026-06-22) https://news.ycombinator.com/item?id=48632115 ／確度: 中（伝聞の集約）

### 解約側（抜粋）

> "I canceled Duolingo subscription in favor of just using ChatGPT. Duolingo wanted $30 (a $20 increase) for Max, which is as far as I can tell less flexible and capable than ChatGPT anyway."
— distortionfield, Hacker News (2024-01-08) https://news.ycombinator.com/item?id=38919824 ／確度: 高

> "Now I use ChatGPT and is does a great job. My experience with DuoLingo is it's barely better than flash cards for language learning, and it's no wonder they're having a hard time making any money offering a product thats competition is cheaper"
— gtmitchell, Hacker News (2024-01-08) https://news.ycombinator.com/item?id=38919185 ／確度: 高

> "I've just uninstalled the app and deleted the account... after having used Duolingo for years (almost 2000 days streak)"
— krowek, Hacker News (2025-04-29) https://news.ycombinator.com/item?id=43827978 ／確度: 高

> "Pro tip: ChatGPT (their AI) is free, so you can get around Max by having both open and being willing to type a little."
— Jonathan, Trustpilot Duolingoレビュー (2025-05-14) https://www.trustpilot.com/review/www.duolingo.com ／確度: 高

> "After trying both Italki and Preply a few times, I realized that I don't like tutoring platforms because they lack a structured approach to learning a language... I like how I can craft my own program and learning path in ChatGPT"
— zkid18, Hacker News (2024-01-30) https://news.ycombinator.com/item?id=39190591 ／確度: 高

（残り6件は上記の仮説検証セクション内、およびサブエージェント原報告に記載。全件がDuolingo関連発言に偏っており、Speak/ELSA/Praktika/Cambly固有の「なぜ金を払うか/なぜ解約したか」の発言はTrustpilot検索で該当ゼロだった点をグレーゾーンとして明記する）

---

## 解約・衰退の証拠

- **Duolingoの株価急落（2025年8月）**: OpenAIのGPT-5デモ（研究者がその場で簡易な語学学習ツールを構築）直後にDuolingo株が2025年5月高値$529.05から38%下落したと報道。Duolingo自身の10-K（有価証券報告書）に "It is possible that a new product could gain rapid scale at the expense of existing brands through harnessing a new technology (such as generative AI)." という記載あり。出典: https://yro.slashdot.org/story/25/08/17/194212/ (2025-08-17)／確度: 高（株価変動と10-K記載の事実は検証可能、因果の断定は報道側の解釈）。
- **Duolingo「AI-first」方針発表後の解約表明（2025年4-6月）**: 前述のkrowek, distortionfield, i80and, awalGarg, rmvt, spaceywilly等、複数のHNユーザーが実際の解約・アンインストールを一次証言として述べている。ただしこれは特定コミュニティのコメント欄の自己申告集積であり、企業側の公式な解約者数データではない。
- **Grammarlyのレイオフ（2024年2月）**: 230名解雇。HN上では複数ユーザーがChatGPT/LLM普及と結びつけて語っているが、企業側は因果を明言していない（確度: 中、レイオフ自体は事実だが原因の帰属は推測）。
- **Grammarly→Superhumanへの事業転換（2025年10月）**: 単体の文法チェッカーからAIエージェント/生産性プラットフォームへの急速なピボット。$1Bの非希薄化資金調達（2025年5月）の記事内で「2021年の評価額$13Bに対し、現在の市場での評価額は大幅に低いと考えられる」という指摘があった（TechCrunch、確度: 高＝資金調達の事実、評価額低下は記事内の指摘で確度中）。
- **見つからなかったもの**: Babbel, Rosetta Stone, Mondly, Memrise, Busuu, Pimsleur, Cambly, Lingoda, italki等について、「ChatGPT普及後のレイオフ・値下げ・サービス終了」を直接報じる一次資料は発見できなかった。Sensor Tower等によるダウンロード数の独立した定量分析も見つからなかった。

---

## 反証（差分は幻想で、惰性とマーケティング予算で生き残っているだけという見方）

HN上で複数のユーザーが以下のように主張している（いずれも匿名掲示板の個人的見解であり、業界分析ではない点に注意）：

> "Not a whole lot stopping Duolingo to be replaced entirely by a thousand ChatGPt wrappers"
— nextworddev, Hacker News (2025-04-29) https://news.ycombinator.com/item?id=43827978

> "We all have access to LLMs, so why do we need a middleman like DuoLingo taking the output of an LLM and cluttering it up with irrelevant ads?"
— trollbridge, Hacker News (2025-04-29) 同上

> "'AI-first' just seems like a dog-whistle for 'we're struggling to figure out how to grow so we're going to cut labor and make it seem like innovation'."
— boh, Hacker News (2025-04-29) 同上

> Grammarlyの差別化についての反論: "Sounds like a UX problem that's trivial to solve with a browser plugin." （diegof79のGrammarly擁護コメントへの反論、user: BossingAround） 加えて "Deepl Write is also rock solid and free."（nicbou）、"LanguageTool has a free version and a self-hostable version."（jamil7）
— Hacker News (2024-02-07) https://news.ycombinator.com/item?id=39295962

**この反証への留保**: 同じ調査の中で、Preply（ユニコーン到達・EBITDA黒字化）、Yoodli（評価額半年で3倍）、Speak（評価額$1B）のように、ChatGPT/Claude普及後も大型資金調達・黒字化を続けている企業が複数見つかっている。「全ては惰性とマーケ予算」という反証は、少なくともこれら3社については資金調達実績・黒字化という定量的な反証材料と矛盾する。反証はDuolingoとGrammarlyという「汎用AIに近いポジショニングだった2社」に偏って見つかっており、人間仲介型・専門特化型の企業には同種の反証が見当たらなかった点は重要な非対称性である。

---

## グレーゾーン・未確認

- **WebSearchはこのセッション全体でクォータ上限（200/200）に達しており、4体のサブエージェントいずれも1回も使用できなかった**。全調査はWebFetch（公式サイト直接アクセス、HN Algolia検索API、Trustpilotのsearchパラメータ、Bing検索結果ページ経由）で代替した。
- **Reddit（r/languagelearning, r/EnglishLearning, r/ChatGPT）は全経路で遮断された**。直接のReddit JSON API、代替フロントエンド（Redlib等5インスタンス）、WebFetch経由のいずれも403またはCloudflareチャレンジで失敗。これは本調査の最大の欠落であり、「ユーザーの生の声」がHacker News（技術者コミュニティに偏る）とTrustpilot（Duolingoにほぼ限定）に依存する結果となった。一般学習者層・非エンジニア層の声はほぼ拾えていない。
- **DuckDuckGo・archive.is/Wayback Machineも全経路でブロック**（CAPTCHA、bot対策、フェッチ拒否）。
- Preply, Loora, Praktika, TalkPal, Pimsleurの具体的な価格・資金調達額の一部は公式ページが404またはJSレンダリングのため直接確認できず、App Store実売価格や非公式ソース、Bing検索スニペット経由の間接情報に依存している。
- Duolingo Maxの単独価格（App Store上のSKU特定）はできなかった。Super系サブスクのいずれがMaxに対応するか不明。
- 「発音評価」「摩擦の無さ」「責任・保証」「記録の資産化」の4仮説は、直接的な一次証言・公式文言による裏付けが薄く、いずれも「未確認」または弱い反証にとどまる。これは調査範囲の限界であり、証拠が存在しないことの証明にはならない。
- ChatGPT音声モード普及がAI英会話スタートアップの成長を明確に阻害したと断定する一次情報は見つからなかった（indie-saas-track-record.mdでも同様の結論）。むしろSpeak, Praktika, Yoodliは音声モード登場後も大型資金調達を継続している。

---

## 影響する論点

この結果は `docs/plan/english-saas-venture/open-questions.md`（未読の場合は要確認）および今後の `experience.md` / `assessing-ai-architecture` の検討で、「英語学習プロダクトの中核体験をどこに置くか」の判断材料として使う。特に:
- 「人間が絡む」線は最も裏付けが強いが、個人開発者が単独で講師マーケットプレイス（italki/Preply/Cambly型）を運営するのは供給側（講師調達）・信頼性担保・決済等の運用負荷が高く、indie-saas-track-record.mdの調査結果（個人開発でマーケットプレイス型の成功事例は見つからなかった）とも整合する。
- 「学習スケジュールと記憶の管理（SRS）」線は、個人開発の実例（Anki, WaniKani, Bunpro）がすでに存在し、運用負荷も比較的小さく、本調査で新たに見つかった一次証言（Alex Shelaevのブログ）とも整合する。

---

## 個人開発者が賭けるべき「線」の判定（確度: 中）

**推奨: 「学習スケジュールと記憶の管理（SRS・継続の仕組み）」に賭けるべきである。**

理由: 「人間が絡む」仮説は本調査の中で最も強く裏付けられた線であり（italkiの明示的な訴求文言、Preply・Yoodliの資金調達・黒字化実績、複数の一次ユーザー証言）、単体で見れば最有力候補に見える。しかし個人開発者の実行可能性という制約を重ねると評価が変わる。人間仲介型は供給側（講師の調達・審査・継続的なマッチング）と信頼性の担保が事業の中核であり、これはコード一本で解決できる問題ではなく、同じ調査領域（indie-saas-track-record.md）でも個人開発による成功事例が見つかっていない。一方、SRS・記憶管理の線は、(a) ChatGPT時代でも生存を続ける個人・少人数開発の実例（Anki, WaniKani, Bunpro）がすでに存在し、(b) 「チューターの不足点は指導の質ではなくスケジュール管理と誤り追跡だった」という一次証言（Alex Shelaevのブログ）によって、単発のAI対話では埋まらない構造的なニーズであることが裏付けられており、(c) 個人開発でも実装可能な規模の問題である。ただし、この推奨の確度を「中」にとどめる理由は、Shelaev氏自身がこのニーズを「アプリへの課金」ではなく「自作」で解決した点――つまり、この線が「個人開発者にとって作りやすい」ことと「ユーザーがそれに金を払い続ける」ことは必ずしもイコールではなく、無料・自作で代替されるリスクも同じ調査から見えている――にある。したがって、この線を選ぶ場合は「スケジュール管理・記憶定着の質」そのものを差別化の核に据えつつ、人間的要素（コミュニティ、添削、フィードバックの温度感）を小さくでも組み合わせるハイブリッド設計が、単独の「SRSアプリ」よりも解約耐性が高い可能性がある（この複合仮説自体は本調査では検証していない、次の検討ステップとして残す）。
