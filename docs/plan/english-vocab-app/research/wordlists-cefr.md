# CEFR レベル基準の汎用語彙リスト調査

- 調査日: 2026-09-07
- 調査手段: メインセッションによる一次情報確認（WebSearch / WebFetch / curl でのライセンス原文取得。サブエージェントは使用していない）
- 問い: CEFR レベル（A1〜C2 相当）が付与された英語の汎用語彙リストのうち、無料で入手でき、かつユーザー課金のある商用アプリに組み込んで再配布できる（NC 不可、ShareAlike は要注意扱い）ものはどれか。

## 結論

調べた範囲では、**無条件で「商用アプリへの組み込み・再配布が可」と言えるのは CEFR-J Wordlist（東京外国語大学 投野研究室）とその C1/C2 拡張（Octanove Vocabulary Profile）、および CEFR-J を元データとする派生データセット Words-CEFR-Dataset（MIT ライセンス）のみ**だった。

- **CEFR-J Wordlist**（Ver.1.6）は東京外国語大学投野研究室が「適切な引用を行えば研究教育および商用においても無償で利用できる」と明記しており、NC 条項がない独自ライセンス。A1〜B2 の 4 段階のみで、C1/C2 は含まれない。
- **Octanove Vocabulary Profile（C1/C2）** は CEFR-J エコシステムの拡張データで CC BY-SA 4.0（NC なし、ShareAlike あり）。CEFR-J と組み合わせれば A1〜C2 をひとまず揃えられる。
- **English Vocabulary Profile（Cambridge/English Profile）**、**Oxford 3000/5000/Phrase List（OUP）**、**Pearson GSE Vocabulary / Teacher Toolkit** は、いずれも一次情報（各社の利用規約・著作権表示）で「個人・非商用（またはクラスルーム）利用限定」「事前の書面許可なしに複製・再配布不可」と明記されており、**商用アプリへの組み込みは不可**。
- **Council of Europe の Threshold / Waystage / Vantage**（Van Ek & Trim）は Cambridge University Press と Council of Europe の著作物であり、書面許可のない複製を禁じる著作権表示がある。English Profile サイトで閲覧できるが再配布は不可。
- **EFLLex（CEFRLex / CENTAL, UCLouvain）** は CC BY-NC-SA 4.0 と明記されており、NC 条項により**不可**。
- **Kelly Project の英語版ワードリスト**は、オンライン検索ツール（kelly.sketchengine.co.uk）でのみ提供されており、まとまったファイルとしての配布・その際のライセンスが確認できなかった（スウェーデン語版は情報源によって CC-BY-SA 3.0/LGPL 3.0 と CC BY 4.0 の記載が食い違っており、かつ英語版そのものの条件ではない）。**要確認**。

「無料で見られる」ことと「商用アプリに同梱して再配布できる」ことは別物であり、Cambridge・Oxford・Pearson・Council of Europe 系はすべて前者のみを満たし後者を満たさない、という切り分けが今回の一次情報確認で明確になった。

## 一覧表

| リスト名 | 語数 | レベル体系 | ライセンス | 商用可否 | 形式 |
| --- | --- | --- | --- | --- | --- |
| CEFR-J Wordlist（投野研, Ver.1.6） | 7,801 エントリ（ユニーク見出し語 6,868） | CEFR A1〜B2（4段階） | 独自ライセンス（引用条件付き無償・商用可、非公式再配布時も要引用） | 可 | Excel(.xlsx) / PDF（非公式 CSV ミラーあり、v1.5） |
| Octanove Vocabulary Profile C1/C2（CEFR-J拡張） | 約2,136エントリ（CSV行数-ヘッダより概算） | CEFR C1〜C2 | CC BY-SA 4.0 | 可（ShareAlike遵守が条件） | CSV |
| English Vocabulary Profile（Cambridge/English Profile） | 約7,000見出し語（サイト説明ベース、未検証） | CEFR A1〜C2 | Cambridge University Press & Assessment 一般利用規約（個人・非商用限定） | 不可 | Web検索のみ（一括ダウンロード不可） |
| Oxford 3000（OUP） | 3,000語 | CEFR A1〜B2 | OUP著作権表示のみ。書面許可なく複製・配布不可 | 不可 | PDF |
| Oxford 5000（OUP） | 5,000語（3000語+追加2000語） | CEFR A1〜C1 | 同上 | 不可 | PDF |
| Oxford Phrase List（OUP） | 750フレーズ | CEFR A1〜C1 | 同上 | 不可 | PDF |
| Pearson GSE Vocabulary / Teacher Toolkit | 約36,000項目（学習目標含む、語彙単体の数は未確認） | GSE（10〜90スケール）、CEFR相当表記あり | Pearson利用規約（個人・非商用・クラスルーム利用限定） | 不可 | Webツール（検索・PDF出力のみ、一括DL不可） |
| Kelly Project 英語版ワードリスト | 記載なし（スウェーデン語版は8,425語） | CEFR A1〜C2 | 未確認（英語版の一括配布ファイル・ライセンス表記が見当たらず） | 要確認 | オンライン検索ツールのみ |
| Threshold / Waystage / Vantage（Council of Europe, Van Ek & Trim） | 記載なし | CEFR相当（Waystage≒A2, Threshold≒B1, Vantage≒B2） | Cambridge University Press / Council of Europe著作権（書面許可なき複製禁止） | 不可 | PDF（English Profileサイトで閲覧のみ） |
| EFLLex（CEFRLex, CENTAL/UCLouvain） | 15,280レンマ | CEFR A1〜C1（5段階、C2除く） | CC BY-NC-SA 4.0 | 不可（NC） | CSV（タブ区切り） |
| Words-CEFR-Dataset（Maximax67, GitHub） | 記載なし（SQLite DB、約20MB） | CEFR-J準拠（A1〜B2中心） | MIT（GitHub上のLICENSEファイルで確認） | 可（ただし基礎データはCEFR-J由来である点に留意） | SQLite DB / Pythonモジュール(cefrpy) |
| UniversalCEFR（参考、語彙リストではなくCEFR注釈テキストコーパス集） | - | CEFR全般 | データセットごとに異なる（多くがCC BY-NC-SA等のNC系） | 不可（多くがNC） | Hugging Face Datasets |

## 根拠

- 事実: CEFR-J Wordlist（Ver.1.6、2020年3月24日更新）は、A1:1,166／A2:1,411／B1:2,445／B2:2,779 の計7,801エントリ（ユニーク見出し語6,868）から成る。著作権表示は「本語彙表の著作権は東京外国語大学投野研究室に帰属するが、適切な引用を行っていただければ研究教育および商用においても無償で利用できる。」ただし「商用利用に関しては、監修などを行う場合には別途相談の上、必要な経費を請求する。」という留保が付いている。引用書式は「『CEFR-J Wordlist Version 1.6』東京外国語大学投野由紀夫研究室。（URL: XXX より◎年◎月ダウンロード）」。
  - URL: http://www.cefr-j.org/download.html
  - 出典日付: 2020-03-24（ページ記載のVer.1.6更新日）
  - 確度: 高

- 事実: CEFR-J データセットの GitHub ミラー（openlanguageprofiles/olp-en-cefrj、CEFR-J Vocabulary Profile Ver.1.5 を収録）の README に「CEFR-J vocabulary and grammar profile datasets can be used for research and commercial purposes with no charge, provided that you cite the dataset properly. The copyright belongs to Tono Laboratory at TUFS.」と明記。Octanove Vocabulary Profile（C1/C2、Ver.1.0）については「can be used under a Creative Commons Attribution-ShareAlike 4.0 International License」と明記。リポジトリに独立したLICENSEファイルはなく、README内のTerms of useが根拠。
  - URL: https://github.com/openlanguageprofiles/olp-en-cefrj (README.md)
  - 出典日付: 記載なし（最終更新日はGitHub上で確認できるが本文に日付記載なし。2020-01-20時点のCEFR-J Ver.1.5を参照と明記）
  - 確度: 高

- 事実: Octanove Vocabulary Profile C1/C2（CSV）は2,137行（ヘッダ含む）＝実質約2,136エントリ。ライセンスはCC BY-SA 4.0。
  - URL: https://github.com/openlanguageprofiles/olp-en-cefrj/blob/master/octanove-vocabulary-profile-c1c2-1.0.csv
  - 出典日付: 記載なし
  - 確度: 中（行数は目視カウントではなくwcコマンドによる概算）

- 事実: English Vocabulary Profile（English Profile / Cambridge）のサイトフッターには「Copyright 2024 Cambridge University Press & Assessment」「Terms of Use」へのリンクがあり、リンク先の Cambridge 一般Webサイト利用規約には「Only use the Site and its content for personal, non-commercial purposes.」「Do not... [商用利用等の禁止事項]」と明記されている。EVP専用の別ライセンスページは見つからず、Cambridgeサイト共通の利用規約が適用されると判断した。
  - URL: https://www.cambridge.org/legal/website-terms-of-use （englishprofile.org/wordlists/evp のフッターからリンクされる、2025-03-26時点のWayback Machineアーカイブ経由で確認: http://web.archive.org/web/20250326081621/https://www.englishprofile.org/wordlists/evp ）
  - 出典日付: 2024年（Cambridge側の著作権表示年）／アーカイブ取得日 2025-03-26
  - 確度: 中（EVP固有のライセンスページを直接確認できず、サイト共通規約からの推定を含むため）

- 事実: Oxford 3000™・Oxford 5000™・Oxford Phrase List™ のPDF（OUP公式配布）は、各ページフッターに「© Oxford University Press」の著作権表示のみがあり、複製・再配布を許諾する文言は含まれていない。Oxford Learner's Dictionaries API の一般利用規約（Legal Notice）には「all such rights are reserved and no materials may otherwise be copied, modified, published, broadcast or otherwise distributed without our prior written permission.」と明記されている。Oxford 5000は「Oxford 3000に加えB2-C1レベルの単語2000語を追加した拡張リスト」、Oxford Phrase Listは「750 common phrases from A1 to C1 level」と明記。
  - URL: https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000.pdf ／ The_Oxford_5000.pdf ／ https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-phrase-list/Oxford%20Phrase%20List.pdf ／ https://developer.oxforddictionaries.com/legal-notice
  - 出典日付: 記載なし（PDF自体に発行日表記なし）
  - 確度: 高（PDF本文とOUP一般規約の両方を直接確認）

- 事実: Pearson の Web サイト利用規約には「Users are permitted to view, print and download the material for personal, non-commercial and class room use only」「Users are not entitled to modify the content of this Site or reproduce, republish, distribute, transmit... without the express permission of Pearson.」と明記されている。GSE Vocabulary は Teacher Toolkit というWebツール経由でのみ提供され、一括ダウンロード可能なファイル形式（CSV等）や別建ての商用ライセンスは確認できなかった。
  - URL: https://www.pearson.com/languages/terms-of-use.html
  - 出典日付: 記載なし
  - 確度: 高

- 事実: Kelly Project について、Språkbanken（イェーテボリ大学）のページはスウェーデン語版Kellyリストを「distributed under the license agreement CC-BY-SA 3.0, LGPL 3.0」と説明する一方、Hugging Face上の`codesue/kelly`データセット（同じくスウェーデン語版）のデータセットカードは「CC BY 4.0」と記載しており、情報源間で食い違いがある。英語版Kellyリストは kelly.sketchengine.co.uk のオンライン検索インターフェースでのみ言及があり、まとまった配布ファイルやその際のライセンス表記は見つからなかった。
  - URL: https://spraakbanken.gu.se/en/projects/kelly ／ https://huggingface.co/datasets/codesue/kelly ／ https://kelly.sketchengine.co.uk/
  - 出典日付: 記載なし
  - 確度: 低（英語版固有の情報が確認できていないため）

- 事実: Threshold Level（Van Ek, 1990版）の文書には「This book is in copyright」という趣旨の著作権表示があり、Cambridge University PressおよびCouncil of Europeの書面許可なしに複製できない。Waystage・Vantage・Threshold の各タイトルはEnglish Profileサイトからダウンロード（閲覧）できるが、これは公開＝再配布許諾を意味しない。
  - URL: https://ealta.eu/documents/resources/Threshold-Level_CUP.pdf （検索結果からの二次確認、原文の著作権表示文言は検索結果内引用に基づく）
  - 出典日付: 記載なし（原著1990年版）
  - 確度: 中（PDF原本を自分で開いての一字一句確認はできておらず、検索結果に含まれた引用に依拠）

- 事実: EFLLex（CEFRLexプロジェクト、CENTAL/UCLouvain）は「Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License」の下で公開されている。15,280レンマを収録し、CEFR A1〜C1（5段階、C2は除く）にわたる頻度分布を持つ。データ形式はタブ区切りCSV（UTF-8、8列）。
  - URL: https://cental.uclouvain.be/cefrlex/efllex/download/ ／ https://cental.uclouvain.be/cefrlex/efllex/
  - 出典日付: 記載なし（原論文はDürlich & François, 2018）
  - 確度: 高

- 事実: Words-CEFR-Dataset（GitHub, Maximax67）のLICENSEファイルはMITライセンスの全文であることを直接確認した。READMEには「CEFR-J vocabulary database」を基礎データとして利用し、Google Books 1-gramsの頻度データやspaCy/LemmInflectでの語形変化処理を組み合わせて未収録語にもレベルを推定付与していると説明されている。
  - URL: https://github.com/Maximax67/Words-CEFR-Dataset （LICENSE, README.md）
  - 出典日付: 記載なし（Copyright (c) 2024 Belikov Maxim との表記あり）
  - 確度: 高（LICENSEファイル原文を直接確認）

- 事実: UniversalCEFR（Hugging Face上のCEFR注釈テキストコーパス集、13言語505,807テキスト）は、収録元データセットの多くが「permissive license for non-commercial research (e.g., Creative Commons, CC-BY-NC)」の下で提供されることを前提として構築されており、個別データセット（例: `UniversalCEFR/cefr_sp_en`, `UniversalCEFR/readme_en`）はCC BY-NC-SA 4.0などNC系ライセンスを継承している。なお、これは見出し語リストではなく学習者作文等のテキストコーパスであり、本調査の主題（見出し語+レベル）には直接該当しない。
  - URL: https://huggingface.co/UniversalCEFR ／ https://huggingface.co/datasets/UniversalCEFR/cefr_sp_en ／ https://arxiv.org/html/2506.01419
  - 出典日付: 記載なし（論文公開: 2025年6月、arXiv番号2506.01419より推定）
  - 確度: 中

## グレーゾーン・未確認

- CEFR-J の「商用においても無償で利用できる」という一文と、「商用利用に関しては、監修などを行う場合には別途相談の上、必要な経費を請求する」という一文の関係が不明瞭。単純に語彙データをアプリに組み込むだけなら前者（無償）が適用されると読めるが、「監修」に該当する使い方（投野研の関与を謳う、教材としての品質保証を求めるなど）の場合は別途費用が発生しうる。どこまでが「監修」に該当するかは投野研への確認なしには断定できない。
- Octanove Vocabulary Profile（C1/C2）の正確な収録語数はCSVの行数から概算した値（約2,136）であり、公式なドキュメントに明記された数値ではない。
- English Vocabulary Profile の「約7,000見出し語」という数字は二次情報（検索結果の要約）に基づくもので、englishprofile.org自体がJavaScriptレンダリングのSPAで内容を直接確認できず、正確な語数・レベル別内訳は未確認。
- Kelly Project の英語版ワードリストについて、まとまった配布ファイル（CSV/Excel等）が存在するのか、存在する場合のライセンスが何なのかを一次情報で確認できなかった。スウェーデン語版のライセンス表記がSpråkbankenとHugging Faceで食い違っている点（CC-BY-SA 3.0/LGPL 3.0 vs CC BY 4.0）も未解決。
- Threshold Level (1990) の著作権表示は、原文PDFを自分で開いて確認したのではなく、検索結果に含まれた引用テキストに依拠している。原文PDF（ealta.eu上のPDF）への直接アクセスは今回試みていない。
- Pearson GSE Vocabulary の総語数「36,000項目」はGSE Learning Objectives等を含む数字であり、純粋な語彙（見出し語）だけの数ではない可能性がある。GSE Vocabularyを単体でCSV等の形式でダウンロードできるAPI/機能があるかどうかも確認できなかった。
- Oxford Phrase List の正確な収録内容（750フレーズの詳細な内訳、CEFRレベルごとの件数）は1ページ目のみ確認しており、全4ページの内訳は未集計。
- CEFR-J の GitHub ミラー（openlanguageprofiles/olp-en-cefrj）はVer.1.5であり、公式サイトの最新版（Ver.1.6）とは語数等が微妙に異なる可能性がある。アプリに組み込む際は公式サイトの最新版を直接取得すべき。
- 「その他、GitHub/HuggingFaceにあるCEFR語彙データセット」は今回 Words-CEFR-Dataset / UniversalCEFR の2件のみ深掘りした。同種のデータセットは他にも存在しうるが、網羅的な探索はしていない。

## 影響する論点

- `docs/plan/english-vocab-app/` の open-questions.md（未作成）に立てるべき論点: 「見出し語+レベルのデータソースをCEFR-J（+Octanove C1/C2拡張）に一本化するか、他の目的別リスト（IELTS/TOEIC用語彙など）は別途調達が必要か」。
- 同ディレクトリの decisions.md（未作成）に記録すべき候補: 「CEFR-Jおよびその拡張データを第一候補として採用する。Cambridge/Oxford/Pearson系の語彙リストは商用アプリへの組み込み不可のため候補から除外する」という決定を、オーナーが正式に決めた時点で追記する。
- CEFR-J の商用利用における「監修」費用発生条件の解釈は、投野研への直接確認（メール等）をしない限り断定できない。実装に進む前に確認するかどうかはオーナー判断が必要な未決事項。
