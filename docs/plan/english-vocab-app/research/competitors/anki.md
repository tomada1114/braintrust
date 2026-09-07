# Anki

- 調査日: 2026-09-07
- 調査手段: メインセッションによる机上調査（公式サイト・App Store・Reddit/ブログ記事の要約）。実操作なし
- URL: https://apps.ankiweb.net/
- 対象ユーザー: 自分でカードを作って暗記する習慣がある学習者。医学部生・語学学習の上級者など、素材作成のコストを厭わない層に特に強い支持がある。

## 位置づけ

SRS（間隔反復システム）フラッシュカードの代表的なオープンソースアプリ。何を覚えるかは完全にユーザー任せで、Anki 自体は「復習タイミングを最適化するエンジン」に徹している。カスタマイズ性・拡張性（アドオン）は競合の中で最強クラスだが、その分セットアップの学習コストも高い。

## 中核の体験（初回ユーザーの流れ）

1. デッキを作成し、表面・裏面（+ 画像・音声・タグなど）を自分で入力してカードを作る、または共有デッキをダウンロードする。
2. 「もう一度」「難しい」「普通」「簡単」の4段階で自己評価しながらカードをめくる。
3. 自己評価に応じて次回の復習間隔がアルゴリズムで自動計算され、以降その間隔で出題され続ける。

## 主要機能

- 間隔反復アルゴリズム（FSRS など): 自己評価に基づき復習間隔を最適化
- 完全なカスタマイズ性: ノートタイプ、テンプレート、画像・音声・動画添付、数千種のアドオン
- クロスプラットフォーム同期: デスクトップ / AnkiWeb / AnkiDroid 間で無料同期

## UI・UX の特徴とそれが嬉しい理由

- 特徴: 「もう一度／難しい／普通／簡単」の4択自己評価で復習間隔を自動最適化するアルゴリズム
  - 嬉しい理由: いつ・何を復習すべきかをユーザーが考えなくて済み、忘れかけたタイミングで自動的に出題してくれる
  - URL: https://flica.app/article/anki-pricing-2026 / 出典日付: 記載なし（2026年時点の記事） / 確度: 中
- 特徴: ノートタイプ・アドオンによる高いカスタマイズ性
  - 嬉しい理由: 上級者は自分の学習スタイルに完全に合わせられる。一方でこの自由度自体が初心者には負荷になる（後述の不満参照）
  - URL: https://www.alllanguageresources.com/anki/ / 出典日付: 記載なし / 確度: 中

## 料金・プラットフォーム

- 課金のモデル: デスクトップ（Windows/Mac/Linux）・AnkiWeb・AnkiDroid（Android）はすべて無料。iOS/iPadOS 公式アプリ「AnkiMobile」のみ買い切り $24.99（開発資金源）。サブスクリプションなし。
- プラットフォーム: Windows / Mac / Linux / Android / iOS（有料） / Web（AnkiWeb）

## ユーザーの声

4 件の出典。

### 賞賛

- 「This app has changed my life so much that I feel compelled to write one [review]」（医学部生として間隔反復で暗記量を伸ばした体験） — URL: https://apps.apple.com/us/app/ankimobile-flashcards/id373493387 / 出典日付: 2018-12-20 / 確度: 中 / 言語: 英語
- 「[After hesitating about] the $25 [price tag, found it] worth it」 — URL: https://apps.apple.com/us/app/ankimobile-flashcards/id373493387 / 出典日付: 2022-07-04 / 確度: 中 / 言語: 英語

### 不満

- 「It takes way too long to make the cards」（カード作成にかかる時間そのものが不満） — URL: https://www.goodreads.com/author_blog_posts/3237096-review-of-anki-srs?tab=book / 出典日付: 記載なし / 確度: 低 / 言語: 英語
- 「[I] wanted just repeating the flashcards over and over [but found] so many gadgets [complicating basic use]」（機能過多で基本操作が分かりにくい） — URL: https://apps.apple.com/us/app/ankimobile-flashcards/id373493387 / 出典日付: 2023-07-07（推定） / 確度: 中 / 言語: 英語
- 「[Some learners] drop [studying] after creating about 100 flashcards, deciding language learning isn't for them」（カード作成の負荷そのものが離脱原因になっているという観察） — URL: https://manabumanda.substack.com/p/challenging-my-relationship-with / 出典日付: 記載なし / 確度: 低 / 言語: 英語

## 解決できていない課題

- 課題: 何を覚えるか・どうカードを作るかを完全にユーザーに丸投げしており、素材作成のコストと学習曲線の高さが最大の離脱要因になっている
  - 根拠: 「It takes way too long to make the cards」「[Some learners] drop [studying] after creating about 100 flashcards」 / URL: https://www.goodreads.com/author_blog_posts/3237096-review-of-anki-srs / https://manabumanda.substack.com/p/challenging-my-relationship-with / 出典日付: 記載なし（低確度）
- 課題: カードの表裏を覚えるだけで、文脈中での使用や産出（Writing/Speaking）への橋渡しは、ユーザーが自分でそのようなカードを設計しない限り発生しない
  - 根拠: 一次観察（Anki の仕様そのもの。中身は完全にユーザー設計に依存する）

## 一次観察（触った場合）

未実施。

## グレーゾーン・未確認

- カード作成の負荷に関する引用の一部（Goodreads、Substack のブログ）は出典の性質上、確度は中〜低とした。より確度の高い一次データ（App Store レビューでの直接的な言及）は今回の調査では十分に見つからなかった。
- オーナー自身の証言「自分で作るのがあれすぎて」（overview.md）が最も確度の高い一次情報であり、この調査結果と方向性は一致している。

## このアイデアへの示唆

- Anki の最大の学びは「エンジン（間隔反復）は優れていても、素材（何を・どう覚えるか）をユーザーに作らせると導入コストで脱落する」という点。語彙リストと例文を最初からアプリ側が用意する設計（オーナーが既に decisions.md で決めている方向）は、この失敗を避ける選択として筋が通っている。
- 一方で Anki のカスタマイズ性・拡張性の高さは、上級者・長期継続者に強く支持されている理由でもある。素材を作らせない代わりに、自分の弱点だけに絞る・自分の言葉で例文を追加するなど「軽いカスタマイズの余地」を残す価値はあるかもしれない。
- 推奨であって決定ではない。決定は decisions.md へ。
