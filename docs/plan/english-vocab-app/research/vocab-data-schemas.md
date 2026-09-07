# 語彙データセット・パッケージのスキーマ実例調査

- 調査日: 2026-09-07
- 調査手段: メインセッションによる一次情報の直接確認（GitHub 上の実データファイル（CSV/DTD/データベースファイル）の `curl` 取得、npm レジストリ API・パッケージソースの直接取得、公式ドキュメントページの WebFetch）。サブエージェントは使用していない。
- 問い: 既存の語彙データセット・辞書データ・npm 配布パッケージは、語の同一性（何をもって「同じ単語」とするか）とレベル・分類の付与を、実際のカラム構成・フィールド構成のレベルでどう解いているか。特に「1 語が複数の目的別リストに属する」問題と「多義語（`bank`, `run`, `abstract` など）の扱い」をどう解いているか。

## 結論

実例を見る限り、語の同一性の粒度は大きく 3 段階に分かれ、どの段階を選ぶかでそのまま多義語の扱いが決まっていた。

1. **見出し語＋品詞どまり（意味は畳み込む）**: CEFR-J Wordlist はこの方式。`bank` は名詞として 1 行しかなく、「銀行」と「土手」という異なる語義を区別しない。1 行に 1 レベルしか持てない設計上、多義語のどちらの意味を指してレベル付けしているかは行を見ても分からない。
2. **見出し語＋品詞＋語源グループ（ゆるい語義分割）**: Wiktextract/kaikki.org はこの方式。`bank` は「Etymology 1（金融機関）」と「Etymology 2（土手）」で別エントリ（別 JSON 行）になり、各エントリの中にさらに細かい `senses` 配列を持つ。品詞だけでなく語源が違えば別レコードにする、という中間的な粒度。
3. **語義（synset）そのものをレコード単位にする**: Princeton WordNet はこの方式。`bank`（名詞）は 10 個の synset（語義）すべてが独立したレコードとして存在し、「金融機関」（offset 08437235、定義文つき）と「土手」（offset 09236472、定義文つき）が完全に別レコードになる。レベル付き語彙リストで、この粒度まで踏み込んで多義語を扱っている実例は今回の調査では見つからなかった。

「1 語が複数リストに属する」問題については、正規化（語マスタ＋所属関係テーブル）を採用した確立されたデータセット・パッケージの実例は見つからなかった。実際に確認できた解き方は、**上位リストが下位リストの語を意図的に除外して排他的な階層を作る方式**（NGSL ファミリー、CEFR-J とその拡張）と、**タグ／カテゴリを語の行に直接持たせる方式**（CEFR-J の CoreInventory 列、Anki の空白区切りタグ文字列、Wiktextract の `tags` 配列）の 2 つだった。正規化方式は個人の GitHub Gist に例があるのみで、実運用されている確立した語彙データセットでは確認できなかった。

npm には「メタデータなしの単語配列／改行区切りテキスト」を配布するだけのパッケージ（`word-list`, `an-array-of-english-words`）が最もダウンロードされており、レベル情報つきの構造化データを配布する npm パッケージの実例は今回見つからなかった（`vocabulary-level-grader` はレベルではなく頻度ランクを CEFR 相当に変換するロジック側のパッケージで、データはランクのみを持つ）。

## スキーマ実例の一覧

| データセット／パッケージ | 語の同一性のキー | レベル・分類の置き場所 | 多義語の扱い | 形式 | 出典 |
| --- | --- | --- | --- | --- | --- |
| CEFR-J Wordlist（ver 1.5, GitHub ミラー） | headword ＋ pos（1 行 1 キー、重複なしを実データで確認） | 同じ行の `CEFR` 列（A1〜B2）。`CoreInventory 1`/`CoreInventory 2` 列にトピック分類、`Threshold` 列に別分類が同じ行に同居 | 区別しない。`bank,noun,A1,...` は 1 行のみで「銀行」「土手」を分けていない。`abstract` は adjective の行のみで noun の行は存在しない（そもそも収録されていない語義もある） | CSV（実データはヘッダー6列 `headword,pos,CEFR,CoreInventory 1,CoreInventory 2,Threshold`） | https://raw.githubusercontent.com/openlanguageprofiles/olp-en-cefrj/master/cefrj-vocabulary-profile-1.5.csv（2026-09-07 直接取得） |
| NGSL（New General Service List） | headword（lemma）単位。ランク付き | 分類はレベルではなく「リストそのもの」＝ NGSL / NAWL / TSL / BSL というファイルの違いがカテゴリを兼ねる | 語義分割なし。関連語形（活用形・スペル違い）は同じ行にまとめる方針（word family 単位ではなく inflected form 単位） | CSV/Excel（Number, Headword, Related word forms, SFI, U の列構成を確認） | https://www.eapfoundation.com/vocab/general/ngsl/（WebFetch, 2026-09-07） |
| NAWL / TSL / BSL（NGSL ファミリー） | NGSL と同じ形式のheadword単位ファイルだが、**NGSL に含まれる語は最初から除外して作られている** | リスト＝分類。NAWL＝学術語、TSL＝TOEIC 頻出語、BSL＝ビジネス語という名前がそのままカテゴリ | 語義分割なし（NGSLと同方針） | CSV/Excel（個別配布） | https://www.eapfoundation.com/vocab/academic/nawl/、https://www.eapfoundation.com/vocab/wordlists/overview/（WebFetch, 2026-09-07） |
| JMdict（EDRDG） | `entry`（`ent_seq` で一意）＝ 1 つの見出し語グループ。`k_ele`（漢字表記）／`r_ele`（読み）を entry 内に複数持てる | レベル情報自体は持たない（本調査の対象外の属性）。分類に近いものとして `sense` ごとの `field`（分野タグ）、`misc`（用法タグ）がある | `sense` 単位で分割。1 entry が複数 `sense` を持ち、`pos` は sense ごとに付与できるため、同じ entry 内でも語義によって品詞が変わりうる | XML（DTD: `entry (ent_seq, k_ele*, r_ele+, sense+)`） | https://www.edrdg.org/jmdict/jmdict_dtd_h.html（WebFetch, 2026-09-07） |
| Princeton WordNet | **synset**（語義・概念）が最小単位。`index.<pos>` ファイルの 1 行が 1 lemma、そこから複数の synset offset を指す（例: `bank n 10 5 ... ` で名詞 bank は 10 synset） | レベル情報は持たない。分類としては synset ごとの語彙分野コード（lex_filenum）と品詞（ss_type） | 完全に synset 単位で分離。`bank` の offset 08437235 は「a financial institution that accepts deposits...」、offset 09236472 は「sloping land (especially the slope beside a body of water)」と、定義文つきで完全に別レコード | プレーンテキスト DB（`data.noun`/`index.noun` 等の固定長フィールド形式） | https://raw.githubusercontent.com/moos/wordnet-db/master/dict/index.noun、data.noun（2026-09-07 直接取得・grep で bank の実データを確認） |
| Open English WordNet（GWN-LMF） | `LexicalEntry`（lemma＋pos、例: `ewn-bank-n`）→ `Sense`（`ewn-bank-n-XXXXXXXX-YY`）→ `Synset` の3層。品詞が違えば別 LexicalEntry、同じ品詞内の語義違いは Sense を複数持つ | レベル情報は持たない | pos ではなく Sense 単位で語義分割。1 LexicalEntry が複数 Sense を持てる | XML（WN-LMF、DTD 準拠） | https://raw.githubusercontent.com/globalwordnet/english-wordnet/main/FORMAT.md（WebFetch, 2026-09-07） |
| Wiktextract / kaikki.org | word ＋ lang_code ＋ pos ＋ **etymology グループ**。品詞が同じでも語源が異なれば別エントリ（別 JSON 行）になる。実例: `bank`(noun) は Etymology 1（金融機関、10 sense）と Etymology 2（土手、9 sense）で別エントリ | レベル情報は持たない。分類に近いものとして各 sense の `tags`（配列、例: countable/slang 等）と `categories` | 語源グループ単位で粗く分割し、さらにその中の `senses` 配列で細分。財務機関と土手は別エントリとして完全に分離されている | JSON Lines（1 行が 1 word×pos×etymology グループ） | https://kaikki.org/dictionary/English/meaning/b/ba/bank.html（WebFetch, 2026-09-07）、README: https://github.com/tatuylonen/wiktextract |
| Wordset Dictionary | word 文字列がオブジェクトのキー。1 word オブジェクトの中に `meanings` 配列（`speech_part` を含む） | レベル情報は持たない | pos＋語義を `meanings` 配列内のオブジェクト単位で分割。word 自体は 1 オブジェクトのまま | JSON（`data/<letter>.json`、word をキーとする巨大オブジェクト） | https://github.com/wordset/wordset-dictionary（WebSearch 経由で得たREADME例、2026-09-07。原文コード例は確認したが自分でファイルを取得してはいない＝確度中） |
| npm: `word-list`（sindresorhus） | なし。改行区切りテキストファイルへのパスを返すだけ | なし | 非該当（単なる単語配列。品詞も語義も持たない） | `.txt`（`\n` 区切り）。パッケージの `main`/`types` はファイルパス文字列を返す `index.d.ts` のみ | https://raw.githubusercontent.com/sindresorhus/word-list/main/readme.md（2026-09-07 直接取得） |
| npm: `an-array-of-english-words` | なし。JSON 配列の要素が全て小文字の単語文字列 | なし | 非該当 | `index.json`（文字列配列）。TypeScript 型定義は同梱していない（`package.json` に `types` フィールドなし） | https://raw.githubusercontent.com/words/an-array-of-english-words/master/package.json（2026-09-07 直接取得） |
| npm: `wordnet-db` | Princeton WordNet のオリジナルファイルをそのまま同梱（上記 WordNet の方式を継承） | 同上 | 同上 | 生の WordNet DB テキストファイル一式（`data.noun` 等）をコピーしてインストール。JS 側での再構造化はしていない | https://raw.githubusercontent.com/moos/wordnet-db/master/README.md（2026-09-07 直接取得） |
| npm: `cmu-pronouncing-dictionary` | 見出し語文字列そのものがオブジェクトキー。**同じ綴りで発音が複数ある場合はキー自体に `(2)`, `(3)` という連番を付けて別キーにする**（例: `unnaturally`, `unnaturally(2)`, `unnaturally(3)`） | なし（発音のみ） | 品詞や語義では分けず、発音バリアントをキー文字列のサフィックスで表現するという独自の回避策 | フラットな `{word: pronunciation}` オブジェクト（ESM export） | https://raw.githubusercontent.com/words/cmu-pronouncing-dictionary/master/readme.md（2026-09-07 直接取得） |
| npm: `vocabulary-level-grader`（内部データ `vocabulary-list-statistics`） | 見出し語（レンマ化済み、小文字）単体。品詞なし | 分類はレベルではなく頻度ランク（`rank` 数値）。ランクをしきい値で CEFR 相当に変換するのは呼び出し側のロジック（A1: rank≤600 など） | 区別しない。`{word, rank}` の 1 レコードのみ | JS モジュール内の配列（`{word, rank}` オブジェクトの配列を `Map` に変換して利用） | https://raw.githubusercontent.com/openderocknlp/vocabulary-level-grader/master/index.js（2026-09-07 直接取得） |

## 「1 語が複数リストに属する」問題の解き方

| 方式 | 採用している実例 | 得るもの | 失うもの |
| --- | --- | --- | --- |
| 上位リストが下位リストの語を除外する排他的階層 | NGSL（基礎 2,801 語）に対し NAWL は「NGSL に含まれない学術語 963 語」として設計されている（一次情報で確認）。TSL・BSL も同じ設計思想（GSL 系リストの伝統を踏襲）。CEFR-J（A1〜B2）と Octanove Vocabulary Profile（C1/C2）も、レベル帯で分担する形で重複を避けている | 同じ語が複数ファイルに重複して現れないため、「この語はどのレベルか」が常に一意に決まる。ファイルを跨いで語を数えても二重カウントが起きない | リストの構成が変わる（例: NGSL の版が上がって収録語が変わる）と、下位リストの前提が崩れて再構築が必要になる。目的別に見たい語（例: IELTS 用と日常会話用の両方に出したい語）を、リストの構造上どちらか一方にしか置けない |
| リストごとに独立ファイル、重複を許容する | 明確な実例は今回の調査で確認できなかった。強いて言えば Oxford 3000 と Oxford 5000（Oxford 5000 は「3000 に 2000 語追加」と説明されている）は重複を許容している可能性があるが、実ファイルの中身までは未確認（ライセンス上ダウンロードできる一次ファイルを直接確認していない） | 各ファイルをその1本だけで独立に配布・利用できる。上位リストの変更が下位リストに影響しない | 同じ語のデータ（レベル、品詞など）を複数ファイルにコピーすることになり、更新時にファイル間の不整合が起きうる。重複語をどう数えるかはファイルを跨いだ集計時に別途ロジックが要る |
| タグ／ラベルを語（またはレコード）に直接持たせる | CEFR-J の `CoreInventory 1`/`CoreInventory 2`/`Threshold` 列（1 語の行にトピック分類が複数列で同居）。Anki の `notes.tags` 列（空白区切りのテキスト値、配列ではなく文字列だが実質タグの集合として機能）。Wiktextract の sense 単位 `tags` 配列（`countable`, `slang` 等の複数タグを配列で保持） | 語のマスタは 1 つのまま保ち、所属を後から自由に増減できる。正規化テーブルを増やさずに済む | タグの語彙（許容される値の集合）を別途どこかで管理しないと表記ゆれが起きる。Anki のように文字列（空白区切り）で持つ場合はDBレベルでの整合性制約（外部キー等）が効かない |
| 正規化（語マスタ＋所属関係テーブル） | 確立された実データセット・パッケージでは実例を確認できなかった。個人の GitHub Gist（`WordLists`/`WordListItems`/`WordGroups`/`WordListAssignments` という中間テーブル設計）が唯一近い例として見つかったが、公開されて広く使われているデータセットではない | 語のデータを 1 箇所にしか持たないため更新が 1 回で済み、所属関係の追加・削除も行の追加・削除だけで完結する。多対多を素直に表現できる | 今回確認した実例が薄いため、実運用でのコスト（クエリの複雑化、JOIN のパフォーマンス等）を裏付ける一次情報がない |

## 根拠

- 事実: CEFR-J Vocabulary Profile（ver 1.5、GitHub ミラー）の実データは 7,799 行、ヘッダーは `headword,pos,CEFR,CoreInventory 1,CoreInventory 2,Threshold` の 6 列。`headword+pos` の組み合わせで重複行がないことを `awk`+`uniq -d` で確認した（重複 0 件）。`bank` は `bank,noun,A1,"Things in the town, shops and shopping",,Services` と `bank,verb,A2,,,` の 2 行のみで、名詞 bank の「銀行」「土手」の語義は区別されていない。`run` も `run,noun,A1,...` と `run,verb,A1,...` の 2 行のみ。`abstract` は `abstract,adjective,B1,,,` の 1 行のみで、名詞形の行は存在しない。
  - URL: https://raw.githubusercontent.com/openlanguageprofiles/olp-en-cefrj/master/cefrj-vocabulary-profile-1.5.csv
  - 出典日付: 記載なし（GitHub リポジトリ自体の最終更新はREADMEにver 1.5 (2020-01-20時点相当) と記載。ファイル自体には更新日表記なし）
  - 確度: 高（実ファイルを直接取得し、grep/awk で内容を確認した）

- 事実: NGSL のダウンロード可能な表示形式は `Number`（順位）, `Headword`（見出し語）, `Related word forms`（関連語形）, `SFI`（Standard Frequency Index）, `U`（100万語あたり頻度）の列で構成される。NGSL は「word families ではなく inflected forms／variant spellings」を個別の語形として提示する方針が明記されている。
  - URL: https://www.eapfoundation.com/vocab/general/ngsl/
  - 出典日付: 記載なし
  - 確度: 中（NGSL 公式サイトではなく eapfoundation.com の要約ページを情報源としている。公式配布 CSV そのもののヘッダー行は未取得）

- 事実: New Academic Word List（NAWL）は「963 語からなり、学術テキストに頻出するが New General Service List（NGSL）には含まれていない語」と明記されている。NGSL と NAWL を合わせて学習すると 288M 語の学術コーパスに対し約92%のカバレッジが得られるとの記載がある。
  - URL: https://www.eapfoundation.com/vocab/academic/nawl/
  - 出典日付: 記載なし
  - 確度: 中（一次配布元である newgeneralservicelist.com 自体のFAQページはアクセスできたが該当記述が見つからず、eapfoundation.com の要約記述に依拠）

- 事実: eapfoundation.com の語彙リスト概観ページには、GSL に対する AWL/UWL/SWL 等の学術・専門リストが「GSL に含まれる語を除外して構成される」という記述が複数箇所にあり、GSL系リスト群が階層的・補完的に設計されていることが確認できる。
  - URL: https://www.eapfoundation.com/vocab/wordlists/overview/
  - 出典日付: 記載なし
  - 確度: 中

- 事実: JMdict の DTD では `entry` は `(ent_seq, k_ele*, r_ele+, sense+)` の階層を持つ。`ent_seq` は各 entry に一意に振られる番号。`sense` 要素は `stagk, stagr, pos, xref, ant, field, misc, s_inf, lsource, dial, gloss` を含み、語義（sense）ごとに品詞・分野・用法タグを個別に持てる。複数の異なる語義がある場合は複数の `sense` 要素として記録される。
  - URL: https://www.edrdg.org/jmdict/jmdict_dtd_h.html
  - 出典日付: 記載なし
  - 確度: 高（公式 DTD ドキュメントを直接確認）

- 事実: WordNet 3.1 の `index.noun` ファイルで `bank` は `bank n 10 5 @ ~ #m %p + 10 4 09236472 08437235 09236341 08479077 13389491 13377435 09236735 04146942 02790795 00170126` という行で、名詞としての `bank` が 10 個の synset（offset のリスト）に対応することが直接確認できる。`data.noun` から該当 offset を引くと、offset `09236472` は "sloping land (especially the slope beside a body of water); ... he sat on the bank of the river ..."（土手・川岸）、offset `08437235` は "a financial institution that accepts deposits and channels the money into lending activities; 'he cashed a check at the bank'"（金融機関、同義語 `depository_financial_institution` を含む synset）、offset `09236341` は "a long ridge or pile; 'a huge bank of earth'"（土の山）であり、同じ lemma `bank` が語義ごとに完全に別々のレコード（synset）として保持されている。
  - URL: https://raw.githubusercontent.com/moos/wordnet-db/master/dict/index.noun 、https://raw.githubusercontent.com/moos/wordnet-db/master/dict/data.noun
  - 出典日付: 記載なし（wordnet-db は WordNet 3.1 のデータをそのまま再配布したもの）
  - 確度: 高（実データファイルを直接取得し、該当行を grep で確認した。ファイルは Princeton WordNet 3.1 の公式配布物のコピーであることを README で確認済み）

- 事実: Open English WordNet（GWN-LMF 形式）は `LexicalEntry`（例: `ewn-bank-n`、`ewn-bank-v` のように lemma＋pos 単位）→ `Sense`（`ewn-lemma-p-XXXXXXXX-YY` の ID 形式）→ `Synset` という3層構造を持つ。品詞が異なれば別の `LexicalEntry` になり、同じ品詞内で語義が複数ある場合は同一 `LexicalEntry` の中に複数の `Sense` を持つ。
  - URL: https://raw.githubusercontent.com/globalwordnet/english-wordnet/main/FORMAT.md
  - 出典日付: 記載なし
  - 確度: 中（WebFetch によるページ要約を情報源としており、FORMAT.md 原文全体を自分の目で通読してはいない）

- 事実: kaikki.org（Wiktextract）の `bank` エントリページでは、名詞の `bank` が「Etymology 1」（金融機関、10 sense）と「Etymology 2」（川岸、9 sense）という別グループに分かれて掲載されている。各 sense は `gloss`、`tags`（例: countable/uncountable）、sense ID、`categories`（例: Buildings, Hydrology）、翻訳などを持つ。財務機関の意味は "An institution where one can place and borrow money"、川岸の意味は "An edge of river, lake, or other watercourse" として、異なる Etymology セクション配下の独立したエントリに記録されている。
  - URL: https://kaikki.org/dictionary/English/meaning/b/ba/bank.html
  - 出典日付: 記載なし
  - 確度: 中（WebFetch によるページ内容の要約を情報源としており、ページの生データ（JSON Lines形式のダウンロードファイル）そのものは取得していない）

- 事実: Wordset Dictionary は `data/<letter>.json` に、word を直接キーとするオブジェクトを持ち、各 word オブジェクトの中に `meanings` 配列（各要素が `id`, `def`, `speech_part`, 任意で `synonyms` を持つ）を持つ構造であることが README のサンプルコードで示されている。
  - URL: https://github.com/wordset/wordset-dictionary
  - 出典日付: 記載なし
  - 確度: 中（WebSearch経由で得たREADMEのコード例を情報源としており、リポジトリの実データファイルは自分で取得していない）

- 事実: npm の `word-list`（sindresorhus 作）は、`\n` 区切りの英単語一覧ファイルへのパスを返すだけのパッケージで、`index.d.ts` は `declare const wordsListPath: string;` のみ。品詞・語義・レベルなどのメタデータは一切持たない。
  - URL: https://raw.githubusercontent.com/sindresorhus/word-list/main/readme.md 、https://raw.githubusercontent.com/sindresorhus/word-list/main/index.d.ts
  - 出典日付: 記載なし
  - 確度: 高（実ファイルを直接取得して確認）

- 事実: npm の `an-array-of-english-words` は `package.json` の `main` が `index.json`（275,000 語程度の文字列配列）であり、`types` フィールドが存在しない（TypeScript 型定義を同梱していない）。
  - URL: https://raw.githubusercontent.com/words/an-array-of-english-words/master/package.json
  - 出典日付: 記載なし
  - 確度: 高（package.json を直接取得して確認）

- 事実: npm の `wordnet-db` は Princeton WordNet 3.1 のオリジナルの DB ファイル（`data.adj`, `data.adv`, `data.noun`, `data.verb`, `index.adj`, `index.adv`, `index.noun`, `index.sense`, `index.verb`）をそのまま同梱するパッケージで、JS 側での再構造化・JSON化は行っていない。パッケージサイズは約10MB（展開後約34MB）。週間ダウンロード数は 685,881（2026-08-31〜09-06 の1週間）で、今回調べた語彙系パッケージの中で最も多かった（依存元の `natural` パッケージ自体の週間ダウンロード数 947,248 も含めると、WordNet 系データの利用は非常に多い）。
  - URL: https://raw.githubusercontent.com/moos/wordnet-db/master/README.md 、https://api.npmjs.org/downloads/point/last-week/wordnet-db
  - 出典日付: 記載なし（README）／2026-09-07（ダウンロード数取得日、集計期間は2026-08-31〜09-06）
  - 確度: 高

- 事実: npm の `cmu-pronouncing-dictionary` は `{word: pronunciation}` というフラットなオブジェクトを返し、同じ綴りで発音が複数ある語は `unnaturally`, `unnaturally(2)`, `unnaturally(3)` のように、キー文字列自体に `(n)` という連番サフィックスを付けて別レコード化する、という独自の回避策を README で明記している。
  - URL: https://raw.githubusercontent.com/words/cmu-pronouncing-dictionary/master/readme.md
  - 出典日付: 記載なし
  - 確度: 高（README原文を直接取得して確認）

- 事実: npm レジストリの週間ダウンロード数（2026-08-31〜09-06）は、`word-list` 40,361、`an-array-of-english-words` 27,380、`wordnet-db` 685,881、`cmu-pronouncing-dictionary` 69,727、`wordlist`（別パッケージ、Aspell系）8、`natural` 947,248、`vocabulary-level-grader` 25 だった。レベル情報つきのメタデータを持つ語彙パッケージ（`vocabulary-level-grader` 等）は、メタデータなしの単語配列パッケージに比べてダウンロード数が2〜3桁少ない。
  - URL: https://api.npmjs.org/downloads/point/last-week/<package名>（npm公式ダウンロード数API）
  - 出典日付: 2026-09-07取得、集計期間2026-08-31〜09-06
  - 確度: 高

- 事実: `vocabulary-level-grader`（内部で `vocabulary-list-statistics` パッケージのデータを利用）は、`{word, rank}` という最小限のレコード配列を `Map` に変換して保持し、CEFR レベルへの変換はランクに対するしきい値判定（`A1: rank<=600`, `A2: rank<=1200`, `B1: rank<=2500`, `B2: rank<=5000`, `C1: rank<=10000` など）をアプリ側ロジックで行っている。つまりデータ自体には CEFR ラベルを直接持たせず、頻度ランクからの変換ロジックで代替している。
  - URL: https://raw.githubusercontent.com/openderocknlp/vocabulary-level-grader/master/index.js
  - 出典日付: 記載なし
  - 確度: 高（index.js原文を直接取得して確認）

- 事実: Anki（`collection.anki2`、SQLite）の `notes` テーブルは `tags` カラムを持ち、これは配列型ではなく「空白区切りのタグ名を並べたテキスト値」として実装されている。
  - URL: 検索結果の要約（複数の技術ブログ・リポジトリドキュメントの要約に基づく。Anki公式のスキーマドキュメント原文は今回直接確認していない）
  - 出典日付: 記載なし
  - 確度: 中（一次のAnkiソースコード・公式スキーマドキュメントではなく、WebSearchによる複数の二次情報の要約に基づく）

## グレーゾーン・未確認

- 「リストごとに独立ファイルとして持ち、重複を許容する」実例を、確立されたデータセットで確認できなかった。Oxford 3000/5000 が重複を許容していそうだという間接的な手がかりはあるが、両ファイルの実データ（ライセンス上ダウンロード制限があり今回は取得していない）を突き合わせて重複の有無を確認してはいない。
- 正規化（語マスタ＋所属関係テーブル）を採用した、広く使われている確立済みデータセット・パッケージの実例は見つからなかった。見つかった唯一の例（GitHub Gist）は個人の設計サンプルであり、実データセットではない。この方式が実運用でどう機能するかは未確認のまま。
- CEFR-J の「監修」に関する留保条件など、ライセンス面は本調査の対象外（`docs/plan/english-vocab-list/research/wordlists-cefr.md` 側で確認済み）。本ファイルはスキーマ構造のみを扱っている。
- Wordset Dictionary、Open English WordNet の FORMAT.md、Anki のスキーマについては、実ファイル・原文ドキュメントを自分で全文取得したのではなく、WebFetch/WebSearch による要約を情報源にしている（確度「中」と明記した箇所）。特に Anki の tags 実装は二次情報のみに基づいており、公式スキーマドキュメントや実際の `.anki2` ファイルでの検証はできていない。
- NGSL・NAWL・TSL・BSL の公式配布 CSV/Excel ファイルそのもの（newgeneralservicelist.com からのダウンロード）は、サイト構造上直接取得できず、eapfoundation.com の要約ページを介した確認にとどまっている。ヘッダー行の正確な文字列（列名の英語表記そのもの）までは未確認。
- 「レベル付き語彙リストが多義語をどう扱うか」について、CEFR-J 以外の CEFR 系リスト（Oxford, Cambridge, Pearson 等）は商用利用不可のため今回改めてファイルを取得しておらず、それらが多義語をどう扱っているかは未確認のまま（`wordlists-cefr.md` の既存調査でもライセンス面の確認にとどまっている）。
- Wiktextract/kaikki.org の「Etymology グループで分ける」という粒度が、CEFR/IELTS のようなレベル付けが必要な文脈でそのまま実用に耐えるか（語源が同じでも意味が大きく違う語、語源データが整備されていない語がどう扱われるか）は、今回の調査範囲では確認していない。

## 影響する論点

- `docs/plan/english-vocab-list/open-questions.md` の「ライブラリに何を収録するか」: 見出し語＋品詞レベルで畳み込む（CEFR-J方式）か、語義単位まで割るか（WordNet/kaikki方式）で、1 語 1 レベルにできるかどうかが変わる。多義語（`bank`, `abstract` の名詞/形容詞など）を厳密に扱うなら語義単位の粒度が必要だが、その分スキーマとデータ生成の複雑さが増す。
- 同じ open-questions.md の「生成した語彙リストの品質をどう担保するか」: 既存データセットはいずれも「見出し語＋品詞」または「見出し語＋品詞＋語義」を一意キーとして重複チェックをしている（CEFR-J は実データで重複ゼロを確認済み）。LLM 生成データでも、最低限このキーでの重複がないことを機械的に検証できる。
- 「目的別リストを複数持つときに単語データがテーブル間で重複するか」というオーナーの当初の懸念そのものへの回答材料: 確立された実例では、(a) 上位リストが下位リストを除外する設計にして重複そのものをなくす、または (b) タグ／カテゴリ列を語の行に直接持たせて 1 つの語マスタに複数の所属を持たせる、のどちらかが主流であり、正規化（語マスタ＋所属テーブル）を採用した確立実例は見つからなかった。この選択は `docs/plan/english-vocab-list/decisions.md` にまだ記録がなく、次の決定事項の候補になる。

## メインセッションが自分で確認した事実（2026-09-07 追記）

- 事実: CEFR-J Wordlist Ver.1.6 の ALL シートを手元でパースした結果、全 7,801 行のうち
  ユニークな見出し語は 6,868 で、**848 の見出し語が複数行を持つ**。複数行はすべて品詞違いだった。
  実例: `fine` は adjective A1 / noun B1 / adverb B2 / verb B2 の 4 行。
  `light` は adjective A1 / noun A1 / verb B1。`mean` は verb A1 / adjective A2 / noun B2。
  `book` は noun A1 / verb B1。`bank` は noun A1 / verb A2。
  一方 `bank` の「銀行」と「土手」は同じ noun 行に畳み込まれており、語義では分けていない。
  したがって CEFR-J の実効的な主キーは **(headword, pos)** であり、語義は畳み込まれている。
  なお `abstract` は adjective B1 の 1 行のみで、名詞の行は存在しない。
  - URL: http://www.cefr-j.org/data/CEFRJ_wordlist_ver1.6.zip
  - 出典日付: 2020-03-24
  - 確度: 高（配布ファイルを取得して直接パース）

- 事実: NGSL プロジェクトの Word Lists ページは、リストを 3 層の情報設計で提示している。
  "START HERE: THE CORE LIST" として NGSL（2,809 words · ~92%+ coverage of general English）を置き、
  "THEN ADD ONE: SPECIAL PURPOSE LISTS" として NAWL / TSL / BSL / BEL / FEL / MOEL を並べ、
  "LISTS THAT WORK ON THEIR OWN" として NGSL-Spoken / New Dolch List / NGSL-Graded Reader を分けている。
  つまり目的別リストは単体で完結せず、コアリストに足して使う前提で設計されている。
  これはサブエージェントが報告した「排他的階層」を、配布側の情報設計として裏づける。
  - URL: https://www.newgeneralservicelist.com/word-lists
  - 出典日付: 記載なし（取得日 2026-09-07）
  - 確度: 高（ページ原文を直接取得）

- 事実: 同ページに "Everything here is free. All lists are released under Creative Commons and
  may be used commercially." と記載があり、商用利用可の明記を再確認した。
  - URL: https://www.newgeneralservicelist.com/word-lists
  - 確度: 高

### 出典どうしの食い違い

同じ NGSL プロジェクト内で、リストの語数の表記が揺れている。
Word Lists ページでは TSL が 1,200 words、NAWL が 960 words と書かれているが、
他ページや配布ファイル由来の記述では TSL 1,250 語、NAWL 957 語とされている。
どちらが現行版かは確認できていない。**語数を根拠にする場面では版を明示する必要がある。**
