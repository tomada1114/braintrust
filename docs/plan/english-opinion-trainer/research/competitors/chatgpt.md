# ChatGPT（意見練習・IELTS Speaking 用のカスタム GPT を含む）

- 調査日: 2026-09-07
- 調査手段: Sonnet サブエージェントによる机上調査 + メインによる原典確認、一次観察あり（サブエージェントがオーナーのブラウザで実施）
- URL: https://chatgpt.com/
- 対象ユーザー: 汎用ユーザー。英語練習用途は GPT Store 上の第三者制作のカスタム GPT が担っており、OpenAI 公式のターゲット定義ではない。

OpenAI 公式ページ（chatgpt.com、chatgpt.com/pricing、openai.com/chatgpt/pricing、help.openai.com 配下の各記事）は机上調査時点でいずれも WebFetch が HTTP 403 を返し、公式一次情報として本文を確認できなかった。以下の「主要機能」「料金・プラットフォーム」の多くは WebSearch のインデックス経由の要約、または第三者記事に依拠しており確度を落として記載している。これに対し一次観察（下記）は、オーナーのブラウザで実際に chatgpt.com にログインして操作しており、本ファイルの中で最も確度の高い一次情報である。

## 位置づけ

ChatGPT 本体は英語学習・意見練習専用ではなく、汎用 AI アシスタントとして自社を位置づけている。「質問への回答、着想、生産性向上のための AI チャットボット」がトップメッセージであり、言語学習は用途の一つに過ぎない。（URL: https://chatgpt.com/ / 出典日付: 記載なし / 確度: 中 — サイト自体は未取得のため WebSearch のスニペット経由）

英語での意見練習・IELTS Speaking 対策という文脈は、OpenAI 公式ではなく GPT Store（ユーザー・第三者が作成する「カスタム GPT」のマーケットプレイス）側で生まれている。GPT Store 上には「IELTS Speaking Simulator」「IELTS Speaking Master」「English Speaking Practice GPT」など、英語スピーキング練習・IELTS 対策を名乗るカスタム GPT が多数存在し、どれも個人または第三者制作物であり OpenAI 公式の教育プロダクトではない。（URL: https://chatgpt.com/g/g-uGueIrCsT-ielts-speaking-simulator ほか / 出典日付: 記載なし / 確度: 高、GPT Store 上に実在することは URL で確認）

## 中核の体験（初回ユーザーの流れ）

公式ヘルプページに基づく一般的な流れ（WebFetch 403 のため WebSearch 要約経由、確度: 中〜低）。

1. ユーザーは Explore GPTs（GPT Store）を開くか、直接リンクでカスタム GPT のページに到達する。チャットを開始するにはサインインが必須。
2. GPT を開くと、説明文と「Conversation starters（会話のきっかけとなる例文プロンプト）」が表示される。
3. IELTS Speaking Simulator 系の GPT では「① 練習したい Part を選ぶ → ② マイクアイコンを押す → ③ 本番同様に応答する」という 3 ステップの案内が示される（第三者ミラーサイトの要約、確度: 低）。
4. 会話はその GPT 専用の 1 スレッドとして進み、そのスレッド内では文脈が保持される。新しいチャットを開始すれば文脈はリセットされ、GPT の instructions 以外に前回までの練習履歴が自動で持ち越されるわけではない（memory 機能が有効な場合を除く）。

一次観察（下記）では、標準チャットにプロンプトを 1 回渡すだけで独自の「お題出題 → 回答 → (1)〜(4) の定型フィードバック」ループを 2 ターンにわたり再現できることを確認しており、上記の公式ヘルプ由来の記述より重要な事実である。

## 主要機能

- **カスタム GPT（GPTs）**: 指示文（instructions）・知識ファイル・有効化する機能を組み合わせて特定用途に特化させたチャットボットを作れる仕組み。（URL: https://help.openai.com/en/articles/8554407-gpts-in-chatgpt（要約） / 確度: 中）
- **Custom instructions**: 「自分について ChatGPT に知っておいてほしいこと」「どう応答してほしいか」の 2 つの入力欄があり、以後すべてのチャットに自動適用される。（確度: 中）
- **Memory（メモリ）**: 「Saved memories」と「Chat history reference」の 2 系統。ユーザーは記憶内容の確認・削除・オフ化ができる。（確度: 中）
- **Voice（音声会話）**: マイクアイコンから音声会話を開始でき、終了すると発話内容の書き起こしがそのままテキストチャット履歴に追加される。一次観察でも「Chat」「Work」の 2 モードタブの存在を確認した（下記）。（確度: 中）

## UI・UX の特徴とそれが嬉しい理由

- 特徴: Conversation starters（会話のきっかけ）。GPT を開いた瞬間にクリックできる例文プロンプトが並ぶ。
  - 嬉しい理由: 白紙のチャット欄を前に何を打つか迷う「blank-page 問題」を避けられる。
  - URL: https://help.openai.com/en/articles/8554407-gpts-in-chatgpt（要約） / 確度: 中
- 特徴: カスタム GPT による instructions の固定。GPT 作成者が「PREP で答えさせる」「レベルを聞いてから調整する」といった振る舞いをあらかじめ書き込める。
  - 嬉しい理由: 利用者は毎回プロンプトを書かずに一定の型で練習できる。ただし GPT 作成者の設計品質に依存し、OpenAI 側が体系化を保証しているわけではない。
  - URL: https://www.toolify.ai/gpts/g-uGueIrCsT / 確度: 低（第三者要約）
- 特徴（一次観察で確認）: 標準チャットに 1 回プロンプトを渡すだけで、「(1) Does it get across? (2) 1-2 things to fix (3) A rewrite at CEFR B1 level (4) Grammar/usage notes」という指定フォーマットと CEFR B1・日本語での説明が、2 ターンにわたり崩れず維持された。
  - 嬉しい理由: LLM の指示追従性の高さにより、フォーマットを毎回書き直さなくて済む。オーナーの現行の「代替手段」としての実力の高さを示す。
  - URL: 一次観察（下記） / 出典日付: 2026-09-07 / 確度: 高（一次観察）
- 特徴（一次観察で確認）: カスタム GPT「Speaking Practice」は、Grammar-Corrected Version（修正版）に加えて C1 Enhanced Version（もう一段上のレベルの言い方）を並べて見せる。
  - 嬉しい理由: 今の自分の英語と目指す先の英語を並置することで「伸びしろ」が一目でわかる。
  - URL: 一次観察（下記） / 出典日付: 2026-09-07 / 確度: 高（一次観察）

## 料金・プラットフォーム

- 課金のモデル: Free / Go（$8/月）/ Plus（$20/月）/ Pro（$100・$200/月の 2 種）/ Business（$25/席/月）という多段階構成（すべて第三者記事、公式ページは 403 で未確認、確度: 低〜中）。既存のカスタム GPT を「使う」のは無料ユーザーでも可能だが、自分で新規に作るのは Plus 以上が必要との第三者記述がある（確度: 低）。
- プラットフォーム: Web（chatgpt.com）、iOS、Android、デスクトップアプリ、API。ログイン必須（GPT を含めチャット開始にはサインインが要る）。一次観察でも Plus プランでのログイン状態を確認済み。（確度: 中）

## ユーザーの声

### 賞賛

- 「こちらの都合のいい時間まで付き合ってくれますし、途中で急にやめることもできるので、気を使わずに済み、とても便利です」— URL: https://www.rarejob.com/englishlab/column/20250606/ / 出典日付: 2025-06-06 / 確度: 中 / 言語: 日本語（**編集記事による観察** — 英会話スクールのコラムであり、実名の個人ユーザーレビューではない）
- 「辞書を調べるよりも早いので、とても使えるツール」— URL: https://www.rarejob.com/englishlab/column/20250606/ / 出典日付: 2025-06-06 / 確度: 中 / 言語: 日本語（編集記事による観察）
- 「英語を話すと緊張してしまうという方にはこの点は良いと言えるでしょう」— URL: https://www.rarejob.com/englishlab/column/20250606/ / 出典日付: 2025-06-06 / 確度: 中 / 言語: 日本語（編集記事による観察）
- 「The model interrupts you less, so you'll have more time to gather your thoughts and not feel like you have to fill in all the gaps and silences all the time.」— URL: https://www.tomsguide.com/computing/artificial-intelligence/talking-to-chatgpt-just-got-better-and-you-dont-need-to-pay-to-access-the-new-functionality / 出典日付: 記載なし / 確度: 中 / 言語: 英語

### 不満

- 「相手がAIであるため、リアルな人間との会話のようにはなりません。こちらが考えていて沈黙している間、最後まで上手に待ってくれず、先に進んでしまったりします」— URL: https://www.rarejob.com/englishlab/column/20250606/ / 出典日付: 2025-06-06 / 確度: 中 / 言語: 日本語（編集記事による観察）
- 「ChatGPTには相槌で会話を受け止めるという感覚はなく、基本的に『聞いてくれる』というコミュニケーションはありません」— URL: https://www.rarejob.com/englishlab/column/20250606/ / 出典日付: 2025-06-06 / 確度: 中 / 言語: 日本語（編集記事による観察）
- 「ChatGPTは音声をすべてテキストに変換して処理しているため、発音を認識してくれないのです」— URL: https://www.rarejob.com/englishlab/column/20250606/ / 出典日付: 2025-06-06 / 確度: 中 / 言語: 日本語（編集記事による観察）
- 「Ask ChatGPT if your sentence was correct and it will almost always say yes」— URL: https://www.talkio.ai/blog/i-used-chatgpt-voice-mode-for-language-practice-for-30-days-here-is-what-it-cannot-do / 出典日付: 2026-08-13 / 確度: 中 / 言語: 英語（**競合による評** — Talkio AI は競合の言語学習アプリのブログ）
- 「Every conversation starts fresh. ChatGPT does not remember that you struggled with subjunctive mood last Tuesday」— URL: 同上 / 出典日付: 2026-08-13 / 確度: 中 / 言語: 英語（競合による評）
- 「The score estimation is for reference only (pronunciation is completely inaccurate because the current voice mode converts speech to text.」— URL: https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/README_EN.md / 出典日付: 記載なし（更新は 2023 年 12 月〜2024 年 8 月頃） / 確度: 中 / 言語: 英語
- 「マイクの絵が出て来なくて手入力しか出来ない状態になります。（中略）それを消して何回かやり直してると、マイクのアイコンが表示されなくなることが多いです。」— URL: https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13290621298 / 出典日付: 2023-12-20 / 確度: 中 / 言語: 日本語

## 解決できていない課題

- 課題: IELTS Speaking 用 ChatGPT 系ツールを半年間繰り返し使っても、スコアの伸びが乏しい。
  - 根拠: 「after simulating multiple times over six months, they felt their score had only improved by about 0.5 at most」/ URL: https://github.com/hubeiqiao/IELTS-Speaking-Simulator/blob/main/README_EN.md / 出典日付: 記載なし / 確度: 低
- 課題: 会話が長くなると文脈がずれ、以前渡した情報と矛盾したことを言い出すため、都度まとめ直して引き継ぐ運用が必要になる。
  - 根拠: 「新しいチャットでやり直すために引き継ぎたいので、今までのやり取りを1つのファイルにして」/ URL: https://note.com/chi3jp/n/n540a965f610f / 出典日付: 2026-06-07 / 確度: 低
- 課題（一次観察で確認、根本的な設計）: 新しいチャットを開いた場合、メモリ機能を意図的に使わない限り毎回プロンプトを再送する必要がある — セットアップの手間が現行の代替手段としての弱点。
  - 根拠: 一次観察（下記） / 出典日付: 2026-09-07 / 確度: 高
- 課題（一次観察で確認）: 添削文だけを抽出して溜める専用の保存機能は ChatGPT 標準にはない。チャット履歴としてサイドバーに残るのみで、コピーボタンもメッセージ単位。
  - 根拠: 一次観察（下記） / 出典日付: 2026-09-07 / 確度: 高

競合ブログ（talkio.ai）由来の指摘（発音を評価しない、記憶が続かない等）は本文中に「競合による評」と明記した。中立なユーザーの声より批判の強さが誇張されている可能性がある。

## 一次観察（触った場合）

- 観察日: 2026-09-07
- 手段: オーナーのブラウザでログイン済みアカウントの範囲を操作（サブエージェントが実施）

### A. 指定プロンプトでの再現（英語オピニオンコーチ役）

1. `https://chatgpt.com/` にアクセス。ログイン済み（Plus プラン、t masuyama）。画面上部に「Chat」「Work」の切替タブがあることに注意（初回、誤って「Work」タブ内の別タスクにテキストが入ってしまうミスが発生 → 新しいチャットを作り直し、明示的に「Chat」タブに切り替えてからやり直した）。
2. 新しいチャットで指定プロンプト全文を送信。ChatGPT は "What do you usually like to do on weekends?" という質問を 1 つ返した。
3. わざと誤りを含む B1 想定の回答を送信: "On weekend I usually go to shopping with my friend and we eat many delicious food."
4. フィードバックは指定フォーマットどおりに返ってきた:
   ```
   (1) Does it get across?
   はい、十分伝わります。「週末に友達と買い物に行って、おいしいものをいろいろ食べる」という意味は自然に理解できます。

   (2) 1-2 things to fix
   On weekend → On weekends / At the weekend（習慣は on weekends が自然）
   go to shopping → go shopping（to は不要）

   (3) A rewrite at CEFR B1 level
   On weekends, I usually go shopping with my friends, and we eat a lot of delicious food.

   (4) Grammar/usage notes
   go shopping はセットで覚える。例: go hiking / go swimming / go fishing
   many delicious food は不自然。food は不可算名詞なので a lot of delicious food。
   my friend/my friends の使い分け。
   ```
5. 「next question」と送信 → 新しい質問 "What's something you like to cook at home?" が来た。
6. わざと誤りを含む回答を送信: "I like cook curry rice because it is easy and my family is loves it very much."
7. 2 ターン目もフォーマットを完全維持:
   ```
   (1) Does it get across? はい、十分伝わります。...
   (2) 1-2 things to fix: I like cook → I like to cook / I like cooking／my family is loves it → my family loves it
   (3) A rewrite at CEFR B1 level: I like to cook curry rice because it's easy to make, and my family loves...
   (4) Grammar/usage notes: like + to不定詞 と like + -ing はどちらも使える。
   ```

**重要な所見**: 2 ターンともフォーマット・CEFR B1 指定・日本語での説明が完全に維持され、フォーマット崩れはなかった。セットアップに必要だったのはプロンプト 1 回分のみ（システムプロンプト相当をユーザー発言として貼るだけ）。**オーナーの overview.md にある既存プロダクトへの不満「フィードバックが思った形式で返らない」は、このケースでは再現されなかった**。新しいチャットを開いた場合に何も引き継がれないことは、本来の設計として明らか（メモリ機能を意図的に使わない限り、毎回このプロンプトを再送する必要がある＝「セットアップの手間」がオーナーの現行の代替手段の弱点）。

### B. GPT ストア調査

8. `https://chatgpt.com/gpts` にアクセスし、検索ボックスで "IELTS speaking opinion" を検索 → **「結果が見つかりませんでした」**（完全一致に近いフレーズ検索でヒットなし）。
9. "English opinion practice" で検索 → 3 件ヒット（下記「GPT ストアの検索結果」参照）。
10. 最も近そうな「Speaking Practice」を開き、会話のきっかけの一つ "What's your opinion on working remotely?" をクリックして実際に 1 往復会話。
11. GPT はまず質問を言い換えて具体化: "Do you think remote work improves people's quality of life, or does it make work and social connection harder? Explain which side matters more to you and why."
12. わざと誤りを含む回答を送信: "I think remote work is good because I can spending more time with my family and I don't need commute."
13. フィードバックは以下の 4 部構成（すべて英語）:
    ```
    1. Grammar-Corrected Version
    I think remote work is good because I can spend more time with my family and I don't need to commute.

    2. C1 Enhanced Version
    I think remote work is beneficial because it allows me to spend more time with my family and eliminates the need to commute. As a result, I can use my time more efficiently and maintain a better work-life balance.

    3. Error Explanations
    - "I can spending" is incorrect. After the modal verb can, use the base form: can spend.
    - "I don't need commute" is incorrect. After need, use to + verb: need to commute.
    - Your reasoning is clear, but it is too brief for B2-level conversation practice — add a sentence or two explaining why...

    4. CEFR Estimate
    Your response is around B1. Your meaning is easy to understand, but there are noticeable grammar errors in a very short response, and your ideas are not developed enough. To reach B2, use basic verb structures accurately and support your idea with reasons, examples, and consequences.

    Now continue: Do you think remote work has any disadvantages? For example, does it make people feel isolated or less motivated?
    ```
    フィードバック後、GPT は同じトピックの深掘り質問で会話を継続した（ランダムな新規トピックには切り替わらず、1 つのお題を掘り下げる設計）。

### GPT ストアの検索結果

- 検索語「IELTS speaking opinion」: **結果が見つかりませんでした（0 件）**。
- 検索語「English opinion practice」: 3 件ヒット
  1. **Speaking Practice** — 「Strict English opinion practice partner with CEFR level scoring.」作成者: Heng-Hao, Hung／10+ 会話。会話のきっかけ 4 つはいずれも「賛否を問う意見トピック」寄り（例: "Do you think social media does more harm than good?"）で、"random light everyday question"（世間話レベルの軽さ）というよりは討論寄りのお題。
  2. **Improve English Expresiveness** — 「Practice English Writing and English Expression by writing opinion toward news or and story and improve it.」作成者: JUN-LONG WANG／30+ 会話。ニュース記事起点で、雑談レベルの軽さではない。
  3. **Meddle Level English Learner** — 「My aim is to help you practise your English conversation skills.」作成者: community builder／40+ 会話。説明文からはループ構造が読み取れず（未確認、開いていない）。

- 引っかかった点:
  - ChatGPT ホーム画面に「Chat」と「Work」という 2 つのモードタブがあり、初見では見分けにくい。誤って「Work」タブ側の（無関係な過去タスクの）入力欄にプロンプトを打ってしまい、既存の別チャットに混入させてしまった。
  - GPT ストア検索は完全一致寄りで、"IELTS speaking opinion" のような複合フレーズだと該当 0 件になる。狙った用途の GPT を見つけるのに試行錯誤が要る。
  - カスタム GPT「Speaking Practice」は、フィードバックだけで終わらず "Now continue: ..." と次の質問を同じ返信内に含めてくる（テンポよく次のお題に移れる反面、フィードバックとお題が同じ吹き出しに混在し、区切りがやや見づらい）。
- 良いと感じた瞬間とその仕組み:
  - ベースの ChatGPT に一度だけプロンプトを渡すだけで、以降のターンで「(1)〜(4)」の指定フォーマットと CEFR B1・日本語説明が崩れずに維持され続けた — LLM の指示追従性の高さにより、フォーマットを毎回書き直さなくて済む仕組み。
  - カスタム GPT「Speaking Practice」は、修正版だけでなく「もう一段上のレベル（C1）ではどう言うか」まで並べて見せる — 今の自分の英語と目指す先の英語を並置することで「伸びしろ」が一目でわかる仕組み。
  - CEFR 推定コメントが「なぜその評価か」（理由づけの薄さ、文法の正確さ等）を明文化しており、単なるレベル判定で終わらず次に何をすれば B2 に上がれるかを示す仕組み。
- 止めた地点: 中核の体験まで到達（サインアップ壁・課金要求は出現せず。Plus 契約はオーナーの既存契約範囲内）。
- フィードバックの形式（観察したまま）: A・B いずれも「発言（1 メッセージ）ごと」に返ってくる per-utterance フィードバック。セッション終了時にまとめて出す仕組みはなし。言語は A は指示どおり日本語での説明、B のカスタム GPT はすべて英語（作成者依存）。
- レベル設定・ヒント・保存されるもの:
  - レベル設定: プロンプト A 内で「CEFR B1」と明示すれば守られる。カスタム GPT B は自動で CEFR 推定を返すが、目標レベルの指定は見当たらない（未確認、作者依存）。
  - ヒント: 「ヒントが欲しい」旨は今回試していない（未確認）。指定プロンプトにヒント機能は含めていない。
  - 保存されるもの: チャット履歴としてサイドバーに残る（自動でタイトルが付く）のみ確認。添削文だけを抽出保存する機能は ChatGPT 標準にはない。
- 未確認: 「Improve English Expresiveness」「Meddle Level English Learner」の実際の 1 往復（開かず終了）、標準チャットでヒント（opinion seeds）を求めた場合の挙動、カスタム GPT での目標 CEFR レベル指定方法（作者依存）、モバイルアプリ版での挙動。

## グレーゾーン・未確認

- OpenAI 公式ページ（chatgpt.com、chatgpt.com/pricing、openai.com/chatgpt/pricing、help.openai.com 配下の各記事）はいずれも机上調査の WebFetch で HTTP 403 を返し、公式一次情報として本文を確認できなかった。上記の「主要機能」「料金・プラットフォーム」の多くは第三者情報に依拠している。**一次観察（本セッション実施）がこの製品では最も確度の高い情報源であり、机上調査の弱さを補っている**。
- IELTS Speaking 系カスタム GPT の「フィードバックの形式と粒度」「レベル設定の有無」「意見のタネ・テンプレート支援の有無」は、GPT ごとに instructions が異なるため一般化できない。今回一次観察で確認した「Speaking Practice」GPT の挙動が他の GPT にも当てはまるとは限らない。
- GPT Store の各 GPT について「利用者数」「レーティング」「レビュー内容」は取得できなかった。
- 音声モードでの発話に対して、テキストと同じ粒度・形式でフィードバックが返るのかは未確認（一次観察はテキストのみ実施）。
- 「賞賛」「不満」の一部引用は rarejob.com（英会話スクールの編集ブログ）由来であり、実名ユーザーレビューではない。上記では「編集記事による観察」と明記して分離した。

## このアイデアへの示唆

- **最も重要な所見**: 一次観察により、オーナーが overview.md で述べていた既存プロダクトへの不満「フィードバックが思った形式で返らない」は、1 回のセットアップ用プロンプトを渡すだけで 2 ターンにわたり再現しなかった。CEFR B1 指定・日本語説明を含む (1)〜(4) の定型フォーマットは崩れなかった。これは overview.md の「既存プロダクトとの違い」からこの不満を外す根拠になる（決定は decisions.md へ）。
- 借りられる仕組み: カスタム GPT「Speaking Practice」の「修正版＋一段上のレベル（C1）を並べて見せる」構成は、本アイデアの「レベル別の言い直し」を実装する際の見せ方の参考になる。
- 避けるべき作り: GPT ストアの検索が完全一致寄りで狙った GPT に辿り着きにくい、Chat/Work タブの誤入力といった UI 上の分かりにくさは、素の ChatGPT の弱点として記録しておく。
- この製品（の代替手段としての強み）が本アイデアに残す課題: 一次観察で確認した通り、素の ChatGPT は「セットアップの手間（毎回プロンプトを再送）」「保存されない（添削文だけを抽出保存する機能がない）」「構造化されない（進捗の自動蓄積・可視化がない）」「レベル自動調整はプロンプト任せ」という弱点を持つ。本アイデアの差分は、この 4 点（設定不要・言い回しリストが溜まる・お題が体系化されている・レベル選択の永続化）に絞り込むのが妥当。ChatGPT がフォーマットを保てた以上、「決まった形式のフィードバック」自体は ChatGPT でも 1 プロンプトで再現できてしまう点には留意する必要がある。
- 推奨であって決定ではない。決定は decisions.md へ。
