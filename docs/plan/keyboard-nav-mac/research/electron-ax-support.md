# macOS キーボードヒント型ナビゲーションツールと Electron / Chromium 対応

- 調査日: 2026-09-21
- 調査手段: Sonnet サブエージェント + メインによる原文確認(メインが確認した原典: Homerow issue #148 の本文とコメント(GitHub API)、Electron docs/tutorial/accessibility.md の AXManualAccessibility の記述、vimac リポジトリが nchudleigh/vimac にあり 3,691★・最終 push 2022-12-31 であること。それ以外はサブエージェントの報告のまま)
- 問い: なぜ Homerow・vimac・Shortcat・neru・mousemaster などの macOS キーボードヒント型ナビゲーションツールは Electron アプリ(Slack・VS Code・Notion・Discord・Claude Desktop)や Chromium ブラウザでしばしば機能不全に陥るのか、AXManualAccessibility / AXEnhancedUserInterface とは何か、Electron はこれを起動のたびに設定する必要があるか、Homerow はこの対応をどう文書化しどんな不具合が報告されているか、OSS ツールはソース/issue上でどう扱っているか、Claude Desktop 固有の報告はあるか、大きな AX ツリーを高速に走査する技術は何か。

## 結論

macOS のキーボードヒント型ナビゲーションツールが Electron アプリ / Chromium ブラウザで機能しにくい根本原因は、Chromium/Electron が**パフォーマンス上の理由でアクセシビリティ機能をデフォルト OFF にし、支援技術の存在を検知して初めて(オンデマンドで)アクセシビリティツリーを構築する**という設計にある。これを外部から強制的に起こす手段として `AXManualAccessibility`(Electron が 2017 年に独自導入、アプリの AXUIElement に対して設定)と、VoiceOver 専用だった旧来の `AXEnhancedUserInterface` の 2 系統の属性が存在し、後者はウィンドウマネージャのアニメーション/位置バグを引き起こすことが Mozilla の公開バグ報告で確認されている。

この技術自体は 2017年(Electron)〜2021年(vimac, Chromium の role 属性読み取りパッチ)にかけて確立された「よく知られた手法」ではあるが、**2026年現在も未解決・再発が続いている**: Homerow 自身の GitHub issue tracker には Claude Desktop・Arc・Slack を名指しした未解決 bug が複数件(2024〜2025年オープンのまま)残っており、Homerow の公式 changelog も 2026年3月時点でなお Chromium 関連の不具合修正を出し続けている。さらに 2026年6月には OpenAI の Codex デスクトップアプリ(Electron製)が `AXManualAccessibility` を true に設定しても AX ツリーを一切公開しない、という一次情報での報告もある。つまり「うまくいく技術」と「実際にうまくいくアプリ」は別問題であり、Homerow の Claude Desktop 不具合報告は Anthropic 側でも未対応、OSS ツール側でも decisive な解決策は確認できなかった。

## 根拠

### (a) AXManualAccessibility / AXEnhancedUserInterface とは何か

- 事実: AXManualAccessibility は Electron の PR #10305 で `ivmirx` が導入。「新しい属性が必要な理由は `AXEnhancedUserInterface` がすでに VoiceOver によって予約されているため("The reason for a new attribute is that `AXEnhancedUserInterface` is already reserved by VoiceOver.")」と本人が明記。
  - URL: https://github.com/electron/electron/pull/10305
  - 出典日付: 2017-09-11(マージ日)
  - 確度: 高

- 事実: Electron 公式ドキュメント(メインで raw markdown を直接確認)は「On macOS, third-party assistive technology can toggle accessibility features inside Electron applications by setting the `AXManualAccessibility` attribute programmatically」と記載し、Objective-C/Swift のサンプルコード(`AXUIElementCreateApplication` でアプリの AXUIElement を取得し `AXUIElementSetAttributeValue(appRef, kAXManualAccessibility, true)` を呼ぶ)を掲載。`app.setAccessibilitySupportEnabled(enabled)` API については「ユーザーのシステム側の支援技術設定が優先され、この設定を上書きする」と明記。
  - URL: https://github.com/electron/electron/blob/main/docs/tutorial/accessibility.md (= https://www.electronjs.org/docs/latest/tutorial/accessibility)
  - 出典日付: 記載なし(main ブランチ、継続更新)
  - 確度: 高

- 事実: 導入者 ivmirx は PR 内で「dev tools によれば(DOM の複雑さと更新頻度に依存する)ある程度のオーバーヘッドがある」とコメント。ただし当時の実機(2012年 Mac mini、Chrome タブ多数)では顕著な劣化は観測されなかった。
  - URL: https://github.com/electron/electron/pull/10305
  - 出典日付: 2017年
  - 確度: 高

- 事実: Firefox も同じ理由(パフォーマンス目的でデフォルト無効)でアクセシビリティを OFF にしており、有効化の唯一の手段が `AXEnhancedUserInterface` だった。これを有効にすると「Spectacle 等でウィンドウを左右にスナップさせようとした際に "sluggish movement and wrong position"(動きがもたつき位置がずれる)といった不具合が発生した」と報告されている。報告者は「Electron はこの問題に対応済みで、別の属性(=AXManualAccessibility)を用意している」と明記し、Firefox にも同様の別属性の実装を求めた。
  - URL: https://bugzilla.mozilla.org/show_bug.cgi?id=1664992
  - 出典日付: 報告 2020年10月、2022年頃に別方式(role属性読み取り時に自動有効化、Bug 1845364)で解消
  - 確度: 高

- 事実: vimac は 2019年10月31日にマージされた PR「Remove Chromium support to fix window managers bug」で、Chromium 向けの `AXEnhancedUserInterface` 使用をいったん撤去している(issue #78 を参照)。vimac 公式ドキュメント `state-of-non-native-support.md`(v0.3.18, 2021-04-22付)には明示的に「Side Effects: Breaks window managers like Spectacle」と記載し、社内 issue #382・#351 を参照している。
  - URL: https://github.com/dexterleng/vimac/pull/62 、 https://github.com/nchudleigh/vimac/blob/master/docs/state-of-non-native-support.md
  - 出典日付: 2019-10-31(PR)/2021-04-22(ドキュメント)
  - 確度: 高

- 事実: Electron 側の実装バグとして、2023年3月1日オープンの Issue #37465「`AXManualAccessibility` attribute can't be set (`kAXErrorAttributeUnsupported`)」がある。Electron 19.1.9 / 22.0.1 / 22.0.2 / 23.1.0(macOS Catalina, x64)で再現。原因は `electron_application.mm` が属性の値チェックはしていたが `accessibilityAttributeNames` で属性の存在自体をアドバタイズしていなかったこと。PR #38102 で修正。
  - URL: https://github.com/electron/electron/issues/37465 、 https://github.com/electron/electron/pull/38102
  - 出典日付: 2023年3月(報告)/2023年4月(修正マージ、取得元によって4/26と5/2の表記ゆれあり)
  - 確度: 高(不具合の存在と修正自体)/中(正確なマージ日)

- 事実: PR #38102 のディスカッションでは、修正後も「`AXManualAccessibility` は依然として `AXUIElementCopyAttributeNames` の結果に現れず、Vimac や AppleScript のようなツールからの発見可能性(discoverability)が制限されている」との指摘がある。
  - URL: https://github.com/electron/electron/pull/38102
  - 出典日付: 2023年
  - 確度: 中(PR コメントの要約経由)

### (b) Electron アプリは起動のたびにこれを設定する必要があるか/無視するアプリはあるか

- 事実: vimac の `state-of-non-native-support.md` によれば、2021年2月13日の Chromium パッチにより「role 属性が読み取られた時点で基本的なアクセシビリティを有効化する」よう検出方式が変わり、Electron 12 以降のアプリでは追加の細工なしに動作するようになった。互換性表では「Electron 12+ = パッチを含み互換」「Electron pre-v12(VSCode・Slack を名指し)= レガシーの support オプションが必要」「Spotify 1.1.57.443 = 古い Chromium のため非互換」と記載。
  - URL: https://github.com/nchudleigh/vimac/blob/master/docs/state-of-non-native-support.md
  - 出典日付: 2021-04-22
  - 確度: 高

- 事実: 2026年現在も AX を一切公開しない Electron アプリが存在する。OpenAI の Codex デスクトップアプリ(Electron製)に関する 2026年6月2日オープンの Issue #25740。Hammerspoon での検証で `applicationElement(Codex):attributeNames()` が空リストを返し `AXWindows` は nil、さらに「`AXManualAccessibility = true` を設定すると成功は返るが、読み戻すと nil になる(=無視されている)」ことが確認されている。VoiceOver を有効にしても解消しない。Hammerspoon / yabai / Rectangle / Moom / AeroSpace / BetterTouchTool すべてが影響を受けると報告。未解決。
  - URL: https://github.com/openai/codex/issues/25740
  - 出典日付: 2026-06-02、未解決(確認時点)
  - 確度: 高

- 事実: 2026年9月14日オープンの Issue(uttrflow/uttrflow-swift #605)は、bundled browser engine 上に構築されたデスクトップアプリは「支援技術クライアントから要求されるまでアクセシビリティツリーを構築しない」とし、「一度有効化されるとアプリが終了するまで有効なまま("stays on until the app quits")」と記述している。これは属性がプロセス単位(=起動ごとの AXUIElement 参照)に紐づき、次回起動時には再度設定が必要であることを示唆する。
  - URL: https://github.com/uttrflow/uttrflow-swift/issues/605
  - 出典日付: 2026-09-14
  - 確度: 中(対象ツールが Homerow/vimac 自体ではなく、一般論としての記述)

- 事実: Electron 公式ドキュメント自体には、「アプリ起動のたびに再設定が必要か」を明記した記述は見つからなかった。
  - URL: https://github.com/electron/electron/blob/main/docs/tutorial/accessibility.md
  - 出典日付: 記載なし
  - 確度: 低(不在の確認)

### (c) Homerow 自身のドキュメント / ユーザー報告

- 事実: Homerow 公式 changelog に v1.5.0(2026-03-15)「Improved Chromium browser performance with instant navigation tree loading」、v1.5.3(2026-03-19)「Fixed accessibility issues with Chrome and other Chromium browsers to prevent Homerow from being automatically disabled」の記載がある。v1.5.1(2026-03-17)、v1.4.1(2025-10-20頃、Tahoe対応)にも関連修正あり。取得できた範囲では changelog 内に "Electron"・"Claude"・"Slack" という単語は見当たらなかった。
  - URL: https://www.homerow.com/changelog
  - 出典日付: 各エントリに記載の日付(上記)
  - 確度: 高(記載内容)/中("Electron"の語が無いという否定的事実)

- 事実: Homerow 公式サイトは Slack・VS Code・Discord・Arc のロゴを「対応アプリ」として並べているが、付随する説明は「Homerow works with most native macOS apps and a growing set of non-native web-based apps.」という一文のみで、Electron/Chromium に関する技術的 FAQ は見当たらなかった。
  - URL: https://www.homerow.app/
  - 出典日付: 記載なし
  - 確度: 高

- 事実: 「Browser labels: Fast/Exhaustive」設定の実在は、GitHub issue #133 のコメントでユーザー devnoname120 が「`Browser labels` を `Exhaustive` に設定していれば常に動いている」と述べ、実際の設定画面のスクリーンショット2枚を添付(Homerow 1.3.2, Arc 1.74.0, macOS 15.2)したことで確認できる。
  - URL: https://github.com/nchudleigh/homerow/issues/133
  - 出典日付: 2025-01-07(コメント日)
  - 確度: 高

- 事実: Claude Desktop に関して確認できた唯一の公開報告は Issue #148(メインが GitHub API で本文・コメントを直接確認)。2024-12-10 オープン、確認時点でも state=open、コメント1件のみ、メンテナ応答なし。報告者 travisjbeck は「Claude デスクトップアプリでラベルがチャット部分を無視する」と報告し、同日の追加コメントで「これは Claude と ChatGPT の Web インターフェースでも同じで、少なくとも Mac の Arc ではシステムがチャットインターフェースを無視する("Further investigation shows this is the case with the web interfaces for both claude and chatgpt. I[t]he system ignores the chat interface at least on Arc on Mac")」と述べている。使用環境は Claude Desktop v0.75, macOS 15.11、Aerospace ウィンドウマネージャ併用。
  - URL: https://github.com/nchudleigh/homerow/issues/148
  - 出典日付: 2024-12-10、確認時点で state=open(GitHub API で直接確認)
  - 確度: 高

- 事実: Arc(Chromium系)関連の他の未解決 issue として、#124(2024-08-14オープン、open のまま): Arc で開いて15〜30分後にウェブページ内のリンクがハイライトされなくなり、ブラウザ側UI(メニューバー等)しかハイライトされなくなる。メンテナ応答なし。#133(2024-09-18オープン、open のまま): Arc で全くタグが表示されない。ユーザー間で「Chromium自体の問題では」「Zen Browser(Firefoxベース)に切り替えたら直った」といったコメントが並ぶが、公式の技術的説明・修正は確認できず。#193(2025-12-20オープン、open のまま): Slack アプリおよび Zen Browser でスクロールモードが正しく機能しない(スクロール可能領域が1つしか認識されない)と報告。
  - URL: https://github.com/nchudleigh/homerow/issues/124 、 https://github.com/nchudleigh/homerow/issues/133 、 https://github.com/nchudleigh/homerow/issues/193
  - 出典日付: 上記各日付
  - 確度: 高(issue自体の内容)/中(メンテナからの反応が本当に皆無かは、取得できた範囲での確認に留まる)

### (d) OSS ツール(vimac, neru, mousemaster, Shortcat)のソース・issue上の扱い

- 事実: vimac(開発終了 2022-12、メインで nchudleigh/vimac リポジトリが 3,691★・最終 push 2022-12-31 であることを確認)は、ソースコード上、frontmost なアプリケーションに対して `AXManualAccessibility` を true に設定する実装だったことが issue #78 のディスカッションで確認できる。`AXEnhancedUserInterface` は上記(a)の通りウィンドウマネージャ副作用のため撤去済み。
  - URL: https://github.com/dexterleng/vimac/issues/78
  - 出典日付: issue オープン 2019-11-22、クローズ済み
  - 確度: 高

- 事実: vimac のマニュアルには「Electron Support」(=AXManualAccessibility相当)と「Non-native Support」/「VoiceOver Emulation」(=AXEnhancedUserInterface相当)という2つの独立したオプションが存在し、「Pre-Electron v12 のアプリには Electron Support の有効化が必要」「Non-native Support は Firefox や CEF アプリなど必要な場合のみ有効化すべき」と明記。
  - URL: https://github.com/nchudleigh/vimac/blob/master/docs/manual.md
  - 出典日付: 記載なし(master ブランチ)
  - 確度: 高

- 事実: vimac ソースコード `TraverseGenericElementService.swift` は、traversal 中に `clipBounds`(親要素で切り取られた可視矩形)と対象要素の frame が交差しない場合、その要素とその子孫をトラバースしない(`isElementVisible()` → `return`)というロジックを実装している(=可視矩形プルーニングの実装例)。`AXTable`/`AXOutline` については `visibleRows` 属性のみを取得するなど、可視要素限定の取得も行っている。
  - URL: https://github.com/nchudleigh/vimac/blob/master/ViMac-Swift/Accessibility/HintMode/TraverseGenericElementService.swift
  - 出典日付: 記載なし(ファイル内コメントは2020-09-06作成)
  - 確度: 高

- 事実: vimac issue #178(2020-08-02オープン、クローズ済み)で、メンテナ dexterleng 自身が「公開アクセシビリティ API(AXUIElement.h)は遅すぎる」とし、アクセシビリティサーバとの XPC 通信が原因であると分析。`AXUIElementCopyMultipleAttributeValues` は個別の `AXUIElementCopyAttributeValue` を複数回呼ぶより高速である、との技術的知見が issue 本文に記載されている(HIServices.framework のリバースエンジニアリングを目的とした issue)。
  - URL: https://github.com/nchudleigh/vimac/issues/178
  - 出典日付: 2020-08-02
  - 確度: 高

- 事実: neru(活動中)の README には Hints モードが「the accessibility tree, on-device OCR, and a pure-Go contour pass」の3エンジンを持つと明記。Grid/Recursive Grid モードは「widget ではなくピクセルを分割するため、canvas・ゲーム・リモートデスクトップ・"thin tree" な Electron アプリでも機能する」と、AX ツリーが薄い/使えない場合の代替手段として設計されていることが README に直接書かれている。
  - URL: https://github.com/y3owk1n/neru (README、raw取得)
  - 出典日付: 記載なし(mainブランチ)
  - 確度: 高

- 事実: neru v1.48.0 リリース(GitHub API で公開日時 2026-07-20T15:06:58Z を確認)のリリースノートに「Neru now auto-detects bundle types (Chromium, Electron, Firefox, WebKit, etc.) automatically」「The accessibility tree is now woken directly — no more `AXManualAccessibility`/`AXEnhancedUserInterface` attribute manipulation」と明記。これ以前は `hints.additional_ax_support` という設定でユーザーが手動で bundle 名を登録し、AXManualAccessibility/AXEnhancedUserInterface を操作する方式だったことが示唆される。この変更以降にどのような代替メカニズムで tree を "wake" しているかの技術的詳細は取得できたリリースノート内には記載がなかった。
  - URL: https://github.com/y3owk1n/neru/releases/tag/v1.48.0
  - 出典日付: 2026-07-20
  - 確度: 高(変更の事実)/低(代替メカニズムの具体的な仕組み=未確認)

- 事実: mousemaster(活動中)の README は macOS での必要権限(Karabiner-Elements の仮想HIDデバイス、`hint.type=ui` のための Accessibility 権限、`mode.zoom` のための画面収録権限)を説明しているが、取得できた README には `AXManualAccessibility` / `AXEnhancedUserInterface` / Electron固有の扱いについての記述は見当たらなかった。
  - URL: https://github.com/petoncle/mousemaster/blob/main/README.md
  - 出典日付: 記載なし
  - 確度: 中(不在の確認であり、README の他ページや実装詳細までは調査していない)

- 事実: Shortcat の公式ドキュメント(accessibility-access ページ)自体は標準的な Accessibility 権限付与手順のみで AXManualAccessibility 等への言及はない。一方、公式 changelog(v0.9.0, 2022-07-11)には「Experimental support for Chrome, Firefox, and Electron apps! This forces applications to expose Accessibility, which can affect performance or cause other behaviours. For example: VS Code will begin emitting audio cues. You can turn this off in VS Code preferences.」と、Electron/Chromium 対応を「実験的」と明言した上で、具体的な副作用(VS Code での音声キュー発生)まで名指しで記載している。
  - URL: https://shortcat.app/docs/getting-started/accessibility-access 、 https://shortcat.app/changelog (= http://updates.shortcatapp.com/changelog.html)
  - 出典日付: 2022-07-11(v0.9.0)
  - 確度: 高

### (e) Claude Desktop に特化した報告

- 事実: Homerow issue #148(上記(c)と同一、メインが GitHub API で本文・コメントを直接確認)が、調査で見つかった唯一の「Claude Desktop × Homerow」を名指しした公開報告。未解決、Anthropic 側・Homerow メンテナ側いずれからの回答も確認できず。
  - URL: https://github.com/nchudleigh/homerow/issues/148
  - 出典日付: 2024-12-10
  - 確度: 高

- 事実: Claude Desktop が Electron ベースであることは、Anthropic 公式の Claude changelog、ビルド v1.49585.0(2026-09-08)の「Updated the app runtime to Electron 44 (Chromium 152); macOS 13 Ventura or later is now required.」という記載で確認できる。
  - URL: https://claude.com/docs/cowork/changelog
  - 出典日付: 2026-09-08
  - 確度: 高

- 事実: 第三者コメンタリー(Daring Fireball, John Gruber、2026-07-03)「Claude's Criminally Bad Electron Mac App Is an Inside Job」は Claude Desktop を "a slow, buggy, and bloated app" と批判し、Electron/Slack/Notion 出身のエンジニアがその設計を主導したと論じているが、アクセシビリティやキーボードナビゲーションの不具合には一切触れていない(取得した範囲内では)。
  - URL: https://daringfireball.net/2026/07/claudes_criminally_bad_mac_app_is_an_inside_job
  - 出典日付: 2026-07-03
  - 確度: 中(第三者の論説記事。一般的な品質批判はあるが、本件のアクセシビリティ論点そのものへの直接的な裏付けにはならない)

- 事実: Claude Desktop を Accessibility API 経由で操作する非公式ツール(claudectl / eldrgeek/mac-controller)のドキュメントに「Claude Desktop builds its accessibility tree only while it is the front app.」と明記されている。Anthropic 公式の説明ではないが、実際に Claude Desktop を AX 経由で自動操作しようとした開発者が確認した挙動として記録されている。
  - URL: https://github.com/eldrgeek/mac-controller
  - 出典日付: 記載なし
  - 確度: 中(非公式サードパーティの実運用知見)

### (f) 大きな AX ツリーの走査レイテンシと高速化手法

- 事実: Chromium 公式のアクセシビリティ概要ドキュメントは「アクセシビリティ機能はデフォルト OFF で、オンデマンドで自動的に有効化される("Accessibility features in Chrome are off by default and enabled automatically on-demand.")」と明記。ブラウザプロセス側に「アクセシビリティツリー全体のキャッシュ表現("a representation of the entire accessibility tree cached in the main process")」を保持し、ネイティブ AX API(同期的)からの呼び出しに対してキャッシュされたスナップショットから同期的に応答することで、マルチプロセスであるレンダラとの通信をブロッキングしないようにしている。更新は「小さな差分更新("small incremental updates")」として送られ、バウンディングボックスはオフセットコンテナ相対でキャッシュされ、スクロールやアニメーション時の全体再シリアライズを避けている。
  - URL: https://chromium.googlesource.com/chromium/src/+/main/docs/accessibility/overview.md
  - 出典日付: 記載なし(mainブランチ)
  - 確度: 高

- 事実: ある macOS 制御 MCP プロジェクトの PR で「get_ui_tree: 1.2s → 31ms、list_windows: 121 → 33ms」という具体的なベンチマーク改善が報告されている。従来は各ノードにつき約9回の個別 AX IPC 呼び出しをしていたが、`AXUIElementCopyMultipleAttributeValues`(失敗時は個別呼び出しへフォールバック)によるバッチ化で実現。
  - URL: https://github.com/AdelElo13/mac-control-mcp/pull/18
  - 出典日付: 記載なし(PR)
  - 確度: 高(対象は本件で挙げられたヒントツール本体ではないが、同種の AX 走査コードに対する直接の計測結果)

- 事実: 第三者解説記事によれば「macOS にはツリー全体を一括取得する API が存在せず、各要素の属性を個別に読む必要がある。1つの要素の複数属性は `AXUIElementCopyMultipleAttributeValues` で1回にまとめて読める」「Windows UIA はツリー全体を一括取得できるが、Linux の AT-SPI2 は個別呼び出しが必須」とされる。
  - URL: https://crowecawcaw.github.io/general/2026/05/30/accessibility-for-computer-use.html
  - 出典日付: 2026-05-30
  - 確度: 中(第三者ブログ)

- 事実: 可視矩形プルーニングの実装例として、vimac のソースコード(上記(d))が該当する。「visible-rect pruning」の具体的な実装をそのまま確認できる一次情報である。
  - URL: https://github.com/nchudleigh/vimac/blob/master/ViMac-Swift/Accessibility/HintMode/TraverseGenericElementService.swift
  - 出典日付: 記載なし
  - 確度: 高

- 事実: 並列クエリ・AXObserver の利用については、Homerow/vimac/neru/mousemaster/Shortcat のいずれについても、直接の裏付けとなる一次情報は見つからなかった。vimac の実際のトラバースコード(TraverseGenericElementService.swift)は単一スレッドの再帰的走査であり、並列化の形跡は確認できなかった。
  - URL: https://github.com/nchudleigh/vimac/blob/master/ViMac-Swift/Accessibility/HintMode/TraverseGenericElementService.swift
  - 出典日付: 記載なし
  - 確度: 低(不在の確認)

## グレーゾーン・未確認

- Electron 公式ドキュメントには「`AXManualAccessibility` をアプリ起動のたびに再設定する必要があるか」についての明示的な記述はない。vimac(issue #78 の記述)や uttrflow の issue(#605)からは、属性がプロセス単位で有効化される(=新しい起動ごとに新しい設定が必要)ことが示唆されるが、Electron / Chromium 自身の一次情報での明言は調べたが分からなかった。
- Firefox 側が 2022年頃に「role 属性読み取り時の自動有効化」(Bug 1845364)に切り替えたという記述は、Bugzilla の別バグへの言及として得られたのみで、そのバグ自体は直接確認していない。
- Homerow の changelog に "Electron" という単語自体が一度も登場しないのか、または取得ツールが見落としただけなのかは断定できない(否定的事実の確認は限界がある)。
- Homerow の GitHub issue(#148, #133, #124)にメンテナ(nchudleigh)からの応答が本当に一件もないのか、取得できた範囲(API経由のコメント取得)を超えて完全に確認したわけではない。
- neru が v1.48.0 で「`AXManualAccessibility`/`AXEnhancedUserInterface` の操作なしにツリーを直接 wake する」ようになったとされるが、その具体的な代替実装(どの API 呼び出し・タイミングで tree を起こしているか)はソースまで確認できておらず、調べたが分からなかった。
- mousemaster と Shortcat の getting-started ドキュメントに AXManualAccessibility / AXEnhancedUserInterface / Electron固有処理への言及がなかったのは事実として確認したが、両プロジェクトのソースコード自体(README以外)までは調査対象外であり、内部で使用している可能性は否定できない(=調べたが分からなかった)。
- Claude Desktop が実際に `AXManualAccessibility` をどう扱うか(サポートしているか、無視するか、ChromeベースのOpenAI Codexデスクトップアプリのように黙殺するか)についての直接的な一次情報(Anthropic自身の記述、または AXUIElementCopyAttributeNames等での実地検証結果)は見つからなかった。claudectl の「front app のときだけツリーを構築する」という記述のみが、非公式ながら最も具体的な手がかりである。
- Homerow issue #148 のコメントが「Claude と ChatGPT の Web版でも同じ問題が Arc で起きる」としている点は、問題が Electron シェル固有ではなく Chromium 上でレンダリングされたチャット UI(おそらく仮想スクロール/動的DOM構造)に起因する可能性を示唆するが、これを裏付ける技術的な深掘り(DOM構造の分析等)は本調査の一次情報の中には見つからなかった。
- 並列 AX クエリや `AXObserver` を用いたキャッシュ無効化について、指定された5ツールのいずれかが実装しているという一次情報は見つからなかった(不在の確認)。

## 影響する論点

- 「よく知られた手法」であることと「実際に機能すること」は別であり、AXManualAccessibility を設定する実装自体は 2017年から存在し vimac 等でも実装例があるが、Homerow はそれを持ちながら(Browser labels 設定として実装済み)なお Claude Desktop・Arc・Slack に関する未解決 issue を抱えている。
- 破綻の再現ポイントが「Electron シェルそのもの」なのか「Chromium 上のチャットUI(仮想スクロール等)」なのかで、対応範囲(Electronラッパーだけ対応すれば足りるのか、Chromiumレンダリングの構造自体への対応が要るのか)が変わりうる。Homerow issue #148 の追加コメントは後者を示唆する数少ない具体的手がかりである。
- 2026年時点でも、Electron製アプリが `AXManualAccessibility` を実装レベルで完全に無視する事例(Codex issue #25740)が現実に存在しており、この手法が「Electronアプリなら原理的に必ず効く」保証にはなっていない。
- Homerow 自身、2026年3月(v1.5.0, v1.5.3)になってようやく Chromium 性能問題・自動無効化バグの修正を出しているなど、Chromium/Electron対応は継続的なメンテナンスコストを要する領域として同社の changelog上でも扱われている。
- neru はむしろ「AXツリーに依存しない Grid/Recursive Grid モード」を Electron 等の薄いツリー向けの代替手段として用意しており、AXManualAccessibility 系の手法に全面的に依拠しない設計選択をしている実例が存在する。
- Shortcat の changelog は Electron 対応を明示的に「Experimental」と位置づけ、対象アプリ側に音声キュー発生などの目に見える副作用を生じさせる場合があることを公表している。
- AXUIElementCopyMultipleAttributeValues によるバッチ化は、実測(1.2s→31ms 等)を伴う効果が複数の一次/準一次情報で裏付けられており、大規模ツリー走査のレイテンシ対策として広く認識されている技術である一方、可視矩形プルーニングは vimac のソースコードで直接確認できた具体的な実装例が1件あるのみで、並列クエリや AXObserver 活用については本調査で確たる裏付けが得られなかった。
- open-questions.md の「Electron 系(Claude Desktop / Slack)を初版の対応範囲に入れるか」に効く。
