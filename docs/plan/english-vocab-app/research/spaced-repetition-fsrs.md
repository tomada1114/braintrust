# FSRS（Free Spaced Repetition Scheduler）の事実確認

- 調査日: 2026-09-10
- 調査手段: メインセッションによる WebSearch / WebFetch、および GitHub API（`gh api`）でのリリース履歴・ソースコード直接確認
- 問い: Anki の FSRS スケジューラを個人用単語アプリの復習ロジックとして採用する前提として、(1) Anki での導入時期とデフォルト状況、SM-2 の現状、(2) FSRS がカード単位・レビュー単位で必要とする入力・状態と初期パラメータ／オプティマイザの要否、(3) 自作アプリから使えるライブラリ（ts-fsrs / py-fsrs）の配布条件と保守状況、(4) SM-2 に対して FSRS が解決する実務上の問題は何か、を確認する。

## 結論

- **導入時期とデフォルト状況**: FSRS は Anki 23.10（2023年10月31日リリース）で組み込み機能として統合された。2026年9月時点の最新安定版は 26.08.1（2026年8月5日）で、26.09 系はベータ段階。**FSRS は現在も既定でオンにはならず、デッキオプション画面で手動で有効化する必要がある**。SM-2 は「legacy（레거시）」と明記されつつも、有効化しない限り引き続き使われる既定のアルゴリズムであり、廃止はされていない。
- **カード／レビュー単位の入力・状態**: FSRS はカードごとに Difficulty（難易度）・Stability（安定度）・Retrievability（想起確率、時間経過と Stability から計算される派生値）という「DSR」3変数を持つ。実装上はこれに加えて `due`（次回期日）・`state`（New/Learning/Review/Relearning）・`last_review`（前回レビュー日時）・学習ステップの進捗を持つ。ts-fsrs はさらに `reps`（レビュー回数）・`lapses`（失敗回数）・`scheduled_days` も Card に持たせている。レビュー単位では「評価（Again=1 / Hard=2 / Good=3 / Easy=4）」と「レビュー日時」が最小限必要。パラメータは21個の重み（w0〜w20）で、既定の `desired_retention`（目標保持率）は90%。**オプティマイザは必須ではない**。組み込みの既定パラメータは多数ユーザーの復習履歴から得た中央値であり、レビュー履歴が少ない開始時点では既定パラメータのままで「SM-2よりは優れている」とされる。オプティマイザは数百件以上のレビュー履歴が溜まってから使うことが推奨されている。
- **ライブラリ**: ts-fsrs（TypeScript、MIT）と py-fsrs（Python、PyPI パッケージ名 `fsrs`、MIT）はいずれも活発にメンテナンスされている。どちらもスケジューラ本体とオプティマイザは別パッケージ／別インストールオプションに分離されており、単語アプリのようにスケジューラだけ使う用途では最小限の依存で済む。
- **SM-2 との対比**: SM-2 実装（Anki版含む）で知られる「ease hell（イーズが下がりきって二度と回復しない状態）」を、FSRS は Difficulty の平均回帰（mean reversion）という設計で解消しているとされる。これは Anki 公式フォーラムおよび FSRS のアルゴリズム解説ページで明言されている。

## 根拠

- 事実: 「Support for FSRS (which improves upon the scheduling provided by SM-2) is now integrated into Anki. You can compute the model weights directly inside Anki, and no longer need to use custom scheduling.」（Anki 23.10 のリリースノート）。同バージョンのリリース日は 2023年11月1日。
  - URL: https://changes.ankiweb.net/changes/23.10.html
  - 出典日付: 2023-11-01（当該バージョンのリリース日として明記）
  - 確度: 高

- 事実: Wikipedia の Anki 項目にも「In 2023 (version 23.10) the Free Spaced Repetition Scheduler (FSRS)... was integrated into Anki as an optional feature」との記載があり、23.10 が最初の統合版であることと「オプション機能」であったことが確認できる。
  - URL: https://en.wikipedia.org/wiki/Anki_(software)
  - 出典日付: 記載なし（ページの最終更新日は取得できず）
  - 確度: 中（二次情報だが一次情報と整合）

- 事実: GitHub の `ankitects/anki` リリース一覧を API 経由で取得したところ、2026年9月10日時点での最新の安定版は `26.08.1`（公開日 2026-08-05T16:48:50Z）、その後は `26.09b1`〜`26.09b3`（ベータ、2026-08-25〜2026-09-10）が続いている。安定版としては 26.08 系が最新。
  - URL: https://github.com/ankitects/anki/releases
  - 出典日付: 2026-08-05（26.08.1 公開日、API から直接取得）
  - 確度: 高

- 事実: Anki 公式マニュアルの Deck Options ページ（FSRS セクション）は「The Free Spaced Repetition Scheduler (FSRS) is an alternative to Anki's legacy SuperMemo 2 (SM-2) algorithm.」「Enable FSRS under the "FSRS" section, at the bottom of the deck options page.」「When you turn on FSRS, some new options become available, and SM-2 specific options... are hidden.」と記載しており、**FSRS は「オンにする」対象として説明されている**＝既定でオンではないことを示唆する。この文書は GitHub 上のソース（`ankitects/anki-manual` リポジトリの `src/deck-options.md`）の最終更新が 2026-07-07 であり、比較的最近の内容。
  - URL: https://docs.ankiweb.net/deck-options.html
  - 出典日付: 2026-07-07（GitHub の当該ファイルの最終コミット日時から確認）
  - 確度: 高

- 事実: Anki 公式 FAQ「What spaced repetition algorithm does Anki use?」は「As of Anki 23.10, Anki has two available algorithms. The first one is based on the SuperMemo 2 algorithm, and the second one is called FSRS.」とし、FSRS の利点を説明する文中で繰り返し「Anki's default algorithm」という表現で SM-2 を指している（例:「With FSRS, users have to do fewer reviews than with Anki's default algorithm to achieve the same retention level.」）。**SM-2 が「default algorithm」であるという明言**。このページのソース（`ankitects/faqs` リポジトリ内 `src/what-spaced-repetition-algorithm.md`）の最終更新は 2024-09-07で、やや古い可能性がある点は留意。
  - URL: https://faqs.ankiweb.net/what-spaced-repetition-algorithm
  - 出典日付: 2024-09-07（GitHub 最終コミット日時）
  - 確度: 中（内容自体はデッキオプションページの記載と整合するため信頼度は上げているが、更新日がやや古い）

- 事実: `open-spaced-repetition/fsrs4anki` リポジトリのチュートリアルには「Even with the default parameters, FSRS is better than the default Anki algorithm (SM-2).」と明記があり、ここでも SM-2 が「default Anki algorithm」と表現されている。GitHub のリリース一覧を検索した限り、「FSRS が新規コレクションの既定になった」という趣旨のリリースノートは見当たらなかった。
  - URL: https://github.com/open-spaced-repetition/fsrs4anki/blob/main/docs/tutorial.md
  - 出典日付: 2025-05-14（GitHub 最終コミット日時）
  - 確度: 中

- 事実: FSRS の DSR モデルについて、Anki 公式 FAQ は「Retrievability (R): The probability... Stability (S): The time, in days, required for R to decrease from 100% to 90%... Difficulty (D): The inherent complexity of a particular information...」と定義している。D と S はレビュー時のみ変化し、R は日々変化する。
  - URL: https://faqs.ankiweb.net/what-spaced-repetition-algorithm
  - 出典日付: 2024-09-07
  - 確度: 高（モデル定義自体は version に依存しない安定した記述）

- 事実: Anki デッキオプションのマニュアルは「Choose a value of desired retention: the proportion of cards recalled successfully when they are due... The default is 90%, which offers a good balance of retention and workload.」と明記。また「FSRS parameters affect how cards are scheduled. Do not change the parameters manually or copy them from someone else.」「The FSRS optimizer uses machine learning to learn your memory patterns and find parameters that best fit your review history... There is no need to optimize your parameters frequently: once every month is sufficient.」とあり、オプティマイザは推奨だが必須という書き方ではない。さらに「Health Check」の項で「Low number of reviews (less than a few hundred)」が FSRS の精度が出ない典型的な原因として挙げられている＝数百件未満のレビュー履歴ではオプティマイザの効果が薄いことを示唆。
  - URL: https://docs.ankiweb.net/deck-options.html
  - 出典日付: 2026-07-07
  - 確度: 高

- 事実: `fsrs4anki` チュートリアルの Q&A に「The default parameters are generated from 20k collections. They are the median values of 20k sets of parameters.」とあり、既定パラメータは多数ユーザーの復習履歴から得た中央値であることが明言されている。また「In Anki 24.06+, there is no minimum number of reviews required for optimization... please use the default parameters that are already entered into the "FSRS parameters" field. Even with the default parameters, FSRS is better than the default Anki algorithm (SM-2).」ともあり、**単一ユーザーが使い始める段階ではオプティマイザなしでも既定パラメータで運用開始できる**ことが確認できる。
  - URL: https://github.com/open-spaced-repetition/fsrs4anki/blob/main/docs/tutorial.md
  - 出典日付: 2025-05-14
  - 確度: 中（「20k collections」という具体的な数値は、FSRS のバージョンアップ（現在は FSRS-6）に伴い学習データセットが更新されている可能性があり、最新版でも同じ数値かは未確認）

- 事実: py-fsrs（PyPI パッケージ名 `fsrs`）の README には、既定の21パラメータの具体値（`0.212, 1.2931, 2.3065, ...`）、`desired_retention = 0.9`、`learning_steps = (1分, 10分)`、`relearning_steps = (10分,)`、`maximum_interval = 36500`、`enable_fuzzing = True` が既定値として明記されている。「`parameters` are a set of 21 model weights... If you're not familiar with optimizing FSRS, it is best not to modify these default values.」ともあり、オプティマイザなしでの利用が前提として書かれている。
  - URL: https://github.com/open-spaced-repetition/py-fsrs（README を `raw.githubusercontent.com` 経由で直接取得）
  - 出典日付: 記載なし（README自体に更新日表記なし。PyPI 上の最新バージョン 6.3.2 の公開日は 2026-08-09）
  - 確度: 高

- 事実: py-fsrs のソースコード（`fsrs/card.py`）を直接確認したところ、`Card` は `card_id, state, step, stability, difficulty, due, last_review` を持つ。`ReviewLog`（`fsrs/review_log.py`）は `card_id, rating, review_datetime, review_duration` を持つ。`rating` は `Rating.Again(1) / Hard(2) / Good(3) / Easy(4)`。
  - URL: https://github.com/open-spaced-repetition/py-fsrs/blob/main/fsrs/card.py および https://github.com/open-spaced-repetition/py-fsrs/blob/main/fsrs/review_log.py
  - 出典日付: 記載なし（`gh api` で確認したリポジトリの最終 push は 2026-08-09）
  - 確度: 高（ソースコード直読のため確度は高いが、時点は最新コミット時点のもの）

- 事実: ts-fsrs（npm パッケージ）のソースコード（`packages/fsrs/src/models.ts`）を直接確認したところ、`Card` インターフェースは `due, stability, difficulty, elapsed_days（非推奨・将来削除予定）, scheduled_days, learning_steps, reps, lapses, state, last_review` を持つ。py-fsrs より詳細な状態（`reps`, `lapses`, `scheduled_days` など）を明示的に保持している点が異なる。
  - URL: https://github.com/open-spaced-repetition/ts-fsrs/blob/main/packages/fsrs/src/models.ts
  - 出典日付: 記載なし（`gh api` で確認したリポジトリの最終 push は 2026-09-11）
  - 確度: 高

- 事実: ts-fsrs の npm レジストリ情報を直接取得したところ、パッケージ名 `ts-fsrs`、最新バージョン `5.4.2`、公開日 2026-09-01、ライセンス MIT。GitHub リポジトリ情報（`gh api repos/open-spaced-repetition/ts-fsrs`）ではスター数780、直近の push は 2026-09-11（このリポジトリは調査時点でも活発にコミットされている）。README では「ts-fsrs: the scheduler for review flows」「FSRS Version: v6」（実装しているアルゴリズムのバージョンが FSRS-6 であることを示すバッジ）と説明されており、**npm パッケージのバージョン番号（5.4.2）と FSRS アルゴリズムのバージョン（v6）は別物**である点に注意。オプティマイザは同リポジトリ内の別パッケージ `@open-spaced-repetition/binding` に分離されている。
  - URL: https://www.npmjs.com/package/ts-fsrs （npm レジストリ API `registry.npmjs.org/ts-fsrs` を直接取得して確認）、リポジトリ本体は https://github.com/open-spaced-repetition/ts-fsrs
  - 出典日付: 2026-09-01（npm 公開日）、2026-09-11（GitHub 最終 push）
  - 確度: 高

- 事実: py-fsrs（PyPI）の登録情報を直接取得したところ、最新バージョン `6.3.2`、公開日 2026-08-09、ライセンス MIT（`Copyright (c) 2022 Open Spaced Repetition`）。GitHub リポジトリのスター数は483。README には「Optimizer (optional)」セクションがあり、`pip install "fsrs[optimizer]"` で追加インストールする形になっている＝スケジューラ本体とオプティマイザは分離されている。
  - URL: https://pypi.org/project/fsrs/ （PyPI JSON API を直接取得）、リポジトリ本体は https://github.com/open-spaced-repetition/py-fsrs
  - 出典日付: 2026-08-09（PyPI 公開日）
  - 確度: 高

- 事実: ts-fsrs / py-fsrs はいずれも `open-spaced-repetition` という GitHub Organization（Anki の FSRS 開発コミュニティ、`fsrs4anki` や `fsrs-rs` と同じ団体）配下の公式実装であり、npm/PyPI 上のプロジェクトページからも同一 Organization を参照していることを確認した。Rust 実装 `fsrs-rs`（Anki 本体が内部で使用しているものと同系統）も同 Organization にあり、BSD-3-Clause ライセンス。
  - URL: https://github.com/open-spaced-repetition
  - 出典日付: 記載なし
  - 確度: 中（Organization ページの一覧はスター数などが取得時点のスナップショット）

- 事実: Anki 公式フォーラムのスレッド「Does FSRS solve "ease hell"?」への回答（2023年12月11日付）で、FSRS の FAQ を引用する形で「FSRS doesn't suffer from the problem of 'Ease Hell'. This problem is solved by mean reversion of difficulty.」「if you keep answering 'good', the difficulty will converge to D0(3)」と説明されている。
  - URL: https://forums.ankiweb.net/t/does-fsrs-solve-ease-hell/38275
  - 出典日付: 2023-12-11（該当投稿の日付）
  - 確度: 中（フォーラム投稿であり運営公式ドキュメントそのものではないが、FSRS のアルゴリズム設計者コミュニティの説明を引用したもの）

- 事実: FSRS のアルゴリズム解説 Wiki（`open-spaced-repetition/awesome-fsrs` の `The Algorithm` ページ、旧 `fsrs4anki` wiki から移設）には、FSRS-5 の difficulty 更新式に平均回帰の項（`w7・D0(4) + (1-w7)・D'`）が含まれると説明されており、これが SM-2 のような「ease（易度係数）が下限に張り付いたまま戻らない」問題を防ぐ設計であることが読み取れる。
  - URL: https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm
  - 出典日付: 記載なし
  - 確度: 中（Wiki 記事であり数式の要約は WebFetch による自動要約に基づく。数式の一次原文を目視で再確認できていない）

- 事実: Anki 公式 FAQ には SM-2 側の問題として「A common complaint with the standard SM-2 algorithm is that repeated failings of a card cause the card to get stuck in "low interval hell".」という記載があり、「ease hell」とほぼ同義の問題（Anki 独自の呼称は "low interval hell"）が公式にも認識されていることが確認できる。
  - URL: https://faqs.ankiweb.net/what-spaced-repetition-algorithm
  - 出典日付: 2024-09-07
  - 確度: 高

## グレーゾーン・未確認

- **「現行の Anki で FSRS が既定でオンになっているか」は、直接的な一次情報の明言を見つけられなかった。** デッキオプションページ（2026-07-07更新）の文面が「turn on FSRS」という表現を使い続けていること、および GitHub の全リリースノートを "FSRS.*default" 等のパターンで検索しても「新規コレクションで FSRS が既定になった」という趣旨の記述が見当たらなかったことから、消極的に「既定ではなくオプトインのまま」と判断した。ただし、これは「見つからなかった」という消極的事実であり、UI 上の初回セットアップウィザードなど、リリースノートに載らない形で既定化されている可能性は排除できない。実装に着手する前に、最新版 Anki のクリーンインストールで実際に確認することを推奨する。
- 「既定パラメータは20,000コレクションの中央値」という数値は 2025年5月時点のドキュメントに基づくもので、FSRS のバージョンが5→6と上がる過程で学習用ベンチマークのサイズが更新されている可能性がある。最新の正確な母数（何件のレビュー・何人のユーザーから学習した既定値か）は未確認。
- ts-fsrs のパッケージバージョン番号（5.4.2）と、実装している FSRS アルゴリズムのバージョン（v6）は別の採番体系であることを本文に明記したが、この対応関係がいつから維持されているか（過去のツールバージョンと FSRS バージョンの対応表）までは調査していない。
- py-fsrs と ts-fsrs で `Card` が持つフィールドが微妙に異なる（py-fsrs は `reps`/`lapses` を明示的に持たず `step` のみ、ts-fsrs は `reps`/`lapses`/`scheduled_days` を明示的に持つ）。どちらも同じ FSRS アルゴリズムを実装しているはずだが、状態表現の抽象化レベルが異なるため、自作アプリでどちらの流儀に合わせるかは設計判断が必要（本調査では判断していない）。
- 「ease hell」という用語自体は Anki 公式ドキュメント（FAQ・マニュアル）には登場せず、Anki 公式は "low interval hell" という表現を使っている。「ease hell」はコミュニティ（フォーラム・非公式解説サイト）で広く使われる呼称であり、両者が同一の問題を指しているという理解でおおむね一致しているが、公式が「ease hell」という語を正式に定義した一次資料は見つからなかった。
- FSRS-6 の平均回帰の具体的な数式（w7・D0(4) + (1-w7)・D' 等）は Wiki ページの自動要約に基づいており、数式そのものを一次ソースで目視確認できていない。厳密な数式が必要になった際は `open-spaced-repetition/awesome-fsrs` wiki または論文原典を直接確認すること。
- SUBTLEX 等とは異なりライセンス面の懸念は薄い（ts-fsrs・py-fsrs とも MIT）が、Anki 本体が使う `fsrs-rs`（BSD-3-Clause）と ts-fsrs/py-fsrs（MIT）とでライセンスが異なる点、また三者間でアルゴリズムの浮動小数点実装差（丸め誤差等）が生じ得るかどうかは未調査。

## 影響する論点

- `docs/plan/english-vocab-app/decisions.md` の「復習スケジューリングは Anki の FSRS を採用する」という決定の実装可能性の裏付けとして使える。特に「オプティマイザなしでも既定パラメータで運用開始できる」という点は、個人利用・データ蓄積前の初期段階での実装方針（オプティマイザは後回しでよい）に直結する。
- `open-questions.md` に立てるべき論点: 「自作実装は ts-fsrs（TypeScript）と py-fsrs（Python）のどちらを使うか」はアプリの実装言語スタックが決まってから判断すべき事項として残る。またオプティマイザ機能（`@open-spaced-repetition/binding` または `fsrs[optimizer]`）を将来的に使うかどうか（レビュー履歴が数百件以上溜まった段階で検討）も未決事項として残せる。
- 「FSRS が既定でオンかどうか未確認」という点は、もし将来 Anki 本体との互換性・データ移行（Anki からのインポート等）を考える場合に、ユーザーが FSRS を有効化しているか SM-2 のままかで前提が変わるため、Anki 連携機能を検討する際に再確認が必要な論点として残せる。

## メインセッションによる原典確認（2026-09-10）

- https://github.com/open-spaced-repetition/ts-fsrs の README を直接確認した。ライセンスは MIT、実装している FSRS のバージョンは v6、スケジューラ（`ts-fsrs`）とパラメータのオプティマイザ（`@open-spaced-repetition/binding`）は別パッケージ。本文の記載と一致する。確度: 高
