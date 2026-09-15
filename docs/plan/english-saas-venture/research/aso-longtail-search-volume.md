# ASOロングテールクエリ（`phrasal verbs`等）に実際の検索需要はあるか

- 調査日: 2026-09-14
- 調査手段: Claude in Chrome（本セッションの実ブラウザ）で Google Trends・Ahrefs Free Keyword Generator・Ubersuggest・YouTube検索結果を直接操作して取得。Google検索オートコンプリートAPI（`suggestqueries.google.com`）はcurlで直接取得。Semrushのキーワード概要ページはログイン要求で取得失敗（後述）。WebSearch/WebFetchは使わず、すべて本セッションが一次データに触れている。
- 問い: `docs/plan/english-saas-venture/research/app-store-aso.md` で「隙あり」と判定された4クエリ（`shadowing english` / `english collocations` / `english idioms` / `phrasal verbs`）に、実際の検索需要（ボリューム）はあるのか。それとも大手が単に最適化していないだけで、そもそも誰も検索していない語なのか。

## 結論

**4クエリを一律に「需要なし」と結論するのは誤り。中身はクエリごとに大きく異なる。**

**`phrasal verbs` と `english idioms` は実在する、無視できない規模の検索需要がある。** Ahrefs Free Keyword Generatorで両語とも米国月間検索ボリューム「>1000」帯に入り、Ubersuggestで`phrasal verbs`単体を確認したところ具体的に**8,100/月**（SEO難易度40=中、CPC $9.71）という数字が出た。Google Trendsの5年間の週次データでも両語は一貫して低いが安定した値（`learn english`を100とした相対値で3〜11程度）を保っており、突発的なバズではなく定常的な検索需要と見られる。YouTube検索でもこの2語は関連動画が数十万〜880万回視聴と、英語学習トピックとして確立している。**これは「大手が気づいていない隙」という当初の見立てを補強する材料になる。**

**一方 `english collocations` は、当初メインセッションが懸念した「そもそも検索されていない語」がほぼそのまま当てはまる。** Ahrefsで米国月間検索ボリュームは「<100」、Google Trendsでは過去5年のほぼ全期間で観測値0（週次データの検出下限以下）。iTunes Search APIで確認された個人開発アプリの最高到達点（276レビュー）は、「参入すれば伸ばせる余地」ではなく「この語自体の需要が薄い中での天井」と読むほうが整合する。

**`shadowing english` はどちらとも言い切れない中間ケースで、かつ興味深い。** Google検索ボリューム自体はAhrefsで「>100」止まり、Trendsでも2025年半ばまでは観測値0が続いていた。しかし**2025年7月頃を境に、Trendsで初めて継続的に検出される値（1〜4程度）が出現し始めており**、かつYouTube上には関連動画で410万回視聴に達するものもある。「衰退している語」ではなく「最近になって立ち上がってきている、まだ小さい語」という読み方が最も自然で、今後数ヶ月〜1年の推移を追う価値がある。

**比較対象クエリ（`workplace english` / `english small talk` / `english pronunciation practice`）との対比では、期待したほどきれいな差が出なかった。** Google Trendsの相対値では`workplace english`(9)が`phrasal verbs`(4)や`english idioms`(5)より**高い**値を示した一方、Ahrefsの絶対ボリューム帯では`workplace english`は「<100」で`phrasal verbs`・`english idioms`より低い。**ツール間でランキングが逆転する**という、単純に「隙ありクエリ＝需要が低い」と決めつけられない結果になった。これはGoogle Trendsが「相対的な検索興味の時系列」を測るのに対し、Ahrefs/Ubersuggestは「推定絶対検索数」を測っており、両者は別の指標であることに起因すると考えられる（詳細はグレーゾーン参照）。`english small talk`はどのツールでも一貫して最低値だった。

**YouTube視聴回数は、当初期待した「隙クエリと非隙クエリを判別する代理指標」としては機能しなかった。** `english collocations`（隙あり）も`workplace english`（隙なし）も、上位動画は数十万〜百万回台の視聴回数を持ち、明確な差は見られなかった。英語学習系トピックはGoogleキーワード検索ボリュームの大小に関わらず、YouTube上では一定の視聴需要を持つ傾向があるようで、この指標単体でASO上の需要判定には使えない。

## 検索ボリューム表

### Google Trends（米国、Web検索、過去12ヶ月、相対値。`learn english`=83を共通アンカーとして2バッチを結合）

| クエリ | 相対値（`learn english`=83基準） | 出典 | 確度 |
|---|---|---|---|
| learn english | 83 | Google Trends（2026-09-14取得、本セッションがブラウザで直接確認） | 高 |
| workplace english | 9 | 同上 | 高 |
| english idioms | 5 | 同上 | 高 |
| phrasal verbs | 4（2バッチで再現、一致） | 同上 | 高 |
| shadowing english | 2 | 同上 | 高 |
| english pronunciation practice | 2 | 同上 | 高 |
| english collocations | 1 | 同上 | 高 |
| english small talk | 1 | 同上 | 高 |

補足: Trendsの数値は週次データの12ヶ月平均。バッチを分けて比較したが、両バッチに共通して入れた`learn english`と`phrasal verbs`の値が完全に一致した（learn english=83、phrasal verbs=4）ため、正規化のずれはないと判断した。

### Ahrefs Free Keyword Generator（米国、フレーズ一致、ログイン不要で確認できた範囲）

| クエリ | 検索ボリューム帯（月間・米国） | KD | 関連キーワード総数 | 出典 | 確度 |
|---|---|---|---|---|---|
| learn english | >1000 | Hard | - | ahrefs.com/keyword-generator（2026-09-14） | 高 |
| phrasal verbs | >1000 | Easy | 6,332件 | 同上 | 高 |
| english idioms | >1000 | Hard | 1,093件 | 同上 | 高 |
| shadowing english | >100 | Medium | - | 同上 | 高 |
| english pronunciation practice | >100 | Medium | - | 同上 | 高 |
| english collocations | <100 | Easy | 198件 | 同上 | 高 |
| workplace english | <100 | Easy | - | 同上 | 高 |
| english small talk | <100 | N/A | - | 同上 | 高 |

注: Ahrefsの無料版は「>1000 / >100 / <100」という粗いバケット表示のみで、正確な数字は有料プランが必要。`learn english`と`phrasal verbs`・`english idioms`が同じ「>1000」バケットに入ってしまうため、これらの間の規模差（おそらく数百倍〜数千倍）はこの粗さでは判別できない。

### Ubersuggest（米国、ログイン不要の無料検索は1回のみ）

| クエリ | 検索ボリューム（月間・米国） | SEO難易度 | CPC | 出典 | 確度 |
|---|---|---|---|---|---|
| phrasal verbs | 8,100/月 | 40（中） | $9.71 | app.neilpatel.com/en/ai-keyword-overview（2026-09-14） | 中 |

`english idioms`で2回目の検索を試みたが、サインアップを求めるモーダルに阻まれ取得できなかった（無料枠は1セッション1回のみ）。追加のクッキークリア等での回避は行わなかった（粘りすぎない方針に従った）。

このページには「Search Volume by Location: 301K, All Locations (100%)」という表示もあったが、集計範囲（全世界の英語圏合計か、別の指標か）が不明瞭なため、参考値にとどめる（グレーゾーン参照）。

### Google検索オートコンプリート（`suggestqueries.google.com`、2026-09-14取得）

8クエリすべてで最大件数（10件）のサジェストが返り、サジェスト数による判別はできなかった。オートコンプリートの豊富さは「検索母数の大きさの弱い代理指標」として期待していたが、今回試した語はいずれも十分に一般的な英語学習トピックであり、サジェスト数では差が出ないことが分かった。この指標は今回の判定には使えない（確度: 低〈判別力なし〉）。

### YouTube検索結果の上位動画視聴回数（2026-09-14取得、`youtube.com/results`を直接ブラウザで確認）

| クエリ | 上位4件の視聴回数（概算） | 出典 | 確度 |
|---|---|---|---|
| english idioms | 152万 / 887万 / 388万 / 72万 | youtube.com/results（2026-09-14） | 高（一次観測） |
| phrasal verbs | 145万 / 230万 / 95万 / 86万 | 同上 | 高 |
| shadowing english | 166万 / 8.7万 / 111万 / 409万 | 同上 | 高 |
| workplace english | 68万 / 28万 / 85万 / 146万 | 同上 | 高 |
| english small talk | 91万 / 268万 / 217万 / 56万 | 同上 | 高 |
| english collocations | 57万 / 73万 / 31万 | 同上 | 高 |

視聴回数の観測自体の確度は高いが、「これがApp Store/Google検索の需要の代理指標として機能する」という解釈の確度は低い（結論参照）。

## グレーゾーン・未確認

- **Semrushの無料キーワード概要は取得できなかった。** `semrush.com/analytics/keywordoverview/`に直接アクセスしたが、Volume/Global Volume/Trend等の主要指標がすべて「n/a」または「Something went wrong」表示となり、ログインなしでは実データが取得できないことを確認した（3回目の試行はせず、ここで打ち切った）。
- **Wordtracker、KeywordTool.ioの無料版は時間の都合で未試行。** 依頼文に挙げられていたが、Ahrefs・Ubersuggestで一定のクロスチェックが取れたため優先度を下げ、試していない。
- **Ubersuggestの「301K All Locations」表示の集計範囲が不明。** 米国のみのSearch Volume(8.1K)と桁が大きく異なり、全世界の英語圏合計なのか、別のクリックストリーム指標なのか、ページ上の説明だけでは判別できなかった。参考値として扱い、本文の結論には使っていない。
- **Google TrendsとAhrefs/Ubersuggestで、クエリ間のランキングが一部食い違う。** 具体的には`workplace english`はTrendsの相対値では`phrasal verbs`・`english idioms`より高いが、Ahrefsの絶対ボリューム帯では両語より低い。これは指標の性質の違い（相対的な時系列興味 vs 推定絶対検索数）に起因すると考えられるが、どちらが実際のApp Store内検索行動に近いかは本調査では判断できない。
- **App Store内検索そのもののボリュームは、依然として一切測定できていない。** 本調査で測ったのはすべてGoogle Web検索（Trends/Ahrefs/Ubersuggest）とYouTube検索の需要であり、App Store検索ボックスに実際に何人が「phrasal verbs」等と打ち込んでいるかは、公式・非公式のいずれのソースからも確認できなかった。Google検索需要とApp Store内検索需要が同じ分布をするとは限らない（例: Google検索は「学習コンテンツを探す」目的が主で、App Store検索は「すでにアプリを探す意図がある」ユーザーに限定される、という違いがありうる）。**これは元の`app-store-aso.md`が指摘した穴を完全には埋めておらず、なお未解決。**
- **`shadowing english`が2025年7月頃から立ち上がった理由は特定できていない。** 特定のYouTuber・TikTokトレンド・書籍の出版等、外的要因があった可能性があるが、本調査では確認していない。
- YouTube視聴回数は日本語UIで「◯万回視聴」表記のまま取得しており、概算値（例: 152万=1,520,000）として扱っている。正確な下1桁までの数字ではない。

## 影響する論点

- `docs/plan/english-saas-venture/open-questions.md`の「アプリストア・ロングテールクエリの検索ボリュームは実在するか」に対し、**クエリごとに答えが異なる**という材料を提供する。一律の「隙あり4クエリ」という括りは維持できない。
  - `phrasal verbs` / `english idioms`: 実在する検索需要あり（月間数千件規模）。大手が最適化していない「隙」という当初の評価は、需要の裏付けが取れたことでむしろ補強された。
  - `english collocations`: 検索需要がほぼ確認できない。「隙があった」のではなく「そもそも需要が薄い」という懸念（メインセッションの追検証コメント）が、本調査でも支持された。
  - `shadowing english`: 現時点では小さいが、2025年半ば以降に立ち上がってきている可能性がある新興トピック。今すぐ「隙あり」と判定するには材料不足だが、「需要なし」と切るのも早計。継続観察が必要。
- 「複数アプリを出して当たったものを伸ばす」戦略（`decisions.md` 2026-09-14）を検討する際、`phrasal verbs`・`english idioms`は検索需要の裏付けがある分、他の2語より優先度を上げてよい候補になりうる。
- App Store内検索ボリューム自体は依然未測定のままであり、この一点は`app-store-aso.md`が指摘した穴として残り続ける。ASOへの依存度を左右する重要な論点であれば、有償ツール（Ahrefs Starter等）での確度の高い数値取得、またはApple Search Adsの「検索語の人気度」機能（Apple公式が提供する候補ボリュームの相対指標）の確認が次の一手になる。
