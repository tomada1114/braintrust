# Langua (LanguaTalk)

- 調査日: 2026-09-07
- 調査手段: Sonnet サブエージェントによる机上調査 + メインによる原典確認、一次観察あり（サブエージェントがオーナーのブラウザで実施）
- URL: https://languatalk.com/langua/communicate
- 対象ユーザー: 自称ユーザー数 30,000 人以上。最も人気の層は A2〜B2 レベルだが、Guided Course / Guided Mode で初心者も対象に含める設計。「real conversations」に備えたい学習者を想定し、Duolingo 的なドリル型アプリのユーザーを暗に対比している。

## 位置づけ

自らを「世界で最も先進的な AI 言語コーチ（the world's most advanced AI language coach）」と位置づける。トップページで「Traditional apps don't prepare you for real conversations」と Duolingo 的な学習アプリを名指しで対比し、ドリルではなく実際の会話練習で流暢さを作るプロダクトだと訴求している。（URL: https://languatalk.com/ / 出典日付: 記載なし / 確度: 高）

音声会話モード（Call mode）が主機能として大きく打ち出されており、「patient conversation partner who's available 24/7 and never judges your mistakes」という「judge されない練習相手」という情緒的な訴求を核にしている。（URL: https://languatalk.com/ / 出典日付: 記載なし / 確度: 高）

## 中核の体験（初回ユーザーの流れ）

公式サポート記事に基づく、会話（Conversations）機能の一般的な流れ。

1. 言語・興味・レベルを選び、会話シナリオ（ロールプレイ、興味ベースの議論、日常シーン）を選択する。
2. 会話中の訂正方式（Correction Mode）を 5 択から選ぶ：Off / Text corrections / Implicitly correct me / Explicitly correct me / Ask me to repeat。
3. テキストまたは音声（Call mode、ハンズフリー対応）で会話を進める。返答に迷ったら電球ボタンで返答候補、ワンドボタンで自分の発言の言い換えを表示できる。
4. 各返答についてペンシルボタンから添削を確認できる。
5. 6 往復以上会話した後、会話を終了すると「detailed feedback, suggestions and even cultural tips」を含むフィードバックレポートを生成できる（音声版のフィードバックレポートもある）。
6. 保存した単語・フレーズはフラッシュカード、AI が作るストーリー、以後の会話に自動的に織り込まれる。

（URL: https://support.languatalk.com/article/160-learn-how-to-use-langua-effectively-conversations-help-guide / 出典日付: 記載なし / 確度: 高、公式サポート記事のため）

初回の実際の画面遷移は一次観察（下記）で確認済み。デフォルトはマイク中心の UI で、テキスト入力は「Toggle keyboard」で切り替える必要がある。

## 主要機能

- **AI 音声会話（Call mode）**: ネイティブの声をクローンした音声で会話する。（URL: https://languatalk.com/ / 確度: 高）
- **会話シナリオ**: ロールプレイ、興味ベースの討論、日常生活シナリオ。（URL: https://languatalk.com/ / 確度: 高）
- **語彙管理（My Path / Vocabulary）**: 保存した単語をフラッシュカード・ストーリー・会話に自動的に織り込む。（URL: https://languatalk.com/ 、第三者記事で補足 / 確度: 中〜高）
- **1 対 1 チューターレッスン**: 選抜済み講師とのライブレッスン（有料オプション）。（URL: https://languatalk.com/ / 確度: 高）
- **記憶機能（Memory）**: ユーザーが話した個人的な事実を保存し会話に織り込む。編集・削除できる。（URL: https://lingtuitive.com/blog/langua-ai-tutor-review / 確度: 中、第三者記事）
- **インポート機能**: 任意テキスト・音声ファイルをアップロードし、理解度クイズや練習に変換できる。（URL: https://lingtuitive.com/blog/langua-ai-tutor-review / 確度: 中、第三者記事）
- **ハンズフリーモード**: 通勤中など画面を見ない状況での練習に対応。（URL: https://languatalk.com/ / 確度: 高）

## UI・UX の特徴とそれが嬉しい理由

- 特徴: 5 段階の訂正モード（Correction Mode）切替。Off / Text corrections（打ち消し線＋太字） / Implicitly correct me（AI の返答に正しい形を自然に混ぜ込む） / Explicitly correct me（明示的に指摘） / Ask me to repeat（言い直しを求める）。
  - 嬉しい理由: 「訂正の強さ」という 1 軸を会話ごとに選べるため、会話の流れを止めたくない場面と、都度直してほしい場面の両方に対応できる。単なる ON/OFF の添削と違う。
  - URL: https://support.languatalk.com/article/160-learn-how-to-use-langua-effectively-conversations-help-guide / 出典日付: 記載なし / 確度: 高
- 特徴: 電話・ペンシル・ワンドの 3 アイコン。電球＝返答候補（2 択）、ペンシル＝各返答の添削確認、ワンド＝自分の発言の言い換え。
  - 嬉しい理由: 「答えに詰まる」「自分の言い方に自信が持てない」という 2 つの詰まりどころを、会話を止めずにその場で解消できる。
  - URL: 同上 / 出典日付: 記載なし / 確度: 高
- 特徴: 会話終了後のフィードバックレポート（6 往復以上が条件）。書面と音声の両方で「detailed feedback, suggestions and even cultural tips」を提供。
  - 嬉しい理由: 会話中の逐次訂正とは別に、会話全体を俯瞰したレポートを分けて用意することで、その場の訂正とセッション全体の振り返りを両立させる。
  - URL: https://lingtuitive.com/blog/langua-ai-tutor-review / 出典日付: 記載なし / 確度: 中（第三者記事のみ、一次観察では未到達）
- 特徴: 発音スコアの意図的な非採用。「どのアプリも信頼できる採点を提供していない」という理由で発音スコアリングを提供しない、と第三者記事が述べる。
  - 嬉しい理由（第三者記事の主張）: 信頼できない数値を見せないことで、誤った自己評価を避けられる。
  - URL: https://lingtuitive.com/blog/langua-ai-tutor-review / 出典日付: 記載なし / 確度: 中（第三者記事のみ、一次情報での裏取り未実施）
- 特徴: My Path（段階的な学習パス）。完了したステージが次を開く進行構造。
  - 嬉しい理由（第三者記事の主張）: 機能が多く初回は圧倒されやすい問題を、明確な出発点として緩和する。
  - URL: https://lingtuitive.com/blog/langua-ai-tutor-review / 出典日付: 記載なし / 確度: 中

## 料金・プラットフォーム

- 課金のモデル: 無料アカウントあり（クレジットカード不要で試用可）。有料は Standard / Unlimited の 2 段階サブスク。第三者情報で Standard $19.99/月・$149.99/年、Unlimited $29.99/月・$199.99/年（公式 pricing ページは 404 で一次情報未確認、出典日付: 記載なし（2026年更新と推定）、確度: 中）。月額プランは 5 日間・年額プランは 7 日間の無料トライアル。Web / Android 購読は 30 日間返金保証（App Store 購入は対象外）。（URL: https://support.languatalk.com/article/142-how-much-does-langua-cost-pricing / 確度: 高）
- プラットフォーム: Web（Chrome 推奨）、iOS、Android。デバイス間同期。20 言語以上に対応。（URL: https://languatalk.com/ / 確度: 高）

## ユーザーの声

### 賞賛

- 「The AI chat is not robotic sounding and you can choose from many versions」— URL: https://www.trustpilot.com/review/languatalk.com / 出典日付: 2025-11-13 / 確度: 高 / 言語: 英語
- 「Languatalk is a more natural conversation by far…accent was very good」— URL: https://www.trustpilot.com/review/languatalk.com / 出典日付: 2026-08-29 / 確度: 高 / 言語: 英語
- 「The AI chat is amazing! I can take it at my pace and review corrections」— URL: https://www.trustpilot.com/review/languatalk.com / 出典日付: 2026-08-28 / 確度: 高 / 言語: 英語
- 「I LOVE the speak function because I can talk about anything and I can even ask it to tell me how to say words without feeling judged」— URL: https://www.reviews.io/company-reviews/store/languatalk / 出典日付: 記載なし（約 7 ヶ月前） / 確度: 中 / 言語: 英語
- 「the implicit option is the one I'd recommend… you get the correction, without interrupting the conversation」— URL: https://lingtuitive.com/blog/langua-ai-tutor-review / 出典日付: 記載なし（2 年利用のレビュアー本人談） / 確度: 中 / 言語: 英語

### 不満

- 「Every session has been glitchy. Long delays after responding」— URL: https://www.trustpilot.com/review/languatalk.com / 出典日付: 2026-08-29 / 確度: 高 / 言語: 英語
- 「Very, very unreliable at receiving user responses…Mis-hears user responses…occasionally mispronounces words」— URL: https://www.trustpilot.com/review/languatalk.com?page=3 / 出典日付: 2026-03-21 / 確度: 高 / 言語: 英語
- 「The conversations aren't really realistic because they're stilted…the level it moves along at is waayyyyy too fast」— URL: https://www.trustpilot.com/review/languatalk.com?page=3 / 出典日付: 2026-02-26 / 確度: 高 / 言語: 英語
- 「on trying to cancel the subscription and have a refund, it appears that it is only the subscription renewal that can be cancelled!」— URL: https://www.trustpilot.com/review/languatalk.com?page=3 / 出典日付: 2026-03-08 / 確度: 高 / 言語: 英語
- 「Never detects what I say in guided mode so I'm repeating many times」— URL: https://www.trustpilot.com/review/languatalk.com?page=3 / 出典日付: 2025-12-19 / 確度: 高 / 言語: 英語
- 「Voice recognition is completely unusable, both in the app and especially in the browser」— URL: https://www.trustpilot.com/review/languatalk.com?page=3 / 出典日付: 2025-10-13 / 確度: 高 / 言語: 英語
- 「The 'free trial'…is a sick joke. After 30 minutes trying it I was informed that I was at the end of my trial period」— URL: https://www.trustpilot.com/review/languatalk.com?page=3 / 出典日付: 2025-09-20 / 確度: 高 / 言語: 英語
- 「There's a lot here. The sheer number of features and options can feel like a lot the first time you open it」— URL: https://lingtuitive.com/blog/langua-ai-tutor-review / 出典日付: 記載なし（2026年更新と推定） / 確度: 中 / 言語: 英語

日本語での Langua / LanguaTalk への言及は、App Store 日本版・X・ブログを複数の切り口で探したが見つからなかった（6 件の出典。日本語ユーザーコミュニティはほぼ存在しないとみられる）。

## 解決できていない課題

- 課題: ガイド付きモード（Guided Mode）の音声認識がほぼ機能せず、同じ発話を何度も繰り返させられる。
  - 根拠: 「Never detects what I say in guided mode so I'm repeating many times」/ URL: https://www.trustpilot.com/review/languatalk.com?page=3 / 出典日付: 2025-12-19
- 課題: 会話履歴・学習履歴がセッションをまたいで保持されず、同じ質問が繰り返される。
  - 根拠: 「It doesn't remember your previous conversations, so it always asks the same questions and it's annoying to have to steer conversations away from always heading in the same direction or repeating identical conversations over and over」/ URL: https://www.reviews.io/company-reviews/store/languatalk / 出典日付: 記載なし / 確度: 中
- 課題: 訂正モードの設定が新しい会話ごとにリセットされる可能性があり、公式サポート記事の「選べる」という説明と矛盾する。
  - 根拠: 一次観察でも Correction mode が既定 Off であることを確認済み（下記）。ユーザー側は「Every time I started a new chat, I had to remind the tutor that I wanted my mistakes corrected」と報告（出典未特定、確度: 中、要約経由）。
- 課題: サブスクリプション解約導線が分かりづらく、更新のみキャンセルできて根本的な退会ができない。
  - 根拠: 「on trying to cancel the subscription and have a refund, it appears that it is only the subscription renewal that can be cancelled!」/ URL: https://www.trustpilot.com/review/languatalk.com?page=3 / 出典日付: 2026-03-08

## 一次観察（触った場合）

- 観察日: 2026-09-07
- 手段: オーナーのブラウザでログイン済みアカウントの範囲を操作（サブエージェントが実施）
- 歩いた流れ:
  1. `https://languatalk.com/langua/communicate` にアクセス。ログイン済み（ユーザー名 Tomoshi、チューター Rebecca 選択済み）。Explore タブに「Chat about anything」「Do a role play」「Have a debate」「Vocab & Games」「Grammar practice」「Design my own」の 6 カードと、下部に「Today's Conversation: Casual Chat」がマイク付き「Start Chat」ボタンで表示。初期状態は音声優先に見える。
  2. 「Chat about anything」→「General conversation」を選択しチャット開始。AI が音声（TTS 再生、カラオケ式ハイライト）で発話。
  3. 入力欄はデフォルト非表示（マイク中心の UI）。「Toggle keyboard」でテキスト入力欄が現れることを確認（音声必須ではなく、テキストのフォールバックあり）。
  4. B1 想定でわざと誤りを含む文を送信: "I think Kyoto is good place for visit because it have many temple."
  5. AI の返答は誤りを訂正せず、内容だけを受けて自然に会話継続（文法エラーへの言及なし）。
  6. 自分の発言の下に 4 つのアイコン（鉛筆＝編集、魔法の杖、翻訳、再生）を発見。杖アイコンをクリックしたが、目に見える添削結果は表示されなかった（未確認のまま）。
  7. 「More options」→「End Chat & Get Feedback」を押すとモーダル: 「Ready to end the chat? … You'll see those options here after you've replied at least 6 times.」→ 発言1回のみだったため「End the chat without feedback」のみ選択可能だった。
  8. 「Chat Settings」を開いて確認（変更はしていない）。「Speed of replies」「Suggested replies」「Auto-record?」「Auto-send?」「Correction mode」「AI model」「Advanced Settings」が並ぶ。**Correction mode は既定で Off、Suggested replies も既定で Off** だった（添削も提案も出なかったのはこの既定設定のため）。
- 引っかかった点:
  - 初回訪問時、実際の入力導線（音声かテキストか）が一目でわからない。テキスト入力に切り替えるには「Toggle keyboard」を能動的に押す必要がある。
  - 送った 1 発言に対する添削が、デフォルト設定では一切出ない。バグではなく Chat Settings の Correction mode が既定 Off という設計。
  - フィードバックレポートは「セッション終了時」かつ「最低 6 発言」という閾値を超えないと選択肢にすら出ない。単発のやり取りに対する即時フィードバックという体験は、Langua の標準フローには存在しない（Correction mode を明示的に有効化した場合は発言ごとに添削が返る設計になっている模様だが未確認）。
- 良いと感じた瞬間とその仕組み:
  - 「Toggle keyboard」でテキスト⇄音声を切り替えられる — マイクが使えない場面でもテキストにフォールバックできる仕組みがある。
  - 「You've earned 4 points in this chat, nice work!」というポイント表示 — 活動量をゲーミフィケーションで見せ、継続動機を作る仕組み。
  - Chat Settings に Correction mode の選択肢が複数用意されている — 「会話の流れを止めたくない人」と「都度直してほしい人」の両方に対応する仕組み。ただし既定は「会話優先・添削は求めれば出す」側に倒している。
- 止めた地点: 中核の体験まで到達（サインアップ壁・課金要求は出現せず）。ただし「発言 6 回以上」というフィードバックレポートのしきい値により、実際の添削レポートのフォーマットまでは確認できていない（1 発言で終了したため）。

## グレーゾーン・未確認

- 公式製品ページ自体（languatalk.com、および `/langua` トップ）は「Speak with AI」と「Create your free account」の 2 要素しか大きく見せておらず、機能の詳細説明はサポート記事（support.languatalk.com）と第三者レビュー（lingtuitive 等）に依存している。トップページ単体では機能の全体像を語れない。
- 一次観察で Correction mode の既定が Off、フィードバックレポートが「6 往復以上」でしか選べないことを確認できたが、**Correction mode を Off 以外にした場合の実際の添削表示形式、および会話後フィードバックレポートの実際のフォーマット（見出し構成・CEFR 反映の有無・言語）は未到達のまま**。公式サポート記事の記述（打ち消し線表示・cultural tips 等）は画面の確認ではなく文書の記述である点に注意。
- CEFR レベル設定の具体的な選択肢と、レベルによってフィードバックの何が変わるかは、公式ページ・サポート記事のいずれにも明示的な CEFR 表記が見当たらない。一次観察でも Chat Settings 内に CEFR レベルの直接指定は見当たらなかった（チューター/トピック選択画面や別の Settings 画面にある可能性は残るが未確認）。
- 料金の正確な現在価格は公式 pricing ページが 404 のため確認できず、第三者レビュー記事の数字のみに依拠している。
- フィードバックの言語（英語固定か、学習者の母語での説明も選べるか）は明記された記述を見つけられなかった。
- 訂正モードの設定が新しい会話ごとにリセットされるかどうかは、公式サポート記事とユーザーレビューで矛盾している（本文参照）。

## このアイデアへの示唆

- 借りられる仕組み: 「訂正の強さ」をユーザーが会話ごとに選べる 5 段階の Correction Mode は、本アイデアの「決まった形式のフィードバック」を設計する際に参考になる — 一律の厳しさではなく段階を持たせる発想。
- 避けるべき作り: 音声入力を主軸に据えると音声認識の不安定さがそのままユーザー体験を壊す（不満の多くがこれに集中）。本アイデアがテキスト専用である判断は、この課題を構造的に回避している。
- この製品が空けている場所: 単発の 1 問 1 答に対する即時フィードバックがない（6 往復以上という高いハードル）。本アイデアの「回答 1 つに対して決まった形式のフィードバックが返る」という設計は、Langua が持たない体験。
- 推奨であって決定ではない。決定は decisions.md へ。
