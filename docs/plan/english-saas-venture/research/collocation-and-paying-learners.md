# コロケーション学習のニーズと、語学学習者の支払い行動（Reddit 直接観察 + 公式サイト確認）

- 調査日: 2026-09-14
- 調査手段: **メインセッションが Claude in Chrome でユーザーの実 Chrome から Reddit を直接閲覧**（WebFetch / Reddit JSON は 403、WebSearch はクォータ枯渇）。加えて Clozemaster 公式サイトを直接閲覧。
- 問い: (1) コロケーションで詰まっている学習者の声は実在するか。既存製品はあるか。(2) 語学学習者は実際に有料アプリに金を払っているか。

## 結論

**(1) 「コロケーション」という語でのニーズは薄い。ただし同じ痛みが別の言葉で大量に語られている。**
r/EnglishLearning で "collocations" を検索すると、ヒットするスレッドは 3 votes / 1 vote 級で、多くが 4〜14 年前。
一方「これは自然に聞こえるか」系のスレッドは新しく、コメントが 31 / 45 / 73 / 310 件と桁違いに多い。
**学習者はこの痛みを「コロケーション」とは呼んでいない。「does this sound natural?」と呼んでいる。**

**(2) 支払い行動は、セグメントによって正反対だった。これは前回の Reddit 調査の結論を修正する。**
`user-needs/reddit-direct-observation.md` では r/developersIndia で「有料アプリの推薦ゼロ」を観測した。
しかし r/languagelearning の熱心な学習者層では、**複数の有料アプリに金を払う行動が明確に観測された**。
つまり「語学学習者は金を払わない」のではなく、**払う層と払わない層がはっきり分かれている**。

## 根拠（原文引用）

### A. コロケーションの痛み、およびコミュニティの通念（この線にとって最大の逆風）

1. 投稿者（2 年前、r/EnglishLearning、33 コメント）:
   「the basic collocations are very easy to know because everyone uses it, but the advanced ones, i think it's very hard」
   - URL: https://www.reddit.com/r/EnglishLearning/comments/1is80ws/how_do_you_know_the_collocations_you_use_are/
   - 確度: 高（メインセッション直接閲覧）

2. **同スレッドの最上位回答（逆風の核心）**:
   「There's no good way to predict or detect them; one must merely get familiar with them by practice. **You can in limited ways enhance this with vocabulary lists/cards/etc. to teach yourself explicitly, but that's not sustainable in practice over the long term except for the more frequent ones.**」
   - URL: 同上、確度: 高
   - **注: コミュニティ自身が「カードで明示的に覚えるのは長期的に持続しない」と言っている。** 今回賭ける線（SRS でコロケーションを回す）への直接の反証。

3. 別の回答: 「There is no rulebook for these... Unfortunately there is no way to know these things without consuming literature/media/conversation.」
   - URL: 同上、確度: 高

4. 用語のミスマッチ（検索結果の比較、2026-09-14 時点の r/EnglishLearning）:
   - "collocations" 系スレッド: 3 votes/33 comments（2 年前）、1 vote/4 comments、5 votes/4 comments（14 年前）など少数・古い
   - 「自然に聞こえるか」系: 「Which one sound natural?」73 コメント（5 ヶ月前）、「Does it sound natural for natives?」45 コメント、「Do Native Speakers Know These Words?」224 votes/310 コメント（5 ヶ月前）
   - 確度: 高（検索結果の件数表示を直接確認）

### B. 支払い行動の実在（前回の観測を修正する材料）

5. r/languagelearning の 8 年・27 アプリのレビュー投稿（384 votes / 166 comments、10 ヶ月前）。
   投稿者は **6 つのアプリについて「I paid for this app」と明記**（Clozemaster、Conjugato、Mimic Method、Beelinguapp、Fluent Forever、Tandem）。
   - URL: https://www.reddit.com/r/languagelearning/comments/1p6ivuu/ive_used_27_appsprograms_in_8_years_of_language/
   - 確度: 高（メインセッション直接閲覧）

6. 同投稿の結論部（狭いプロダクトの正当化として重要）:
   「KEY POINT: No one app is your magic bullet. None... **They're all good at some narrow slice of the process, and you still have to build your own mix around them.**」
   - URL: 同上、確度: 高
   - 注: **熱心な学習者は「狭い道具」を複数買うことを前提にしている。** 個人開発が「1 機能だけの製品」を出すことは、この層では欠点ではない。

7. 無料 Anki の重力（逆風）:
   「i'll check it out. but **going to be really hard to compete with anki**」（投稿者自身のコメント）
   「Anki is superior in all ways to vocabulary memorization」（Memrise 評）
   「I prefer to make my own cards in Anki and have them forever rather than in a paid app that **may disappear like Fluyo**」
   - URL: 同上、確度: 高
   - 注: Fluyo（インフルエンサー主導の語学アプリ）は 2025 年 11 月に閉鎖したと同投稿に記載（確度: 中、伝聞）。

### C. 最も近い先行事例: Clozemaster（公式サイトで直接確認）

8. 価格: Pro 月額 **$12.99**、年額 **$79.99**（月あたり $6.67、48% off と表示）。30 日返金保証。無料プランあり。
   - URL: https://www.clozemaster.com/pro
   - 取得日: 2026-09-14、確度: 高（メインセッション直接閲覧）

9. 運営と規模（**自己申告・マーケティング文言のため確度 低〜中**）:
   「What started as a side project has grown into a community of hundreds of thousands of learners across 50+ languages. **We're a small, independent team**」
   - URL: https://www.clozemaster.com/about
   - 取得日: 2026-09-14、確度: 低〜中（第三者検証なし。「hundreds of thousands of learners」は課金者数ではない）

10. **中級の停滞を正面から狙っている**（同社 about ページの自社説明）:
    「you finish a course, you know a few hundred words, and then you hit a wall. Textbooks are boring. Flashcards are tedious. Real content is overwhelming.」
    - URL: https://www.clozemaster.com/about、確度: 高（文言そのもの）
    - ユーザーレビュー（Google Play、同社サイト掲載のため選別されている点に注意、確度 中）:
      「Best language learning app for intetmediat level... I've been studying Korean for 2.5 years **with a plateau in my learning for 6 months** on other language apps. 1 months on Clozemaster (2 weeks with pro) and my comprehension has skyrocketed.」
    - 注: `user-needs/intermediate-plateau.md` で「中級の停滞に特化した課金訴求は見つからなかった」と書いたが、**これは反例にあたる**。訂正的な位置づけで扱う。

11. 同社は AI を「必要なときだけ」の位置に置いている: 「AI where it helps... Deeper understanding when you want it, out of the way when you don't.」
    - URL: 同上、確度: 高

## グレーゾーン・未確認

- Clozemaster の課金者数・売上は**一切不明**。「hundreds of thousands of learners」は自己申告かつ課金者数ではない。App Store レビュー数 1,400 / 評価 4.8 という数字は上記 Reddit 投稿の記載（確度 中、未検証）。
- Clozemaster の**獲得経路は未確認**。どうやって客を取ったかはこのファイルでは分からない（`srs-precedents.md` の調査対象）。
- 引用 5 の「I paid for this app」は 1 人の行動であり、この層の広さは不明。384 votes は関心の広さを示すが、支払い者の割合は示さない。
- 「コロケーション」で検索して薄かったことは、**ニーズの不在を証明しない**。用語が使われていないだけの可能性が高い（引用 4 の対比がそれを示唆する）。
- 英語以外の言語（スペイン語等）の学習者の声が混ざっている。英語学習に限った支払い行動は別途確認が要る。
- r/EnglishLearning と r/languagelearning の数スレッドのみ。標本は小さい。

## 影響する論点

- `decisions.md` 2026-09-14「SRS で管理する対象はコロケーション・句動詞とする」— **用語の見直しが必要**（引用 4）。痛みは実在するが「コロケーション」とは呼ばれていない。
- 同決定への**直接の反証**が引用 2。「カードで明示的に覚えるのは持続しない」というコミュニティ通念。
- `open-questions.md`「中級（B1→B2）の停滞は課金に結びつく痛みか」— **有利な材料が出た**（引用 10）。Clozemaster は中級の停滞を名指しして有料で売っている。
- `user-needs/reddit-direct-observation.md` の「支払い意思が観測できない」— **セグメント依存であることが分かった**。熱心な語学学習者層は複数の有料アプリに払う（引用 5）。
- `open-questions.md`「グローバル × 月 30 万円」— 価格の目安が 1 つ得られた（$12.99/月 または $79.99/年）。月 30 万円は月額課金なら約 155 人、年額課金なら約 300 人に相当（概算、為替により変動）。
