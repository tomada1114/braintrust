# 学習アプリのゲーミフィケーション: 実例と、効果・反発の根拠

- 調査日: 2026-09-22
- 調査手段: Opus サブエージェント 8 セル（Workflow）による机上調査。メインセッションが原典 3 本を確認（2026-09-22）
  - Deci, Koestner & Ryan 1999（Psychological Bulletin 125(6)）要旨: 取り組み・完了・成績連動の報酬で自由選択時の内発的動機が低下（d = −0.40, −0.36, −0.28）、ポジティブなフィードバックは向上（d = 0.33）。一致
  - Duolingo blog「improving-the-streak」（2020-11-19）: 日次目標とストリーク条件を分けて Day 14 継続率 +3.3%、ストリーク中の割合 +10.5%。一致。自社発表である点は変わらない
  - Kao ら CHI 2024（事前登録、n=1,699）要旨: 「Success dependence enhanced all motives, while amplification unexpectedly reduced them」。一致。ただし題材はアクション RPG で、学習アプリへの当てはめは類推
  - セル: Duolingo / 日本の英語学習アプリ / RPG・ゲーム型英語アプリ / スピードドリル系 / 習慣・学習記録アプリ / マイクロフィードバック / 効果の研究 / 反発の研究
  - 取得できなかったセル: なし。個別に開けなかったページは末尾の「取得できなかったページ」に並べる
- 問い: 学習アプリのゲーム的な仕組み（ポイント・レベル・称号・ストリーク・ランキング・演出・進捗表示・強い報酬）は、継続と学習にどれだけ効き、どんな反発を生むか。

## 結論

1. ゲーミフィケーション全体の学習効果は小〜中程度で、正。成績は g≈0.5〜0.8、動機は 0.26〜0.36、行動は 0.25。ただし厳密な研究に絞ると、動機と行動への効果は不安定になる。「入れれば続く」とは言えない。
2. 期間とともに効果が消えるかは、研究間で逆の結論が出ている。新奇性が主因とみる研究もある。毎日を長く続ける前提なら、新しさに頼る演出だけで動機を支える設計は危うい。
3. 条件つきで期待される報酬（こなした量や成績に応じて付くポイントなど）は、内発的動機を下げる。これは頑健な根拠がある（Deci ら 1999、128 研究）。一方、情報を伝えるポジティブなフィードバックは動機を上げる。報酬とフィードバックは分けて考える必要がある。
4. ポイント・レベル・リーダーボードは、量は増やすが内発的動機も有能感も上げない（Mekler 2017）。リーダーボードとバッジで動機と成績が下がった授業の例もある（Hanus & Fox 2015）。ただしどちらも要旨の原文は未確認で、確度は中。
5. ストリークは強い。ただし「途切れる」ことが最大の弱点。延長条件を緩めること、猶予（フリーズ・週末免除）を入れることは、どちらも継続率を上げたという公式データがある。途切れると動機が下がることは査読研究（Silverman & Barasch 2023）でも示され、「修復できる」と悪影響が弱まる。公式データはすべて Duolingo 自社発表で、第三者の再現はない。
6. ランキング・リーグ・対戦への反発は、日本語の声でも研究でもはっきり出ている。「邪悪」「実益がない」「関心がない」、1 敗でやる気を失う、迷惑プレイ、不安と嫉妬。タイムのランキングは不正ツールまで生んだ（Quizlet Match）。
7. 自己申告の成績に報酬を結びつけると、申告は水増しされる。これは実験経済学で繰り返し示されている（部分的な嘘。最大限には偽らない）。報酬がなくても、自己採点は「忘れたと認めたくない」「早く終わらせたい」で甘くなる。ただし、学習アプリの自己採点とゲーム報酬の組み合わせを直接測った研究は見つからなかった。ここは類推にとどまる。
8. その場の演出は「成否に連動していること」が効き、演出を大きくすることはかえって動機を下げうる（CHI 2024、n=1,699）。演出の効果音オフと reduce-motion への追従は事実上の標準。
9. 日本の学習記録アプリで継続の理由として最も語られるのは、ストリークより「量の累計とグラフ」（Studyplus の自社調査で 80.7%）。実力の代理指標（abceed の予測スコア）が動機づけとして評価される例もある。自社調査で、やめた人の声は含まれない点は割り引く。
10. RPG・ガチャ型の強い報酬は「続いた」という声を生んでいる。ただし根拠は個人ブログとレビューで、学習効果の検証はない。効いた例は 1 問数秒・機械採点の単語 4 択に限られる。

弱いところ:

- 要素（ポイント・バッジ・ストリーク）ごとの単独の効果量を示すメタ分析は、要旨の範囲では見つからなかった。要素別の結論は、個別研究と実例の寄せ集め。
- ストリークの学習効果（継続ではなく学力）を調べた査読研究は見つからなかった。
- 日本語ユーザーの声は、ストリークとリーグには一定量ある。ポイント・XP、レベル、称号・バッジ、コンボ・時間制限、その場の演出については薄い。演出を「子どもっぽい」「うるさい」とする日本語の声は、探したが原文で確認できなかった。

## 根拠

凡例: 「公式」は事業者自身の発表。「第三者」は記事・レビューサイト。「声」は利用者本人の文章。「研究」は論文。声の引用は原文のまま（取得ツールが要約・英訳したものは引用として扱わず、その旨を書く）。

### ポイント・XP

- 研究: 期待された有形の報酬は、自由選択時の内発的動機を下げる。取り組んだだけでもらえる報酬 d=-0.40、完了でもらえる報酬 -0.36、成績に応じた報酬 -0.28。一方で「Positive feedback enhanced both free-choice behavior (d = 0.33) and self-reported interest (d = 0.31).」
  - Deci, Koestner & Ryan (1999) Psychological Bulletin 125(6)、128 研究のメタ分析
  - URL: https://home.ubalt.edu/tmitch/642/articles%20syllabus/Deci%20Koestner%20Ryan%20meta%20IM%20psy%20bull%2099.pdf
  - 出典日付: 1999
  - 確度: 高（ただし実験室の短期課題が中心。アプリの長期利用への当てはまりは不明）
- 研究: 画像タグ付け課題の 2×4 実験。ポイント・レベル・リーダーボードは内発的動機にも有能感にも有意な影響がなく、タグの量だけを増やした。質は上がらなかった。
  - Mekler, Brühlmann, Tuch & Opwis (2017) Computers in Human Behavior 71
  - URL: https://www.semanticscholar.org/paper/Towards-understanding-the-effects-of-individual-on-Mekler-Br%C3%BChlmann/70a4d654151234924c0a7ce7822f12108bf3db49
  - 出典日付: 2017
  - 確度: 中（検索要約で確認。要旨の原文は未取得）
- 公式: mikan は学習で得たポイントをランキングの元にする。「ランキングは、学習によって得たポイントをランキング形式にしたものです」。付与の詳しい仕組みは別ページ（未取得）。
  - URL: https://mikan.helpshift.com/hc/en/3-%E8%8B%B1%E8%AA%9E%E3%82%A2%E3%83%95%E3%83%AA-mikan/faq/340-q-%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%AF%E3%81%A8%E3%81%AF/
  - 出典日付: 記載なし（約 1 年前更新の表示）
  - 確度: 高
  - 関連: https://mikan.helpshift.com/hc/ja/3-%E8%8B%B1%E8%AA%9E%E3%82%A2%E3%83%95%E3%83%AA-mikan/section/51-%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%AF-%E3%83%9B%E3%82%A4%E3%83%B3%E3%83%88/ （記載なし、確度 中）
- 第三者: Duolingo はレッスン中の連続正解に Combo Bonus として最大 5 XP を足す。
  - URL: https://duolingo.fandom.com/wiki/XP
  - 出典日付: 記載なし
  - 確度: 低（検索スニペットのみ。ページは 402 で開けず、現行仕様か不明）
- 声: 長期ユーザーは「リーグ等にも全く興味がなかった」と書き、XP にも関心がなかった。
  - URL: https://note.com/chi_world/n/ne14463025f68
  - 出典日付: 2025-01-21 頃（別セルは 2025-05-06 と記録。食い違い）
  - 確度: 高
- 日本語の声の薄さ: ポイント・XP そのものへの日本語の賛否は、上の 1 件以外に見つからなかった。

### レベル・称号・バッジ

- 第三者: mikan は 100 語ごとにランクアップテストがあり、合格でランクが上がる。「気付いたらこんなにランクが上がってた！という達成感が生まれ、モチベーションが上がります」。
  - URL: https://eigomonogatari.com/mikan-review/
  - 出典日付: 2020-02-29（2021-04-06 更新）
  - 確度: 中
- 声: 満点を求めるランクアップテスト（関門）への不満。「時間の無駄です。単語は何周も回して覚えるものなので、8割ぐらい覚えたら次の単語に行けばいいと思います。ランクアップテストの満点を10に戻してください」（mikan 鉄壁）。
  - URL: https://applion.jp/iphone/app/1287396055/review/
  - 出典日付: 2019-10-10
  - 確度: 高
- 第三者: えいぽんたん！は 41 段階の英語レベル（K++〜S6）を進む。各レベルで 100 問連続正解するとトロフィーを得るコンプリート要素がある。
  - URL: https://www.eigonou.net/16580/
  - 出典日付: 2015-06-24
  - 確度: 中
- 第三者（保護者のブログ）: 英語物語で、小 5 の子が 5 ヶ月で英検 5 級相当から準 2 級相当に。一方で「単語ばかりレベルがあがっていることに気づきました」。ゲームの進み方が学ぶ中身の偏りを生んだ例。
  - URL: https://yuzuka-note.com/english-story
  - 出典日付: 2023-09-24
  - 確度: 中
- 研究: 16 週の授業で、リーダーボードとバッジのあるクラスは、ないクラスより内発的動機・満足・エンパワメントが時間とともに下がり、期末試験の点も低かった。内発的動機の低下が点の差を媒介した。
  - Hanus & Fox (2015) Computers & Education 80
  - URL: https://www.semanticscholar.org/paper/Assessing-the-effects-of-gamification-in-the-A-on-Hanus-Fox/dff76a9862467d426113ec530f83942016ae3a97
  - 出典日付: 2015
  - 確度: 中（検索要約のみ。ResearchGate の要旨は 403）
- 研究: Mekler 2017（上記）。レベルも内発的動機と有能感に影響しなかった。
- 日本語の声の薄さ: レベルの「関門」への不満は 1 件ある。称号・バッジへの日本語の賛否は見つからなかった。

### ストリークと猶予

- 公式: 延長条件を「日次目標 XP 達成」から「1 日 1 レッスン」に緩めた。「3.3% increase in Day 14 retention」。DAU +1%、ストリーク中の学習者の割合 +10.5%（新規は +19%）。「Learners who reach a streak of 7 are 2.4 times more likely to continue using Duolingo the next day than learners without a streak.」
  - URL: https://blog.duolingo.com/improving-the-streak
  - 出典日付: 2020-11-19
  - 確度: 高（数値の記載として）。2.4 倍は相関で、選抜効果と区別されていない
- 公式: ストリークフリーズを同時に 2 個まで装備可能にした。「this change actually increased the relative number of active learners on Duolingo every day by +0.38%」。「Duolingo learners who reach a streak of just 7 days are 3.6 times more likely to complete their course」（相関）。
  - URL: https://blog.duolingo.com/how-duolingo-streak-builds-habit
  - 出典日付: 2022-01-31
  - 確度: 高（+0.38%）/ 中（3.6 倍は相関）
- 公式: Weekend Amulet（週末に休んでも保てる）で、1 週間後の復帰 +4%、ストリーク喪失 -5%。Streak Wager で D7 継続率 +14%。「losing a streak can be very discouraging」。
  - URL: https://blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals/
  - 出典日付: 2017-05-10
  - 確度: 中（社内実験。測っているのは継続率で学習効果ではない）
- 公式（日本法人）: ストリーク喪失が離脱理由の上位だと公式が認めている。「ストリークを失うことは学習継続への意欲低下につながることもあり、離脱理由として最も多く挙げられる要因のひとつとなっています。」30 日以上続けた人向けの期間限定の復活キャンペーン。
  - URL: https://prtimes.jp/main/html/rd/p/000000092.000069537.html
  - 出典日付: 2026-06
  - 確度: 高
- 研究: 7 つの研究。記録の中で連続が保たれているとその後の行動が増え、途切れた連続を強調すると減る。自分のせいで途切れたと感じると効果が強まり、修復できると弱まる。「attenuated when consumers can "repair" a broken streak」。
  - Silverman & Barasch (2023) Journal of Consumer Research 49(6)
  - URL: https://academic.oup.com/jcr/article-abstract/49/6/1095/6623414
  - 出典日付: 2023
  - 確度: 高
  - 解説記事（Psychology Today）: 「About 66 percent of participants chose to do another strength exercise when their streak remained intact, but only about 58 percent did another strength exercise when the streak was broken.」記録の仕組みがない条件では効果が消えた。https://www.psychologytoday.com/us/blog/ulterior-motives/202306/how-broken-streaks-sap-motivation （2023-06、確度 中）
- 声（猶予に肯定）: 「やれなかったときに『もういいや』という気持ちが炸裂してしまいそう」。シールド（猶予）で休むことで重圧が和らいだ。
  - URL: https://note.com/yuccopooh/n/n439b0797926c
  - 出典日付: 2026-01-08
  - 確度: 高
- 声（長期ストリークが重荷）: 「気づいたら1000日を超えてしまいました。そうなるとさらにゼロに戻しにくくなります」。「積み上げたストリークが何百日とか行っているとゼロに戻すのには相応の勇気が必要でした。Mottainai精神です。」2370 日でやめた。
  - URL: https://note.com/chi_world/n/ne14463025f68
  - 出典日付: 2025-01-21 頃 / 2025-05-06（セル間で食い違い）
  - 確度: 高
- 声（ストリークのために最小限の利用）: 「Maintaining my streak has ensured I use the app daily, not that I actually learn a new word or character.」42 秒だけの利用、フリーズ購入の誘導をペイ・トゥ・ウィンと感じた。
  - URL: https://www.androidauthority.com/reasons-give-up-duolingo-streak-3543009/
  - 出典日付: 2025-04-17
  - 確度: 中
- 声: 「I rage quit Duolingo today. After a 1,569 day streak.」ストリーク・ポイント・順位が、効かない学習法を続けさせていたと振り返る。
  - URL: https://talentandsarcasm.substack.com/p/i-rage-quit-duolingo-today
  - 出典日付: 2021-05-10
  - 確度: 中
- 声（リセットで離脱）: 「昨日サボったからもうリセットされた『どうせ続かない』——そういう気持ちになって、そのままやめてしまう」。自作の習慣アプリにはストリークを入れなかった。
  - URL: https://note.com/montbranc_8122/n/n01781abc9113
  - 出典日付: 2026-03-22
  - 確度: 中
- 声（通知は肯定）: ストリーク切れ前の通知は良い機能と評価。一方で「ゲーム感覚で楽しいと評されるが、普通の英語ドリルである」。
  - URL: https://note.com/forsteri12/n/n4f2f72d4ff37
  - 出典日付: 2025-02-02
  - 確度: 高
- 声（最低ラインの低さ）: スタディサプリ ENGLISH「1日1分、2分しか勉強しない日もありますが、使いはじめてから1403日連続学習記録を達成しています」（まとめ記事での引用。元の投稿は未確認）。
  - URL: https://eikaiwa.gakumado.mynavi.jp/studysapuri-english-reviews/
  - 出典日付: 2026-08-15
  - 確度: 中
- 声（最低ラインの低さ）: mikan で日々の目標を低くして続いた。「流石に数十秒スマホを触るくらいならできる」。
  - URL: https://note.com/yuzakana_lang/n/n77406cc8ddf3
  - 出典日付: 2025-04-18
  - 確度: 高
- 公式: mikan は「学習記録が貯まってモチベーションが上がる」と打ち出し、1,000 日連続の利用者例を載せる。
  - URL: https://apps.apple.com/us/app/-/id920856839
  - 出典日付: 記載なし
  - 確度: 高
- 公式（宣伝）: BizSprinto One は連続練習日数と発話量を記録し、「もうちょっとだけ続けようという気持ちになる」。書き手は自社製品を宣伝する立場。
  - URL: https://bizsprinto.com/blog/instant-english-app-recommend
  - 出典日付: 2026-01-11
  - 確度: 中
- 第三者: スタディサプリ ENGLISH は連続学習日数と総学習時間を記録し、ウィジェットで出せる。
  - URL: https://searchhall.com/study-record/
  - 出典日付: 記載なし
  - 確度: 中

### リーグ・ランキング・対戦

- 声: リーダーボードを課金誘導の仕組みとして否定。「個人的にはとても邪悪な機能だと思っている」。
  - URL: https://note.com/forsteri12/n/n4f2f72d4ff37
  - 出典日付: 2025-02-02
  - 確度: 高
- 声: 「ダイヤモンドリーグに上がっても何もいいことはありませんｗ」。質問者はリーグ参加をやめた。
  - URL: https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13253203168
  - 出典日付: 2021-11-29
  - 確度: 高
- 声: 「リーグ等にも全く興味がなかった」（上記 chi_world）。
- 声（英語物語、App Store）: レート上限で 1 敗すると大きく下がりやる気を失う、連勝記録が 1 敗で消える、ランキング報酬が足りない。協力・対戦イベントでの妨害・煽り。「ゲーム重視で学習効果が薄い」という指摘も。
  - URL: https://apps.apple.com/jp/app/id805477882?see-all=reviews / https://appreview.jp/app/f1dcbc657c229194621a427da35753b2
  - 出典日付: 記載なし
  - 確度: 低（取得ツールの要約経由。逐語は未確認なので引用扱いしない。「ゲーム重視で学習効果が薄い」も要約中の表現）
- 声（不正）: Quizlet Match のタイムランキングに対抗する自動解答ツール。「Kids on Quizlet sets I use have gotten match scores of below one second, which annoys me. Therefore, I have written my own hack for it.」タイマー凍結スクリプトも複数公開されている。
  - URL: https://github.com/theaquarium/quizletmatch-autosolver （記載なし、確度 高）/ https://github.com/jaeheonshim/quizlet-match-hack （記載なし、確度 中）
- 公式: Anki Leaderboard アドオンは今日のレビュー数・学習時間・ストリーク・保持率で順位づけ。README に不正対策の記述はない。
  - URL: https://github.com/ThoreBor/Anki_Leaderboard
  - 出典日付: 記載なし
  - 確度: 高
- 研究: Hanus & Fox 2015（上記）。Bai ら 2020（下記）は、嫌われた理由として「gamification can cause anxiety or jealousy」を挙げる。
- 公式: Studyplus の自社調査で、動機が上がった理由の 2 位は「ライバルや友だちの勉強記録が見えるようになったため（49.5%）」。比較が効く層もいる。
  - URL: https://prtimes.jp/main/html/rd/p/000000196.000047308.html
  - 出典日付: 2023-06-05
  - 確度: 中（自社調査。継続中のユーザーに偏る）
- 日本語の声の薄さ: mikan のランキングへの賛否は、探したが見つからなかった。

### コンボ・時間制限

- 第三者: mikan は 30 秒以内に 10 問を答えるテンポの速い出題。「単語をテンポよくポンポン出題してくれるから、ゲーム感覚で楽しく学習できる！」
  - URL: https://eigomonogatari.com/mikan-review/
  - 出典日付: 2020-02-29（2021-04-06 更新）
  - 確度: 中
- 第三者: 瞬間英作文アプリ 15 本のうち制限時間があるのは 6 本。「制限時間があるのは15個中6個だけ」。BizSprinto One は 7 秒、トーキングマラソンは 6 秒。
  - URL: https://bizsprinto.com/blog/instant-english-app-recommend
  - 出典日付: 2026-01-11
  - 確度: 中（書き手は自社製品を宣伝する立場）
- 研究: ゲーム化した TBL の準実験（医学生 250 名）。参加度と成績が上がった一方、「13% cited time pressure as stressful」。
  - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC13459313/
  - 出典日付: 2026-08-10
  - 確度: 高
- 公式（検索要約）: Quizlet Match は誤マッチ 1 回ごとに 1 秒加算。
  - URL: https://help.quizlet.com/hc/en-us/articles/360031183611-Playing-Match
  - 出典日付: 記載なし
  - 確度: 低（ヘルプは 403）
- 声（学習アプリ外）: マッチ系ゲームのタイマー。「The timer is very STRESSFUL」。ストレスとやみつきの両面で語られる。
  - URL: https://larrybtoys.itch.io/match-panic/comments
  - 出典日付: 記載なし
  - 確度: 低（検索要約のみ）
- 声: ぼくらの瞬間英作文。「「日本語→英語で考える→回答を見る」の流れがシンプルで使いやすく、隙間時間に学習しています。」タイマーやゲーム要素に触れた口コミは見つからなかった。
  - URL: https://eigoto.jp/bokurano-shunkan-eisakubun/
  - 出典日付: 2023-12-20（記事）
  - 確度: 中
- Duolingo の Combo Bonus は「ポイント・XP」の節を参照（確度 低）。
- 日本語の声の薄さ: コンボ・時間制限への日本語の賛否はほぼ見つからなかった。もじあった（文字パズル）のレビューは英訳でしか取れていない（https://apps.apple.com/jp/app/%E3%82%82%E3%81%98%E3%81%82%E3%81%A3%E3%81%9F/id1661235840 、2023-01-13、確度 低）。

### マイクロフィードバック（その場の演出）

- 研究: 事前登録の n=1,699 のオンライン実験。成否に連動したフィードバックはすべての動機を高め、演出の増幅はかえって下げた。「Success dependence enhanced all motives, while amplification unexpectedly reduced them, possibly because the tested condition unintentionally impeded players' sense of agency.」
  - Kao, Ballou, Gerling, Breitsohl, Deterding (CHI 2024)
  - URL: https://people.csail.mit.edu/dkao/pdf/3613904.3642656.pdf
  - 出典日付: 2024
  - 確度: 高
- 研究: juicy 版は主観的な品質評価を上げたが、スコアは下がった（40,340 対 49,682）。認知負荷の可能性。
  - Juul & Begy, Good Feedback for bad Players?
  - URL: https://www.academia.edu/28934462/Good_Feedback_for_bad_Players_A_preliminary_Study_of_juicy_Interface_feedback
  - 出典日付: 記載なし
  - 確度: 低（検索スニペットのみ。原典は 403）
- 公式: ストリーク延長時のアニメーション。「seeing these animations increased the likelihood a brand new learner was still using Duolingo 7 days later by +1.7%」。
  - URL: https://blog.duolingo.com/how-duolingo-streak-builds-habit
  - 出典日付: 2022-01-31
  - 確度: 高
- 公式: 1 週・1 ヶ月・100 日・1 年の節目で Duo が不死鳥になる演出。「more people are keeping their streaks alive, celebrating their milestones」。定量効果は示していない。
  - URL: https://blog.duolingo.com/streak-milestone-design-animation
  - 出典日付: 2022-01-21
  - 確度: 中
- 第三者: 正解時は小さく羽ばたき、節目では回転する。演出の強さを出来事の大きさに合わせて段階づけている。「Whether it's a subtle wing flap when you ace a quiz or a triumphant spin when you cross a milestone, every micro-movement celebrates progress.」
  - URL: https://60fpsdesign.substack.com/p/fun-in-every-frame
  - 出典日付: 2024-12-29
  - 確度: 中
- 公式・声: mikan は点数に関係なく褒める。公式「どんな点数でも励ましてくれるので楽しく勉強できます」（https://apps.apple.com/us/app/-/id920856839 、記載なし、確度 高）。声「正解が0問でも、「よっ、奇才！」などと褒めてくれて」（https://note.com/yuzakana_lang/n/n77406cc8ddf3 、2025-04-18、確度 高）。
- 声: mikan は演出の派手さより操作の軽さ。「動きもスムーズなので、簡単な操作で気軽に単語学習できた」。
  - URL: https://eigoto.jp/mikan/
  - 出典日付: 記載なし
  - 確度: 中
- 公式（基準）: 操作をきっかけに動くアニメーションは、必須でない限り無効にできるべき（WCAG 2.2 SC 2.3.3、レベル AAA）。「some users experience distraction or nausea from animated content」。
  - URL: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
  - 出典日付: 記載なし
  - 確度: 高
- 第三者: Duolingo には効果音のオンオフがある。「レッスン中に鳴る正解・不正解時などのサウンドを抑えて学習できます」。
  - URL: https://chakomori.xsrv.jp/duolingo-sound-off/
  - 出典日付: 2026-08-27
  - 確度: 中
- 第三者: Duolingo のアニメーション設定は Web と Android はトグル、iOS は OS の Reduce Motion に従う。
  - URL: https://support.duolingo.com/hc/en-us/articles/360058189572-How-do-I-enable-disable-animations-
  - 出典日付: 記載なし
  - 確度: 低（検索スニペットのみ。公式ヘルプは移転していて未確認）
- 第三者: Duolingo のキャラクターは状態（待機・正解・不正解）の集まりとして作られている（Rive のステートマシン）。
  - URL: https://dev.to/uianimation/how-duolingo-uses-rive-for-their-character-animation-and-how-you-can-build-a-similar-rive-mascot-5d19
  - 出典日付: 記載なし
  - 確度: 低（公式の一次資料ではない）
- 声: 日本語の「うざい」系の不満は、メール・広告・キャラクターの表情・ライフ制に向いていた。「毎レッスン終わるたびに有料プランの広告が表示される」。正解時の効果音やエフェクトへの不満は出てこない。
  - URL: https://coco-english-109.com/duolingo-annoying/
  - 出典日付: 記載なし
  - 確度: 中
- 研究: Deci ら 1999（上記）。情報を伝えるポジティブなフィードバックは動機を上げる。有形の報酬は大学生より子どもで悪影響が大きい。「Tangible rewards tended to be more detrimental for children than college students」。
- 日本語の声の薄さ: 演出そのものへの日本語の反発（うるさい・子どもっぽい）は、探したが原文で確認できなかった。

### 進捗の可視化

- 公式: Studyplus の自社調査（ユーザー 5,977 名）。使って良かったこと「モチベーションが上がった」67.9%。その理由「自身の勉強時間がグラフで見えるようになったため（80.7%）」。
  - URL: https://prtimes.jp/main/html/rd/p/000000196.000047308.html
  - 出典日付: 2023-06-05
  - 確度: 中（自社調査。やめた人の声は含まれない）
- 声（Studyplus、APPLION 経由）:
  - 「これまでの勉強の合計を見ると自分こんなにやってるんだ…と嬉しくなれる」（2025-05-17）
  - 「グラフで自分の1日の勉強時間が表示されるので、どれくらい1日に自分が勉強したのかが一目瞭然でわかります」（2023-01-14）
  - 「やらないと数値は減るし、やったら数値は増えるんです」（2021-03-16）
  - URL: https://applion.jp/iphone/app/505410049/review/
  - 確度: 中
- 声（Forest、APPLION 経由）: 「植えられた木によって視覚的に把握できて達成感があります」。
  - URL: https://applion.jp/Forest/iphone-866450515/review/
  - 出典日付: 2021-08-03
  - 確度: 中
- 第三者: abceed は問題を解くたびに AI の予測 TOEIC スコアが更新され、スコアが上がるのが楽しくて続くという声が多いとレビュー記事は評する。
  - URL: https://word-sprint.app/blog/abceed-review
  - 出典日付: 2026（記事表記「2026年最新」）
  - 確度: 中
- 公式: InstaEnglish は WPM、即時フィードバック、使えた語を数える「アクティブ語彙」を 2,000 語の目標に向けて表示する。「答えも一つに決まっておらず、意味が伝わればOKのスタイル」。
  - URL: https://www.insta-english.net/
  - 出典日付: 記載なし
  - 確度: 中
- 第三者（まとめ記事が要約した声）: スタディサプリ ENGLISH は学習時間や履歴が見えること、通知が来ることが継続の理由。「通知でサボりを防げた」。
  - URL: https://eikaiwa.gakumado.mynavi.jp/studysapuri-english-reviews/
  - 出典日付: 2026-08-15
  - 確度: 中
- 声: Anki の年間ヒートマップ拡張が動機づけとして紹介されている。「色の濃さはその日復習したカードの枚数で決まります」。
  - URL: https://note.com/anki_man/n/n1e4487776d2c
  - 出典日付: 2025-05-09
  - 確度: 中
- 第三者（反例）: DotHabit では未達成の日が無色のドットとして溜まる。「達成しなかったことを示す無色のドットばかり増えていき、それを見ていると、継続できない自分に少し残念な気持ちになってきてしまった」。
  - URL: https://minchalle.com/blog/best-apps-to-build-habits
  - 出典日付: 記載なし（タイトルに 2026 年）
  - 確度: 中（競合の運営が書いた記事なので偏りがありうる）
- 公式: スタディサプリ ENGLISH 新日常英会話が打ち出す継続の仕組みは、ドラマ仕立てのストーリーと「1回最短3分から」のレッスン。バッジやランキングの記述はない。
  - URL: https://eigosapuri.jp/conversation/daily/
  - 出典日付: 記載なし
  - 確度: 高
- 研究: 内発的動機へのメタ分析で、有能感への効果が最も弱い（0.277）。自律性 0.638、関係性 1.776。
  - URL: https://link.springer.com/article/10.1007/s11423-023-10337-7
  - 出典日付: 2024
  - 確度: 中（本文は認証リダイレクト）

### 強い報酬（RPG・キャラ育成・ガチャ・損失の演出）

- 第三者: えいぽんたん！は学習で得たおやつでキャラを育成する。筆者は 4 ヶ月続き、「続く」は本当だと報告（個人の体験）。
  - URL: https://www.eigonou.net/16580/
  - 出典日付: 2015-06-24
  - 確度: 中
- 第三者: 「『続く英語学習』のウリ文句にウソはなさそう」。
  - URL: https://yuchrszk.blogspot.com/2014/08/blog-post_21.html
  - 出典日付: 2014-08-21
  - 確度: 中
- 声: えいぽんたん！の終了を惜しむ声。前身アプリからの友達とのつながりが続いていた。2019-12-17 に終了（検索要約）。
  - URL: https://applion.jp/iphone/app/592674216/review/5271782275/
  - 出典日付: 2019-12-14
  - 確度: 中（取得ツールは英訳の要約のみ返した。原文未確認）
- 第三者: 英語物語はバトル形式。「正解すれば味方が敵に攻撃でき、不正解だと敵から一方的に攻撃されてしまう」。強いキャラはガチャで得る。課金で報酬やガチャ確率が上がる。
  - URL: https://yuzuka-note.com/english-story
  - 出典日付: 2023-09-24
  - 確度: 中
- 第三者: 英語物語は「ついついプレイしたくなる仕掛けがたくさんある」。間違えた問題を一覧で見て苦手を把握できる。
  - URL: https://ushikubou.com/english-eigomonogatari-review
  - 出典日付: 2023-05-01
  - 確度: 中
- 声（英語物語、App Store、要約経由）: 「普段の英語学習の合間の休憩を使いゲームをしながら英語を学べている」。評価 4.7（1.7 万件）。全ステージをクリアすると続ける理由がなくなる、上級者との格差、プレイヤー減少という不満も。
  - URL: https://apps.apple.com/jp/app/id805477882?see-all=reviews
  - 出典日付: 記載なし
  - 確度: 低
- 公式: Pokemanki（Anki アドオン）はデッキごとにポケモンを割り当て、学習で進化する。「As you learn and review the cards in that deck, your Pokémon will level up and may even evolve!」どの指標でレベルが上がるかは書かれていない。
  - URL: https://github.com/sivenchinniah/Pokemanki
  - 出典日付: 記載なし
  - 確度: 高
- 声（Forest、損失の演出）: 「あ、やめとこ。って勉強に戻れます。木が枯れてしまうからやめとこう」（2021-05-01）。「途中で別アプリを開くと木が枯れてしまうのがすごい嫌な気分になり、スマホいじるのやめようと」（2022-09-20）。
  - URL: https://applion.jp/Forest/iphone-866450515/review/
  - 確度: 中
- 第三者（効果の減衰）: Forest は 3〜4 週目には木が十分に溜まり、1 本枯れても気にならなくなる。「You have enough trees that one dead one barely registers. The guilt dissolves.」
  - URL: https://screentimeindex.com/posts/forest-app-review/
  - 出典日付: 2026-07-18
  - 確度: 低（レビュー 1 件の主観）
- 第三者（ピアの継続装置）: みんチャレは匿名 5 人チームで毎日報告して褒め合う。「少人数では報告の間隔が空いて継続率が落ち、多人数では「社会的手抜き」が起きる」。70% が 21 日以上続いたとする。
  - URL: https://www.tekural.com/lab/minchalle-peer-support-habit-teardown
  - 出典日付: 記載なし
  - 確度: 中（公式の原典は未確認）
- 第三者: Duolingo の無料版はハート（ライフ）制で学習が約 15 分に制限される不満、自動課金への不満。75 人の口コミで肯定 36 / 否定 39。「ゲーム感覚で続けられた」。
  - URL: https://resemom.jp/mitsukaru-eikaiwa/duolingo-kuchikomi/
  - 出典日付: 記載なし
  - 確度: 中
- 研究: Sailer & Homner 2020（下記）は、行動面の効果の調整変数として「inclusion of game fiction and social interaction were significant moderators」を挙げる。物語と社会的相互作用は効きうる。

### 研究（全体の効果・自己申告と報酬）

効果の大きさ:

- Sailer & Homner (2020) Educational Psychology Review。「significant small effects of gamification on cognitive (g = 0.49), motivational (g = 0.36), and behavioral learning outcomes (g = 0.25)」。厳密な研究に絞ると、動機と行動は不安定。
  - URL: https://eric.ed.gov/?id=EJ1245270
  - 出典日付: 2020-03
  - 確度: 高
- Bai, Hew & Huang (2020) Educational Research Review。24 研究・3,202 人で成績 g=0.504。好まれた理由は熱意・成績のフィードバック・承認欲求・目標設定。嫌われた理由は追加の実益がないこと、不安や嫉妬。「gamification can cause anxiety or jealousy」。
  - URL: https://repository.eduhk.hk/en/publications/does-gamification-improve-student-learning-outcome-evidence-from-/
  - 出典日付: 2020-06
  - 確度: 高
  - 期間の調整分析（1〜3 ヶ月が最大 g=0.610、1 学期超でほぼゼロか負）は検索要約のみ。https://www.sciencedirect.com/science/article/abs/pii/S1747938X19302908 （確度 低）
- Zeng, Sun, Looi & Fan (2024) BJET。22 の実験研究で成績 「Hedges's g = 0.782, p < 0.05」。
  - URL: https://eric.ed.gov/?id=EJ1443146
  - 出典日付: 2024-11
  - 確度: 高
- Kim & Castelli (2021)。18 研究で行動 d=0.48。1 時間未満 1.57、2〜16 週 0.39、1〜2 年 -0.20。「The novelty of the gamified elements is likely driving the effects.」
  - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8037535/
  - 出典日付: 2021
  - 確度: 高
- Li, Ma & Shi (2023) Frontiers in Psychology。全体 g=0.822。1 学期超（3.304）が 1〜3 ヶ月（0.519）より大きく、Kim & Castelli と逆向き。「the highest effect size (Hedges' g = 1.285) was seen in the 'mechanics + dynamics + esthetics' subcategory」。
  - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10591086/
  - 出典日付: 2023
  - 確度: 中
- 内発的動機へのメタ分析（ETR&D）。35 介入・2,500 人で g=0.257。「a significant but small effect size favoring gamified learning」。
  - URL: https://link.springer.com/article/10.1007/s11423-023-10337-7
  - 出典日付: 2024
  - 確度: 中

自己申告と報酬:

- Mazar, Amir & Ariely (2008) と事前登録の追試（Verschuere et al. 2018）。成績を自己申告させ申告分だけ払うと、人は自己イメージを保てる範囲で水増しする。1 問 $0.50 と $2 で水増しの程度に差はなかった（Study 2、検索要約のみ）。道徳を思い出させると不正が減るという元の結果は、追試で再現されなかった。
  - URL: https://journals.sagepub.com/doi/10.1177/2515245918781032
  - 出典日付: 2018
  - 確度: 中
- Fischbacher & Föllmi-Heusi のサイコロ申告パラダイム（後続研究の要約経由）。検証できない自己申告に報酬がつくと、平均すると嘘をつくが最大限には偽らない。嘘で得られる利得のうち、実際に取るのは平均約 1/4。
  - URL: https://ideas.repec.org/a/spr/jecrev/v75y2024i2d10.1007_s42973-023-00139-0.html
  - 出典日付: 2024
  - 確度: 中
- 第三者（SRS の自己採点）: 報酬がなくても自己採点は甘くなる。理由は、忘れたと認めるのがつらいこと、溜まった復習を早く終わらせたいこと。「it is painful to admit defeat. Forgetting a character or word that we really ought to know means that we have failed」。
  - Hacking Chinese
  - URL: https://www.hackingchinese.com/about-cheating-spaced-repetition-and-learning-chinese/
  - 出典日付: 2014-09-04
  - 確度: 高

## グレーゾーン・未確認

公式の主張と独立した根拠の区別:

- ストリーク・猶予・演出の定量効果は、すべて Duolingo 自社の発表。第三者の再現はない。測っているのは継続率・DAU で、学習成果ではない。
- 7 日ストリークで 3.6 倍・2.4 倍といった数値は相関で、選抜効果と区別されていない。
- Studyplus の 80.7% は自社調査で、継続中のユーザーに偏る。
- BizSprinto の比較記事は、自社製品を宣伝する立場の書き手による。DotHabit の体験談は、競合（みんチャレ）の運営ブログ。

食い違い:

- 期間と効果の関係が研究間で逆向き。Kim & Castelli、Bai ら（要約）は長いと低下、Li ら は長いと増大。
- Duolingo のフリーズの効果。公式ブログ（2022）は +0.38% のみ。「離脱 21% 減」は二次記事にしかない。フリーズ枚数 1→2 の実験結果もポッドキャスト要約経由のみ。
- note『私がDuolingoを2370日で止めた理由』の日付が、セルによって 2025-01-21 頃と 2025-05-06 に分かれた。

採用しなかった数値（原典が見つからない）:

- リーグの効果「レッスン完了 +25%」（二次記事のみ）。
- iOS ウィジェットでコミットメント +60%（検索要約のみ）。
- 「連続日数で記録する人は 1 日休むと 63% 放棄しやすい（2020 年研究）」「CHI 2020 でストリーク不安が離脱の主因」（ブログ・検索要約のみ）。
- 「ペンシルバニア大学の研究で、24 時間以内に再開すると 71%」（原典不明）。
- スタディサプリの継続率 92%（定義不明、原典未確認）。

調べたが見つからなかったもの:

- 要素（ポイント・バッジ・ストリーク）ごとの単独の効果量を示すメタ分析。
- ストリークの学習効果（学力）に関する査読研究。
- 猶予が学習習慣そのものを守るのか、アプリへの滞在を守るだけなのかを区別した研究。
- 学習アプリの自己採点（○×の自己申告）にゲーム報酬を結びつけたときの水増しを直接測った研究。根拠は金銭報酬の実験からの類推にとどまる。高い誘因ほど不正が増えるとする反対の研究（JEBO 2017）は 403 で読めなかった。
- 自己申告の採点とゲーム報酬を組み合わせた日本の英語アプリの例。
- 自己採点型の学習で、その場の演出が学習効果に与える影響を調べた研究。コンボや自己ベスト更新の演出を学習面で評価した研究。
- Duolingo のレッスン中のコンボ・効果音・正解アニメの効果データ（公式が出しているのはストリーク演出だけ）。ジェム（通貨・ショップ）の効果データ。
- 報酬のために○を甘くつけるという日本語の声。
- 演出を「子どもっぽい」「うるさい」とする日本語の声（X の投稿は 402 で開けなかった）。
- mikan のランキングへの日本語の賛否。
- ストリークが途切れた後に離脱した・罪悪感が出たという日本語の声は、スタディサプリ・mikan・abceed では見つからなかった。Duolingo と自作アプリの note 数件のみ。
- えいぽんたん！・英語物語の継続率や学習効果の定量データ。えいぽんたん！の終了理由。
- abceed に連続日数・ランキング・バッジがあるか。Studyplus・Forest にストリークや猶予があるか。Pokemanki のレベルがどの指標で上がるか。

未確認のまま使っている記述:

- Hanus & Fox 2015、Mekler 2017 は検索要約のみで、要旨の原文を取得できていない。
- Quizlet Match の 1 秒加算、Duolingo のアニメーション設定、Combo Bonus の XP 値、Juul らの数値は検索スニペットのみ。
- App Store の声の一部（英語物語、えいぽんたん！、もじあった）は取得ツールの要約・英訳経由。逐語ではない。
- スタディサプリ ENGLISH の声は、まとめ記事が要約・引用したもの。
- 今回の調査は App Store / Google Play の日本語レビューと X を体系的には取得していない。日本語の声の量は、その分だけ過小に見えている可能性がある。

### 取得できなかったページ

- https://www.duolingo.com/help/leaderboards-and-league（本文を取得できず）
- https://www.duolingo.com/help/what-is-a-streak（本文を取得できず）
- https://blog.duolingo.com/widget-feature（未取得）
- https://support.duolingo.com/hc/en-us/articles/360058189572（duolingo.com/help へリダイレクト、未取得）
- https://www.getrecall.ai/... Lenny's Podcast 要約（リダイレクト先に該当内容なし）
- mikan ヘルプ「ポイント付与の仕組み」ページ（未取得）
- https://studystudio.jp/contents/archives/53810（未取得）
- https://www.eicommu.net/free-study/eipontan/（証明書エラー）
- https://e-note.jp/eigomonogatari（404）
- https://englishhub.jp/app/englishstory.html（口コミ未掲載）
- https://help.quizlet.com/hc/en-us/articles/360030988091-Studying-with-Match（403）
- https://ankiweb.net/shared/info/1771074083（本文が空）
- https://ankiweb.net/shared/info/579111794（本文が空）
- https://x.com/onotakashi/status/1853831683373773141（402）
- https://dl.acm.org/doi/fullHtml/10.1145/3613904.3642656（403、MIT の PDF で代替）
- https://powerusers.codidact.com/posts/287683（403）
- https://forum.duome.eu/viewtopic.php?t=3311（ログイン画面）
- https://medium.com/@HHintze/an-easy-way-to-kill-animations-in-the-duolingo-app-b4b7863ed8e（403）
- https://duolingo.hobune.stream/comment/47101433 と /55408974（本文が読み込まれない）
- https://support.khanacademy.org/hc/en-us/articles/360015623271（403）
- https://duolingo.fandom.com/wiki/XP（402）
- https://www.academia.edu/28934462（403）
- https://www.hardreset.info/devices/apps/apps-duolingo/disable-animations/（403）
- https://link.springer.com/article/10.1007/s10648-019-09498-w（Sailer & Homner 本文、認証リダイレクト）
- https://www.sciencedirect.com/science/article/abs/pii/S1747938X19302908（Bai ら、403）
- https://www.researchgate.net/publication/265644737（Hanus & Fox、403）
- https://link.springer.com/article/10.1007/s11423-025-10493-y（要素組み合わせのメタ分析、認証リダイレクト）
- https://link.springer.com/article/10.1007/s11423-023-10337-7（内発的動機のメタ分析、認証リダイレクト）
- https://www.medrxiv.org/content/10.1101/2024.12.26.24319676.full.pdf（途切れたランニングストリークの研究、403）
- https://www.sciencedirect.com/science/article/abs/pii/S0167268117300872（高い誘因と不正、403）
- https://www.nature.com/articles/s41598-022-06072-3（金銭誘因と不正、認証リダイレクト）
- https://bruehlmann.io/publication/mekler-towards-2017/（不審なドメインへリダイレクトされたため開かなかった）
- https://apps.apple.com/jp/app/forest-集中-勉強タイマー/id866450515?see-all=reviews（未取得。APPLION で代用）
- App Store / Google Play の日本語レビューと X 全般（体系的な取得は試していない）

## 影響する論点

特定のアイデアの決定はここに書かない。次のような判断の材料になる。

- 学習アプリで、報酬（ポイント・XP・レベル・称号・バッジ）をどこまで入れるかを決めるとき。特に、成績を自己申告させる形式で、報酬を何に結びつけるか（正答数か、完了か、継続か）。
- ストリークを入れるか、入れるなら延長条件と猶予・修復をどう設計するかを決めるとき。
- ランキング・リーグ・対戦など、他人との比較を入れるかを決めるとき。
- その場の演出（正解時の反応・コンボ・効果音）の強さと、オフにできる設定の範囲を決めるとき。
- 継続の見せ方を、日数（ストリーク）・量の累計・実力の代理指標のどれに寄せるかを決めるとき。
- 制限時間を入れるか、緩められるようにするかを決めるとき。

参照先の例:

- `docs/plan/instant-composition-app/open-questions.md` の「ゲーム的な演出の中身」「報酬の上限（ポイント・レベル・称号を入れるか）」
