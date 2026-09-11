# 試験スコアと CEFR の公式対応表調査

- 調査日: 2026-09-10
- 調査手段: メイン Claude セッションによる WebSearch / WebFetch（PDF は curl + pdftotext で本文を直接抽出し、AI 要約に頼らず原文を目視確認）での原典確認（サブエージェント不使用）
- 問い: IELTS（Academic）/ TOEFL iBT / TOEIC L&R / TOEIC S&W / 英検（CSE スコア）/ Cambridge English Scale について、試験団体が公式のスコア→CEFR 対応表を公表しているか。公表されている場合、その粒度は IELTS 6.0 / 6.5 / 7.0 のような近接スコアを CEFR 上で区別できるほど細かいか。これらの対応表は語彙難易度に触れているか。CEFR Companion Volume の「プラスレベル」は内部スケールの候補になり得るか。

## 結論

- 調べた 6 つの試験・スケールすべてで、試験団体自身（または共同運営組織）による公式のスコア→CEFR 対応表が存在する。「公式対応表が存在しない」試験はなかった。
- ただし粒度には大きな差がある。**IELTS と TOEIC（L&R・S&W）は CEFR の 1 レベルに複数の生スコア／バンドをまとめて割り当てるだけで、レベル内部を区別する仕組みを持たない**。IELTS の 6.0 と 6.5 はどちらも公式には B2 の範囲内であり、C1 になるのは 7.0 から。IELTS 公式ページ自身が「C1 の閾値は 6.5 と 7 の間のどこかにあり、6.5 の受験者の多くは C1 だが一部はわずかに届かない」とボーダーラインの存在を明言しており、一対一の精密な対応ではないと釘を刺している。
- **TOEFL iBT は 2026 年 1 月 21 日から 1〜6 点（0.5 刻み）の新スケールに移行し、CEFR 整合を設計に最初から組み込んだ**としているが、公表されている対応は「C1 = 5 と 5.5」のように 1 つの CEFR レベルに 2 つの半刻みスコアをまとめて割り当てる形であり、CEFR 側をさらに細分しているわけではない（0.5 刻みの精度が CEFR レベルの中間点を表すわけではない）。
- **英検の CSE スコアは技能ごとに連続値を持つが、CEFR ラベルが公式に付くのは 5 段階（A1〜C1、C2 表記なし）の下限値のみ**で、レベル内部の細分（プラスレベル等）は公式には示されていない。
- **Cambridge English Scale が、調べた中では最も粒度が細かい**。80〜230 の連続尺度に加え、各 CEFR レベル内をさらに Grade A / B / C の 3 段階に分けて認定しており、さらに「境界付近はスコアの前後 3 点程度を目安に慎重に見るべき」という数値ベースの注意書きまで公式に持つ。ただし、この Grade A/B/C はあくまで「特定の資格試験（例: Cambridge English: Advanced）内での成績評価」であり、IELTS の 6.0 と 6.5 のような「試験横断で任意の 2 点を細かく区別する」用途に転用できる保証はない。
- どの対応表も「話す・書く・読む・聞くの総合的な英語運用能力」についてのものであり、**個々の単語の難易度をこれらのスコアや CEFR レベルにひも付けるという記述は、6 つの一次資料のいずれにも見つからなかった**（想定どおりの沈黙。グレーゾーンに明記）。
- CEFR Companion Volume（Council of Europe, 2018 年 2 月版）は "plus levels"（A2+、B1+、B2+ など）を正式に定義しており、これは「次のレベルの基準にはまだ届かないが、そのレベルの特徴が現れ始めている、非常に強い到達度」を表す区分。ただし CEFR 本体の主要 3 表（Table 1〜3、六段階の共通参照レベル表）にはプラスレベルの記述子は含まれておらず、あくまで補助的・任意的な細分という位置づけである。

## 根拠

- 事実: IELTS の公式比較ページに、IELTS バンドスコアと CEFR の対応について「IELTS band scores have never aligned exactly with the CEFR transition points」「Some IELTS band scores are shown as borderline (e.g. it is not clear whether band 5 is B1 or B2)」「a C1 minimum threshold would fall between the 6.5 and 7 bands on the IELTS scale. Therefore, whilst many 6.5 test takers would be at C1, a number will be marginally below」「Band scores of 8.5 and higher are recognised as C2. Band 8 is borderline」と明記されている。厳密な数値表というより、CEFR とのおおよその対応関係とその不確実性を文章で説明する構成。
  - URL: https://ielts.org/organisations/ielts-for-organisations/compare-ielts/ielts-and-the-cefr
  - 出典日付: 記載なし
  - 確度: 高

- 事実: ETS 公式ページに、TOEFL iBT が「In January 2026, TOEFL introduced an updated score scale (from 1 – 6 in increments of 0.5)」と明記され、"TOEFL SCORE SCALE (1-6) V. CEFR" という対応表（Total・Reading・Listening・Writing・Speaking 共通）で C2=6、C1=5〜5.5、B2=4〜4.5、B1=3〜3.5、A2=2〜2.5、A1=1〜1.5 と対応づけられている。2026〜2028 年の移行期間中はスコアレポートに旧 0-120 点も併記される。
  - URL: https://www.ets.org/toefl/institutions/ibt/score-scale-update.html
  - 出典日付: 記載なし（新スケールの発効日は 2026-01-21 と明記）
  - 確度: 高（同一ページを 2 回、異なる抽出プロンプトで確認し、内容が一致）

- 事実: ETS Global（ETS の欧州法人）配布の「TOEIC® Listening and Reading Test Scores and the CEFR Levels」（PDF）に、Total スコア（10〜990 点）の CEFR 対応表が明記されている：C1 = 945 点以上（Listening 490 点以上・Reading 455 点以上）、B2 = 785 点以上（Listening 400 点以上・Reading 385 点以上）、B1 = 550 点以上（Listening 275 点以上・Reading 275 点以上）、A2 = 225 点以上（Listening 115 点以上・Reading 110 点以上）、A1 = 120 点以上（Listening 60 点以上・Reading 60 点以上）。C2 の記載はなく、上限は C1。出典は Tannenbaum, R.J., & Wylie, E.C. (2006) による標準設定研究とされ、「ETS does not recommend to use the minimum cut scores strictly」という留保が付く。
  - URL: https://www.eu.ets.org/content/dam/ets-org/eu/pdfs/toeic/mapping-cefr-toeic-listening-reading-test.pdf
  - 出典日付: Copyright © 2025 by ETS Global B.V.（文書コード MAR090）
  - 確度: 高（PDF 本文を pdftotext で直接抽出し目視確認）

- 事実: 同じく ETS Global 配布の「TOEIC® Speaking and Writing Tests Scores and the CEFR Levels」（PDF）に、Speaking／Writing 各スコア（0〜200 点、10 点刻み）の CEFR 対応表が明記されている：C1 = Speaking 180 点以上・Writing 180 点以上、B2 = Speaking 160 点以上・Writing 150 点以上、B1 = Speaking 120 点以上・Writing 120 点以上、A2 = Speaking 90 点以上・Writing 70 点以上、A1 = Speaking 50 点以上・Writing 30 点以上。総合スコアは算出されないと明記。こちらも同じ Tannenbaum & Wylie (2006) の標準設定研究に基づく。
  - URL: https://www.eu.ets.org/content/dam/ets-org/eu/pdfs/toeic/toeic-4-skills-tests-mapping-table.pdf
  - 出典日付: Copyright © 2025 by ETS Global B.V.（文書コード MAR1058）
  - 確度: 高（PDF 本文を pdftotext で直接抽出し目視確認）

- 事実: 日本英語検定協会の公式ページに、英検 CSE スコアと CEFR の対応が技能別・4 技能総合の両方で示されている。4 技能総合スコアでは C1 = 2600 点以上、B2 = 2300 点以上、B1 = 1950 点以上、A2 = 1700 点以上、A1 = 1400 点以上（C2 の表記なし）。技能別（Reading/Listening/Writing/Speaking）の下限値も個別に掲載されている。対応表の根拠として「平成30年3月版の『各資格・検定試験とCEFR対照表』」（文部科学省の作業部会資料）を参照している旨の記載がある。また「4技能すべてを受験しないと『4技能総合CEFR』は表示されない」「4級・5級は CEFR 算出範囲外」との注記がある。
  - URL: https://www.eiken.or.jp/cse/
  - 出典日付: 記載なし
  - 確度: 中（WebFetch の要約に基づく。ページの表そのものをブラウザで目視再確認していない点は他の情報源より確認密度が低い）

- 事実: 文部科学省の作業部会資料にも、英検を含む各資格・検定試験と CEFR の対照表が掲載されている（英検 CSE スコアの対応表の一次的な典拠として、公益財団法人 日本英語検定協会のページから参照されている文書）。
  - URL: https://www.mext.go.jp/b_menu/shingi/chousa/koutou/091/gijiroku/__icsFiles/afieldfile/2018/07/27/1407616_003.pdf
  - 出典日付: 平成30年3月版（2018年3月）
  - 確度: 中（検索結果のタイトルから存在を確認したのみで、PDF 本文は今回未確認）

- 事実: Cambridge English（Cambridge University Press & Assessment）の 2015 年版ファクトシートに、Cambridge English: Advanced（142〜210 点のスケール）を例として、CEFR レベルとの対応が具体的に示されている：200〜210 点＝Grade A（C2 認定）、193〜199 点＝Grade B（C1 認定）、180〜192 点＝Grade C（C1 認定）、160〜179 点＝B2 認定、142〜159 点＝認定書なし（Statement of Results のみ）。CEFR レベルと試験内グレードの両方が同じ数値尺度上で表現されている。
  - URL: https://www.cambridgeenglish.org/images/167506-cambridge-english-scale-factsheet.pdf
  - 出典日付: 2015年4月（"April 2015" と明記）
  - 確度: 高（PDF 本文を pdftotext で直接抽出し目視確認）

- 事実: Cambridge English の 2023 年版ガイド（"The Cambridge English Scale explained"）に、A2 Key／B1 Preliminary の各技能（Reading・Writing・Listening・Speaking）ごとの模擬試験スコア→Cambridge English Scale スコア→CEFR レベルの換算表が複数掲載されている。そこから読み取れる Cambridge English Scale 全体の CEFR 境界値は、A1 = 100 点以上、A2 = 120 点以上、B1 = 140 点以上、B2 = 160 点以上、C1 = 180 点以上、C2 = 200 点以上（尺度全体は 80〜230）。また「境界に近いスコアは慎重に扱うべきで、目安として達成に必要なスコアの前後 3 点程度（例: B2 レベルなら 157〜163 点）を境界として見るべき」との数値付きの注意書きがある。文末に「All details are correct at the time of going to print in November 2023.」と明記。
  - URL: https://www.cambridgeenglish.org/images/210434-converting-practice-test-scores-to-cambridge-english-scale-scores.pdf
  - 出典日付: 2023年11月（"All details are correct at the time of going to print in November 2023." と明記）
  - 確度: 高（PDF 本文を pdftotext で直接抽出し、複数技能の換算表から境界値を突き合わせて確認）

- 事実: Council of Europe の CEFR Companion Volume（2018年2月版）に、"plus levels"（例: A2+ または A2.2）について「the CEFR introduced the idea of the plus levels」「Plus levels represent a very strong competence at a level that does not yet reach the minimum standard for the following criterion level. Generally, features of the level above are starting to appear」「Descriptors from the 'plus levels' are not included in the three tables that introduce the CEFR levels (CEFR Tables 1, 2 & 3)」と明記されている。プラスレベルは元々 2001年版 CEFR の Section 3.5 で導入された概念であり、Companion Volume はそれを踏襲・強化した位置づけ。
  - URL: https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2018/1680787989
  - 出典日付: 2018年2月（"© Council of Europe, February 2018" と明記。この文書は 2018 年の草案版で、正式版は 2020 年に "Companion Volume 2020" として公開されている）
  - 確度: 高（PDF 本文を pdftotext で直接抽出し目視確認。ただし今回確認したのは 2018 年版であり、2020 年正式版の該当箇所は未確認）

## グレーゾーン・未確認

- 単語の難易度をこれらの試験スコア・CEFR レベルにひも付ける記述は、6 つの一次資料のいずれにも存在しなかった。すべて「4技能の総合的な運用能力」についての対応表であり、語彙アプリが必要とする「この単語は CEFR のどのレベルか」という粒度の情報は、これらの公式資料の守備範囲の外にある。CEFR 自体には語彙シラバス（vocabulary specifications）を各言語の教育機関が別途作る慣習があるが、それは CEFR や各試験団体自身が公表しているものではなく、今回の調査範囲外（`research/wordlists-cefr.md` 等の既存調査を参照）。
- 英検 CSE スコアの対応表は WebFetch の要約に基づいており、公式ページの表をブラウザで直接目視再確認していない。実装判断に使う前に一度、ブラウザで `eiken.or.jp/cse/` を開いて数値を再確認することを推奨する。
- TOEIC の「4-skills-tests-mapping-table.pdf」は実質的に「Listening & Reading」用と「Speaking & Writing」用の 2 種類の資料を 1 ファイルに束ねたもので、ファイル名から中身を予測しづらい。別に見つけた「ETS-TOEIC Link-CEFR flyer」（`ets.org/pdfs/toeic/mapping-toeic-link-cefr.pdf`）は主力の TOEIC Speaking and Writing ではなく、オンライン簡易版の「TOEIC Link」というモジュール式アセスメント（0〜25点の技能別スケール）の対応表であり、別物だった。TOEIC 関連 PDF は名称の紛らわしさがあるため、参照時は URL とスケールの範囲（0〜200 か 0〜25 か）を必ず確認する必要がある。
- Cambridge English Scale の 2015 年版ファクトシートと 2023 年版ガイドは、境界値自体（A1=100, A2=120, B1=140, B2=160, C1=180, C2=200）は整合していたが、2015 年版は特定の資格試験（Advanced）内のグレード区切りを例示する構成、2023 年版は技能別の模擬試験換算表という構成で、直接比較できる同一形式の一枚表を一次資料から得られたわけではない。境界値は複数の技能別表を突き合わせて導出したものであり、Cambridge 自身が単一の「全体像の表」として明記しているわけではない点は留意。
- CEFR Companion Volume は今回 2018 年の草案版（rm.coe.int 上の PDF）を確認した。2020 年に公式版として "Companion Volume 2020" が別途公開されているとされるが、今回はアクセスできず（`coe.int` の該当ページは 403 で直接取得不可）、2020 年版でプラスレベルの説明が変わっていないかは未確認（変更は考えにくいが、断定はしない）。
- TOEFL iBT の新スケールと CEFR の対応表について、ページ本文をブラウザで目視した生の表そのもの（画像やテーブルタグ）を直接確認したわけではなく、WebFetch（AI要約）による抽出を 2 回行い内容が一致したことで確度を「高」としている。移行直後で ETS 側のページ構成が今後変わる可能性もあるため、実装時期が近づいたら再確認が望ましい。
- IELTS 公式ページには「6.0 と 6.5 がどちらも B2、7.0 から C1」という明確な数値の切れ目を示す一文までは見当たらず、境界の曖昧さを強調する記述が中心だった。非公式サイト（ielts.international、IELTS 運営団体とは無関係と自ら明記）は「IELTS 6.5 falls within the CEFR B2 range」「CEFR C1 starts at IELTS 7.0」と明確に言い切っていたが、これは二次情報であり、IELTS 公式の立場（「厳密な一対一対応ではない」）とはニュアンスが異なる。内部スケールの設計では、公式が認める「境界の曖昧さ」自体を無視しないほうがよい。

## 影響する論点

- `docs/plan/english-vocab-app/open-questions.md` の「IELTS のバンドと語彙の対応をどう作り、どう名乗るか」に対する材料: 公式のスコア→CEFR 対応表は存在するが、粒度は粗い。IELTS・TOEIC は CEFR 1 レベルに複数のバンド／スコア帯をまとめており、「IELTS 7.0 相当の単語」は言えても「6.5 相当」と「7.0 相当」を公式対応表だけで区別することはできない。CEFR を内部スケールに採用する場合、「試験の目標スコアを CEFR に変換する」段階で既に 1 段階分の粒度の粗さが混入することを前提に置く必要がある。
- 同論点への追加材料: Cambridge English Scale は Grade A/B/C という細分を持つが、これは Cambridge の各資格試験専用の仕組みであり、IELTS や TOEIC のスコアをこのグレードに変換する公式な方法は確認できていない。試験横断で CEFR より細かい共通スケールを作りたい場合、Cambridge English Scale をそのまま流用するのではなく、CEFR Companion Volume の「プラスレベル」（A2+, B1+, B2+）を内部スケールの目盛りとして自前で採用し、各語をどのプラスレベルに置くかはアプリ側の自己申告にする、という設計のほうが筋が通る（ただし、これは推奨であり決定ではない）。
- `research/wordlists-exams.md` で確認済みの「IELTS・TOEFL・英検・GTEC には公式の語彙リストが存在しない」という結論と合わせると、「語彙難易度そのものを CEFR やスコアに公式にひも付ける手段はどこにも存在しない」という点が二重に裏付けられた。CEFR ベースのレベル付けを採用しても、それは「試験の総合得点の目安」を借りているだけであり、単語 1 つ 1 つのレベルづけの正しさを担保するものではないことを、アプリのどこかで明示する必要がある。

## メインセッションによる原典確認（2026-09-10）

- https://ielts.org/organisations/ielts-for-organisations/compare-ielts/ielts-and-the-cefr を直接確認した。公式の対応図があり、次の記載がある。本文の記載と矛盾しない。確度: 高（ページに日付の表示はない）
  - "As IELTS preceded the CEFR, IELTS band scores have never aligned exactly with the CEFR transition points."
  - "a C1 minimum threshold would fall between the 6.5 and 7 bands on the IELTS scale."
