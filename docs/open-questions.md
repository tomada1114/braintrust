# リポジトリ運用の未決の論点

決まったら decisions.md にエントリを足し、ここの状態を更新する。

## 5 つの skill それぞれの中身

- 何が決まれば決まるか: intaking-ideas / shaping-experience / recording-research / assessing-ai-architecture / handing-off-plans の各手順・出力・判断基準。実際に skill を書く段階で確定する
- 材料: AGENTS.md の skills 節（適用場面のみ記載）、`docs/plan/_templates/` の各テンプレート
- 状態: 決定済み（`.claude/skills/` 配下の 5 スキル。決定は `docs/decisions.md`）

## docs/landscape/ の更新頻度

- 何が決まれば決まるか: 3 ヶ月という目安が実運用に合うか。分野によって陳腐化の速さが違うなら、トピック単位で頻度を変えるかどうか
- 材料: 現状の運用ルール（最新ファイルが 3 ヶ月より古ければ更新を提案する）。実際に古い landscape を参照した回数と、そのとき困ったかどうか
- 状態: 未決（当面は 3 ヶ月目安で運用し、実績を見て見直す）

## handoff.md を特定の下流に合わせるか

- 何が決まれば決まるか: 卒業先で最初に何をするかが定まること。グローバル skill の refining-requirements の入力形式に寄せると受け渡しは滑らかになるが、その skill を使わない卒業先では余分な構成になる
- 材料: `docs/plan/_templates/handoff.md`（現状は汎用）、refining-requirements の入力要件
- 状態: 未決（最初の卒業が出るまで汎用で運用する）

## 「必ず推奨を出す」が議論を偏らせないか

- 何が決まれば決まるか: 実際の対話で、推奨がオーナーの結論をどれだけ引っぱるか。推奨に流された決定が続くようなら、推奨の出し方（確度の併記、対抗案の強めの提示など）を調整する
- 材料: 各アイデアの decisions.md に残る「却下した案」。推奨と実際の決定が一致し続けているかどうかで判断できる
- 状態: 未決（運用しながら観察する）
