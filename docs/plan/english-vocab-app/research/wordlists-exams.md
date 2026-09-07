# 試験別・頻度別の語彙リスト調査

- 調査日: 2026-09-07
- 調査手段: メイン Claude セッションによる WebSearch / WebFetch での原典確認（サブエージェント不使用）
- 問い: 英単語学習アプリ（IELTS / TOEIC / TOEFL / 日常会話など目的別）の見出し語ソースとして、無料かつ「ユーザー課金のある商用アプリに組み込んで再配布できる」語彙リストは存在するか。

## 結論

- **NGSL ファミリー全体（NGSL / NAWL / TSL / BSL / New Dolch List など、Browne, Culligan, Phillips 作成分）は CC BY-SA 4.0 で、商用利用は明確に可**。ただし ShareAlike 条件があるため、アプリ内でこれらのリスト（またはその改変物）を配布する部分は同じ CC BY-SA 4.0 で提供する義務が生じる可能性が高い。単語自体は事実（arguably 非著作物）としても、リストの選定・構成物としては著作物とみなされ得るため、保守的に ShareAlike 遵守を前提にすべき。
- **公式サイトは newgeneralservicelist.com のみ**。newgeneralservicelist.org は同プロジェクトの FAQ ページで「もはや権限を持たない非公式サイトであり、コピーしたコンテンツを使ってギャンブル関連サイトへ誘導している」と名指しで警告されている。今後の調査・実装で .org 版を参照するのは避けるべき。
- **IELTS・TOEFL には公式の語彙リストが存在しない**（ETS も British Council/IDP/Cambridge も語彙リストを公表していない）。市販・Web の "IELTS/TOEFL vocabulary list" は民間の二次生成物で、出典元コーパスやライセンスがまちまちであり、そのまま商用転載できるかは個別確認が必要。
- **TOEIC には ETS 公式の語彙リストは存在しないが、TSL（TOEIC Service List, NGSL ファミリー）が実質的な代替として使える**。TSL は TOEIC 公式教材そのものではなく「TOEIC 対策教材」150 万語コーパスから作成されており、ETS の著作物を直接転載したものではない。ライセンスは CC BY-SA 4.0 で商用利用可。
- **英検・GTEC には公式の級別語彙リストが存在しない**（確認した範囲では見当たらなかった）。Weblio 等の民間サイトが過去問解析で独自リストを作っているが、これは第三者の二次生成物でありライセンス不明。
- **GSL（West 1953）および Coxhead の AWL はライセンス条文が見当たらない**。特に GSL は 1953 年発行の書籍が原典であり、著作権が生きている可能性が高く、パブリックドメインと決めつけられない。AWL も Victoria University of Wellington のページに商用利用に関する記載が一切ない＝「記載なし」＝商用可否は要確認・要問い合わせ。
- **Paul Nation の BNC/COCA word family lists は CC BY-SA 4.0 または GNU GPL v2/v3** で配布されており、商用利用は可能と読める。
- **wordfreq（Python パッケージ）は コード Apache License、データ CC BY-SA 4.0** で商用利用可。ただし内部に SUBTLEX（学術的に許可を得た二次利用）や Google Books Ngrams など複数出典が混在しており、CSV 化するとライセンス表示が失われる点に注意が必要、との記載あり。
- **SUBTLEX-US/UK は著者 Marc Brysbaert から「学術目的に限らずあらゆる目的での配布・利用」の許可を得ている**とされる（wordfreq 経由の記載）。ただし SUBTLEX 自体の一次配布元（Ghent 大学 CRR）の利用規約は今回未確認。
- **frequencywords（hermitdave, OpenSubtitles 由来）はコード MIT・データ CC BY-SA 4.0 で商用利用可**。ただし元データが映画・TV字幕（OpenSubtitles corpus）であり、字幕テキスト自体の著作権に触れない「単語の出現頻度カウント」という体裁のため実務上のリスクは低いと考えられるが、一次配布元（OPUS/OpenSubtitles）側の規約は今回未確認。
- **COCA/Word Frequency Data（wordfrequency.info / wordfrequency.org, Mark Davies）は無料版が上位 5,000 語相当のみで、規約上「コピー・転売・自社サービスとして提示することの禁止」「他製品への統合はブロックされ得る」と明記**されており、商用アプリへの組み込みは事実上不可、大規模利用は有償ライセンス契約が必要。
- **Google Books Ngram（本体データセット）は CC BY 3.0 で商用利用可**。ただし構文 n-gram（syntactic ngrams）データセットは CC BY-NC-SA 3.0 であり非商用限定なので、どちらを使うか区別が必要。

## 一覧表

| リスト名 | 語数 | 紐づく試験・レベル | ライセンス | 商用可否 | 形式 |
|---|---|---|---|---|---|
| NGSL 1.2（New General Service List） | 2,809語 | 一般英語（TOEIC 94%カバー等） | CC BY-SA 4.0 | 可 | ダウンロード（Excel/CSV 相当、サイト配布） |
| NAWL（New Academic Word List） | 957語 | アカデミック英語 | CC BY-SA 4.0 | 可 | ダウンロード |
| TSL 1.2（TOEIC Service List） | 1,250語（コアは1,200語との記載もあり） | TOEIC | CC BY-SA 4.0 | 可 | ダウンロード |
| BSL 1.2（Business Service List） | 1,700語 | ビジネス英語 | CC BY-SA 4.0 | 可 | ダウンロード |
| New Dolch List (NDL) 1.1 | 874語 | 子ども向け基礎語彙 | CC BY-SA 4.0 | 可 | ダウンロード |
| AWL（Academic Word List, Coxhead） | 570 word families | アカデミック英語 | 記載なし | 要確認 | PDF/リスト |
| GSL（General Service List, West 1953） | 約2,000語 | 一般英語 | 記載なし（原典は書籍・著作権存続の可能性） | 要確認 | PDF等 |
| GSL Bauman & Culligan 版 (1995) | 2,284語 | 一般英語 | 記載なし（未確認） | 要確認 | Web/PDF |
| BNC/COCA word family lists（Paul Nation） | 1,000語×25バンド | 一般英語（頻度帯） | CC BY-SA 4.0 または GNU GPL v2/v3 | 可 | ダウンロード |
| wordfreq（Python パッケージ） | 多言語、数万語規模 | 汎用頻度 | コード: Apache License / データ: CC BY-SA 4.0（一部 SUBTLEX 等の混在出典） | 可（要注意点あり） | pip パッケージ |
| SUBTLEX-US/UK | US: 約74,000語形 | 一般英語（字幕コーパス由来） | 著者許可により「学術以外の目的も含め自由に利用可」（wordfreq 経由の記載） | 可（要一次規約確認） | テキスト/Excel |
| frequencywords（hermitdave, OpenSubtitles由来） | 言語ごとに数万語 | 一般英語ほか多言語 | コード: MIT / データ: CC BY-SA 4.0 | 可 | GitHub 上のテキストファイル |
| COCA / Word Frequency Data（wordfrequency.info） | 無料版: 上位5,000語 / 有料版: 20,000〜60,000語 | 一般英語（頻度） | 独自規約（転売・自社サービス化の禁止、統合ブロックの可能性を明記） | 不可（無料枠は再配布・組込み不可、大規模利用は要有償契約） | Web/購入データ |
| Google Books Ngram（本体データセット） | Nグラムベース、語数は非固定 | 一般英語（通時的頻度） | CC BY 3.0 | 可 | ダウンロード（大容量） |
| Google Books Ngram（syntactic ngrams） | 同上 | 同上 | CC BY-NC-SA 3.0 | 不可 | ダウンロード |
| IELTS 公式語彙リスト | 存在しない | IELTS | 該当なし | 該当なし | 該当なし |
| TOEFL 公式語彙リスト（ETS） | 存在しない | TOEFL | 該当なし | 該当なし | 該当なし |
| TOEIC 公式語彙リスト（ETS） | 存在しない（TSL が代替として利用可能） | TOEIC | 該当なし | 該当なし | 該当なし |
| 英検 公式語彙リスト | 存在しない（確認範囲内） | 英検 | 該当なし | 該当なし | 該当なし |
| GTEC 公式語彙リスト | 存在しない（確認範囲内） | GTEC | 該当なし | 該当なし | 該当なし |

## 根拠

- 事実: NGSL は「Browne, C., Culligan, B., and Phillips, J. is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License」と明記。また FAQ ページでは「Free under Creative Commons, including commercial use」「The lists are free to use, including commercially」とも記載。
  - URL: https://www.newgeneralservicelist.com/new-general-service-list
  - 出典日付: 記載あり（NGSL 1.2 は "released in April of 2023"）
  - 確度: 高

- 事実: NAWL のページに「New Academic Word List by Browne, C., Culligan, B., and Phillips, J. is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License」と明記。収録語数は957語（サイト内表記では963語という記述もあり、原文引用時に957語と957との差異あり＝ページ内表記ゆれの可能性）。NGSL 1.2 と合わせて学術コーパスで92%カバー。
  - URL: https://www.newgeneralservicelist.com/new-academic-word-list
  - 出典日付: 記載なし
  - 確度: 高

- 事実: TSL のページに「TOEIC Service List by Browne, C. and Culligan, B., is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License」と明記。「Based on a 1.5 million word corpus of various TOEIC preparation materials」（=ETS公式教材そのものではなく、市販のTOEIC対策教材コーパス由来）。1,250語で、NGSL 2,809語と組み合わせて「98.5% coverage of the most recent TOEIC tests」。ライセンス範囲外の許諾は「www.charlie-browne.com」で相談可能、との記載あり。
  - URL: https://www.newgeneralservicelist.com/toeic-service-list
  - 出典日付: 記載なし（TSL 1.2 表記）
  - 確度: 高

- 事実: BSL のページに「Business Service List by Browne, C. and Culligan, B., is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License」と明記。1,700語、BSL 1.2、一般的ビジネステキストの97%をカバー。
  - URL: https://www.newgeneralservicelist.com/business-service-list
  - 出典日付: 記載なし
  - 確度: 高

- 事実: New Dolch List のページに「New Dolch List by Browne, C. and Culligan, B., is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License」と明記。874語、NDL 1.1、子ども向け英語テキストの約90%をカバー。
  - URL: https://www.newgeneralservicelist.com/new-dolch-list
  - 出典日付: 記載なし
  - 確度: 高

- 事実: 公式 FAQ ページに「The only official website of the New General Service List Project is newgeneralservicelist.com」との記載があり、.org ドメインについては権限のない非公式サイトで、コピーしたコンテンツを使ってギャンブル関連コンテンツへ誘導していると警告している。
  - URL: https://www.newgeneralservicelist.com/faqs-4
  - 出典日付: 記載なし
  - 確度: 中（Fetch 結果の要約に基づく。ページ全文を目視で再確認できていない）

- 事実: Victoria University of Wellington の Academic Word List（Coxhead）ページには、AWL の利用条件・ライセンス・商用利用に関する記述が一切見当たらない。ページには開発の経緯（Averil Coxhead の修士論文として開発）と570語族という情報のみが記載されている。
  - URL: https://www.wgtn.ac.nz/lals/resources/academicwordlist
  - 出典日付: 記載なし
  - 確度: 中（Fetch による要約確認。二次ページ複数を確認したが明示的ライセンス文言は発見できず）

- 事実: Paul Nation の Resources ページに「These resources may be used under the terms of the Creative Commons Attribution-ShareAlike 4.0 license or the GNU General Public License Version 2 or 3」と明記。BNC/COCA word family lists はこのページ経由で配布。
  - URL: https://www.wgtn.ac.nz/lals/resources/paul-nations-resources
  - 出典日付: 記載なし（BNC/COCA lists の情報 PDF は "17 September 2012" の版あり）
  - 確度: 高

- 事実: GSL（West 1953）および Bauman & Culligan 版（1995）について、eapfoundation.com の解説ページには著作権・パブリックドメイン・ライセンスに関する記述が一切ない。同サイト自体の再利用条件（「教育・非商用目的なら自由に再利用可、要クレジット」）はサイトのコンテンツに対するものであり、GSL リスト自体のライセンスではない。
  - URL: https://www.eapfoundation.com/vocab/general/gsl/
  - 出典日付: 記載なし
  - 確度: 中

- 事実: wordfreq（GitHub: rspeer/wordfreq）の README に「ソフトウェアは Apache license で自由に再配布可能、データファイルは Creative Commons Attribution-ShareAlike 4.0 license で配布」との記載。Google Books Ngrams データは「may be freely used for any purpose」（要クレジット）、SUBTLEX 由来のワードリストは「著者から学術目的に限らずあらゆる目的での利用許可を得ている」との記載。CSV 形式には帰属表示欄がないため CC BY-SA のライセンス要件を満たさない、との注意書きあり。
  - URL: https://github.com/rspeer/wordfreq
  - 出典日付: 記載なし
  - 確度: 高

- 事実: hermitdave/FrequencyWords（OpenSubtitles 由来の頻度リスト）の README に「MIT License for code.」「CC-by-sa-4.0 for content.」と明記。2016年版・2018年版のデータ出典はそれぞれ OPUS の OpenSubtitles2016 / OpenSubtitles2018。
  - URL: https://github.com/hermitdave/FrequencyWords
  - 出典日付: 記載なし（リポジトリの LICENSE ファイルは2016年付与）
  - 確度: 高

- 事実: wordfrequency（Word Frequency Data, Mark Davies, COCA由来）の利用規約に「you may not copy, resell, or present the service as your own」（コピー・転売・自社サービスとしての提示の禁止）、および「Automated access, high-volume requests, or integration into another product may be blocked」（他製品への統合はブロックされ得る）との記載。無料版は上位5,000語相当のみで、20,000〜60,000語版や大規模データは有償。
  - URL: https://wordfrequency.org/terms-of-use
  - 出典日付: 記載なし
  - 確度: 中（wordfrequency.info と wordfrequency.org の関係性を一次情報で明確に確認できていない。同一運営者の別ドメインとみられるが要再確認）

- 事実: Google Books Ngram Viewer のデータセットは Creative Commons Attribution 3.0 Unported License で提供され、「graphs may be used freely for any purpose」（要クレジット）と案内されている。一方、構文 n-gram（syntactic ngrams）データセットは「Creative Commons Attribution-Non Commercial ShareAlike 3.0 Unported License」で非商用限定。
  - URL: http://books.google.com/ngrams/datasets
  - 出典日付: 記載なし
  - 確度: 中

- 事実: IELTS を運営する British Council / IDP / Cambridge のいずれも公式の語彙リストを公表していない。市販・Web の "IELTS vocabulary" コンテンツは第三者（Magoosh, IDP のブログ記事等）によるまとめであり、公式リストではない。
  - URL: https://takeielts.britishcouncil.org/blog/vocabulary-for-ielts （公式ブログの一般的な学習アドバイスであり、単語「リスト」の公表ではないことを確認）
  - 出典日付: 記載なし
  - 確度: 中（「存在しないこと」の証明は悪魔の証明に近く、複数の検索で確認できなかったという消極的事実に基づく）

- 事実: ETS は TOEFL 向けの公式語彙リストを公表していない。市販の "TOEFL vocabulary list"（Magoosh 等）は ETS の公式教材から独自に抽出した非公式のリストである。
  - URL: https://magoosh.com/toefl/toefl-vocabulary-words-from-official-toefl-ibt-tests/
  - 出典日付: 記載なし
  - 確度: 中（同上、消極的事実に基づく）

- 事実: 日本英語検定協会（英検）の公式サイト（eiken.or.jp）には「審査基準」「Can-Do リスト」はあるが、級別の公式語彙リストは見当たらない。Weblio 等が過去問（2004〜2010年度分）を独自解析して級別頻出語リストを作成しているが、これは第三者の二次生成物。
  - URL: https://www.eiken.or.jp/eiken/exam/about/
  - 出典日付: 記載なし
  - 確度: 中

- 事実: ベネッセの GTEC 公式サイトにも公式語彙リストの公表は見当たらない。
  - URL: https://www.benesse.co.jp/gtec/
  - 出典日付: 記載なし
  - 確度: 低（サイト内を網羅的に確認したわけではなく、検索結果ベースの消極的確認）

## グレーゾーン・未確認

- newgeneralservicelist.com の FAQ ページと NGSL/NAWL/TSL/BSL/NDL 各リストページの内容は、WebFetch（要約 AI）経由で取得したものであり、ページ全文を目視で再確認していない。特に .org ドメインへの警告文言は今後の実装判断に影響するため、着手時にはブラウザで直接原文を再確認することを推奨する。
- CC BY-SA 4.0 の「ShareAlike」条件が、単語見出し語そのもの（事実の羅列、著作物性が低い可能性）に及ぶのか、リストという「編集著作物」としての側面に及ぶのかは法的にグレー。訳語・例文を LLM で新規生成した場合でも、見出し語の選定・グルーピング自体を流用すれば ShareAlike 義務が生じ得る、という保守的な解釈を取るべきかは要検討（弁護士確認が望ましい領域）。
- NAWL の収録語数について、公式ページの一部で「957語」、別の二次情報（検索結果の要約）で「963語」という記載のゆれがあった。どちらが最新かは原文の再確認が必要。
- AWL（Coxhead）は Victoria University of Wellington の複数ページを確認したが、明示的なライセンス条文は発見できなかった。「記載なし」を「商用不可の可能性あり」として扱うと、AWL は現時点では商用組み込みの根拠が薄い。Coxhead 本人または大学への問い合わせが必要。
- GSL（West 1953）はパブリックドメインだと紹介する二次情報が多いが、一次のライセンス表明は確認できなかった。1953年の著作物は西の没年（1973年）を基準にすると多くの法域でまだ保護期間内の可能性があり、「古いから自由に使える」という前提は危険。Bauman & Culligan 版（1995, jbauman.com 由来）は、当該サイトへのアクセスができず未確認（DNS解決不可）。
- SUBTLEX-US/UK の一次配布元（Ghent University, crr.ugent.be）の利用規約ページそのものは今回未確認。wordfreq の README 経由の伝聞（「著者から許可を得た」という記載）のみに依拠しており、一次規約文の原文引用ができていない。
- frequencywords の元データである OpenSubtitles/OPUS コーパス自体の利用規約（字幕の著作権）は未確認。頻度カウントという二次生成物であるため実務上のリスクは低いとみられるが、法的な確証はない。
- wordfrequency.info（COCA無料版）と wordfrequency.org（利用規約を確認したドメイン）が同一運営者のものかを一次情報で確定できていない。無料版ページ（wordfrequency.info/free.asp）は403エラーで直接確認できず、規約の適用範囲（無料版にも同じ規約が及ぶか）は推測に留まる。
- IELTS・TOEFL・英検・GTEC について「公式語彙リストが存在しない」という結論は、複数回の検索で見つからなかったという消極的事実に基づく。将来的に公式サイトの構成が変わり公開される可能性、または調査で見落としている可能性は残る。
- wordfreq は開発が事実上停止・アーカイブ状態にあるとの情報を見聞きしたことがあるが、今回のライセンス調査の範囲では確認していない（ライセンス自体には影響しないが、保守性の観点では要確認）。

## 影響する論点

- `docs/plan/english-vocab-app/open-questions.md`（現時点では未作成）に立てるべき論点: 「見出し語ソースは NGSL ファミリー（CC BY-SA 4.0）を第一候補とし、ShareAlike 義務をどう扱うか（アプリの語彙データ部分を CC BY-SA 4.0 で公開するか、独自に語を選定し直すか）」
- 同ディレクトリの決定事項として今後扱うべき論点: 「IELTS/TOEFL/英検/GTEC 向けの見出し語は公式リストが存在しないため、NGSL+NAWL+分野別語彙、または CEFR 準拠の民間リストとの組み合わせで代替する方針にするか」
- AWL・GSL は商用利用の可否が未確定なため、決定を急ぐ場合は NGSL ファミリー（確実に商用可）を優先し、AWL・GSL は「保留」として扱うのが安全側の判断。
- COCA/Word Frequency Data は無料版であっても商用アプリへの組み込みには使えない可能性が高い（規約上の転売・統合禁止）ため、頻度データが必要な場合は frequencywords（hermitdave, MIT/CC BY-SA 4.0）または wordfreq（Apache/CC BY-SA 4.0）を優先候補とすべき。
