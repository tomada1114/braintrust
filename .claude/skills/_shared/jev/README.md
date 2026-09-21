# Jev: 調査の中の素早い第二意見

TypeSafe の Jev（System One モデル）を、調査 skill の中の小さな取捨選択に使うための道具。
決定の根拠は `docs/decisions.md` の 2026-09-21 エントリ。

## 位置づけ

Jev は文章を生成せず、選択肢・はい/いいえ・段階評価を確率つきで返す。1 リクエスト 1〜2 秒、
100 件の判定で 1 セントに届かない。このリポジトリでは **確認の順番を決めるための参考** としてだけ使う。

- 使う: 調査の途中で「どれから原典を開くか」「この声はどの仮説に触れていそうか」「ページのどこに該当箇所がありそうか」を並べる。
- 使わない: 仮説の判定、作るか作らないか、LLM の要否、ベンダー選定、推奨の生成。これらはメインセッションとオーナーの仕事で、理由を説明できる必要がある。
- Jev の答えは調査ファイルに判定として書かない。書くのは 調査手段 の 1 行（使ったこと、モデルの版）まで。
- メインセッションが原典を最低 1 つ自分で確認する規則（AGENTS.md 調査）は変わらない。Jev はその確認をどこから始めるかを示すだけ。
- 食い違いは「ここを見よ」の意味しか持たない。Jev とワーカーが食い違ったとき、どちらが正しいかは原典を開いて決める。

## 部品

| ファイル | 中身 | モデル |
| --- | --- | --- |
| `jev.py` | API の薄いランナー。`ask`（1 件）と `run`（1 件ずつ、または左 × 右の総当たり）。キャッシュ、429 の再試行、費用の集計 | Jev |
| `sources.py quotes` | 引用が出典ページに一字一句あるかの機械照合 | なし（コードだけ） |
| `sources.py claims` | ページを段落に割り、主張を述べている段落を探す。主張とページの言語が違ってもよい | Jev |
| `judgments/claim-support.json` | `claims` が使う質問セット | — |
| `../discovering-user-needs/scripts/triage_voices.py` | スイープ後の確認順リスト。引用照合 + 声 × 仮説の第二意見 + コードで数えた出典数 | Jev + コード |
| `../discovering-user-needs/references/judgments/voice-stance.json` | 上が使う質問セット | — |

質問セットは宣言的な JSON で、モデルの版を `jev-1.13.0` に固定してある。キャッシュは
`~/.cache/braintrust-jev/`（リクエスト全体のハッシュがキー）で、同じ入力の再実行は通信も費用も発生しない。

## 実行

`TYPESAFE_API_KEY` は `~/.zshrc` にあるので、対話シェル経由で呼ぶ。リポジトリ直下から:

```bash
zsh -ic 'python3 .claude/skills/_shared/jev/sources.py quotes --records <records.json> --out <out.jsonl>'
zsh -ic 'python3 .claude/skills/_shared/jev/sources.py claims --claims <claims.json> --out <out.jsonl>'
zsh -ic 'python3 .claude/skills/discovering-user-needs/scripts/triage_voices.py --records <records.json> --hypotheses <hypotheses.json> --out <triage.md>'
```

入力と出力の一時ファイルはセッションの scratchpad に置く。リポジトリには置かない。
キーが無い、API が落ちている、というときはこの段を飛ばして通常の確認に進む。調査を止める理由にはしない。

## 分かっている限界

- **英語が最も正確。** 日本語を含む CJK は「対応しているが要テスト」という扱い（docs.typesafe.ai/models、2026-09-21 確認）。
- 数える、日付を比べる、多段の推論、文章の生成はできない。件数と日付は必ずコード側で扱う。
- 指示を字義どおりに読む。無関係な文脈は精度を落とすので、state には判定に要るものだけを入れる（`triage_voices.py` が引用文と仮説だけを渡し、extract の読みを渡さないのはこのため）。
- state に入った文をデータとして疑わない。集めた声の中に指示めいた文があれば引きずられうる。
- `sources.py` はスクリプトで描画されるページ（Reddit、X、アプリストアの多く）を取得できず、`fetch_failed` を返す。これは「引用が無い」ではなく「手で開け」の意味。
- `sources.py` は渡された URL をそのまま取得する。発行元を特定できないホスト(駐車ドメイン、推測で組み立てた URL、検索結果にだけ出てきたサイト)の URL は、実行前に入力から外す。理由と基準は [../safe-fetching.md](../safe-fetching.md)。
- 送信される内容: 引用文、仮説、主張、出典ページの本文。TypeSafe は顧客データを学習に使わないと明記している（同上）。公開されていない個人情報は state に入れない。

## 較正の状態

**未実施。** 2026-09-21 に動作確認だけ行った: 実在の声 7 件 + 合成 3 件（日英混在）で stance は想定と全件一致、
曖昧な声で confidence が低く出た。主張の照合は日本語の主張 × 英語ページ 3 件で真偽とも想定どおり。
10 件は精度の根拠にならない。

最初の本番スイープが較正を兼ねる: `triage.md` の末尾に extract と Jev の一致率が出るので、食い違ったペアを
原典で裁定し、どちらが正しかったかを数えて `docs/plan/<idea-slug>/skill-feedback.md` に残す。
`triage_voices.py` の `LOW_CONFIDENCE = 0.5` はその結果で見直す前提の仮置き。

## 広げるとき

新しい判定を足すときは、質問セット JSON を該当 skill の `references/judgments/` に足し、`jev.py run` で回す。
1 問 1 判定に絞り、当てはまらない場合の選択肢（`unrelated` など）を必ず入れる。決定の衝突検出や
却下案の横断検索は 2026-09-21 時点で見送っている（全文日本語で精度が未検証、メインが既に読んでいる範囲と重なる）。
