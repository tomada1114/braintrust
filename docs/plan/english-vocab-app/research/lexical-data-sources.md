# 語彙リスト周辺データ（訳・例文・発音・辞書API・語形変化）のライセンス調査

- 調査日: 2026-09-07
- 調査手段: メインセッションによる一次情報の直接確認（`curl` / WebFetch で配布元ページ・LICENSE ファイル・利用規約原文を取得）。一次情報が Cloudflare 等でブロックされた一部の TTS API・辞書 API については WebSearch の二次情報を用いたうえで、可能な範囲で一次ページ（サービス条項本文）を再取得して裏取りした。裏取りできなかった箇所は個別に明記した。
- 問い: 英単語アプリの見出し語に付随する周辺データ（和訳・英和辞書データ、例文コーパス、発音記号・音声、辞書 API、語形変化データ）のうち、(1) 無料で入手でき、かつ (2) ユーザー課金のある商用アプリに組み込んで再配布できるものはどれか。

## 結論

無料かつ商用アプリへの組み込み・再配布が明確に可能なのは、**JMdict/EDICT 系（EDRDG）、Wiktionary/kaikki.org（Wiktextract）、Princeton WordNet、日本語 WordNet、ejdict-hand、CMU Pronouncing Dictionary、LibriVox、AGID/SCOWL（ESDB）、spaCy モデル・spacy-lookups-data**である。ただし JMdict 系と Wiktionary 系は CC BY-SA（+ Wiktionary は GFDL 併記）であり、ShareAlike の対象は「配布するデータそのもの」であって「アプリのソースコード」ではないことを EDRDG が明文で確認している（後述）。とはいえ帰属表示は軽くない義務（アプリ内に専用の About/Sources 画面を設け、辞書データを月1回以上更新する等）を課しており、「使えるが要注意」に分類すべき。

**例文コーパスは Tatoeba のみが候補になる。** OPUS/OpenSubtitles は原版が CC BY-NC-SA（NC=非営利限定）で、Hugging Face 版（OpenSubtitles2024）は表示上 ODC-BY だが「著者は字幕内容の著作権を主張しない」「削除ポリシーあり」という注記があり、字幕そのものの原著作権（映画・TV スタジオ）がクリアになっていない可能性が高い。有料アプリに組み込むデータとしては法的リスクが高く、**採用しないことを推奨**する。Tatoeba も CC BY 2.0 FR で商用利用自体は否定されていないが、ライセンスは文単位で投稿者に紐づき帰属表示義務も文単位のため、大量利用時の運用コストは軽くない。

**発音音声は無料×再配布可の選択肢がほぼ存在しない。** Forvo は無料 API が非商用限定な上、有料プランでも「音声のキャッシュは一切禁止」と明記されており、オフライン利用前提のアプリには根本的に使えない。Wikimedia Commons の音声はファイルごとにライセンスが異なり（CC BY / CC BY-SA / CC0 など）、一括利用には個別ライセンス確認とファイル単位の帰属表示が必要で、実務上は「要確認」止まり。LibriVox はパブリックドメインで商用利用に制限はないが、単語単位の発音ではなく朗読音源なので、そのままでは単語アプリの発音データとして機能しない。**現実的には TTS API（Google Cloud / Azure / OpenAI / ElevenLabs）でオンデマンド生成し、キャッシュ可否は各社の商用プラン・規約を個別に確認した上でキャッシュする方針が最有力**になる。ただし「無料で」の条件は TTS API 各社とも実質満たせない（無料枠はあるが商用利用が制限される、または量が少ない）ため、絶対条件①（無料）は満たさず、絶対条件②（商用再配布可否）についても各社ばらつきがあり、個別に確認を要する（下記グレーゾーン参照）。

**辞書 API は軒並み「無料かつ商用再配布可」を満たさない。** Merriam-Webster Developer API は無料枠が明文で非商用限定。Wordnik API は商用利用とキャッシュの両方を明文で禁止。Oxford Dictionaries API は商用利用自体はできるが有料 Enterprise プラン必須（年額目安 £5,000/言語）でキャッシュも Enterprise 限定。dictionaryapi.dev（Free Dictionary API）は利用規約・データライセンスの明文が存在せず、サーバーコード自体は GPLv3、データは Wiktionary 由来と推測されるものの音声フィールドは Google がホストする出典不明の mp3 を指しており、ボランティア運営で SLA もない。商用アプリの本番データソースとして採用するのは根拠不足であり、**辞書 API は却下、辞書データは JMdict/Wiktionary/WordNet 系のダンプを自前で保持する方針が妥当**と考えられる。

**語形変化・品詞データ**は AGID/SCOWL（現 ESDB）が BSD 的な自由ライセンスで商用利用可、spaCy のモデル・spacy-lookups-data も MIT で問題ない。NLTK 経由でのデータ配布は per-corpus でライセンスが異なるため、必要なコーパスごとの確認が必要（WordNet 自体は NLTK 経由でも Princeton の元ライセンスがそのまま付く）。

## 一覧表

| データ | 用途 | ライセンス | 商用可否 | 帰属表示義務 | 形式 |
|---|---|---|---|---|---|
| JMdict/EDICT（EDRDG） | 日英・英日訳、見出し語データ | CC BY-SA 4.0（EDRDG 独自の追加条件付き） | 可 | あり（作品への謝辞＋アプリ内 About 画面等での明記＋月1回以上のデータ更新義務） | XML |
| JMdict-simplified（GitHub） | JMdict の JSON/派生形式 | JMdict/JMnedict部分は EDRDG ライセンス継承、Kanjidic部分は CC BY-SA 4.0、npmパッケージ本体は MIT | 可（データ部分は要注意） | あり（元データと同様） | JSON |
| Wiktionary本文 / kaikki.org（Wiktextract） | 英英定義・語源・IPA・例文 | データ: CC BY-SA 4.0 + GFDL（二重ライセンス）／抽出ツール(wiktextract)自体: MIT | 可（データはShareAlike対象） | あり | JSON/JSONL |
| Princeton WordNet | 英英シソーラス、同義語・階層関係 | WordNet 独自ライセンス（SPDX: WordNet、OSI承認の許諾的ライセンス） | 可 | あり（著作権表示の保持のみ、ShareAlike無し） | DB/テキスト |
| 日本語WordNet（NICT, bond-lab/wnja） | 日本語シソーラス、和訳の裏付け | WordNet と同型の許諾的ライセンス（NICT） | 可 | あり（著作権表示の保持のみ） | DB/TSV |
| ejdict-hand（GitHub） | 簡易英和辞書 | CC0 1.0（パブリックドメイン） | 可 | なし | テキスト/TSV |
| Tatoeba | 例文とその日本語訳 | CC BY 2.0 FR（文・投稿者単位） | 可（投稿者依存、文単位で要確認） | あり（文・投稿者単位） | CSV/TSV |
| OPUS / OpenSubtitles | 例文コーパス（字幕由来） | 原版 CC BY-NC-SA 3.0（NC）／HF版は表示上 ODC-BY だが原著作権の帰属が不明瞭 | 不可（NC）〜要確認（HF版も権利関係が不明瞭） | あり（ODC-BY版） | TSV |
| CMU Pronouncing Dictionary | 英語発音記号（ARPAbet） | BSD類似の独自許諾ライセンス（Carnegie Mellon） | 可 | あり（著作権表示の保持） | テキスト |
| Wiktionary IPA | 発音記号(IPA) | Wiktionary本文と同じ CC BY-SA 4.0 + GFDL | 可 | あり | JSON（kaikki.org経由等） |
| Wikimedia Commons 音声 | 発音音声ファイル | ファイルごとに異なる（CC BY / CC BY-SA / CC0 / PD 等） | 要確認（ファイル単位） | あり（ファイル単位、ライセンスにより異なる） | OGG/MP3 |
| Forvo（無料API） | 発音音声（ネイティブ録音） | 独自ライセンス：Attribution・非商用・ShareAlike（商用プランは別途契約） | 不可（無料枠は非商用、有料でもキャッシュ禁止） | あり（無料枠でも表示義務） | 音声リンク（都度取得、2時間有効） |
| LibriVox | 朗読音声（パブリックドメイン書籍） | パブリックドメイン | 可（ただし単語単位の発音データではない） | なし | MP3 |
| Google Cloud Text-to-Speech | 発音音声のオンデマンド生成 | Google Cloud利用規約 + Generative AI追加条項（生成物はCustomer Dataとして顧客に帰属） | 要確認（無料枠は少量・出力の長期キャッシュ/同梱可否の明文未確認） | 記載なし | 生成音声(有料API) |
| Azure AI Speech (TTS) | 発音音声のオンデマンド生成 | Microsoft Product Terms / Cognitive Services規約（有料ティアなら出力に追加ライセンス不要） | 要確認（無料ティアの商用可否は情報が錯綜、有料ティアは概ね可） | AI生成である旨の開示義務あり | 生成音声(有料API) |
| OpenAI TTS（API） | 発音音声のオンデマンド生成 | Business Terms（Output所有権は顧客、一次情報未直接確認）／Service Terms（ChatGPT Voice Outputは非商用・単体配布禁止と明記、TTS APIとは別条項） | 要確認（API出力自体は商用可とされるが一次のBusiness Terms本文を直接確認できず） | AI生成である旨の開示義務あり | 生成音声(有料API) |
| ElevenLabs | 発音音声のオンデマンド生成 | Terms of Use（Freeプランは非商用限定、Paidプランは商用利用・Services外での利用も許可、ただしOEM組み込みは別途OEM Terms） | 可（有料プランのみ）／不可（無料プラン） | プランにより異なる（Freeは帰属表示義務あり） | 生成音声(有料API) |
| Free Dictionary API (dictionaryapi.dev) | 英英定義・発音音声リンク取得 | サーバーコード: GPLv3／データ自体の利用規約・ライセンス明記なし（Wiktionary由来と推測） | 要確認（データのライセンス不明、SLAなし、音声リンクの出典も不明） | 記載なし | REST API (JSON) |
| Wordnik API | 英英定義・使用例 | 独自利用規約（商用利用・キャッシュを明文で禁止） | 不可 | あり（表示改変禁止） | REST API (JSON) |
| Merriam-Webster Developer API | 英英定義 | 独自ライセンス契約（無料枠は明文で非商用限定） | 不可（無料枠）／要確認（有料契約） | あり | REST API (XML/JSON) |
| Oxford Dictionaries API | 英英定義 | 独自利用規約（商用利用可だがEnterpriseプラン必須、キャッシュもEnterprise限定） | 不可（無料枠は商用不可・評価用のみ） | あり | REST API (JSON) |
| AGID/SCOWL（現ESDB, en-wl/wordlist） | 語形変化・スペルバリエーション・品詞 | Copyright by Kevin Atkinson、BSD類似の許諾的ライセンス（一部派生ソースは追加条件あり） | 可（基本ワードリストは可、サイズ80超やAU版などは追加条件を要確認） | あり（著作権表示の保持） | テキスト/SQLite |
| spaCy 言語モデル (en_core_web_*) | 品詞タグ付け・レンマ化 | MIT | 可 | なし（実務上は記載推奨） | バイナリモデル |
| spacy-lookups-data | レンマ変換ルックアップテーブル | MIT | 可 | なし（実務上は記載推奨） | JSON |
| NLTK data（各コーパス） | WordNet等の同梱データ配布経路 | コーパスごとに個別ライセンス（README単位）。WordNet自体はPrinceton版と同一ライセンスがそのまま付与 | 要確認（コーパスごとに異なる） | コーパスによる | NLTK data形式 |

## 根拠

### JMdict / EDICT / KANJIDIC（EDRDG 一般辞書ライセンス）

- 事実: EDRDG の辞書ファイル（JMDICT, EDICT, KANJIDIC 等）は Creative Commons Attribution-ShareAlike License (V4.0) の下で配布される。商用利用に制限はなく、ソフトウェア自体をオープンソースにする義務もない。
  > "The dictionary files are made available under a Creative Commons Attribution-ShareAlike Licence (V4.0)."
  > "there is NO restriction placed on commercial use of the files. The files can be bundled with software and sold for whatever the developer wants to charge. Software using these files does not have to be under any form of open-source licence."
  帰属表示義務についても具体的に規定されている（スマートフォンアプリの場合、メニューからアクセスできる専用画面での明記が必要、起動画面だけでは不十分）。
  > "For smartphone and tablet apps, acknowledgement must be made, e.g. on a separate screen accessed from a menu, such as one labelled 'About', 'Sources', etc. It is not sufficient just to mention it on a start-up/launch page of the app."
  また、辞書ファイルを利用するアプリ・サーバーは最新版への定期更新義務を負う。
  > "If a software package, WWW server, smartphone app, etc. uses the files or incorporates data from the files, there must be a procedure for regular updating of the data from the most recent versions available... Failure to keep the versions up-to-date is a violation of the licence to use the data."
  - URL: https://www.edrdg.org/edrdg/licence.html
  - 出典日付: 記載なし（ページ本文に更新日の明記なし。ライセンス自体はCC BY-SA 4.0への移行後のもの）
  - 確度: 高（EDRDG公式ライセンスページの原文を直接確認）

### JMdict-simplified（GitHub: scriptin/jmdict-simplified）

- 事実: JMdict/JMnedict の元 XML は EDRDG の著作物であり EDRDG のライセンスに準拠して使用されている。派生ファイル（JSON化データ）もすべて元のライセンスと同一条件で配布される。Kanjidic 由来データは CC BY-SA 4.0。npm パッケージ自体（コード）は MIT。
  > "The original XML files ... are the property of the Electronic Dictionary Research and Development Group, and are used in conformance with the Group's license."
  > "All derived files are distributed under the same license, as the original license requires it."
  - URL: https://github.com/scriptin/jmdict-simplified （README.md License セクション）
  - 出典日付: 記載なし（リポジトリの現行 README を取得）
  - 確度: 高（GitHub上のREADME原文を直接取得）

### Wiktionary 本文・IPA / kaikki.org（Wiktextract）

- 事実: Wiktionary の本文（定義・語源・例文・IPA発音表記を含む）は CC BY-SA 4.0 と GFDL の二重ライセンスで公開されている。
  > "The original texts of Wiktionary entries are dual-licensed to the public under both the Creative Commons Attribution-ShareAlike 4.0 International License (CC-BY-SA) and the GNU Free Documentation License (GFDL)."
  > "your materials have to be licensed under the same, similar, or compatible license, you must attribute the work in the manner specified by the author or licensor"
  - URL: https://en.wiktionary.org/wiki/Wiktionary:Copyrights
  - 出典日付: ページ内に「This page is outdated. It dates to 2002」との注記があるが、ライセンス条項自体（CC BY-SA 4.0 / GFDL）は現行のWiktionary標準ライセンスと一致
  - 確度: 高（Wiktionary公式ポリシーページの wikitext を直接取得）
- 事実: kaikki.org のデータは Wiktextract というツールで Wiktionary から機械的に抽出したものであり、抽出ツール自体（コード）は MIT ライセンスだが、抽出された辞書データそのものは Wiktionary のライセンス（CC BY-SA / GFDL）がそのまま適用される。
  > "Copyright (c) 2018-2020 Tatu Ylonen ... This package is free for both commercial and non-commercial use. It is licensed under the MIT license." （wiktextract の README、対象はツールのコード）
  > "Certain files under tests/ are under Wiktionary license (CC-BY-SA or GFDL at your choice)."（LICENSE ファイル冒頭）
  - URL: https://github.com/tatuylonen/wiktextract （README.md License節、LICENSEファイル）
  - 出典日付: 記載なし（現行mainブランチを取得）
  - 確度: 中（wiktextract ツールのライセンスは直接確認できたが、kaikki.org 自体の配布ページ https://kaikki.org/dictionary/rawdata.html にはライセンスに関する明示的な記述が見当たらず、「データはWiktionary由来だからWiktionaryのライセンスが適用される」という解釈は妥当だが kaikki.org 運営者自身の明文の確認はできていない）

### Princeton WordNet

- 事実: WordNet は商用アプリケーションでの利用を含め、無償・無条件（著作権表示の保持のみを条件）で利用・複製・改変・配布が許諾される独自ライセンス。ShareAlike（同一条件での再配布義務）は課されていない。
  > "Permission to use, copy, modify and distribute this software and database and its documentation for any purpose and without fee or royalty is hereby granted, provided that you agree to comply with the following copyright notice and statements, including the disclaimer, and that the same appear on ALL copies of the software, database and documentation, including modifications that you make for internal use or for distribution."
  > "The name of Princeton University or Princeton may not be used in advertising or publicity pertaining to distribution of the software and/or database."
  - URL: https://wordnet.princeton.edu/license-and-commercial-use
  - 出典日付: ライセンス本文中に「WordNet 3.0 is copyrighted 2006 by Princeton University」との記載
  - 確度: 中（当該URLはCloudflareに保護されており直接アクセスできなかったため、WebSearchの検索結果スニペットに含まれるライセンス全文を採用。同一の文言はSPDXのWordNetライセンス項目（https://spdx.org/licenses/WordNet.html）とも一致しており、内容自体の信頼性は高い）

### 日本語WordNet（NICT, bond-lab/wnja）

- 事実: Princeton WordNet と同型の独自許諾ライセンス。商用利用を含め無償で利用・複製・改変・配布が許諾され、著作権表示の保持のみが条件。
  > "Permission to use, copy, modify and distribute this software and database and its documentation for any purpose and without fee or royalty is hereby granted, provided that you agree to comply with the following copyright notice and statements..."
  > "The name of the National Institute of Information and Communications Technology may not be used in advertising or publicity pertaining to distribution of the software and/or database."
  - URL: https://raw.githubusercontent.com/bond-lab/wnja/master/docs/license.txt （GitHubリポジトリ bond-lab/wnja のLICENSEファイルが指すファイル）
  - 出典日付: ファイル冒頭に "Copyright: 2021-2024 Francis Bond, Takayuki Kuribayashi" 等の記載あり。ライセンス条項自体の制定日は記載なし
  - 確度: 高（GitHub上のライセンスファイル原文を直接取得）

### ejdict-hand（GitHub, 英和辞書データ）

- 事実: CC0 1.0（パブリックドメイン）で公開されており、商用利用・再配布・改変のいずれにも制限がなく、著作権表示義務もない。
  - URL: https://github.com/kujirahand/EJDict （README.md および LICENSE）
  - 出典日付: 記載なし
  - 確度: 中（サブエージェント経由のWebFetch要約による確認。LICENSEファイル原文そのものの引用取得はできておらず、CC0である旨はREADMEの記述を根拠にしている）

### Tatoeba

- 事実: テキスト文（例文）のデフォルトライセンスは CC BY 2.0 FR。商用利用そのものは一般には否定されていないが、最終的な可否は投稿者（コントリビューター）の選択に依存する。
  > "Creative Commons Attribution 2.0 France license (CC-BY 2.0 FR) for the use of textual sentences."
  > "We are not generally opposed to using our content for commercial purposes. However, this choice depends primarily on contributors."
  - URL: https://tatoeba.org/en/terms_of_use
  - 出典日付: 記載なし
  - 確度: 中（WebFetchによる要約引用。ページ自体は取得できたが構造上テキスト全文の直接grepができなかったため、要約された引用文の原文照合は簡易的なもの）

### OPUS / OpenSubtitles

- 事実: OPUS の Subtitles コーパス（旧版）は CC BY-NC-SA 3.0（非営利限定）で配布されている。Hugging Face 上の新しい OpenSubtitles2024 データセットは ODC-BY ライセンスを掲げているが、著作権者は字幕テキストの所有権を主張しておらず、削除ポリシー（takedown policy）を維持している。
  > "This dataset is released under the ODC-BY license. The dataset redistributes subtitle texts originally contributed to OpenSubtitles.org."
  > "The authors do not claim ownership of the subtitle content and maintain a takedown policy for copyright holders."
  - URL: https://huggingface.co/datasets/Helsinki-NLP/OpenSubtitles2024
  - 出典日付: 記載なし
  - 確度: 中（Hugging Faceのデータセットカード記述を直接確認。ただし原版OPUSのCC BY-NC-SA表記についてはWebSearchの二次情報のみで、opus.nlpl.eu上の一次ページを直接照合できていない）

### CMU Pronouncing Dictionary

- 事実: BSD類似の独自許諾ライセンス。著作権表示の保持を条件に、ソース・バイナリ形式いずれでも再配布・改変・商用利用が許可される（ShareAlike無し）。
  > "Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: 1. Redistributions of source code must retain the above copyright notice... 2. Redistributions in binary form must reproduce the above copyright notice..."
  - URL: https://raw.githubusercontent.com/cmusphinx/cmudict/master/LICENSE
  - 出典日付: "Copyright (C) 1993-2015 Carnegie Mellon University"
  - 確度: 高（LICENSEファイル原文を直接取得）

### Wikimedia Commons 音声ファイル

- 事実: Wikimedia の利用規約は、投稿者に対しコンテンツの自由な再利用・再配布を許諾するライセンスの付与を義務付けているが、実際に適用されるライセンスはファイルごとに異なる（CC BY、CC BY-SA、CC0、パブリックドメインなど）。
  > "all users contributing to the Projects or Project Websites are required to grant broad permissions to the general public to redistribute and reuse their contributions freely"
  - URL: https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use
  - 出典日付: 記載なし
  - 確度: 中（Terms of Useの一般原則は確認できたが、個別の発音音声ファイルのライセンス分布や具体的な帰属表示フォーマットまでは未確認。大量の単語発音音声を集める場合、ファイル単位でのライセンス調査・帰属管理コストが発生する点は「グレーゾーン」として扱う）

### Forvo（発音音声API）

- 事実: 無料APIプランの利用規約は「帰属表示・非商用・ShareAlike」であり、商用プランのみ商用利用が可能。加えて、音声リンクの生成後2時間しか有効でなく、**キャッシュ（ローカル保存）自体が明文で禁止**されている。
  > "Forvo general rules and terms of use applies. Basically: Attribution, non-commercial and share-alike, except for the commercial plans."
  > "When you generate an audio link using Forvo API it's valid during the next 2 hours. If you want to reuse it after that time it won't work. Important: It is not allowed to cache audio pronunciations."
  - URL: https://api.forvo.com/documentation/general-information/
  - 出典日付: 記載なし
  - 確度: 高（Forvo API公式ドキュメントページの原文を直接取得）

### LibriVox

- 事実: LibriVox の録音はすべてパブリックドメインであり、商用利用を含め用途に制限はない。
  > "All LibriVox audio is in the public domain, so you may use it for whatever purpose you wish."
  - URL: https://librivox.org/pages/public-domain/ （WebSearchで確認、LibriVox Wiki「Copyright and Public Domain」も同旨）
  - 出典日付: 記載なし
  - 確度: 中（二次情報（WebSearch要約）による確認。LibriVoxの公式ページ本文の直接取得・原文grepは行っていない。ただし内容はLibriVoxの一貫した公表方針と整合）

### Google Cloud Text-to-Speech

- 事実: Google Cloud の生成AIサービスにおける生成物（Generated Output）は顧客データ（Customer Data）として扱われ、Google は生成物に新たな知的財産権を主張しない。
  > "Generated Output is Customer Data. As between Customer and Google, Google does not assert any ownership rights in any new intellectual property created in the Generated Output."
  - URL: https://policies.google.com/terms/generative-ai （WebSearchのスニペットで確認。cloud.google.com/terms/service-terms の一次ページはWebFetchで直接取得したが、Text-to-Speech固有の商用利用・キャッシュ条項は見当たらなかった）
  - 出典日付: 記載なし
  - 確度: 低〜中（一般的な生成AI利用規約の原則としての出力所有権は確認できたが、Text-to-Speech APIに固有の「生成音声を商用アプリにキャッシュ・同梱して再配布してよいか」を明記した条項は発見できなかった。実務上はGoogle Cloud Platform利用規約全体・音声合成APIの利用制限を専門家レビューする必要がある）

### Azure AI Speech（Text-to-Speech）

- 事実: 有料（従量課金）ティアであれば、生成された音声出力を商用目的で利用するために追加のライセンスやロイヤリティの支払いは不要。無料ティアでの商用利用可否については情報源間で食い違いがある。
  - URL: https://learn.microsoft.com/en-us/answers/questions/1192398/can-i-use-azure-text-to-speech-for-commercial-usag （Microsoft Q&A、コミュニティ回答であり一次の利用規約文書そのものではない）
  - 出典日付: 記載なし
  - 確度: 低（Microsoft Learn Q&Aのコミュニティ回答をWebSearchで集約したものであり、Microsoft Product Terms や Cognitive Services 利用規約の一次条文そのものを直接取得・引用できていない。無料ティアの商用可否について複数の質問スレッドで見解が割れている点も含め、要専門家確認）

### OpenAI（Chat/TTS API の出力）

- 事実: OpenAI Service Terms（2026年6月12日更新版、一次情報を直接取得）には、ChatGPT の「Voice Conversations」機能で生成される音声（ChatGPT Voice Output）について、非商用利用限定であり単体の音声ファイルとして配布・再パッケージ化することを明確に禁止する条項がある。
  > "ChatGPT Voice Output is for non-commercial use only and may not be distributed or repackaged as a standalone audio recording or any other sound file. Any rights in Output assigned to you do not include ChatGPT Voice Output."
  - URL: https://openai.com/policies/service-terms/
  - 出典日付: ページ内に "Updated: June 12, 2026" と明記
  - 確度: 高（この条項自体はService Termsの原文を直接取得して確認）
- 事実: 一方、`api.openai.com` 経由の TTS（Audio API）出力の所有権・商用利用条件を定める箇所は OpenAI の Business Terms 側にあるとみられるが、当該ページ（openai.com/policies/business-terms/ 等）は Bot対策により403でアクセスできず、一次情報での直接確認ができなかった。
  - URL: https://openai.com/policies/business-terms/ （アクセス不可、403）
  - 出典日付: 記載なし
  - 確度: 低（二次情報では「APIのOutputは顧客に帰属し商用利用可、ただしChatGPT Voice Outputの非商用制限はAPI TTSには及ばない」とされているが、一次条文で確認できていない）

### ElevenLabs

- 事実: 生成音声（Output）の所有権はユーザー側に残る。無料プランは非商用利用限定、有料プランは商用利用が可能で、Services外での利用も規約とProhibited Use Policyに従う限り許可される。アプリへの組み込み（OEM的な利用）については別途「OEM Terms」が適用される。
  > "Except as expressly set forth herein, as between you and ElevenLabs, you retain all rights in and to your Output."
  > "you may only use the Services for non-commercial purposes"（Freeプラン）
  > "you may use the Services for commercial purposes"（Paidプラン）
  > "you are permitted to use such Output outside of the Services but always subject to these Terms and our Prohibited Use Policy"
  - URL: https://elevenlabs.io/terms-of-use
  - 出典日付: 記載なし
  - 確度: 高（Terms of Useページの原文を直接取得。ただしOEM Terms自体は別文書であり中身は未確認）

### Free Dictionary API（dictionaryapi.dev）

- 事実: GitHub上のソースリポジトリ（meetDeveloper/freeDictionaryAPI）は GPLv3 でライセンスされている。ただし、これはAPIサーバーの「コード」のライセンスであり、APIが返す辞書データ自体の利用規約やライセンスを明記した文書は見当たらなかった。README には運営コストの逼迫と寄付（Buy Me a Coffee）の呼びかけが書かれており、SLAの明記もない。
  - URL: https://github.com/meetDeveloper/freeDictionaryAPI （LICENSE, README.md）
  - 出典日付: 記載なし
  - 確度: 高（GPLv3であること自体はLICENSEファイル原文で確認）。ただしデータ自体のライセンスは確度が低い（後述グレーゾーン参照）

### Wordnik API

- 事実: 利用規約で、商用利用とキャッシュ（ローカル保存）の両方が明確に禁止されている。
  > "(c) Use the Wordnik API for commercial uses (i.e., charging end users for access to or selling the Wordnik Data to third parties as a separate service from the authorized applications You create);"
  > "(e) Cache, record, pre-fetch or otherwise make or store local copies of the Wordnik content or Wordnik Data, including without limitation making calls for the purpose of creating, or actually creating, an independent store of the Wordnik Data."
  - URL: https://developer.wordnik.com/terms
  - 出典日付: 記載なし
  - 確度: 高（利用規約ページの原文を直接取得）

### Merriam-Webster Developer API

- 事実: 無料枠の利用規約タイトル自体が「NON-COMMERCIAL USE OF MERRIAM-WEBSTER DICTIONARY API」であり、明文で商用利用が禁止されている。商用利用したい場合は別途連絡し条件・支払いについて交渉する必要がある。
  > "NON-COMMERCIAL USE OF MERRIAM-WEBSTER DICTIONARY API"
  > "you agree not to: ... (b) use the Service for commercial use"
  > "If your usage will exceed any of these terms (A-C above), a request and details must be sent to us via a contact form on the API site. Merriam-Webster staff will then respond to arrange terms and payment."
  - URL: https://www.dictionaryapi.com/info/terms-of-service
  - 出典日付: 記載なし
  - 確度: 高（利用規約ページの原文を直接取得）

### Oxford Dictionaries API

- 事実: 商用プロジェクトでのAPI利用自体は許可されているが、無料のSandbox（500コール）は評価用であり、非商用利用のための代替プランは提供されていない。データのキャッシュ・オフライン保存はEnterpriseプラン契約者のみに許可される。
  > "Can I use the API in a commercial project? Use of the Oxford Dictionaries API as a commercial product is permitted in line with our terms and conditions."
  > "Is there a plan for non-commercial use? ... We do not offer any other alternative plan for non-commercial use."
  > "Can I cache data? Caching or any saving and use of the data offline is only permitted under an Enterprise license."
  - URL: https://developer.oxforddictionaries.com/faq
  - 出典日付: 記載なし
  - 確度: 高（FAQページの原文を直接取得）

### AGID / SCOWL（現 English Speller Database, en-wl/wordlist）

- 事実: 語形変化・スペルバリエーションデータの中核部分は Kevin Atkinson による著作権表示のもと、無償での利用・複製・改変・配布・販売が許諾されている（BSD類似の許諾的ライセンス）。ただし一部の派生データ（オーストラリア英語データ、UKACD由来のサイズ80超ワードリスト）には追加の著作権条件が付く。
  > "Permission to use, copy, modify, distribute, and sell any part of the English Speller Database (ESDB, previously known as SCOWLv2), or word lists created from it, is hereby granted without fee, provided that the above copyright notice appears in all copies..."
  > "If you are using the Australian English dictionary ... then the copyright after '=== AU' applies. If you are using a generated word list larger than 80, the copyright after '=== UKACD' applies."
  - URL: https://raw.githubusercontent.com/en-wl/wordlist/v2/Copyright
  - 出典日付: "Copyright 2000-2026 by Kevin Atkinson"
  - 確度: 高（Copyrightファイル原文を直接取得）

### spaCy 言語モデル / spacy-lookups-data

- 事実: spaCy の英語モデル（en_core_web_sm/md/lg等）はMITライセンスで配布されている。レンマ化のルックアップテーブルを提供する spacy-lookups-data パッケージも同様にMITライセンス。
  > MIT License, Copyright (c) 2019 ExplosionAI GmbH（spacy-lookups-dataのLICENSEファイル原文）
  - URL: https://raw.githubusercontent.com/explosion/spacy-lookups-data/master/LICENSE （spacy-lookups-dataは直接取得）／spaCyモデル自体のMITライセンスはWebSearchの二次情報（spacy.io/modelsの記載内容の要約）による
  - 出典日付: 記載なし
  - 確度: 高（spacy-lookups-data）／中（spaCyモデル本体：一次のspacy.io/modelsページを直接取得はしていない）

### NLTK data（各コーパスの配布）

- 事実: NLTK が配布するコーパスはコーパスごとに個別のREADME・ライセンスが付与されており、一律のライセンスは存在しない。WordNet自体はNLTK経由で入手してもPrinceton版と同一のライセンス文が付与される。
  - URL: 二次情報（WebSearch要約）に基づく。NLTKデータの一次配布ページ（nltk.org/nltk_data/、GitHub nltk/nltk_data）への直接アクセスは404等で失敗し、一次テキストでの直接確認はできていない。
  - 出典日付: 記載なし
  - 確度: 低（一次情報未確認。NLTK経由でWordNet等を利用する場合は、結局Princeton/NICTの原本ライセンスを直接参照するほうが確実という結論に留める）

## グレーゾーン・未確認

- **JMdict/Wiktionary系のShareAlikeの実務上の射程**: EDRDGは「アプリのソースコードをオープンソースにする必要はない」と明言しているが、これは「辞書データそのものを改変・再配布する場合、そのデータ部分は同等ライセンスで公開せよ」という意味であり、アプリ内で辞書データをそのまま参照するだけであれば実務上問題になりにくい。ただしLLMで生成した訳語・例文をJMdict由来の訳語と混在させた「派生データベース」を作った場合、その混在データがShareAlikeの対象になるかどうかは条文上明確ではなく、法的にはグレー。
- **OPUS/OpenSubtitlesの原著作権**: ODC-BYやCC BY-NC-SAという「データセットとしてのライセンス」表示と、字幕そのものの原著作権（映像スタジオ等）が誰にあるかは別問題。運営者自身が「所有権を主張しない」「削除ポリシーがある」と明言している時点で、法的にクリーンな権利関係とは言えない。有料商用アプリへの組み込みは非推奨。
- **Wikimedia Commonsの音声ファイル**: 個々のファイルのライセンスを機械的に大量取得・管理する運用コストは高く、CC BY-SA/GFDLのファイルが混在している場合、帰属表示の一括管理が煩雑になる。どの単語にどのライセンスの音声が存在するかは、実際にファイル一覧を取得してみるまで分からない。
- **TTS各社のキャッシュ可否**: Google Cloud / Azure / OpenAI いずれも「出力の所有権は顧客にある」という原則までは確認できたが、「生成した音声ファイルを商用アプリに同梱して無期限にキャッシュ・再配布してよいか」を明記した条項は発見できなかった（OpenAIはChatGPT Voice Outputについてのみ非商用・単体配布禁止を明記しているが、これがAPI経由のTTS出力にも及ぶかは条文上明確ではない）。ElevenLabsのみ、有料プランでのServices外利用を明文で許可しているが、OEM Terms（アプリへの組み込み専用の条件）は別文書であり中身を確認できていない。TTSをキャッシュ運用する前提で採用するなら、各社に直接問い合わせるか法務レビューを推奨する。
- **NLTK data配布の一次情報**: nltk.org/nltk_data や GitHub nltk/nltk_data の一次ページに直接アクセスできず、二次情報（WebSearch要約）に留まっている。
- **Princeton WordNetライセンスページの直接アクセス不可**: Cloudflareにより403となり、一次ページのHTMLを直接取得できていない。WebSearchのスニペットとSPDXのWordNetライセンス項目の記述が一致していることから内容の信頼性は高いと判断したが、ページ自体の更新日は未確認。
- **ejdict-hand（CC0）**: サブエージェント経由の要約に基づく判断であり、LICENSEファイル原文そのものをこのセッションで直接引用・確認できていない。
- **OpenAI Business Terms**: 403エラーで一次情報にアクセスできず、API TTS出力の所有権・商用利用条件は二次情報のみに依拠している。

## 影響する論点

- `docs/plan/english-vocab-app/` にはまだ overview.md / decisions.md / open-questions.md が存在しない（本調査時点で research/ ディレクトリのみ着手済み）。今後 intaking-ideas / shaping-experience を進める際、以下を open-questions.md の候補として持ち込むべき:
  - 「LLM生成の訳・例文をどこまで既存データ（JMdict/WordNet/Wiktionary）で代替し、生成コストを下げるか」の設計判断（本調査の結論が直接効く）。
  - 「発音音声をTTSオンデマンド生成＋キャッシュとするか、音声を一切持たずクライアント側TTS（端末組み込みの読み上げ機能）に倒すか」という技術方針の分岐（Forvo・Wikimedia Commonsが実質使えないことが判明したため、この分岐が重要になる）。
  - 「辞書APIを使わず自前でJMdict/Wiktionaryダンプを保持・更新する運用コストを誰が負うか」という実現性の論点（assessing-ai-architecture / shaping-experience の技術スタック検討に影響）。
  - 「EDRDG・Wiktionaryの帰属表示義務（アプリ内Aboutページ、月次更新）をプロダクト要件にどう落とし込むか」は decisions.md 記載候補（データソース選定が決定した段階で追記すべき）。
