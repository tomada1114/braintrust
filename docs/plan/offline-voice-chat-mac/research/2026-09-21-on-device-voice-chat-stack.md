# macOS で「オフラインの音声会話アプリ」を組むための部品の確認

- 調査日: 2026-09-21
- 調査手段: メインセッションの WebSearch(検索結果の要約のみ。**各ページ本文は開いていない**)+ モデルの既存知識(2026-05 時点まで)
- 問い: macOS 27 以降で、音声入力 → LLM の返答 → 読み上げ、をオフライン・無料・API キー不要で組めるか。組めるなら部品は何か

## 結論

組める。3 つの部品(音声認識、LLM、読み上げ)はすべて macOS 標準の Swift API としてあり、いずれもオンデバイスで動く。3 つを組み合わせた OSS の実例(Talkify、ただし音声入力アプリで会話アプリではない)も存在する。

| 役割 | 部品 | オフライン | 確度 |
|---|---|---|---|
| 音声 → 文字 | SpeechAnalyzer / SpeechTranscriber(Speech フレームワーク、macOS 26〜) | 可 | 高(Apple 公式ドキュメントあり、WWDC25 で発表) |
| 返答を作る | Foundation Models framework(Apple のオンデバイス LLM、macOS 26〜) | 可 | 高 |
| 文字 → 音声 | AVSpeechSynthesizer(拡張 / プレミアム音声をダウンロードすると自然になる) | 可 | 高 |
| 文字 → 音声(より自然) | Kokoro-82M を MLX Swift で動かす(kokoro-swift-mlx、mlx-audio-swift) | 可(モデル同梱) | 中 |

## 根拠

- 事実: Foundation Models framework は Apple Intelligence のオンデバイス LLM を Swift から呼ぶフレームワーク。iOS/macOS 26 で導入。無料・オフライン・キー不要。構造化出力(`@Generable`)と tool calling がある。Apple Intelligence 対応の Apple Silicon Mac が前提
  - URL: https://developer.apple.com/videos/play/wwdc2026/241/ (WWDC26「What's new in the Foundation Models framework」)
  - 出典日付: 2026-06
  - 確度: 高(基本仕様は WWDC25 以降の公式情報。WWDC26 の差分はページ未読)
- 事実: WWDC26(2026-06)で第 3 世代モデルを発表。オンデバイスは AFM 3 Core(3B dense)と AFM 3 Core Advanced(20B sparse、1 リクエストあたり 1〜4B が活性)。Google と協力して開発したと説明されている
  - URL: https://rits.shanghai.nyu.edu/ai/apple-foundation-models-macos-27/ ほか
  - 出典日付: 記載なし(2026-09-21 取得)
  - 確度: 中(第三者のまとめ。Apple 公式ページは未読)
- 事実: WWDC26 で Foundation Models に公開プロトコル層が入り、クラウド LLM(Claude 等)やローカル OSS モデルを同じ API の背後に差し替えられるようになった
  - URL: https://dev.to/arshtechpro/wwdc-2026-apple-just-opened-the-foundation-models-framework-to-any-llm-provider-5ejn / https://blog.vibecoder.me/apple-foundation-models-claude-swift-wwdc-2026
  - 出典日付: 記載なし
  - 確度: 中(第三者ブログ)
- 事実: macOS 27 "Golden Gate" は 2026-09-14 公開、Apple Silicon 専用。オンデバイスモデルを叩く `/usr/bin/fm` CLI が標準で入っている。Python SDK もあるとの記述
  - URL: https://rits.shanghai.nyu.edu/ai/apple-foundation-models-macos-27/ / https://qiita.com/StayHomeLabNet/items/4b8178717abf23c7022e / https://qiita.com/chibicco/items/ef1a9e40c4cdf15d8e21
  - 出典日付: 記載なし
  - 確度: 中(手元の Mac で `fm` を叩けば即確認できる)
- 事実: SpeechAnalyzer は macOS 26 以降に標準搭載、20 言語対応、オンデバイス
  - URL: https://developer.apple.com/documentation/Speech/bringing-advanced-speech-to-text-capabilities-to-your-app / https://dicta.to/blog/best-offline-speech-to-text-mac/
  - 出典日付: 記載なし
  - 確度: 高(公式ドキュメントあり。言語数は第三者記事)
- 事実: AVSpeechSynthesizer はオンデバイスで合成し、オフラインで動く
  - URL: https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer / https://www.callstack.com/blog/on-device-text-to-speech-on-apple-devices-with-ai-sdk
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Talkify(OSS、macOS)は SpeechAnalyzer/SpeechTranscriber で認識、AVSpeechSynthesizer で読み上げ、Translation で翻訳、Foundation Models で整形を、すべてオンデバイスで行う音声入力アプリ
  - URL: https://github.com/tornikegomareli/Talkify
  - 出典日付: 記載なし
  - 確度: 中(検索結果の要約。README 未読)
- 事実: Kokoro TTS は MLX Swift で macOS/iOS に移植されており、iPhone 13 Pro で実時間の約 3.3 倍の速度。Murmur というネイティブ Mac アプリが Kokoro を同梱し、米英英語と日本語を含む音声を持つ
  - URL: https://github.com/mattmireles/kokoro-swift-mlx / https://github.com/Blaizzy/mlx-audio / https://www.murmurtts.com/blog/kokoro-tts-mac-guide
  - 出典日付: 記載なし
  - 確度: 中
- 事実: Whisper.cpp + Ollama + Kokoro で完全ローカルの音声 AI を組む構成の実例記事がある(Apple 純正部品を使わない代替)
  - URL: https://dev.to/xadenai/building-a-local-voice-ai-stack-whisper-ollama-kokoro-tts-on-apple-silicon-eo0
  - 確度: 中
- 日本語の入門記事(Foundation Models): https://zenn.dev/pupepa/articles/8cb94416356108 (WWDC25 セッション要約)、https://zenn.dev/5enxia/articles/2061169fff00cd (SwiftUI でチャットアプリ)、https://zenn.dev/kyoichi/articles/llmcodable-introduction (構造化出力)、https://qiita.com/nolanlover0527/items/89e7f73f8edaa30112b6 (WWDC26 まとめ)

## グレーゾーン・未確認

- オンデバイス LLM(3B / 20B スパース)の英会話相手としての質。短い雑談の往復は足りる見込みだが、長い会話での一貫性、キャラクター維持、コンテキスト長の上限は未確認。`fm` で実際に試すのが最安の検証
- AFM 3 Core Advanced(20B)が使える Mac の条件(メモリ量など)。未確認
- SpeechTranscriber の非ネイティブ(日本語訛り)英語の認識精度。未確認
- AVSpeechSynthesizer のプレミアム音声のダウンロードをアプリから促せるか、どの音声が使えるか(Siri の音声はサードパーティから使えないはず、は記憶ベースで未確認)
- 3 部品を直列につないだときの 1 往復の待ち時間。実測値は見つけていない
- Foundation Models の利用規約上、会話アプリとしての用途に制限があるか。未確認
- 上記の第三者記事はいずれも本文を開いていない。WWDC26 の差分と macOS 27 の `fm` は Apple 公式で裏取りしていない

## 影響する論点

- 最初の版の技術スタック(Apple 純正のみ / Kokoro を足す / LLM をクラウドへ逃がす道を残すか)
- 対象 Mac の範囲(macOS 27 以降、Apple Intelligence 対応機のみ、で良いか)
- 過去の却下アイデア `small-talk-trainer` / `english-opinion-trainer` との関係(却下理由は技術ではなく体験設計。`docs/plan/english-opinion-trainer/decisions.md` の 2026-09-15)

## 追記（2026-09-21、別セッション）: 一次ソースでの確認

上の記述は消さず、確認できた点と食い違った点をここに足す。確認手段は Apple 公式ページの本文取得（WebFetch）と、オーナーの Mac での実測。

- 事実: macOS 27 で `fm` CLI が入る。`fm chat` で対話的に試せ、シェルにパイプもできる。Python SDK（`apple_fm_sdk`）もある。上の「確度: 中」を **高** に改める
  - URL: https://developer.apple.com/videos/play/wwdc2026/241/ （transcript 本文）
  - 出典日付: 2026-06
  - 確度: 高
- 事実: モデル差し替えの層は `LanguageModel` プロトコル。ローカル用の実装として `CoreAILanguageModel`（Neural Engine）と `MLXLanguageModel`（GPU）が OSS で提供されると説明されている。Anthropic と Google が Swift パッケージを出すとの言及あり。上の「確度: 中」を **高** に改める
  - URL: 同上、および https://developer.apple.com/documentation/foundationmodels （`LanguageModel` / `LanguageModelExecutor` の記載）
  - 確度: 高
- 事実: コンテキスト長は **資料間で食い違う**。公式ドキュメントと TN3193（2026-03-31 改訂）は「1 セッション 4096 トークン」（入力と出力の合計）。WWDC26 のセッション 241 のコード例は `model.contextSize` の出力を 8192 と示し、「新しいオンデバイスモデルは作り直された」と説明している。同セッションに「動いているハードウェアに合わせてアプリを適応させるためにこれらの API を使う」という趣旨の発言があり、機種で値が違う可能性がある（これは推測）
  - URL: https://developer.apple.com/documentation/foundationmodels/managing-the-context-window / https://developer.apple.com/documentation/technotes/tn3193-managing-the-on-device-foundation-model-s-context-window / https://developer.apple.com/videos/play/wwdc2026/241/
  - 確度: 中（実機で `contextSize` を読めば確定）
- 事実: 上限に達するとセッションはエラーを投げて以後のリクエストを処理できない。Apple の推奨は、履歴を削るか新しいセッションを作ること、その際は最初のエントリ（指示）と最後のエントリ（直近の文脈）を残すか、要約で新しいセッションを始めること。`contextSize` と `tokenCount(for:)` で計測できる
  - URL: https://developer.apple.com/documentation/foundationmodels/managing-the-context-window
  - 確度: 高
- 食い違い: 上の「AFM 3 Core（3B dense）/ AFM 3 Core Advanced（20B sparse）、Google と協力」は、セッション 241 の transcript には出てこなかった。第三者記事のみの情報のまま。**確度を 低 に下げる**
- 事実: Private Cloud Compute のモデル（32K コンテキスト）も同じ API から使えるが、これはオフラインではないので本アイデアの対象外
  - URL: https://developer.apple.com/videos/play/wwdc2026/241/
  - 確度: 高
- 事実: SpeechTranscriber は macOS 26.0 以降。`supportedLocales`（ダウンロード可能なものを含む）と `installedLocales`（端末に入っているもの）が分かれており、言語アセットは初回にダウンロードが要る
  - URL: https://developer.apple.com/documentation/speech/speechtranscriber
  - 確度: 高（オフライン動作の明文は今回のページでは見つけていない。上の公式記事の記述に依る）
- 事実: Foundation Models の利用規約（Acceptable use requirements）に会話アプリ自体を禁じる条項はない。禁止事項の中に「ユーザーの精神的健康を害する依存やスパイラル的なやり取りを可能にすること」がある。上のグレーゾーン「利用規約上の制限」はこれで一部解消
  - URL: https://developer.apple.com/apple-intelligence/acceptable-use-requirements-for-the-foundation-models-framework/
  - 出典日付: 2026（フッターの年のみ）
  - 確度: 高
- 実測（オーナーの Mac、2026-09-21）: Apple M2 / 16 GB / macOS 26.5.2 / Xcode 26.5。`fm` は未導入。macOS 27 のアップデートが配信待ち。`say -v '?'` で見える英語音声は標準の低品質なもの（Samantha、Daniel、Eddy、Flo など）と効果音的な声だけで、Premium / Enhanced は入っていない

### この追記で残る未確認

- M2 / 16 GB で新しいオンデバイスモデルが使えるか、`contextSize` がいくつになるか
- 日本語訛りの英語の認識精度、1 往復の待ち時間（いずれも実測値なし）
- MLX で動く OSS モデルが、音声処理と並べて M2 / 16 GB で快適に動くか
- サードパーティのアプリから使える Premium 音声の範囲（Siri の音声が使えないかどうかは引き続き記憶ベース）
