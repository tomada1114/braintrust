# 商用アプリに組み込める英単語リストの絞り込み（3 調査の統合 + 原典確認）

- 調査日: 2026-09-07
- 調査手段: Sonnet サブエージェント 3 本（cefr / exams / lexical-data）+ メインセッションによる原典確認・実データのダウンロード検証
- 問い: 「無料で入手でき、ユーザー課金のある商用アプリに組み込んで再配布でき、かつレベルまたは目的が付与されている英単語リスト」は存在するか。

## 結論

存在する。ただし使えるのは 2 系統に限られ、どちらも「試験の公式リスト」ではない。

1. **CEFR レベル軸** — CEFR-J Wordlist（A1〜B2）+ Octanove Vocabulary Profile（C1/C2）。
   合計およそ 9,900 エントリで A1〜C2 が連続して埋まる。同一スキーマ（headword / pos / CEFR）。
2. **目的軸** — NGSL ファミリー（NGSL / TSL / NAWL / BSL / NDL）。すべて CC BY-SA 4.0、商用可を明文で許可。

一方、**IELTS・TOEFL・TOEIC・英検・GTEC のいずれにも、試験実施団体が公表した公式語彙リストは存在しない**。
「IELTS 用」「TOEIC 用」を名乗るには、上記の素材に自前でラベルを付け直すしかない。TOEIC だけは
TSL（TOEIC 対策教材コーパス由来、ETS 非公式）が実質的な代替になる。

商用不可が確定したのは Cambridge English Vocabulary Profile / Oxford 3000・5000 / Pearson GSE /
Council of Europe Threshold 系 / EFLLex（CC BY-NC-SA）/ COCA (wordfrequency.info)。
いずれも「無料で見られる」が「同梱して売れない」側に落ちる。

## 使える素材の一覧

| 素材 | 語数 | 付いている軸 | ライセンス | 形式 |
| --- | --- | --- | --- | --- |
| CEFR-J Wordlist Ver.1.6 | 7,801 エントリ（見出し語 6,868） | CEFR A1〜B2 | 投野研独自（引用を条件に商用も無償） | xlsx（非公式 CSV ミラー: v1.5） |
| Octanove Vocabulary Profile C1/C2 Ver.1.0 | 2,136 エントリ | CEFR C1〜C2 | CC BY-SA 4.0 | CSV |
| NGSL 1.2 | 2,809 語 | 一般英語頻度（日常の約 92% をカバーと主張） | CC BY-SA 4.0 | サイト配布 |
| TSL 1.2（TOEIC Service List） | 1,250 語 | TOEIC | CC BY-SA 4.0 | サイト配布 |
| NAWL | 957 語 | アカデミック（IELTS/TOEFL の代替軸） | CC BY-SA 4.0 | サイト配布 |
| BSL 1.2 | 1,700 語 | ビジネス | CC BY-SA 4.0 | サイト配布 |
| New Dolch List 1.1 | 874 語 | 子ども向け基礎 | CC BY-SA 4.0 | サイト配布 |
| BNC/COCA word family lists（Nation） | 1,000 語 × 25 バンド | 頻度帯 | CC BY-SA 4.0 または GPL v2/v3 | ダウンロード |
| ejdict-hand | — | 英和訳 | CC0 | TSV |
| JMdict/EDICT | — | 英和・和英訳 | CC BY-SA 4.0 + EDRDG 追加条件 | XML |
| Tatoeba | — | 例文（日本語訳付き） | CC BY 2.0 FR（文・投稿者単位） | CSV |
| CMU Pronouncing Dictionary | — | 発音記号 | BSD 類似 | テキスト |

詳細な出典とライセンス原文は `wordlists-cefr.md` / `wordlists-exams.md` / `lexical-data-sources.md` を参照。

## メインセッションが自分で確認した事実

- 事実: CEFR-J の配布ページに「なお、本語彙表の著作権は東京外国語大学投野研究室に帰属するが、適切な引用を行っていただければ研究教育および商用においても無償で利用できる。」と記載。
  続く引用条件に「2)商用利用に関しては、監修などを行う場合には別途相談の上、必要な経費を請求する。」「4)本語彙表を改変して別の語彙表を作ることはかまわないが、必ず本語彙表を適切に引用しなければならない。」とある。
  経費請求は「監修などを行う場合」に係る条件であり、監修を求めずに引用だけして使う分には無償と読める。
  - URL: http://www.cefr-j.org/download.html
  - 出典日付: Ver.1.6 は 2020.3.24 更新版と記載
  - 確度: 高（HTML 原文を直接取得して確認）

- 事実: CEFR-J Wordlist Ver.1.6 の xlsx を実際にダウンロードして中身を検証した。シート構成は
  README / ALL / A1 / A2 / B1 / B2 / ALL_sep / A1_sep / A2_sep / B1_sep / B2_sep。
  ALL シートは 7,801 行（ヘッダを除く）で、列は headword, pos, CEFR, CoreInventory 1, CoreInventory 2, Threshold の 6 列。
  **日本語訳・例文・発音記号・頻度は含まれない。** 見出し語とレベルだけのデータ。
  - URL: http://www.cefr-j.org/data/CEFRJ_wordlist_ver1.6.zip
  - 出典日付: 2020-03-24
  - 確度: 高（ファイルを取得して直接パース）

- 事実: NGSL 公式サイトに "Free under Creative Commons, including commercial use." および
  "New General Service List by Browne, C., Culligan, B., and Phillips, J. is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License." と記載。
  加えて "The lists are free to use, including commercially, and publishers and developers have built real products on them." とあり、商用利用が明示的に想定されている。
  - URL: https://www.newgeneralservicelist.com/
  - 出典日付: フッタに © 2026 Dr. Charles Browne
  - 確度: 高（HTML 原文を直接取得して確認）

- 事実: `newgeneralservicelist.org`（.org）は現在ギャンブル系サイトに置き換わっており、NGSL とは無関係。
  公式サイトにも "The only official site of the NGSL Project is newgeneralservicelist.com" と明記されている。
  過去の技術記事やブックマークが .org を指していることがあるため、参照時は必ず .com を使う。
  - URL: http://www.newgeneralservicelist.org/ （取得して内容を確認、カジノ系コンテンツ）
  - 出典日付: 2026-09-07 時点
  - 確度: 高（メインセッションが直接取得）

- 事実: Octanove Vocabulary Profile C1/C2 は Open Language Profiles リポジトリで配布されており、
  README に "The Octanove Vocabulary Profile for C1/C2 levels can be used under a Creative Commons Attribution-ShareAlike 4.0 International License." と記載。
  同 README は CEFR-J 側についても "CEFR-J vocabulary and grammar profile datasets can be used for research and commercial purposes with no charge, provided that you cite the dataset properly." と英語で明記しており、投野研の日本語表記と整合する。
  CSV の実データは 2,136 行（ヘッダ除く）、列は headword, pos, CEFR, notes。CEFR-J と同一スキーマで結合できる。
  - URL: https://github.com/openlanguageprofiles/olp-en-cefrj
  - 出典日付: 記載なし（CEFR-J Wordlist は Ver.1.5 を 2020-01-20 取得と記載）
  - 確度: 高（README と CSV を直接取得）

## グレーゾーン・未確認

- CEFR-J のライセンスは Creative Commons ではなく独自の許諾文である。「適切な引用」の具体的な様式
  （アプリ内のどこに、どの粒度で出すか）は明文化されていない。アプリ規模で使う前に投野研究室へ
  一度確認するのが安全。**特に「見出し語だけ抜き出してレベルを付け替えた派生リスト」を配布する場合の扱いは条文が沈黙している。**
- CC BY-SA 4.0 の ShareAlike が「アプリに同梱した語彙データ」にどこまで及ぶかは、単語リストが
  著作物として保護されるか（選択・配列の創作性）に依存し、法的にグレー。保守的には、同梱した
  リスト部分は CC BY-SA 4.0 のまま提供する前提で設計すべき。アプリのソースコード側には及ばないと
  EDRDG は明言しているが、これは JMdict についての見解であって NGSL についての見解ではない。
- Octanove の C1/C2 は 2,136 語と小さく、CEFR-J（A1〜B2）とは作成主体もコーパスも異なる。
  A1〜C2 を「ひと続きの尺度」として扱ってよいかは検証していない。
- AWL（Coxhead）と GSL（West 1953）はライセンス表記が存在しない。GSL は 1953 年の書籍が原典で
  著作権が生きている可能性があり、パブリックドメインと決めつけられない。
- IELTS のバンドスコアと語彙を紐づける公開データは見つからなかった。CEFR と IELTS の対応表
  （British Council 等が出す目安）を経由して間接的に紐づけるしかない。この対応表自体の
  ライセンスと精度は未確認。
- 発音音声は「無料 × 再配布可」の選択肢が実質存在しない。TTS API 各社の出力キャッシュ・同梱の
  可否は一次規約から確定できなかった。

## 影響する論点

- `open-questions.md` の「どの軸でレベルを切るか」「CEFR-J の引用義務をどう満たすか」
  「ShareAlike をどこまで被せるか」「IELTS/TOEFL の帯をどう自作するか」。
