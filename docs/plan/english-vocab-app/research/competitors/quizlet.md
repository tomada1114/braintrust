# Quizlet

- 調査日: 2026-09-07
- 調査手段: メインセッションによる机上調査（公式 App Store ページ・比較ブログ記事）。実操作なし
- URL: https://quizlet.com/
- 対象ユーザー: 学校教育の課題（教員が配布する単語セット）から独学の資格試験対策まで幅広い。自分でセットを作る、または他人が作った共有セットを使う学習者。

## 位置づけ

カード型学習の最大手の一つ。Anki と異なりウェブ・モバイルの UI が洗練されており、AI（Q-Chat、Magic Notes）による自動セット生成やゲーム化されたモード（Match、Learn）を備える。Anki より導入は容易だが、素材（何を覚えるか）をユーザーが用意する、または既存の共有セットに依存する点は共通の弱点として残っている。

## 中核の体験（初回ユーザーの流れ）

1. 自分で単語セットを作る、教材から AI に自動生成させる（Magic Notes）、または検索して既存の共有セットを見つける。
2. Flashcards・Learn・Match・Test など複数のモードで反復する。
3. 「覚えた／まだ」の自己申告で出題対象を絞り込みながら進める。

## 主要機能

- AI 自動生成（Magic Notes・Q-Chat）: 教材やノートからセットを自動生成し、作成コストを下げる試み
- 共有デッキ検索: 他ユーザーが作った既存セットを検索して流用できる
- 複数の学習モード: Flashcards / Learn / Write / Spell / Test / Match（ゲーム化）
- Quizlet Plus: 広告なし・オフライン利用・出題数無制限などの有料機能

## UI・UX の特徴とそれが嬉しい理由

- 特徴: Match（タイムアタック形式のゲームモード）
  - 嬉しい理由: 「覚える」という作業をゲームの点数競争に変換し、単調さを紛らわせる
  - URL: https://apps.apple.com/us/app/quizlet-flashcards-maths-more/id546473125 / 出典日付: 2025-07-29 / 確度: 中
- 特徴: AI によるセット自動生成（Magic Notes）
  - 嬉しい理由: 教材をアップロードするだけでセットができるため、Anki で最大の離脱要因だった「カード作成」の手間を部分的に肩代わりする
  - URL: https://apps.apple.com/us/app/quizlet-flashcards-maths-more/id546473125 / 出典日付: 2023-12-14 / 確度: 中

## 料金・プラットフォーム

- 課金のモデル: 無料プランあり（機能・出題数に制限）。Quizlet Plus は月額 $7.99 または年額 $35.99（月換算約$2.99）。上限を完全に撤廃する Plus Unlimited は年額 $44.99（月換算約$3.74）。
- プラットフォーム: Web / iOS / Android

## ユーザーの声

3 件の出典。

### 賞賛

- 「Automated flashcard creation from documents saves significant time」「[AI assistance helped understand] challenging material」 — URL: https://apps.apple.com/us/app/quizlet-flashcards-maths-more/id546473125 / 出典日付: 2023-12-14 / 確度: 中 / 言語: 英語
- 「[App] effectiveness depends on daily consistent usage」（裏を返せば継続できれば効果はあるという声） — URL: https://apps.apple.com/us/app/quizlet-flashcards-maths-more/id546473125 / 出典日付: 2024-04-01 / 確度: 中 / 言語: 英語

### 不満

- 「[This app has] never been accessible on any platform whatsoever」「[recent updates feel like a] feature downgraded cash grab」 — URL: https://apps.apple.com/us/app/quizlet-flashcards-maths-more/id546473125 / 出典日付: 2022-11-19 / 確度: 中 / 言語: 英語
- 「自分で作るのがあれすぎて」（Quizlet を含むカード型アプリ全般に対するオーナー自身の証言。overview.md より） — URL: 社内ヒアリング（docs/plan/english-vocab-app/overview.md） / 出典日付: 2026-09-07 / 確度: 高 / 言語: 日本語

## 解決できていない課題

- 課題: AI 自動生成である程度緩和されているとはいえ、質の高いセットを一から作る、または大量の共有セットから当たりを探すコストは依然として残る
  - 根拠: オーナー自身の証言「自分で作るのがあれすぎて」／一次観察（Quizlet の基本構造がユーザー作成・共有セット依存であること）
- 課題: 有料プランへの機能移動（無料版の機能縮小）が「改悪」と受け取られ、信頼を損ねている
  - 根拠: 「[recent updates feel like a] feature downgraded cash grab」 / URL: https://apps.apple.com/us/app/quizlet-flashcards-maths-more/id546473125 / 出典日付: 2022-11-19

## 一次観察（触った場合）

未実施。

## グレーゾーン・未確認

- Quizlet の共有セットの品質（誤訳・誤りの混入率）は今回の調査では検証していない。ユーザー作成コンテンツである以上、品質のばらつきは構造的な問題として残っている可能性が高いが、定量的な根拠は未確認。
- IELTS 特化の観点での Quizlet 評価（IELTS 用共有セットの充実度など）は個別に調べておらず未確認。

## このアイデアへの示唆

- Quizlet は「AI にセット作成を肩代わりさせる」という形で Anki の弱点を埋めようとしている。語彙リストを LLM 生成で用意するという既存の決定（decisions.md）は、方向性としてはこの流れに近い。作成コストをアプリ側が最初から負担する設計は妥当性が高い。
- 一方で「覚えた／まだ」の自己申告ベースの進捗管理は、mikan のランク制などに比べて達成感が弱いという印象を与えやすい。進捗の可視化は工夫の余地がある論点として残る。
- 推奨であって決定ではない。決定は decisions.md へ。
