# braintrust

プロダクトを作る前の「何を作るか」を壁打ちするための、Claude Code 専用リポジトリ。

主な対象は、AI を組み込んだアプリケーション全般。ベンダーや SDK は選定対象として扱う。
アイデアの整理、アプリとしての体験の構想、実現性と技術スタック候補の検討、
そもそも LLM が必要かの検討、エージェント構成の設計などを、PdM 兼 CTO のような
相談相手として対話しながら詰めていく。

## ここでやらないこと

- 実装。プロトタイプも置かない
- 決定を代行すること。指摘と選択肢の提示までで、決めるのは人間

## 構成

- `AGENTS.md` — 壁打ち相手としての原則
- `docs/plan/` — アイデアごとのディレクトリ。索引は `docs/plan/README.md`、書式は `_templates/`
- `docs/landscape/` — LLM / エージェント基盤の前提知識。日付つきで、古くなったら取り直す
- `docs/decisions.md` / `docs/open-questions.md` — このリポジトリ自体の運用の決定と未決
- `.claude/skills/` — 局面ごとの進め方
  - `intaking-ideas` — 新しいアイデアを受け取る
  - `shaping-experience` — 体験の構想と実現性・技術スタック候補
  - `recording-research` — 出典つきで調査を残す
  - `assessing-ai-architecture` — LLM の要否と構成、ベンダーの比較
  - `handing-off-plans` — 実装へ進むときの引き継ぎ

## 名前の由来

Pixar の Braintrust。未完成のものを持ち込んで率直なフィードバックを受ける場で、
「問題は指摘するが、解決策を押し付けず、決定権は作者に残す」のがその原則。
