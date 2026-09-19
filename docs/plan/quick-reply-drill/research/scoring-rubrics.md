# 短文英作文の採点ルーブリック調査

- 調査日: 2026-09-15
- 調査手段: Sonnet サブエージェント 1 体による出典収集 + メインセッションによる原文確認（TOEFL Write an Email ルーブリック PDF を pdftotext で抽出して確認、Grammarly Writing Score API ページを直接確認）
- 問い: 短い英文（チャットの返信のような 1〜2 文）を評価するときに、確立された採点の観点と尺度にはどんなものがあるか。特にレジスター・場面への適切さを扱う枠組みがあるか。

## 結論

- CEFR Companion Volume（Council of Europe, 2018 年版 PDF）には書き言葉のやり取りの尺度が複数ある。「Correspondence」と「Online conversation and discussion」がともに Pre-A1〜C2 の記述子を持ち、後者はチャット・オンライン投稿のような短いやり取りを名指しで扱う。レジスター・丁寧さ専門の独立尺度「Sociolinguistic appropriateness」（A1〜C2）もある。
- IELTS Writing は 4 観点・9 バンドだがエッセイ形式で、チャット的な短文返信やレジスターを直接評価する記述子はない。
- TOEFL iBT Writing（2026 年新形式）には「Write an Email」課題があり 0〜5 の 6 段階。記述子に politeness, register が明記されている。短い実務的返信を採点する公的ルーブリックとして最も近い。
- Cambridge English Writing Assessment Scale は Content / Communicative Achievement / Organisation / Language の 4 観点・0〜5 の 6 段階。Communicative Achievement に genre, format, register, function が含まれる。
- 自動採点ツール: Cambridge Write & Improve は総合 CEFR レベルのみ。Grammarly は Correctness / Clarity / Engagement / Delivery の 4 カテゴリ（Delivery が politeness/formality/friendliness）だが API は 30 語未満でスコア null。ETS e-rater は 10 のマクロ特徴量。DeepL Write は採点次元を公開していない。
- 学術的 AES（Ke & Ng, IJCAI 2019）の次元一覧に register / appropriateness は登場しない。SLA の CAF（Complexity, Accuracy, Fluency）は別系統。
- チャット的な 1〜2 文を直接想定した公開ルーブリックは見つからなかった。最も近いのは CEFR の Online conversation and discussion と TOEFL の Write an Email だが、いずれもより長い投稿・メールを想定した記述子である。

## 根拠

### (1) CEFR Companion Volume

- 事実: written interaction に 2 尺度（Correspondence / Notes, messages and forms）があり、online interaction は多モーダルとして別立てで扱われる。引用: "There are two scales for written interaction: Correspondence and Notes, messages and forms... Online interaction is dealt with separately because it is multimodal"
  - URL: https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2018/1680787989
  - 出典日付: 2018-02（© Council of Europe, February 2018）
  - 確度: 高
- 事実: Correspondence 尺度は Pre-A1〜C2 の 7 段階。B1: "Can exchange information by text message, e-mail or in short letters, responding to questions the other person had"
  - URL: https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2018/1680787989（p.93）
  - 出典日付: 2018-02
  - 確度: 高
- 事実: Online conversation and discussion 尺度も Pre-A1〜C2 の 7 段階。B1: "Can post a comprehensible contribution in an online discussion on a familiar topic of interest, provided that he/she can prepare the text beforehand..." B2: "Can participate actively in an online discussion, stating and responding to opinions on topics of interest at some length..."
  - URL: https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2018/1680787989（p.96-97）
  - 出典日付: 2018-02
  - 確度: 高
- 事実: 進行の説明でレジスター調整が C1/C2 の特徴とされる: "By C1, the user/learner can modulate his/her register and giving critical evaluations diplomatically."
  - URL: https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2018/1680787989（p.96）
  - 出典日付: 2018-02
  - 確度: 高
- 事実: 独立尺度 Sociolinguistic appropriateness（A1〜C2、Pre-A1 なし）。B1: "Can perform and respond to a wide range of language functions, using their most common exponents in a neutral register. Is aware of the salient politeness conventions and acts appropriately." B2: "Can express him/herself confidently, clearly and politely in a formal or informal register, appropriate to the situation and person(s) concerned."
  - URL: https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2018/1680787989（p.137）
  - 出典日付: 2018-02
  - 確度: 高
  - 備考: 話す/書く両方に適用される一般尺度。

### (2) IELTS / Cambridge / TOEFL

- 事実: IELTS Writing は 4 観点・0〜9 バンド。Task 2 Band 7 Lexical Resource: "An awareness of style and collocation is evident, though inappropriacies occur."
  - URL: https://ielts.org/cdn/Guides/ielts-writing-band-descriptors.pdf
  - 出典日付: Updated May 2023
  - 確度: 高
  - 備考: エッセイ形式でチャット的返信・レジスター専用観点なし。
- 事実: Cambridge English Writing Assessment Scale は Content / Communicative Achievement / Organisation / Language の 4 サブスケール、Bands 0〜5。用語集: "Each piece of writing gets four sets of marks for each of the subscales, from Bands (0–5)." Communicative Achievement: "These include genre, format, register and function. For example, a personal letter should not look like a formal report, and an email to a teacher would probably be more formal and polite than an email to a close friend!"
  - URL: https://www.cambridgeenglish.org/images/231794-cambridge-english-assessing-writing-performance-at-level-b1.pdf
  - 出典日付: 記載なし
  - 確度: 高
- 事実: TOEFL iBT Writing（2026 新形式）に Write an Email と Write for an Academic Discussion があり、各 0〜5。Write an Email Score 5: "Elaboration that effectively supports the communicative purpose / Effective syntactic variety and precise, idiomatic word choice / Consistent use of appropriate social conventions (e.g., politeness, register, organization of information and formulation of actions such as requests, refusals, criticisms, etc.)". Score 4: "Adequate elaboration to support the communicative purpose / Syntactic variety and appropriate word choice / Mostly appropriate social conventions / Few lexical or grammatical errors"
  - URL: https://www.kr.ets.org/content/dam/ets-org/pdfs/toefl/writing-rubrics.pdf
  - 出典日付: Copyright© 2025 by ETS
  - 確度: 高（メインセッションで原文確認済み）
- 事実: TOEFL Writing セクション全体は 1.0〜6.0（0.5 刻み）、各課題 0〜5 を正規化して平均する。
  - URL: https://www.reach120.com/blog/toefl-writing-rubrics , https://prepdrills.com/blog/toefl-2026-writing-guide/
  - 出典日付: 2026 年（サードパーティ）
  - 確度: 中（ETS 公式ページで未確認）

### (3) 自動評価ツール

- 事実: Write & Improve は観点別ではなく総合 CEFR レベル推定 + 語レベルの誤りへの間接フィードバック + 文単位コメントを提供する。"Write & Improve provides summative, overall assessment of writing competence, giving an estimated CEFR level..."
  - URL: https://help.writeandimprove.com/en/articles/1104369-how-does-write-improve-work
  - 出典日付: 2020-03-24
  - 確度: 高
- 事実: Grammarly は総合スコア + Engagement / Correctness / Delivery / Clarity の 4 カテゴリを提供する。Correctness: "reflects issues related to spelling, punctuation, and grammar" / Clarity: "signifies potential clarity and conciseness improvements" / Engagement: "highlights the potential to make the writing more engaging" / Delivery: "assesses striking the right balance of politeness, formality, and friendliness"
  - URL: https://developer.grammarly.com/writing-score-api.html
  - 出典日付: 記載なし
  - 確度: 高（メインセッションで原文確認済み）
- 事実: Grammarly Writing Score API は最低 30 語必要で、未満はスコア null になる。"The minimum word count is 30, including special characters (e.g., emoji)." / "A document that contains at least 1 word will result in COMPLETED with no score (i.e., score is null)."
  - URL: https://developer.grammarly.com/writing-score-api.html
  - 出典日付: 記載なし
  - 確度: 高（メインセッションで原文確認済み）
  - 備考: 1〜2 文のチャット返信は Grammarly のスコア対象になりにくい。
- 事実: ETS e-rater の 10 マクロ特徴量は organization, development, grammar, usage, mechanics, style, word length, word choice, collocation and preposition, sentence variety。
  - URL: https://onlinelibrary.wiley.com/doi/full/10.1002/ets2.12131
  - 出典日付: 2017
  - 確度: 高
  - 補足: https://www.ets.org/erater/about.html は "grammar, usage, mechanics, style and organization, and development" と要約している（出典日付 記載なし、確度 高）。
- 事実: DeepL Write は誤り訂正・文体（Business/Academic/Casual）・トーン（Friendly/Enthusiastic/Diplomatic）の選択・明瞭性の提案を提供するが、スコアや観点別評価は公開していない。
  - URL: https://www.deepl.com/en/products/write
  - 出典日付: 記載なし
  - 確度: 中

### (4) 学術的 AES

- 事実: Ke & Ng (IJCAI 2019) Table 1 の次元は Grammaticality / Usage / Mechanics / Style / Relevance / Organization / Development / Cohesion / Coherence / Thesis Clarity / Persuasiveness。register / appropriateness は登場しない。
  - URL: https://www.ijcai.org/proceedings/2019/0879.pdf
  - 出典日付: 2019
  - 確度: 高
- 事実: SLA の CAF（Complexity, Accuracy, Fluency）が第二言語パフォーマンスの基本 3 次元として広く使われる。
  - URL: https://benjamins.com/catalog/lllt.32（書籍紹介ページ等）
  - 出典日付: 記載なし
  - 確度: 中（原典本文は未確認）
- 事実: 会話エージェント評価の文脈で "Appropriateness"（社会的規範への感度、丁寧さ）を評価軸にする研究例がある。
  - URL: https://arxiv.org/pdf/2501.09493
  - 出典日付: 2025 年前後
  - 確度: 低（要約経由、原文未確認、文脈が英語学習と異なる）

## グレーゾーン・未確認

- CEFR は rm.coe.int の 2018 年 2 月版 PDF を確認した。Council of Europe Publishing の 2020 年正式版そのものは未確認。記述子本文はほぼ同一とされるが差異の有無は調べたが分からなかった。
- IELTS・Cambridge の PDF は WebFetch では読めず、ローカルにダウンロードして pdftotext で抽出して確認した。URL は公式のもの。
- Cambridge の B1 向けガイドに発行年月の記載がない。他レベル（B2, C1）向けで観点名・バンド数が変わるかは調べたが分からなかった。
- TOEFL Writing セクション全体の 1.0〜6.0 は ETS 公式では未確認で、サードパーティ複数の一致のみに基づく。
- Grammarly・DeepL Write とも 1〜2 文のチャット的テキストへの挙動を述べた一次情報がない。DeepL Write は最小文字数の記載自体が見当たらず、調べたが分からなかった。
- 学術 AES の次元一覧に register/appropriateness がない一方、CEFR には専用尺度がある。両体系は 1 対 1 に対応しない。
- CAF の一次文献は要約経由のみで原文は未確認。
- チャット的な 1〜2 文を直接想定した公開ルーブリックは見つからなかった。最も近い CEFR の Online conversation and discussion と TOEFL の Write an Email も、より長い投稿・メールを想定した記述子である。

## 影響する論点

- open-questions.md「採点の観点セットと尺度」: 借りる元によって「構成 (organisation)」のような使えない観点を含むかが変わる。IELTS / Cambridge / 学術 AES は構成・展開を含み、CEFR の Online conversation and discussion と TOEFL Write an Email は短い応答向き。
- 同論点: 段階数は情報源でばらつく（CEFR 6〜7 段階、Cambridge / TOEFL 0〜5 の 6 段階、IELTS 0〜9）。天井到達の懸念には段階数だけでなく各段階の記述子の細かさが効く。
- 同論点: レジスター・appropriateness を独立観点として持つ一次情報源は CEFR の Sociolinguistic appropriateness、TOEFL Write an Email、Grammarly の Delivery の 3 つ。他では他観点に埋め込まれている。
