# 開発者向けツールの需要調査(作者として名前が売れるプロダクト探し・第1〜2ラウンド)

- 調査日: 2026-09-20
- 調査手段: Sonnet サブエージェント 8 本 + メインによる一次確認(GitHub API / HN Algolia API)
- 問い: 個人が無料/OSS で出して「〇〇の作者」として知名度を取れる開発者向けプロダクトは、どこが空いているか
- 状態: **途中**。オーナーが「開発者限定だとニッチ。対象を Mac の操作効率化(Raycast / Homerow 系)など一般パワーユーザーまで広げて調べ直す」と方針変更。このファイルは再調査を省くための引き継ぎノート。

凡例: 【確認済】= メインが API で直接取得 /【報告】= サブエージェント報告で未再確認 /【推測】= 解釈。
Reddit の数値は非公式ミラー(redlib / safereddit.com)経由の参考値。

## 前提(オーナーの決定事項)

- 市場はグローバル(英語)。指標は GitHub スター、HN、Product Hunt。まず無料/OSS、収益化は当たってから。
- 既存主力ツールの置き換え(ターミナル、エディタ)、エディタ拡張、スマホアプリは対象外。
- スクショ/GIF 1 枚で伝わること。
- 形態の傾向: macOS アプリ(メニューバー含む)と CLI。ブラウザ拡張は半信半疑。
- 2026-09-20 追加: Claude Code や AI とは**あえて無関係**にする。対象も開発者限定にしない(Mac のパワーユーザー一般まで広げる)。
- ゴールは日本の開発者イベントに「〇〇の作者」で呼ばれる知名度。日本語圏には配布網あり(書籍、Udemy、X/Zenn/Qiita)、英語圏にはなし。

## 結論

### 当たる型(確度: 中〜高)

1. **1 つの問いに答えるツール**が直近で最強。witr「なぜ動いている?」526pt / 22.4k★(9 か月)、WhatCable「このケーブルは何?」566pt / 8.8k★(4.5 か月)、isd(systemd TUI)546pt、ccusage 18.7k★【確認済】。多機能な道具箱型は初速が遅い。
2. **止まった/信頼を失った人気ツールの無料 OSS 後継**。Ice(29.7k★、2025-09 から push なし、Tahoe 安定版要望 73👍)→ Thaw 11.4k★(8 か月)【確認済】。Bartender 買収炎上 → Ice【報告】。
3. **k9s / lazygit for X 型 TUI**。taws(AWS)390pt / 2.3k★、posting 12.4k★、harlequin 6.4k★【確認済】。X の母数が小さいと伸びない。
4. **見て楽しいもの**。gitlogue 159pt / 5.0k★。Claude Code の最多👍 issue は「Buddy を返せ」1,181👍【確認済】。
5. 飽和領域でも普遍的な痛みなら後発が当たる(port-killer 5.1k★ / 9 か月、Sonar 204pt)。ただし決定版にはなりにくい【確認済+推測】。
6. 経路: Show HN が初速の本線。macOS アプリは Homebrew cask と r/macapps。Windows 対応要望は複数スレッドで反復【報告】。
7. **プロダクトのヒットと作者名の認知は別**。Stats 42k★ や Rectangle は作者名が知られていない【報告】。名前が売れるのは発信・登壇を重ねた場合【推測】。

### 避ける場所(確度: 高)

- ホスト側が作れば終わる領域: Homebrew 7.0 が GUI 同梱(WailBrew 2.8k★ が直撃)【報告】、`gh auth switch` で複数アカウント問題が大半解決【報告】、AI 周辺では Anthropic が worktree 管理 / 差分ビューア / /rewind / /voice / Remote Control を本体に取り込み【報告・未検証】。
- 外付けで解けない痛み: terraform、actions/runner、docker/for-mac(2,175👍)はホスト修正必須【報告】。
- 飽和: 使用量モニター(ccusage + 派生 8 以上)、Mac 掃除(Mole 67.9k★)、メニューバー管理(Thaw)、ポートキラー、クリップボード、ウィンドウ管理、ランチャー、API クライアント(Bruno、Yaak 19.2k★)、secrets、依存更新、changelog、ターミナル録画(VHS)、dotfiles、jq 代替、コンテキスト梱包(repomix 28.4k★)、スペック駆動(Spec Kit)、AI コードレビュー【確認済+報告】。
- アプリごとの音量ミキサーは需要最大級(r/macapps 2,181pt、r/MacOS 5,817pt)だが FineTune が取得済み【報告】。

### ブラウザ拡張の見解(確度: 中)

後回し推奨。拡張のヒットだけで開発者として名が通った例は見つからず。Refined GitHub 32.2k★【確認済】は作者が先に有名。Language Reactor は 200 万ユーザーだが作者名は出てこない【報告】。過去 12 か月の Show HN で 150pt 超の拡張は 1 件のみ(検索語依存)【確認済】。成立条件は「ブラウザ内でしかできない」「中核を OSS ライブラリに切り出す」「データ/API がエコシステムになる」【推測】。

### 出した候補と確信度(開発者向け)

非 AI:
1. launchd の可視化(macOS アプリ + CLI/TUI)— 中〜高。isd 546pt の macOS 版。競合は全部 150★ 未満(launchk 137★ 停止、launchd-ui 145★、launchdeck 15★)、標準は有料 LaunchControl $19.99【確認済】。macOS 版を求める直接の声は未取得。
2. GitHub Actions の失敗を読む TUI — 中〜高。cli/cli #3484 76👍(2021 年〜未解決)、act 72k★、lazyactions 101★ / gama 482★ 停滞【確認済】。gh-dash 12.5k★ の拡張が懸念。
3. Cloudflare の k9s — 中。競合は全部 57★ 以下【確認済】。ただし workers-sdk の関連 issue は票が弱い【報告】。
4. ターミナル PDF ビューア — 中〜低。doxx 3.8k★ のスレッドに直接要望【報告】。itsjunetime/tdf の現状未確認。
5. localhost に名前と HTTPS を付けるメニューバー(mkcert 59.7k★ は 2024-08 から停滞【確認済】)— 中〜低。
6. メモリも測るベンチ CLI(hyperfine #86 76👍【確認済】)— 低〜中。
7. 止まった macOS 開発ツールの後継(HexFiend 5.9k★ 2025-06 停止、Periphery 6.2k★ アーカイブ【確認済】)— 低〜中。
8. 軽量ネイティブ SSH ハブ(XPipe 14.5k★ が強い)/ ネイティブ diff GUI / Apple container GUI(orchard 1.6k★)/ LAN 可視化(sniffnet 41k★)— 低。

AI 周辺(オーナーが対象から外した。参考):
- エージェントの残留物(プロセス/ポート/worktree)可視化 — 中。専用ツールは全部 17★ 以下、issue は小粒(#1935 19👍)【確認済】。
- セッションのリプレイ共有 — 中。既存は 75★ 以下【確認済】。
- 複数アカウント切替は需要最大(818👍 / 731👍【確認済】)だが claude-swap 2.7k★ が先行、規約グレー。
- コンテキスト可視化は競合が全部 23★ 以下で、需要が弱い兆候とも読める【確認済】。

## 根拠(主な一次ソース)

- 事実: 各リポジトリのスター数・最終 push・アーカイブ状態、issue の👍数
  - URL: https://api.github.com (gh api repos/…、search/issues sort=reactions-+1)
  - 出典日付: 2026-09-20 取得
  - 確度: 高
- 事実: Show HN の点数と日付(witr 46392910、WhatCable 47972511、isd 42749402、taws 46491749、Sonar 47452515、gitlogue 45964956)
  - URL: https://hn.algolia.com/api/v1/items/<id>
  - 出典日付: 2026-09-20 取得
  - 確度: 高
- 事実: r/macapps の高評価投稿(FineTune、Thaw 626pt、Homebrew 7.0 GUI 656pt、「Vibeware がこのサブを殺した」1,030pt、Raycast 値上げ批判の投稿削除への反発 405pt、SuperCmd(Raycast の OSS 代替)461pt / 3.2k★)
  - URL: reddit.com/r/macapps/comments/<id>(1qhiexg、1qwkq38、1wfjbir、1nompg5、1wfi93v、1sfve50)
  - 出典日付: 2025-09〜2026-09
  - 確度: 中(ミラー経由、メイン未再確認。SuperCmd のスターのみ確認済)
- 事実: macOS の更新でメニューバー/WM 系が壊れ続ける(hidden #360 156👍、yabai #2684「The future」126👍)
  - URL: https://github.com/dwarvesf/hidden/issues/360 、https://github.com/asmvik/yabai/issues/2684
  - 確度: 高【確認済】

## グレーゾーン・未確認

- 第 1 ラウンドのサブエージェントは集約記事(dev.to 等)に依拠し、HN の証拠を 2 件誤読していた(OpenAPI ずれ検出の Ask HN は 1pt、PR 再レビューのコメントは逆文脈)。第 1 ラウンド由来の【報告】は弱い。
- Reddit は直接取得不可(403)。WebFetch も reddit.com を拒否。redlib ミラーか検索経由になる。
- HN 本体は 429 を返す。Algolia API は通る。
- Homebrew/brew と jdx/mise は issue を使っておらず、issue 票の手法では捕捉できない。
- 2026 年の Anthropic のベンダー機能(デスクトップ刷新等)は【報告】のみで未検証。
- 「Mac の操作効率化」(Raycast / Homerow / キーボード操作系)は**未調査**。今回わかっているのは、ランチャーは競合過多だが Raycast 値上げで OSS 代替需要が出ている、という断片だけ。
- 作者名の認知につながるかは、どの候補でも未検証。

## 影響する論点

- 対象を開発者に限るか、Mac のパワーユーザー一般に広げるか(オーナーは後者で再調査する方針)。
- 広げた場合、「開発者イベントに呼ばれる知名度」というゴールとどう接続するか(Raycast や Homerow の作者は開発者コミュニティで知られているか)。
