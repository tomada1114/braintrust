# LLM モデルの「賢さ」比較とチャット用途での選定方針

- 調査日: 2026-09-15
- 調査手段: メインセッションで LMArena Text Arena・Artificial Analysis を直接確認 + 個別 Sonnet サブエージェント5体(ベンダー別)による並列調査(Sonnet-5相当ティアの特定)。プライマリソース(LMArena, Artificial Analysis, 各社公式料金ページ)は都度ブラウザで直接確認。
- 更新の目安: 3 ヶ月(ただしこの分野は他の landscape ファイルより変化が速い。GPT-6 Astra は今回の調査期間中の 2026-09-03 発表で、OpenAI のモデル階層をまるごと再編していた)
- 想定用途: **チャット形式**で使う英語学習の会話相手・添削フィードバックアプリ。コーディングやエージェント的タスクではなく、一般的な言語運用能力とレイテンシ(体感速度)を重視。
- 比較指標: LMArena Text Arena「Overall」カテゴリ(クラウドソースの人間選好投票)、Artificial Analysis の Intelligence Index(0-100の複合ベンチマーク)・Speed・Latency(TTFT=最初のトークンまでの秒数)・End-to-End Response Time。

## 結論(このリポジトリでのチャット用途モデル選定方針)

**第一候補: GPT-5.6 Luna(reasoning effort = high)。**

- 価格 $0.20 / $1.20(per MTok, 推定 — reasoning effort によって課金レートは変わらず生成トークン量が変わる仕組みのため)。Claude Sonnet 5 の 1/10 程度。
- Artificial Analysis の Intelligence Index は 32 で、Claude Sonnet 5(high, 同じく 32)と同値。
- レイテンシは TTFT 8.6秒・総応答 13.4秒とチャットで許容できる範囲(xhigh の TTFT 45秒は論外)。
- **留保**: LMArena の人間選好スコアは xhigh 変種(1452)でしか計測されておらず、high 単体の値は未確認。実際の英語チャット品質は本番投入前に手元で試して確認すること。

**次点: Gemini 3.8 Flash(medium)。** 現行 $0.75/$3.75 だが 2027-01-01 から $1.50/$7.50 に値上げ予定(公式ページの脚注で確認、確度 高)。値上げ後でも Sonnet 5 より安く、Intelligence Index は 40(high の 41 とほぼ同等)で今回の比較全体で最高。無料枠があり検証コストが低いのも利点。ただし medium 効果時の実測レイテンシは未計測(3.7世代からの類推で high の半分以下と推定、未確認)。

**Claude Sonnet 5 はコスパでは推さない。** 「賢さの基準点」として比較対象に置いたが、今回調べた6モデル中で価格が最も高く($2/$10)、Intelligence Index は最下位タイ(32)。medium に下げても速度メリットがほぼゼロ(TTFT 2.3秒→1.5秒、総応答はほぼ変わらず)なので、下げる理由もない。Sonnet を選ぶ理由があるとすれば、コスパではなく Claude Agent SDK / Claude Code など既存スタックとの統一や Anthropic の安全性方針への信頼といった別軸。

**Grok は今回のチャット用途では見送り。** reasoning effort を high→medium に下げてもレイテンシがほぼ変わらない(TTFT 36秒→33秒)。速くしたい場合は low(TTFT 5.6秒)まで落とす必要があり、そこまで落とすと知性面で比較の前提が崩れる。

**DeepSeek V4-Pro は候補として保留。** TTFT は最速級(1.7秒)で価格も安いが、総応答時間が28秒と長い(出だしは速いが生成が長く続くタイプ)。ストリーミング表示のUIなら体感の悪さは緩和されるかもしれず、プロトタイプで実際の体感を確認する価値はある。

## エフォートレベル(reasoning effort)とレイテンシの関係 — ベンダーごとに挙動が違う

「high を medium に下げれば速くなる」という単純な話ではない。Artificial Analysis で実測した限り、ベンダー・モデルファミリーごとに全く傾向が異なる。

| モデル | high: TTFT/総応答/知性指数 | medium: TTFT/総応答/知性指数 | 傾向 |
|---|---|---|---|
| Claude Sonnet 5 | 2.3s / 10.9s / 32 | 1.5s / 10.3s / 28 | high→medium でほぼ速度変わらず、知性だけ落ちる。**medium にする意味がない** |
| GPT-5.6 Luna | 8.6s / 13.4s / 32 | 2.4s / 6.7s / 25 | high→medium で速度は3〜4倍、知性は3割減。**トレードオフが明確**(だからこそ high が甘い所) |
| Gemini 3.8 Flash | 16.3s / 17.8s / 41 | (未計測、3.7世代からの類推で半分以下) / 40 | 知性はほぼ変わらず速くなる可能性が高い。**ほぼ無料の乗り換え** |
| Grok 4.6 | 36.2s / 44.7s / 44 | 32.8s / 42.0s / 43 | **high→medium でほとんど速くならない**。速くしたければ low(TTFT 5.6秒)まで落とす必要がある |
| DeepSeek V4-Pro | TTFT 1.7s / 総28.2s(effort変種なし) | — | 出だしは速いが生成が長く総時間は遅い |
| Mistral Medium 3.5 | TTFT 2.2s / 総19.8s(effort変種なし) | — | 単一設定 |

(出典: https://artificialanalysis.ai/leaderboards/models, 確認 2026-09-15, 確度 高。Intelligence Index は Artificial Analysis 独自の0-100複合指標で、LMArena の Elo 風スコアとは別スケール)

## Sonnet 5 相当ティアの一覧(LMArena Overall スコア順)

| 順位 | モデル | ベンダー | Arena スコア | Arena 順位 | 投票数 | 価格(入力/出力, per MTok) |
|---|---|---|---|---|---|---|
| 1 | Gemini 3.1 Pro (Preview) | Google | 1487 ±3 | 15 | 106,951 | $2 / $12(200k超は $4/$18) |
| 2 | GPT-5.6 Terra (xhigh) | OpenAI | 1466 | 45 | 28,119 | $2 / $12(長文脈で入力 $4、出力未確認) |
| 3 | Claude Sonnet 5 (high) | Anthropic | 1461 | ~51 | 35,301 | $2 / $10 |
| 4 | DeepSeek V4-Pro | DeepSeek | 1457(-high 変種は1463・50位) | 57 | 54,130 | $0.66 / $1.98(オフピーク)〜$1.32 / $3.96(ピーク) |
| 5 | Grok 4.6 (high) | xAI | 1456 | 63 | 15,521 | $2 / $6(200k超は $4/$12、キャッシュ入力 $0.5) |
| 6 | Mistral Large 3 | Mistral | 1413 | 133 | 69,028 | $0.5 / $1.5 |

(LMArena 全体は 2026-09-13 時点で 8,146,274 票・402 モデル。https://arena.ai/leaderboard/text, 確認 2026-09-15, 確度 高)

## Flash/軽量ティアの一覧(LMArena Overall スコア順)

「Sonnet 5 相当は過剰で、Flash 相当で十分」という基準に切り替えて比較した各社の軽量ティア。

| モデル | スコア | 順位 | 価格(入力/出力 per MTok) |
|---|---|---|---|
| Gemini 3.8 Flash (high) | 1493(Preliminary, 投票 5,076) | 9 | $0.75 / $3.75(2027-01から $1.50/$7.50) |
| GPT-5.6 Luna (xhigh) | 1452 | — | $0.20 / $1.20 |
| DeepSeek V4-Flash | 1436 | 108 | $0.30 / $1.20 |
| Mistral Medium 3.5 | 1426 | 106 | $0.75 / $3.75 |
| Grok 4.1 Fast (reasoning) | 1430 | 101 | $1.25 / $2.50 |
| Claude Haiku 4.5 | 1415 | 129 | $1 / $5 |

Anthropic にとって都合の悪い結果だが率直に書いておく: **Claude Haiku 4.5 はこの6モデル中スコア最下位**で、同価格帯の Grok 4.1 Fast にも劣る。「Flash 相当で十分」という基準を採用するなら、Anthropic 系列で揃えるより他社の軽量モデルの方がコスパで優位。

## ベンダー別メモ

### Anthropic — Claude Sonnet 5 / Haiku 4.5
- Sonnet 5(high): 価格 $2/$10、Arena 1461・順位~51、AA Intelligence Index 32、TTFT 2.3秒/総10.9秒。medium に下げても TTFT 1.5秒・総10.3秒とほぼ変化なし(知性指数だけ28に低下)。
- Haiku 4.5: 価格 $1/$5、Arena 1415・順位129(軽量ティア内最下位)。
- (https://arena.ai/leaderboard/text, https://artificialanalysis.ai/leaderboards/models, 確認 2026-09-15, 確度 高)

### OpenAI — GPT-5.6 Terra / Luna
- 2026-09-03 の GPT-6 Astra 発表で、OpenAI のモデル階層は Astra(最上位)→ Sol(「複雑な専門業務向け旗艦」)→ Terra(「知性とコストのバランス」)→ **Luna(高ボリューム/低コスト)** の4段に再編された(https://developers.openai.com/api/docs/models, 確認 2026-09-15, 確度 高)。
- Luna は reasoning effort により Intelligence Index・レイテンシが大きく変わる: xhigh(35, TTFT 45.0s)→ high(32, TTFT 8.6s)→ medium(25, TTFT 2.4s)→ low(22, TTFT 2.1s)→ non-reasoning(17*, TTFT 0.85s)。LMArena での人間選好スコアは xhigh(1452)のみ計測(https://arena.ai/leaderboard/text?q=gpt-5.6, https://artificialanalysis.ai/leaderboards/models, 確認 2026-09-15, 確度 高)。
- Terra: 価格 $2/$12、Arena 1466(xhigh)・45位。Sonnet 5 とほぼ横並びで、Luna ほどの割安感はない。
- **グレーゾーン**: 2026-09-06 時点で存在した gpt-5.1 / gpt-5.2 / gpt-4.1 / gpt-4o は現行の料金・モデル一覧ページに現れなくなった。廃止か掲載漏れかは未確認。Luna(high)単体の LMArena スコアは未計測。

### Google — Gemini 3.1 Pro (Preview) / 3.8 Flash
- Pro ティアは `gemini-2.5-pro`(旧)と `gemini-3.1-pro-preview`(最新、GA版は存在しない)のみ。価格 $2/$12(200k超で$4/$18)、Arena 1487・15位(https://ai.google.dev/gemini-api/docs/pricing, 確認 2026-09-15, 確度 高)。
- 3.8 Flash(high): 価格 $0.75/$3.75、Arena 1493・9位(Preliminary)、AA Intelligence Index 41、TTFT 16.3秒。**2027-01-01 から $1.50/$7.50 に値上げ予定**と公式ページに明記(スクリーンショットで確認、確度 高)。
- 3.8 Flash(medium): Intelligence Index 40(high とほぼ同等)。AA はまだレイテンシを実測していない(「--」表示)。同世代3.7 Flash では high→medium で TTFT が 10.2秒→4.4秒に半減以下となっており、3.8 でも同様の傾向と推定(未確認)。
- **グレーゾーン**: LMArena 上の Gemini 3.1 Pro の価格欄($1/$6)が公式標準料金($2/$12)と一致しない(Batch/Flexティアの可能性、未確認)。3.8 Flash(medium)の実測レイテンシは未確認。

### xAI — Grok 4.6 / 4.1 Fast
- Grok 4.6: xAI 公式が「コード・チャット双方で使うべき」と明記する現行旗艦。価格 $2/$6(200k超で$4/$12)、Arena 1456・63位(https://docs.x.ai/docs/models, 確認 2026-09-15, 確度 高)。
- reasoning effort を下げても速くならない: high(TTFT 36.2s)→ xhigh(33.1s)→ medium(32.8s)とほぼ横ばい。low まで下げてようやく TTFT 5.6秒(Intelligence Index は未確認だが大きく下がると推定)。
- Grok 4.1 Fast(reasoning): Arena 1430・101位、価格$1.25/$2.50。Artificial Analysis の現行モデル一覧には出てこず(レガシー扱いの可能性、未確認)、レイテンシは未計測。
- **グレーゾーン**: 同系列のベータ版(`grok-4.20-*`)が公式旗艦の 4.6 より Arena スコアが高いという逆転現象があり、位置づけは未確認。

### DeepSeek — V4-Pro / V4-Flash
- V4-Pro: ピーク/オフピーク制、$0.66/$1.98(オフピーク)〜$1.32/$3.96(ピーク)。Arena 1457・57位。TTFT 1.7秒だが総応答28.2秒と長い(https://api-docs.deepseek.com/quick_start/pricing/, https://artificialanalysis.ai/leaderboards/models, 確認 2026-09-15, 確度 高)。
- V4-Flash: $0.30/$1.20、Arena 1436・108位。
- **グレーゾーン**: `-high` 変種がデフォルト API 挙動に対応するかは未確認。ピーク/オフピークどちらを「代表価格」とすべきかも判断が分かれる。

### Mistral — Mistral Large 3 / Medium 3.5
- Large 3(`mistral-large-2512`): $0.5/$1.5、Arena 1413・133位(全体最下位)。
- Medium 3.5: $0.75/$3.75 相当、Arena 1426・106位で Large 3 より上位。TTFT 2.2秒・総応答19.8秒。reasoning effort の変種なし。
- 補足: Mistral 自身の FAQ は一般用途に Medium を推奨しており、Large は最上位 SKU だが主力商品ではない可能性(未確認)。

## グレーゾーン・未確認

- LMArena の "Overall" は人間の選好投票であり、英語学習アプリが必要とする「文章読解・添削・フィードバックの精度」を直接測るものではない。英語学習用途特化のベンチマークは今回の調査対象に含めていない。
- **GPT-5.6 Luna(high)単体の LMArena 人間選好スコアは未計測**(xhigh の 1452 のみ確認済み)。本番投入前に実際のプロンプトで英語チャット品質を目視確認することを推奨。
- Gemini 3.8 Flash(medium)の実測レイテンシは未確認(3.7世代からの類推)。
- Artificial Analysis の Intelligence Index(0-100の複合指標)と LMArena の Elo 風スコアはスケールも算出方法も異なる。本ファイルでは両方併記しているが、単純比較はできない。
- OpenAI の新ラインナップ(Astra/Sol/Terra/Luna)は 2026-09-03 発表からまだ日が浅く、旧モデルが API から完全に消えたのか掲載漏れなのかは未確認。
- Gemini 3.1 Pro の LMArena 価格表示と公式標準料金の不一致の原因は未確認。
- xAI の Grok 4.6 が「公式の旗艦」でありながら同系列のベータ版より Arena スコアが低い理由は未確認。Grok 4.1 Fast のレイテンシも未計測。
- DeepSeek の `-high` 変種がデフォルト API 挙動に対応するかは未確認。
- 今回はテキストチャットの Overall カテゴリのみを見ており、Instruction Following や Creative Writing など英語学習用途に近いサブカテゴリ別の順位は取得していない。
