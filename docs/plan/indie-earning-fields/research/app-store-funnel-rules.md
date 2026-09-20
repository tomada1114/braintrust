# App Store の無料アプリを入口にして外部（自前）課金へ誘導できるか

- 調査日: 2026-09-19
- 調査手段: メインセッションによる Apple 公式ガイドライン原文の直接取得（WebFetch）+ 判例の状況は WebSearch 経由の二次情報
- 問い: 「無料アプリを App Store に量産し、App Store 外の本体プロダクト（自前 Stripe 課金）へ誘導する」は、Apple の規約上どこまで許されるか。

## 結論

**「誘導」は条件つきで可能だが、「量産」はガイドライン 4.3(b) に正面から抵触し、繰り返すと Apple Developer Program からの除名リスクがある。** 両方を同時にやる戦略は、規約上もっとも危険な組み合わせになる。

分解すると次の 3 層になる。

1. **量産（4.3 Spam）** — 明示的に禁止されている。同一アプリの Bundle ID 違いの量産（4.3a）も、既存カテゴリの亜種を機会主義的に作ること（4.3b）も名指しされており、後者は「繰り返すと Developer Program から除名されうる」と書かれている。**オーナーの構想のうち「量産」の部分は、規約上ほぼそのまま否定されている。**
2. **アプリ内から外部課金へ誘導（3.1.1(a) / 3.1.3）** — **米国ストアフロントに限り**、エンタイトルメント申請なしでボタン・外部リンク・CTA を置いてよい。**米国以外のストアフロントでは原則禁止**（一部地域は StoreKit External Purchase Link Entitlement で限定的に可能）。オーナーの狙いは「英語圏・グローバル」なので、**同じコードを世界配信すると米国以外でリジェクト対象になる**。
3. **誘導せず、ただの無料コンパニオンアプリとして置く（3.1.3(f)）** — 課金導線をアプリ内に一切置かないなら、IAP 不要で成立する。ただし「アプリ内に購入も、アプリ外購入への CTA も置かない」ことが条件なので、**アプリはマーケティング装置としてほぼ何も言えない**。

## 根拠

### 4.3 Spam（量産の禁止）

- 事実: 4.3(a) の原文 — "Don't create multiple Bundle IDs of the same app (for example, submitting a separate map app for every city in the world instead of a single worldwide map that allows users to search any city). This practice results in unnecessary apps, which makes it hard for users to find the apps they want."
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし（ページに更新日の表示なし）
  - 確度: 高（Apple 公式ページの原文を直接取得）
- 事実: 4.3(b) の原文 — "Don't submit apps that are indistinguishable from what's already widely available. Opportunistically creating variants of existing app categories or popular apps degrades App Store discovery, reduces overall app quality, and harms both users and developers. (...) Repeated submissions of this kind may lead to removal from the Apple Developer Program."
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし
  - 確度: 高（同上）
- 事実: 4.3(b) はさらに「dating, flashlight, sound effects, wallpaper, simple timers, fortune telling」といった確立済みカテゴリを名指しし、"we will not accept new submissions unless they offer a meaningfully different or improved experience" と書いている。加えて "We may remove these apps from the App Store going forward if they are not updated, improved, or do not attract customers."（＝顧客を集められないアプリは事後的に削除されうる）
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし
  - 確度: 高

### 3.1.1(a) / 3.1.3（外部課金への誘導）

- 事実: 3.1.1(a) の原文 — "These entitlements are not required for developers to include buttons, external links, or other calls to action in their United States storefront apps."
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 同 3.1.1(a) — "The entitlements are limited to use only in the iOS or iPadOS App Store in specific storefronts. In all other storefronts, except for the United States storefront, where this prohibition does not apply, apps and their metadata may not include buttons, external links, or other calls to action that direct customers to purchasing mechanisms other than in-app purchase."
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 3.1.3 柱書 — "Apps in this section cannot, within the app, encourage users to use a purchasing method other than in-app purchase, except for apps on the United States storefront and as set forth in 3.1.1(a) and 3.1.3(a). Developers can send communications outside of the app to their user base about purchasing methods other than in-app purchase."（＝アプリ外のチャネル（メール等）で既存ユーザーに外部課金を案内するのは、ストアフロントを問わず可）
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 3.1.3(f) Free Stand-alone Apps — "Free apps acting as a stand-alone companion to a paid web based tool (i.e. VoIP, Cloud Storage, Email Services, Web Hosting) do not need to use in-app purchase, provided there is no purchasing inside the app, or calls to action for purchase outside of the app."
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし
  - 確度: 高

### 3.1.1 本体（ライセンスキー等による解錠の禁止）

- 事実: "Apps may not use their own mechanisms to unlock content or functionality, such as license keys, augmented reality markers, QR codes, cryptocurrencies and cryptocurrency wallets, etc."（＝「Web で課金してもらい、アプリにライセンスキーを入れて機能解放」は不可。3.1.3(b) のマルチプラットフォーム例外に乗せる場合でも、同じ item を IAP でも提供する必要がある）
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし
  - 確度: 高

### 米国ストアフロントで外部リンクが解禁された経緯（二次情報）

- 事実（二次）: 2025 年 4 月の Epic v. Apple 差止命令に対する contempt 判断を受け、Apple は 2025 年 5 月 2 日に米国向けガイドライン 3.1.1 / 3.1.3 を更新し、エンタイトルメント不要・手数料なしで外部決済リンクを認めた。その後 2025 年 12 月の第 9 巡回区控訴裁の判断で contempt 認定は維持されつつ「実費に紐づく合理的な手数料」は認めうるとされ、2026 年 4 月に最高裁への上告受理申立てが行われた（＝米国の 0% は係争中で、将来変わりうる）。
  - URL: https://appleinsider.com/articles/25/05/02/apples-app-store-guidelines-updated-to-reflect-court-order-over-external-purchases , https://www.revenuecat.com/blog/growth/apple-anti-steering-ruling-monetization-strategy , https://stora.sh/blog/2026-05-16-apple-app-store-external-purchase-links-implementation-guide
  - 出典日付: 2025-05-02 / 記載なし / 2026-05-16
  - 確度: 低〜中（判決文・Apple の公式アナウンスの原文は未確認。検索エンジンの要約と二次メディア経由。**特に「2025 年 12 月の第 9 巡回区判断」「2026 年 4 月の上告受理申立て」は原典未確認**）

### クロスプロモーション（「他にもこういうのを出してるよ」）の扱い

オーナーの意図は「外部課金への誘導」ではなく「自分の他のプロダクトの告知」だったため、2026-09-19 に追加で原文を確認した。

- 事実: 3.2.1(i) は Acceptable（許容される行為）として次を挙げている — "Displaying your own apps for purchase or promotion within your app, provided the app is not merely a catalog of your apps."（自分のアプリの宣伝は可。ただし自分のアプリのカタログにすぎないアプリは不可）
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし
  - 確度: 高（原文を直接取得）
- 事実: 4.2.2 — "Other than catalogs, apps shouldn't primarily be marketing materials, advertisements, web clippings, content aggregators, or a collection of links."（アプリ自体が主に宣伝物・リンク集であってはならない）
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 3.2.2(i) は Unacceptable として "Creating an interface for displaying third-party apps, extensions, or plug-ins similar to the App Store or as a general-interest collection." を挙げる（第三者のアプリを並べるのは不可。自分のアプリの宣伝とは扱いが違う）
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし
  - 確度: 高
- 事実: 2.3.10 — "don't include names, icons, or imagery of other mobile platforms or alternative app marketplaces in your app or metadata, unless there is specific, approved interactive functionality."（他のモバイルプラットフォーム／代替アプリマーケットへの言及は不可。Web プロダクトはこの条文の対象ではないと読める）
  - URL: https://developer.apple.com/app-store/review/guidelines/
  - 出典日付: 記載なし
  - 確度: 高（原文は高。ただし「Web プロダクトは対象外」という解釈は当方の読みであり、Apple の運用としては未確認）

**読み取れる境界**: 誘導先が「App Store 上の自分の別アプリ」なら 3.2.1(i) で明確に許容される。しかし誘導先が **サブスクを販売している自前の Web プロダクト**の場合、そのリンクは 3.1.1(a) の言う "calls to action that direct customers to purchasing mechanisms other than in-app purchase" に該当しうるため、米国以外のストアフロントではリジェクトリスクが残る。「告知」と「購入への誘導」は、リンク先が課金ページを持つ時点で外形的に区別しにくい。

### 母数の問題（規約とは別の、より本質的な障害）

オーナー自身が「使ってくれる人も多くないといけない」と指摘した点。逆算すると次のようになる。

- 目標 $700〜$2,000 MRR。価格 $10/月なら有料ユーザー 70〜200 人が必要。
- 無料アプリから別プロダクトの有料契約まで到達する転換率を 1%（楽観）〜0.3%（現実的）と仮置きすると、**無料アプリ側に 7,000〜67,000 人のアクティブユーザーが必要**になる。

**この転換率は出典のある数字ではなく、当方の仮置きである（確度: 低、要検証）。** ただし桁の話として、この構想は「有料 70〜200 人を獲得する問題」を「無料 1 万人規模を獲得する問題」に置き換えており、**制約（発信・集客をメインにしない）をより厳しい形で再生産している**。無料アプリのファネルは母数勝負であり、母数勝負とは集客勝負である。

対して、マーケットプレイス（Shopify App Store、VS Code Marketplace 等）の検索流入は母数こそ小さいが、検索している時点で購入意図がある。**必要な母数の桁が 2 つ違う**という点が、今回の制約下での判断の分かれ目になる。

## グレーゾーン・未確認

- **ガイドラインページに更新日の表示がない。** 取得した本文が 2026-09-19 時点の現行版であることは、ページの内容からは確認できない。Apple Developer News 側に更新告知があるはずだが未確認。
- **米国外への展開方法が未確認。** 「米国ストアフロントだけ CTA を出し、他ストアフロントでは出し分ける」実装が審査を通るのか、そうしている実例があるのかは調べていない。技術的には可能に見えるが、Apple が出し分け自体をどう評価するかの一次情報は取れていない。
- **EU の DMA 対応（代替ブラウザエンジン・代替決済・Core Technology Fee）は今回調べていない。** 英語圏＝米国だけではないので、EU / 英国の扱いは別途確認が必要。
- **4.3(b) の運用実態が不明。** 「量産」が何本から 4.3 でリジェクトされるのか、どの程度の差分があれば "meaningfully different" と見なされるのかの運用基準は公開されていない。開発者コミュニティの体験談は今回収集していない。
- **第 9 巡回区判断と上告の状況が原典未確認。** 米国の外部リンク 0% が今後も続く保証はなく、この戦略の前提は係争の結論に依存する。
- **「無料アプリからの誘導」の転換率データは一切見つけていない。** 規約上できるかどうかと、実際に本体プロダクトの有料ユーザーになるかは別問題。この点は未調査。

- **無料アプリ → 別プロダクトの有料転換率について、出典のある数字を持っていない。** 上記の逆算で使った 0.3〜1% は仮置きであり、実測値ではない。この戦略を真剣に検討する場合は、ここを調べ直す必要がある。
- **「自分の Web プロダクトへの告知リンク」が米国以外で実際にリジェクトされるかは未確認。** 条文の読みからリスクを指摘しているが、Apple の運用実績（同様の構成で通っている／落ちている実例）は収集していない。

## 影響する論点

- オーナーが挙げた「App Store に無料アプリを量産して、App Store 外の本体プロダクトへ誘導する」案の可否。**「量産」は 4.3(b) により推奨できない。「1 本の無料コンパニオンアプリを、米国ストアフロントで外部リンク付きで出す」なら規約上は成立する**が、これは "量産による数の暴力" ではなく "1 本を当てる" 話に戻るため、集客の負担は減らない。
- 「スマホアプリは避けたい」という当初の方針を覆す材料にはならない、というのが現時点の読み。
