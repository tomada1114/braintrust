# Reddit の自己宣伝ルール（獲得経路としての可否）

- 調査日: 2026-09-14
- 調査手段: **メインセッションが Claude in Chrome でユーザーの実 Chrome から公式 wiki を直接閲覧**（WebFetch / Reddit JSON は 403、old.reddit はログイン必須、WebSearch はクォータ枯渇）
- 問い: Reddit は個人開発の英語学習アプリの獲得経路として使えるか。`research/acquisition-channels.md` で「r/EnglishLearning の自己宣伝ルール未確認」と残っていた穴を埋める。

## 結論

**r/languagelearning（約 340 万人）は、オーナーが作ろうとしているものに対して実質的に閉じている。** 確度: 高。
規約に照らすと、複数の条項に同時に抵触する。

## 根拠: r/languagelearning 公式 wiki「Rules for promotion」

出典: https://www.reddit.com/r/languagelearning/wiki/rules_for_promotion/
**最終改訂: 2026-08-29 頃（ページ表示「16 日前」、2026-09-14 時点）** — 極めて最新。確度: 高（メインセッション直接閲覧）

### 基本構造
- **月次の固定スレッド（"Share Your Resources"、毎月 4 日頃に出て約 2 週間）以外での自己宣伝は、すべて許可制。** 無許可の投稿・コメントは「grounds for instant banning」。
- 許可は 1 投稿につき 1 回。**コメント経由での宣伝は一切不可。**
- 許可を得て投稿する際は、タイトルに `(self-promotion)` タグ必須。無いと即 BAN。
- 固定スレッドでも、同じものの再投稿は 6 ヶ月に 1 回まで。

### オーナーの構想が抵触する条項（重要）

| 条項（原文） | オーナーの構想との関係 |
| --- | --- |
| 「All commercial products must: **Work for more than one language.**」 | **英語学習専用のアプリは、許可投稿の対象から構造的に外れる。** 最も重い条項 |
| 「**Apps and programs that people must pay for are allowed only very rarely**」 | サブスク課金前提と衝突 |
| 「**Apps for which AI powers the core features are generally not allowed. These are just wrappers over LLMs which are already available for free.**」 | 「型を同定して別問題を生成する」は AI が中核。抵触 |
| 「Free trials or "first x users get it free" type posts receive no special consideration」 | 無料枠での回避は効かない |
| 「was vibe coded in a relatively short amount of time (i.e. it took you less than 6 months to develop), you are likely falling short on this criterion」 | 短期開発は品質基準で落ちる |
| 「Allow testing of key features without entering credit card information」 | これは満たせる |

### モデレーター自身による市場評価（プロダクト判断の材料としても重い）
- AI 会話アプリについて: 「somebody already thought of it. In fact, lots of people already thought of it, and it seems like none of them bothered to do market research first. Please do not make our lives harder by adding another one.」
- フラッシュカードについて: 「**Nobody has managed to unseat Anki; many have tried.**」加えて「users will eventually want to move off your app and are aware that without Anki export, they won't be able to take them with them」「we also highly recommend you implement an FSRS or SM-2 algorithm」
- 現況: 「**With the lowered cost of software development thanks to AI, we are currently experiencing a flood of new apps.**」「the quantity was angering the userbase」

### ペナルティの重さ
- 複数アカウントでの宣伝が検知された場合: **ドメインごと、製品名の言及ごと BAN する能力があり、実行する。** さらに「we will still manually approve negative reviews. Positive reviews will be suspected as coming from the owner and left hidden」。
- 実例への言及: 「There are products for which **the top result on Google includes negative reviews on this subreddit** and the company in question is banned.」
- **つまり失敗した場合のダウンサイドは「効果がない」ではなく「検索結果に否定的レビューが残る」。** 試行のコストが非対称に高い。

### AI 生成文への態度
- 「Do not write with AI, we can see it a mile away and it will result in rejection.」
- 「AI-written posts are egregious enough to get you banned instantly.」
- **2026-09-14 の決定「発信は Claude Code の skill で半自動化する」と正面から衝突する。**

## r/EnglishLearning（約 70 万人）

- サイドバーのルールに「Spam」項があり、「Comments to substantial outside resources may be marked as spam and removed. You will be banned if y[ou ...]」（表示が途中で切れており全文未確認）。
- 出典: https://www.reddit.com/r/EnglishLearning/ サイドバー、2026-09-14 閲覧、確度: 中（全文を取得できていない）
- r/languagelearning ほど詳細な宣伝 wiki は確認できなかった。**ここは未確認として残る。**

## グレーゾーン・未確認

- r/EnglishLearning の宣伝ルール全文。上記の通り取得できていない。緩い可能性はあるが、`user-needs/reddit-direct-observation.md` で観測した「アプリ推薦への不信スレッド」を踏まえると、コミュニティの空気は同様に厳しいと推測される（推測であり未確認）。
- 月次の固定スレッドから実際にどれだけの流入・課金が発生するかは未確認。規約上は使えるが、効果の数字は無い。
- r/IELTS、r/EnglishGrammar など他のサブレディットのルールは未確認。
- 許可申請が通った個人開発アプリの実例と、その後の成果は未確認。

## 影響する論点

- `research/acquisition-channels.md`「Reddit: 現実性 中」— **下方修正が必要**。少なくとも r/languagelearning については「低」。
- `decisions.md` 2026-09-14（追記）「発信は Claude Code の skill で半自動化する」— Reddit では AI 生成文が即 BAN 事由。**この経路では半自動化が使えない。**
- `open-questions.md`「複数アプリを出す戦略における共通の入口を何にするか」— Reddit はその候補から外れる。
- `decisions.md` 2026-09-14「SRS の線に賭ける」— モデレーターの「Nobody has managed to unseat Anki; many have tried」は、この線への外部からの警告として記録しておく。
- **副次的に重要**: 「英語専用であること」が規約上の失格条件になっている。多言語対応（`decisions.md` 2026-09-14「日本語話者に限定しない」で言及した中国語・韓国語・スペイン語 UI）とは別の話で、**学習対象言語が英語だけ**という点が問題になっている。
