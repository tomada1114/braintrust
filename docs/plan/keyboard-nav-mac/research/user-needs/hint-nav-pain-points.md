# macOS キーボードヒントナビゲーションツールのユーザーの不満・要望

- 調査日: 2026-09-21
- 調査手段: Sonnet サブエージェント + メインによる原文確認(メインが GitHub API で確認した原典: Homerow #106 open・👍12、#212 open・👍13 と本文、#226 open、#211 open・👍4 と本文、#208 open・👍6、#98 open・👍13、#63 open・👍20、#71 open・👍5 と本文、#75 open・👍13、#3 open、#136 open・👍5、neru #933 closed と本文。サブエージェントは #106 を 👍21 と報告したが、API の +1 は 12 だった(他の種類のリアクションを含む合計の可能性)。👍合計の列はサブエージェントの集計のままで未検算。それ以外の引用もサブエージェントの報告のまま)
- 問い: macOS のキーボードヒントナビゲーションツール(Homerow / vimac / neru / Shortcat)のユーザーは何に不満を持ち、何を求め続けているか。看板機能の候補になりうる、実在してまだ解消されていない痛みはどれか。

## 結論

Homerow の Issue 全件(state=all、224 件)、vimac の Issue 上位 30 件、neru の Issue 上位(reactions・comments 基準で 50+ 件)、Hacker News 6 スレッド分の本文とコメントを読んだ。Reddit は `old.reddit.com` / `reddit.com` の JSON エンドポイントが軒並みログイン要求(302)にブロックされ、WebSearch でも実際のスレッド本文を取得できなかったため、今回は実質的に未取得(詳細はグレーゾーン参照)。

最も 👍 と出典数の多いクラスタは「マルチモニター対応」「スクロール機能の不足」「クリックの信頼性(特に Homerow v1.5.0 以降の二度押しバグ)」「価格・配布経路」で、いずれも公式リリースノートや直近のコメントで見る限り**まだ解消されていない**。逆に「アクセシビリティ権限の再付与の手間」「プライバシー/テレメトリー」は 👍 は少ないが、コメント数が多く維持コストの高い構造的な不満で、neru では未解決のまま(有料 Apple Developer アカウントがない、という開発側の制約に起因)。

| クラスタ | 出典数 | 👍合計 | 対応状況 |
|---|---|---|---|
| A. 特定アプリでヒント/ラベルが出ない・機能しない | 11 | 24 | 混在(Notion・#205 は修正済み、Arc・Spotify・Telegram・Teams 等は未解消のまま数年放置) |
| B. メニューバー/Dock/ステータスアイコンの扱い | 5 | 11 | 混在(neru #386 は修正・リリース済み、Homerow #3/#71 は未解消) |
| C. Mission Control 連携 | 6 | 18 | 混在(Homerow はトグル追加で部分対応、neru は「OS に検知 API がない」ため恒久修正なし) |
| D. マルチモニター対応 | 7 | 32 | 主要リクエスト(Homerow #106)は**未解消**(2023-12 open のまま)。neru は個別バグを修正 |
| E. スクロール機能の不足・不具合 | 11 | 58 | 混在。基本機能は各アプリとも実装済みだが、細部(gg/G、特定アプリでのスクロール不可)は未解消のものが多い |
| F. クリックの信頼性(特に Homerow v1.5.0 以降の二度押しバグ) | 11 | 30 | Homerow の二度押しバグ(#201/#212/#226)は**半年以上未修正**。neru 側の個別バグは概ね修正済み |
| G. キーボードレイアウト・IME(日本語/韓国語/Dvorak 等)との相性 | 5 | 20 | 混在。Dvorak の単発リグレッションは即日修正されたが、日本語 Romaji・韓国語 Gureum の入力ソース問題は**未解消**(v1.5.3 時点) |
| H. 他のリマッパー/ホットキーアプリ(Karabiner 等)との競合 | 4 | 11 | neru は根本原因を特定し修正。Homerow/vimac は真のアプリ除外機能自体が無いため競合は残る |
| I. アプリ単位の除外・一時無効化 | 6 | 19 | Homerow は「Exceptions」リストが機能しないとの報告あり(#136)、**未解消のものが多い** |
| J. アクセシビリティ権限の再付与の手間(署名コスト問題) | 5 | 2 | neru は無償の Apple Developer 署名がないため**構造的に未解決**。緩和 UI のみ追加 |
| K. プライバシー/テレメトリー懸念 | 3 | 13 | Homerow の高頻度 analytics 通信への懸念は 2023-10 以来**未対応**。neru は画面共有時の非表示化を数日で実装 |
| L. 価格・ライセンス・配布経路(Homebrew 等) | 8 | 78 | 出典数最多クラスタの一つ。vimac の Homebrew 化は**最後まで未解決**、Homerow は 2 年越しでコミュニティ主導で解決 |
| M. ラベルの配置・視認性・ランダム性 | 8 | 19 | 混在。コントラスト等は改善されたが、「決定論的ラベル」「重なり回避」は Homerow で数年 open のまま |
| N. 速度・CPU・バッテリー消費 | 4 | 4(+関連クラスタに重複あり) | 混在。neru は重大な CPU リーク3件を特定し修正、Homerow のバッテリー問題は未解消 |
| O. クリック以外の操作(コピー・ドラッグ&ドロップ・ホバー)への要望 | 7 | 26 | Homerow は**何年も未実装**。neru は原始的な組み合わせ命令で対応 |
| P. モディファイアクリック(command/shift/option-click)の設計 | 3 | 5 | vimac は設計討議のまま未実装で終了。neru は「モード中に一度タップでスティッキーモディファイア化」という設計で解決 |
| Q. 特定 UI 要素への直接ショートカット割当・スクリプト自動化 | 3 | 0 | neru はスクリプト的な組み合わせで代替可能にしたが、ネイティブな「要素へのバインド」機能ではない |
| R. 設定のプレーンテキスト化・ポータビリティ | 1 | 4 | vimac は明確に却下(plist のまま)。neru の TOML 設定はこの要望への回答そのもの |
| S. プロジェクトの継続性への不安 | 2(新規)+2(重複参照) | 2 | vimac は事実上終了、Homerow も「もう保守されていないのでは」という投稿あり。neru は "Road to v2" で継続姿勢を明言 |
| T. 検索 vs ヒントのワークフロー論争(対象アプリは検索なし方針) | 4 | 6 | Homerow は検索方式への移行で猛反発を受け、ヒント専用モードを復活させた経緯あり |

## 根拠

### A. 特定アプリでヒント/ラベルが出ない・機能しない

- 事実: Homerow #31「Homerow doesn't work with <App>」は開発者自身が立てた「対応してほしいアプリを書き込んでください」という受付スレッドで、54 件のコメントに Spotify・Telegram・Safari・Zotero・Zen browser・Slack サイドバー等、3 年以上にわたり継続的に要望が書き込まれている。2026-02 時点でも Spotify は「advertised to work in spotify so that sucks」という不満が続いている。
  - URL: https://github.com/nchudleigh/homerow/issues/31
  - 出典日付: 2023-01-04(作成)〜2025-10(最終コメント)
  - 確度: 高
- 事実: Homerow #86(Notion 対応)は 2023-07 open、2024-06-17 に v1.0 で修正され、ユーザー p-iknow と開発者 nchudleigh 双方が動作確認を明言。
  - URL: https://github.com/nchudleigh/homerow/issues/86
  - 出典日付: 2024-06-17
  - 確度: 高
- 事実: Homerow #205「Labels not appearing in web content after 1.5.0 update」は 2026-03-17 open、2026-03-20 の v1.5.3 で修正され、ユーザーが `"Thank you for the quick fix @nchudleigh 🙏"` と確認。
  - URL: https://github.com/nchudleigh/homerow/issues/205
  - 出典日付: 2026-03-20
  - 確度: 高
- 事実: vimac #78(Chrome/Chromium/Firefox 対応)は、Chromium のアクセシビリティ有効化がウィンドウマネージャ(Magnet 等)を壊す副作用のため、開発者は Apple・Chromium・Mozilla に個別にバグ報告するまでした上で「実験的サポート」を v0.3.16 で追加するに留めた。根本原因はブラウザ側にあり未解決のまま vimac は開発終了。
  - URL: https://github.com/nchudleigh/vimac/issues/78
  - 出典日付: 2021-03-18
  - 確度: 高
- 事実: neru #1019「Missing hints on some web pages」(Hacker News のコメントリンクにヒントが出ない)は、Electron/Chromium の AX ツリーが非常にノイズが多いためのヒューリスティック(15px 未満の要素を除外)が原因と判明。閾値を 10px に下げるパッチが同日中に main へ反映された。
  - URL: https://github.com/y3owk1n/neru/issues/1019
  - 出典日付: 2026-07-12
  - 確度: 高
- 事実: neru #915「Duplicate hints」(Teams/Outlook で同じラベル(AA 等)が複数出て選択不能になる)は #934 で一部対応されたが、報告者自身が「I might take a shot at fixing that」と述べておりコミュニティ協力で進行した経緯。
  - URL: https://github.com/y3owk1n/neru/issues/915
  - 出典日付: 2026-06-11
  - 確度: 中(完全解決の確認コメントまでは追えていない)

### B. メニューバー/Dock/ステータスアイコンの扱い

- 事実: Homerow #71「Add a way to exclude menu bar items from suggestions」は、メニューバーが押しやすい1文字ラベルを独占してしまうという不満。2023-05 open のまま 2024-12 まで催促コメントが続く。
  > "I never, ever use menubar options, so that would unlock these precious keys for the UI elements."
  - URL: https://github.com/nchudleigh/homerow/issues/71
  - 出典日付: 2024-12-14
  - 確度: 高
- 事実: Homerow #3「Using Homerow closes Apple Menu Dropdown」は 2022-10 open。開発者は「メニュー対応は CGEventTap を使う必要がありバグが多い」と明言して対応を保留、2023-01 に「よくある要望なので可視化のため再オープン」した後も未解決。
  - URL: https://github.com/nchudleigh/homerow/issues/3
  - 出典日付: 2023-01-21
  - 確度: 高
- 事実: neru #386「include_menubar_hints = true が効かない」は、実は Mission Control 誤検知バグが原因(`isMissionControlActive` が常に true になり、メニューバー要素の収集自体をスキップしていた)。30 コメントに渡るユーザーとの共同デバッグの末、`detect_mission_control` をオプトインの config に切り出す形で v1.19.0 として即日リリース。
  - URL: https://github.com/y3owk1n/neru/issues/386
  - 出典日付: 2026-02-19
  - 確度: 高

### C. Mission Control 連携

- 事実: Homerow #203「Any way to turn off labeling in Mission Control?」は v1.5.0 で Mission Control 対応が追加されたが常時オンでオフにできないとの苦情。公式チェンジログの v1.5.3(2026-03-19)に「Added Mission Control auto-activate toggle in clicking settings」と明記されており対応確認できる。
  - URL: https://github.com/nchudleigh/homerow/issues/203 / https://www.homerow.app/changelog
  - 出典日付: 2026-03-19
  - 確度: 高
- 事実: neru #837 のコメントで開発者は「macOS には Mission Control の状態変化を通知する API が存在しない。タイマーによるポーリングでハックするしかなく、OS バージョンによって壊れやすい」と明言。Homerow がどうやっているのか分からないとも述べている。
  > "there's no native way to get any notification from macOS about state changes for mission control at all... it feels very fragile against different OS version."
  - URL: https://github.com/y3owk1n/neru/issues/837
  - 出典日付: 2026-05-22
  - 確度: 高

### D. マルチモニター対応

- 事実: Homerow #106「Multi monitor support」は Homerow 全 Issue 中で 👍 最多(21)。2023-12 open のまま、2025-11-24 のコメントでも「実装されたらすぐ Pro 版を買う」という声があり未解決が続いている。
  > "The day this gets implemented is the day I get the pro version. Really hope this happens at some point"
  - URL: https://github.com/nchudleigh/homerow/issues/106
  - 出典日付: 2025-11-24
  - 確度: 高
- 事実: Homerow #227「Add an option to show labels on the mouse pointer's display」は 2026-09-09 作成(調査日の 12 日前)、未解決。アクティブウィンドウとマウスポインタが別ディスプレイにある場合の使い勝手の悪さを指摘。
  - URL: https://github.com/nchudleigh/homerow/issues/227
  - 出典日付: 2026-09-09
  - 確度: 高
- 事実: neru #1030「System-wide WindowServer stutter on window/monitor switching」は、マルチモニター環境でオーバーレイウィンドウが Space 変更のたびに全 Space へ再アタッチされ WindowServer を 100% CPU に張り付かせる重大な回帰バグ。開発者はソースコードレベルで原因を特定し、後日さらに 2 件のメモリリークも合わせて発見・修正した。
  - URL: https://github.com/y3owk1n/neru/issues/1030
  - 出典日付: 2026-08-03
  - 確度: 高

### E. スクロール機能の不足・不具合

- 事実: Homerow #63「[Scroll] Slack: doesn't seem to work for slack channels side bar」は 👍20 で Homerow 全体でも上位。2023-04 open のまま 2025-04 にも「Would love this supported as well!」というコメントが付き、2 年以上未解決。
  - URL: https://github.com/nchudleigh/homerow/issues/63
  - 出典日付: 2025-04-20
  - 確度: 高
- 事実: Homerow #60「Scroll: vimac like scroll keys」(👍12)は u/d(半画面)、gg/G(上端/下端)、0/$ 等 vim ライクなスクロールキーの要望。コミュニティが具体案を出しているが未実装のまま open。
  - URL: https://github.com/nchudleigh/homerow/issues/60
  - 出典日付: 2023-05-07
  - 確度: 高
- 事実: vimac #146「Add <G> and <gg> to scrolling」(👍10、💬12)は、コミュニティメンバー(NolanChan)が開発者の丁寧なコードナビゲーションの下でコントリビュートし、約9か月かけて実装・クローズされた稀な成功例。
  - URL: https://github.com/nchudleigh/vimac/issues/146
  - 出典日付: 2021-04-23
  - 確度: 高
- 事実: neru #751「in scroll mode, action go_bottom does not work」は Shift+G が本来スクロールすべきところ、テキスト入力欄にフォーカスがあると文字入力として素通りしてしまうバグ。翌日修正。
  - URL: https://github.com/y3owk1n/neru/issues/751
  - 出典日付: 2026-05-05
  - 確度: 高

### F. クリックの信頼性(特に Homerow v1.5.0 以降の二度押しバグ)・自動クリック

- 事実: Homerow #40「Select text input without need for ENTER」(👍7、💬20)は歴史的に最も長く議論された機能要望で、開発者が「auto-click prototype」を作って公開ベータテストを重ね、Alpha 19(2023-04-07)で "Click automatically when label is selected" オプションとして正式実装された。
  - URL: https://github.com/nchudleigh/homerow/issues/40
  - 出典日付: 2023-04-07
  - 確度: 高
- 事実: Homerow #212「Hotkey with Space requires double press since v1.5.0」(👍13)は v1.5.0(2026-03-15)以降のリグレッションで、Cmd+Shift+Space 等 Space を含むショートカットが 1 回目の押下で反応しない。2026-08-16 時点でも "Any updates? It doesn't seem like this is the hardest bug in the world to solve." というコメントが付き、6 か月近く未解決。
  - URL: https://github.com/nchudleigh/homerow/issues/212
  - 出典日付: 2026-08-16
  - 確度: 高
- 事実: 同根と見られる Homerow #226「Activation shortcut swallows every other press」は、オーバーレイをショートカット以外の手段(クリック完了や Esc)で閉じると内部のアクティブ状態フラグが同期しなくなり、次回の起動が無効化される、という根本原因まで報告者が特定している。2026-09-08 作成、未修正。
  - URL: https://github.com/nchudleigh/homerow/issues/226
  - 出典日付: 2026-09-08
  - 確度: 高
- 事実: neru #511「No click with --action left-click in some apps」(Telegram)は、クリック後にカーソルを中央へ戻す処理と、対象アプリ側の「カーソルがまだボタン上にあるか」判定がレースコンディションを起こしていたことが判明。マウスアップ後の待機時間を 50ms→75ms に延ばす等の修正 PR がユーザー検証つきでマージされた。
  - URL: https://github.com/y3owk1n/neru/issues/511
  - 出典日付: 2026-03-07
  - 確度: 高
- 事実: neru #508「Neru stucks if you click too fast」は、再現方法不明のまま報告されたが、開発者自身が高速クリックで再現に成功し、イベントタップ関連のフリーズバグとして同日中に修正。
  - URL: https://github.com/y3owk1n/neru/issues/508
  - 出典日付: 2026-03-06
  - 確度: 高

### G. キーボードレイアウト・IME(日本語/韓国語/Dvorak 等)との相性

- 事実: Homerow #211「Clicking functionality fails with specific Japanese Input Source configuration」は、日本語 Romaji 入力メソッド内の「ABC(英字)」チェックボックスを使い、単体の English(US)ソースを削除した構成だとクリックが登録されなくなるという非常に具体的な再現手順つきの報告。2026-03-26 open のまま未解決。
  - URL: https://github.com/nchudleigh/homerow/issues/211
  - 出典日付: 2026-03-26
  - 確度: 高
- 事実: Homerow #208「Clicking is not working with third party input source in 1.5.3」は韓国語入力の Gureum アプリの "Roman" ソースでクリックが機能しなくなる問題。ユーザーは `1.4.1` に留まらざるを得ず、2026-06-02 時点でも「currently stuck on version 1.4.1 and can't upgrade」と修正を催促している。
  - URL: https://github.com/nchudleigh/homerow/issues/208
  - 出典日付: 2026-06-02
  - 確度: 高
- 事実: Homerow #210「Input source not respected in 1.5.3」(Dvorak)は、公式修正ではなく「アプリの再インストールで直った」というユーザー同士の回避策共有のみで収束。
  - URL: https://github.com/nchudleigh/homerow/issues/210
  - 出典日付: 2026-03-30
  - 確度: 中
- 事実: vimac #201「Ctrl + Space is not a good choice for default hint key」は非英語圏ユーザーからの指摘で、`Ctrl+Space` が中国語等の IME 切り替えのグローバルショートカットと衝突し、"the people in these countries even could not chat with others" とまで表現されている。IntelliJ や Eclipse のコード補完とも衝突するという追加報告あり。
  - URL: https://github.com/nchudleigh/vimac/issues/201
  - 出典日付: 2020-08-31
  - 確度: 高

### H. 他のリマッパー/ホットキーアプリ(Karabiner 等)との競合

- 事実: neru #623「Karabiner and neru conflicts」は、Karabiner で Option+hjkl を矢印キーにリマップしているユーザーが、neru のスティッキーモディファイア検出(Option キーの押下・解放のタイミングで判定)と衝突する問題。開発者は自ら再現し、デバウンス処理を追加するブランチを作って解決した。
  - URL: https://github.com/y3owk1n/neru/issues/623
  - 出典日付: 2026-03-22
  - 確度: 高
- 事実: neru #899「Tap Cmd hotkey」(Mouseless のような修飾キー単体タップでの起動)は、開発者が「スティッキーモディファイアとの共存が複雑で、既存ワークフローの回帰リスクが怖い」と何度も慎重な姿勢を示し、結局実装せず Karabiner での代替を勧めるに留まった。
  - URL: https://github.com/y3owk1n/neru/issues/899
  - 出典日付: 2026-07-25
  - 確度: 高
- 事実: vimac #139「Disable Shortcut in some app.」は iTerm2/Emacs での Ctrl-F 衝突が発端。開発者は「アプリ単位のブロックリストは保守コストが上がる」と本音を述べ、代わりにキー・シーケンス起動方式(fd 等)を実装して代替としたが、報告者自身が「jk を頻繁に打つので誤爆する」と再度不満を述べている。
  - URL: https://github.com/nchudleigh/vimac/issues/139
  - 出典日付: 2021-03-05
  - 確度: 高

### I. アプリ単位の除外・一時無効化

- 事実: Homerow #35「Feature Request: Exclude Application」(👍7)は 2023-01 open のまま、2025-12-02 にも「除外設定したアプリへのショートカットのパススルーができない」という新しいコメントが付いており未解決が続く。
  - URL: https://github.com/nchudleigh/homerow/issues/35
  - 出典日付: 2025-12-02
  - 確度: 高
- 事実: Homerow #136「Deactivate Homerow for specific app」は Exceptions リストに Xcode を追加しても実際には無効化されないというバグ報告。
  - URL: https://github.com/nchudleigh/homerow/issues/136
  - 出典日付: 2024-10-03
  - 確度: 中(その後の追跡コメントなし)
- 事実: Homerow #76「Disable Homerow shortcut while text input focused」は、テキストフィールドにフォーカスがある間だけ無効化したいという要望。ユーザー同士のやり取りで「Grammarly はテキストフィールドの検出ができているようだ」という手がかり共有はあったが、Homerow 側では未実装のまま 2 年以上 open。
  - URL: https://github.com/nchudleigh/homerow/issues/76
  - 出典日付: 2025-05-14
  - 確度: 高

### J. アクセシビリティ権限の再付与の手間(署名コスト問題)

- 事実: neru #737 で開発者は、バンドルが変わる(バージョン更新・ソースからの再ビルド等)たびにアクセシビリティ権限を手動で削除・再付与する必要がある根本原因を詳細に説明している。「有償の Apple Developer アカウントで署名する以外に信頼できる解決策がない」「自己署名は CI では機能しなかった」と明言し、2026-05-02 に「権限が無い場合の案内画面」という緩和策のみ実装した。2026-09-17 のフォローアップコメントでは Input Monitoring 権限も別途再要求が必要になるケースが報告されている。
  > "the only reliable way is to get a developer account and codesign with it (But it's paid, unless someone can sponsor me for the account)"
  - URL: https://github.com/y3owk1n/neru/issues/737
  - 出典日付: 2026-09-17
  - 確度: 高
- 事実: neru #351「Accessibility permisions not granted」は、開発者自身が `tccutil reset All` を提案するなど原因を特定できないまま経過観察でクローズされた例。
  - URL: https://github.com/y3owk1n/neru/issues/351
  - 出典日付: 2026-02-09
  - 確度: 中

### K. プライバシー/テレメトリー懸念

- 事実: Homerow #98「Request for Opt-Out Feature to Address High Frequency Analytics Calls」(👍13)は、ユーザーがネットワークトラフィックを解析し、Homerow が segment.io へ 1 秒間に 100 回以上の analytics 通信を行っていることを実測データとペイロード付きで報告した。2024-11-12 のコメントでも「せめて何を送っているのか透明性が欲しい」との要望があり、2023-12 の作成から 3 年近く未対応。
  > "In the span of writing this post Homerow called segment 10,490 times, and a few hundred more since I started typing this number..."
  - URL: https://github.com/nchudleigh/homerow/issues/98
  - 出典日付: 2024-11-12
  - 確度: 高
- 事実: neru #388「Make overlay invisible on screen sharing」は、画面共有中にオーバーレイ(グリッド/ヒント)が視聴者に見えてしまうプライバシー上の懸念。開発者は `NSWindow.sharingType` API の存在をユーザーから教わり、数日で `toggle_screen_sharing` 機能を実装・リリースした。
  - URL: https://github.com/y3owk1n/neru/issues/388
  - 出典日付: 2026-02-19
  - 確度: 高
- 事実: Hacker News の Shortcat Show HN(2022)で、必須テレメトリーへの opt-out がないことへの強い拒否反応があった。
  > "TL;DR: Shortcat collects diagnostic data for the purposes of product improvements only, using self-hosted services. Yeah, f*ck you. You can't opt out of it. Won't use it then."
  - URL: https://news.ycombinator.com/item?id=33231385
  - 出典日付: 2022-10-17
  - 確度: 高

### L. 価格・ライセンス・配布経路(Homebrew 等)

- 事実: Homerow #29「Add Homebrew formulae」(👍16)は 2023-01-02 open、開発者は「AppCenter の URL が非固定だから」と移行を約束しつつ放置し、最終的に 2025-01-06 にユーザーが「Homebrew cask が既にコミュニティによって追加されている」ことを発見してクローズされた。開発者自身の対応ではなく事実上放置されたまま解決した例。
  - URL: https://github.com/nchudleigh/homerow/issues/29
  - 出典日付: 2025-01-07
  - 確度: 高
- 事実: vimac #152「Brew vimac?」(👍15、💬27)は 2020-06-02 open のまま vimac が開発終了するまで正式解決せず、AppCenter の署名付き URL が定期的に変わる問題、Homebrew cask 命名規則("Mac" 語の扱い)を巡る Homebrew Cask 開発者本人の詳細な解説、コミュニティによる非公式 tap の乱立という経緯を経て、公式には未解決のまま終わった。
  - URL: https://github.com/nchudleigh/vimac/issues/152
  - 出典日付: 2021-04-08(最終的な技術的やり取り)
  - 確度: 高
- 事実: vimac #477「State of project」(👍17、💬19)は 2022-04-24 open。開発が 1 年以上止まっていることへの問い合わせに対し、開発者は 2022-06-25 に「Homerow という新しいアプリに移行した」と回答。ユーザーからは「有償でもいいから使い続けたい」という声が複数あった。
  > "Would also be willing to pay @dexterleng - makes for a great companion to KindaVim"
  - URL: https://github.com/nchudleigh/vimac/issues/477
  - 出典日付: 2022-06-25
  - 確度: 高
- 事実: Hacker News の Homerow Show HN(2022-06-30)で価格への抵抗感が複数示された。
  > "Love vim, love the Mac. But $49 seems pretty high for something like this."
  > "$25 feels like the max I'd consider for this type of thing."
  - URL: https://news.ycombinator.com/item?id=31938689
  - 出典日付: 2022-06-30
  - 確度: 高

### M. ラベルの配置・視認性・ランダム性

- 事実: Homerow #75「Deterministic click labels」(👍13)は、ヒントラベルが毎回ランダムな文字に再割り当てされるため、一時的にラベルを非表示にして裏を確認し再表示すると別のラベルに変わってしまい混乱する、という指摘。2023-06 open のまま未解決。
  - URL: https://github.com/nchudleigh/homerow/issues/75
  - 出典日付: 2023-06-28
  - 確度: 高
- 事実: Homerow #24「Label placement in 0.13 is suboptimal for lists」は、開発者が水平ラベル配置を試作(ビルドまで配布)したものの「場所が一貫しない方が目が迷う」と判断して垂直配置に差し戻し、根本的な解決策は見つからないまま open で継続。
  - URL: https://github.com/nchudleigh/homerow/issues/24
  - 出典日付: 2023-01-09
  - 確度: 高
- 事実: neru #933「One letter hints」は、常に 1 文字ラベルにしてほしいという要望に対し、開発者が「26 文字を超えるラベル数の画面ではどうするのか」と技術的な限界を説明。最終的には `label_direction`(reverse/normal)という設定を追加することで妥協点を探った。
  - URL: https://github.com/y3owk1n/neru/issues/933
  - 出典日付: 2026-06-18
  - 確度: 高

### N. 速度・CPU・バッテリー消費

- 事実: Homerow #209「High battery usage」は、Zoom や並列 Claude セッションを含むターミナルより Homerow の方が電力を消費しているというスクリーンショット付き報告。2026-03-20 作成、コメントなしのまま未解決。
  - URL: https://github.com/nchudleigh/homerow/issues/209
  - 出典日付: 2026-03-20
  - 確度: 中
- 事実: vimac #449「Slow Response Time」は Catalina でヒント選択から実行まで約2秒の遅延があるという報告。open のまま vimac は開発終了。
  - URL: https://github.com/nchudleigh/vimac/issues/449
  - 出典日付: 2021-08-13
  - 確度: 中
- 事実: Hacker News の vimac Show HN(2020)で、開発者自身が「Electron/WebKit アプリの UI ツリーを辿るための大量の mach IPC 呼び出しが高 CPU の原因だった」と説明し、投稿の2日前に修正したばかりだったと明かしている。
  - URL: https://news.ycombinator.com/item?id=24323860
  - 出典日付: 2020-08-30
  - 確度: 高

### O. クリック以外の操作(テキスト選択・コピー・ドラッグ&ドロップ・ホバー)への要望

- 事実: Homerow #153「Support yank with keyboard only」(👍8)と #66「Copy text from labeled area」(👍7)はいずれも Vimium の `yf`(ヤンク)のような、クリックせずにテキストやリンクをコピーする機能の要望。どちらも何年も open のまま。
  - URL: https://github.com/nchudleigh/homerow/issues/153 / https://github.com/nchudleigh/homerow/issues/66
  - 出典日付: 2024-12-16 / 2025-02-16
  - 確度: 高
- 事実: Homerow #51「Hover - Move the mouse cursor to the target label without click」(👍9)は、ホバーだけしたいというニーズ。ユーザーの一つは「右クリック(shift+ラベル)してから Esc すると疑似的にホバーできる」という非公式な回避策を共有している。
  > "What I currently do is 'right click' ... and then press <Esc>, which leaves the mouse at the location, effectively hovering the element."
  - URL: https://github.com/nchudleigh/homerow/issues/51
  - 出典日付: 2025-04-10
  - 確度: 高
- 事実: vimac #383「Idea: Support for Drag and Drop or Selection」は、クリック/リリースをトグルするキーを使ったドラッグ&ドロップの設計を提案者と開発者が数往復議論したが、実装には至らず vimac は開発終了。
  - URL: https://github.com/nchudleigh/vimac/issues/383
  - 出典日付: 2021-04-29
  - 確度: 高
- 事実: neru #1102「Additional Hotkeys for click-and-drag workflows」は、中クリック/右クリックの mouse down/up や、選択位置へのカーソル移動用ホットキーの追加要望。クローズはしているが「mouse down/up の非対称な操作感が良くない、トグル式にしたい」という UX 上の指摘も含まれる。
  - URL: https://github.com/y3owk1n/neru/issues/1102
  - 出典日付: 2026-07-30
  - 確度: 中

### P. モディファイアクリック(command/shift/option-click)の設計

- 事実: vimac #204「Need a way to do command-click」(👍5、💬12)は、コマンドクリック(新規タブで開く等)がダブルクリックに割り当てられていて衝突する、という指摘から始まり、`D+ラベル`(ダブルクリック)、`C+ラベル`(コントロールクリック)のようなプレフィックス方式の提案まで議論が進んだが、実装されないまま vimac は開発終了した。
  - URL: https://github.com/nchudleigh/vimac/issues/204
  - 出典日付: 2021-05-18
  - 確度: 高
- 事実: neru #576「Command + click implementation in scroll mode」は、開発者が「グリッドモードでは L/R/M キー自体がラベル文字と衝突するため、Shift+L 等の固定バインドしかできない」という設計上の悩みを吐露した末、「モード中に一度モディファイアキーをタップしてから操作すると、次のアクションにそのモディファイアが乗る」というスティッキーモディファイア方式の一般化(#586)で解決した。
  - URL: https://github.com/y3owk1n/neru/issues/576
  - 出典日付: 2026-03-15
  - 確度: 高

### Q. 特定 UI 要素への直接ショートカット割当・スクリプト自動化

- 事実: neru #998「Create a custom keyboard shortcut for a specific UI element」は、Claude for macOS が Cmd+1/2/3 のタブ切り替えショートカットを削除したことをきっかけに立てられた要望。開発者は「特定要素へのネイティブなバインド」は実装せず、代わりに `move_mouse --window --x -1000 --y -1000` のような相対座標移動命令や `app_configs`(バンドル ID ごとのショートカット上書き)といったスクリプト的な組み合わせ機能で対応可能にした。報告者は最終的に Neru の `action` を呼ぶシェルスクリプトを BetterTouchTool 経由でバインドする形で解決している。
  - URL: https://github.com/y3owk1n/neru/issues/998
  - 出典日付: 2026-07-10
  - 確度: 高

### R. 設定のプレーンテキスト化・ポータビリティ

- 事実: vimac #230「Move from User Preferences to JSON stored in ~/.config/vimac/」(👍4、💬9)は、設定を他マシンへ持ち運びたい(dotfiles 管理したい)という動機から出たが、開発者は「UI の発見可能性を優先したい」「config ファイル対応は保守コストに見合わない」と明言して却下した。ユーザーは代わりに `defaults write com.dexterlang.vimac ...` のような shell コマンドで疑似的にポータブルな設定を実現していた。
  - URL: https://github.com/nchudleigh/vimac/issues/230
  - 出典日付: 2021-05-20
  - 確度: 高
- 事実: neru は最初から TOML ファイルでの設定を前提に設計されており(README や各 Issue のテンプレートに `[hotkeys]` 等の TOML スニペットが標準的に使われている)、vimac ユーザーが求めていたポータブルな設定管理をそのまま体現している。ただし「設定 UI が無いこと」自体が新規ユーザーの学習コストになっている様子も複数の Issue(#909 のフィードバック等)から読み取れる。
  - URL: https://github.com/y3owk1n/neru
  - 出典日付: 記載なし
  - 確度: 中

### S. プロジェクトの継続性への不安

- 事実: Homerow #111「This project has been unmaintained for a long time. Well, great!」(👍8)という皮肉混じりの投稿がきっかけで、「買収されたのでは」という憶測コメントまで生まれたが、2024-06-17 に nchudleigh が v1.0 リリースをもって開発継続を表明した。
  - URL: https://github.com/nchudleigh/homerow/issues/111
  - 出典日付: 2024-06-17
  - 確度: 高
- 事実: Hacker News の vimac Show HN で、ユーザーが「vimac がもう更新されていないことも、Homerow という後継があることも知らなかった。トップページで案内すべき」と指摘している。
  > "I highly recommend updating the main page of this project with what you said here and your link to Homerow."
  - URL: https://news.ycombinator.com/item?id=24327727
  - 出典日付: 2022-07-27
  - 確度: 高
- 事実: neru #1663「Road to v2」(👍2)は、開発者が 2027 年年始の v2 リリースに向けて機能開発を凍結し性能・バグ修正に専念すると宣言した投稿。継続開発の意思表示として好意的に受け止められている。
  - URL: https://github.com/y3owk1n/neru/issues/1663
  - 出典日付: 2026-09-10
  - 確度: 高

### T. 検索 vs ヒントのワークフロー論争(対象アプリは検索なし方針)

- 事実: Homerow #6「Where is the 'keyboard shortcuts' feature?」(👍6、💬20)は、旧 Homerow(vimac 後継の初代)がヒント専用方式から検索方式に切り替えた際の大規模な反発スレッド。
  > "I am quite disappointed with the change... Currently the app is a worse version of Wooshy.app"
  最終的に開発者は「Shift 押下でヒントのみ、離すと検索」というハイブリッド方式(Jumpers)を作り、ヒント専用の "Classic workflow" を残すことで収束させた。
  - URL: https://github.com/nchudleigh/homerow/issues/6
  - 出典日付: 2022-12-05
  - 確度: 高
- 事実: Homerow #17「Please add settings for 1) lowercased click area identifiers 2) automatic click on entering lowercase identifiers」(💬15)も同根で、検索を使わずヒントのみで即クリックしたいという要望。最終的に "Classic Workflow"(検索なし)と "Press Space to click" オプションが追加されて収束。
  - URL: https://github.com/nchudleigh/homerow/issues/17
  - 出典日付: 2023-04-07
  - 確度: 高
- 事実: Hacker News の vimac Show HN で、js2sj が「vim は一度モードに入れば連続操作できるが、vimac は 1 操作ごとにモードへ入り直す必要があり生産的に感じない」と、モード持続性の欠如を批判している。これは今回の計画アプリが「スコープ別に固定ショートカット」を採用する上で、1 操作ごとの再起動コストが同様に問題になりうることを示唆する。
  - URL: https://news.ycombinator.com/item?id=24328021
  - 出典日付: 2020-08-31
  - 確度: 中

## グレーゾーン・未確認

- **Reddit は実質未取得。** `old.reddit.com` / `www.reddit.com` の `.json` エンドポイントはいずれもログインページへの 302 リダイレクトを返し、直接取得できなかった(safe-fetching の「既知ホスト」には該当するが、Reddit 側が未認証アクセスをブロックする仕様変更をしたと見られる)。WebSearch でも `site:reddit.com` を含む複数クエリを試したが、実際のスレッド本文・コメントを含む検索結果は得られず、alternativeto.net や公式サイトの説明文しか返ってこなかった。唯一確認できた Reddit への言及は、Homerow Issue #66 のコメント内で shwanton がリンクした次の URL のみで、本文は未取得。
  - URL(未取得): https://www.reddit.com/r/macapps/comments/16fb6ql/need_help_with_shortcat_app_or_homerow_or_looking/
  - 確度: 低(スニペットすら取得できていないため内容不明)
- **Shortcat 自身の公開 Issue トラッカーは存在しない。** `gh api search/repositories?q=shortcat` で `mergesort/Shortcat`(iOS の UITableView 用キーボードナビゲーションライブラリ、無関係)や `quexten/swiftmouse`(Linux 向けクローン)がヒットしたが、shortcat.app(macOS 版、開発者 `_chendo_`)自身のリポジトリは非公開または存在しないと判断した。Shortcat に関する声は Hacker News の 3 回の Show HN(2012/2013、2022)経由でのみ収集した。
- **neru #933(one-letter hints)・#548(mode indicator dot)** はクローズされているが、機能が実際にリリースされ本人が満足したところまでのコメントは確認できたものの、最終的な安定動作の追跡コメントは薄く、確度は中程度に留める。
- **クラスタ間の重複**: Homerow #98(analytics)は「プライバシー」と「速度・CPU」の両方に関わる。neru #1030(WindowServer stutter)は「マルチモニター」起因だが実質は「速度」の問題。件数集計では二重計上を避けるため主たるクラスタ 1 つにのみ計上し、他方では参照のみとした。
- **Homerow の総 Issue 224 件のうち、本調査で本文を読んだのは reactions/comments が一定数以上、または直近 12 か月に作成された計 78 件。** 残りの低反応・低コメントの Issue(タイトルのみ確認)は読んでいないため、そこに埋もれた少数意見がある可能性は否定できない。vimac・neru も同様に上位/直近を中心に読んでおり、全件精査ではない。

## 影響する論点

open-questions.md の「看板になる差別化が何か」と「オーナー以外に同じ痛みがあるか」に効く。
