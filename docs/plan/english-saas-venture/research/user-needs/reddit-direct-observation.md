# Reddit 直接観察: エンジニアと英語学習者の生の声、および支払い意思

- 調査日: 2026-09-14
- 調査手段: **メインセッションが Claude in Chrome でユーザーの実 Chrome から直接閲覧**（WebFetch / Reddit JSON API は全経路 403、WebSearch はクォータ枯渇のため、サブエージェント 2 体はいずれも Reddit に到達できなかった。その穴を埋めるための調査）
- 問い: 非ネイティブのエンジニアは英語で何に困っているか。そして、その痛みに対して**アプリに金を払う行動が観測できるか**。

## 結論

**痛みは極めて鮮明に実在する。ただし、支払い行動はほぼ観測できなかった。**
r/developersIndia の複数スレッドで、当事者が助けを求め、多数の回答が付いている。しかし
**回答として挙がる手段はほぼ全て無料**（映画・ドラマ、ポッドキャスト、友人と話す、鏡の前で話す、
面接を数多く受ける、録音して ChatGPT に見てもらう、free4talk、カスタマーサポートに電話する）。
**有料アプリを推薦する声は 1 件も観測できなかった。** 有料として挙がったのは Netflix の
サブスクリプション、対面の spoken English classes（インド国内）、渡英のみ。

さらに r/EnglishLearning では、アプリ推薦そのものへの不信が公然と表明されている。

## 根拠（原文引用）

### クラスタ A: 痛みの実在（現在進行形）

1. 「I'm from a desi family and I struggle a lot with spoken English. I know the answers and logic but I can't express it properly I fumble can't frame sentences and lose confidence while speaking. It's affecting my interviews and overall communication.」
   - URL: https://www.reddit.com/r/developersIndia/comments/1sk7p97/anyone_from_a_desi_background_struggled_with/
   - 出典日付: 約 5 ヶ月前（2026-09-14 時点の Reddit 表示）
   - 確度: 高（メインセッションが直接閲覧）

2. 「I can understand basic English, but when I try to speak, my mind goes blank.」
   - URL: https://www.reddit.com/r/developersIndia/comments/1tn1pkk/how_to_speak_english_fluently_without_feeling/
   - 出典日付: 約 4 ヶ月前
   - 確度: 高

3. 「Not being good at English severely limits your job opportunities because interviews are almost always conducted in English. If you can't communicate well during an interview, you're either not getting hired or you're getting lowballed.」（採用側として多数を面接してきた人物の投稿。211 votes / 55 comments）
   - URL: https://www.reddit.com/r/developersIndia/comments/13za7es/english_is_not_just_a_language/
   - 出典日付: 約 3 年前
   - 確度: 高

### クラスタ B: 汎用 AI では埋まらないという当事者の証言（最重要）

4. 「People say just speak more in English but I don't have anyone to practice with. **Even using AI feels unnatural and repetitive.**」
   - URL: https://www.reddit.com/r/developersIndia/comments/1sk7p97/anyone_from_a_desi_background_struggled_with/
   - 出典日付: 約 5 ヶ月前
   - 確度: 高
   - 注: 「ChatGPT があるから不要」への直接の反証。ただし**この人物が代わりに金を払ったという記述は無い**。

### クラスタ C: 支払い意思の不在（仮説にとって最も不利な材料）

5. 上記 3 スレッドの回答は全て無料手段に収束した。代表例:
   - 「Just watch content which makes you familiar with those words, and SPEAK!」
   - 「Give some mock interviews and record yourself... or you can share the recording with ChatGPT and ask ChatGPT to help you.」
   - 「Make sure for the next few months, that you speak with all your friends in English. They will mock you, sure. But it's worth it, both parties benefit.」
   - 「There is no 3 step program or one hidden trick. You just have to do it.」
   - URL: 上記 3 スレッド、確度: 高
   - **コミュニティに「近道は無い / 只管やれ」という規範が強く共有されている**。これは有料プロダクトの訴求と正面から衝突する。

6. 有料として言及されたのは次のみ: Netflix サブスクリプション、対面の spoken English classes、渡英（「I went to UK and that helped me improve」）。**アプリの有料プランへの言及は観測されなかった。**

### クラスタ D: アプリ推薦そのものへの不信（r/EnglishLearning）

7. スレッドタイトル（Rant / Venting タグ）: 「Here people suggesting an app does they really want to help or just want to promote their app? **we do already have ai I don't find any of them making a difference**」本文「I have downloaded bunch of them 🥹 It's easy to fool dumb one 😔」
   - URL: https://www.reddit.com/r/EnglishLearning/comments/1qzxhdf/here_people_suggesting_an_app_does_they_really/
   - 出典日付: 約 7 ヶ月前
   - 確度: 高

8. 同スレッドで個人開発者が自作アプリを弁明しつつ規模を開示: 「to be transparent I currently have around **200 sign ups**」
   - URL: 同上、出典日付: 約 7 ヶ月前、確度: 高（自己申告）
   - 注: **サインアップ 200 件であって有料課金者数ではない。** `indie-saas-track-record.md` の
     「個人開発の語学アプリはほぼ規模ゼロ」という結論と整合する。

9. 検索結果に現れたスレッドタイトルの傾向も示唆的: 「Which **free** app would you recommend me to practice only speaking and become more fluent?」
   - URL: https://www.reddit.com/r/EnglishLearning/comments/1sdljev/which_free_app_would_you_recommend_me_to_practice/
   - 確度: 高（タイトルのみ確認。本文未読）

## グレーゾーン・未確認

- 本調査は r/developersIndia と r/EnglishLearning の**数スレッドのみ**。r/brdev、r/ExperiencedDevs、
  r/cscareerquestions、中国語・韓国語圏のコミュニティは未確認。
- 「無料手段しか挙がらない」ことは、**そのコミュニティの規範を示すだけで、支払い意思の不在を証明しない**。
  金を払っている人は公開の場でそれを言わない可能性がある（特に「近道は無い」規範が強い場では言いにくい）。
- r/developersIndia はインドの開発者コミュニティであり、**購買力と価格感度が地域によって大きく異なる**。
  $15/月 のサブスクリプションに対する反応は、欧州・北米の非ネイティブエンジニアでは違う可能性がある。
  この点は本調査では確認していない。
- 各スレッドのコメントは上位のみ閲覧。折りたたまれた返信は未読。

## 影響する論点

- `open-questions.md`「中級（B1→B2）の停滞は課金に結びつく痛みか」— **不利な材料が増えた**。
- `open-questions.md`「グローバル × 月 30 万円の組み合わせに前例が無いことをどう扱うか」— 補強材料。
- `decisions.md` 2026-09-14「エンジニア・技術職の英語を検証対象の有力仮説として置く」— 痛みの実在は
  強く支持されたが、**支払い意思は支持されなかった**。仮説の扱いを再判断する材料。
- `chatgpt-substitution-line.md` の「摩擦の無さ」仮説 — 引用 4 は間接的な支持材料になり得る。
