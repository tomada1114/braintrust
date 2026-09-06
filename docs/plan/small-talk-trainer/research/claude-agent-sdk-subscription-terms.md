# Claude Agent SDK とサブスクリプション規約

- 調査日: 2026-09-06
- 調査手段: Sonnet サブエージェントによる Web 調査 + メインセッションによる原文確認
- 問い: Claude サブスク(Pro/Max)で Agent SDK を自作アプリから無料で使えるか。ChatGPT サブスクは同等のことができるか。

## 結論

技術的には `claude setup-token` で発行した OAuth トークンを使い、Agent SDK や `claude -p` から自作アプリでも Claude を呼び出せる。しかし規約上は、この OAuth 認証は「Claude Code や他の Anthropic 純正アプリケーションの通常利用」を支える目的に限定されており、サードパーティのプロダクト・サービスを作る開発者は API キー認証を使うべきとされている。加えて 2026-05-13 には Agent SDK / `claude -p` / サードパーティアプリの利用をサブスクの通常枠から切り離し月額クレジットに移す発表があり、施行日当日の 2026-06-15 に一時停止されたが、2026-09-06 時点で再開の続報はない。つまり「個人のローカル練習アプリ」がサブスク OAuth で無料利用を続けられるかはグレーゾーンであり、いつ変更されてもおかしくない状態。ChatGPT 側は Codex CLI / IDE 拡張 / デスクトップアプリで Plus/Pro の枠を "for local work" として使えるが、自作の別アプリでの利用可否は公式に明記されていない。

## 根拠

- 事実: `claude setup-token` で OAuth トークンを発行し、Agent SDK / `claude -p` から利用できる。
  URL: https://code.claude.com/docs/en/authentication
  出典日付: 確認 2026-09-06(ページ自体に更新日記載なし)
  確度: 高

- 事実: 規約原文に「Advertised usage limits for Pro and Max plans assume ordinary, individual usage of Claude Code and the Agent SDK.」「OAuth authentication is intended exclusively for purchasers of Claude Free, Pro, Max, Team, and Enterprise subscription plans and is designed to support ordinary use of Claude Code and other native Anthropic applications.」「Developers building products or services that interact with Claude's capabilities, including those using the Agent SDK, should use API key authentication ... Anthropic does not permit third-party developers to offer Claude.ai login into their own applications, or to route requests through Free, Pro, or Max plan credentials on behalf of their users.」とある。
  URL: https://code.claude.com/docs/en/legal-and-compliance
  出典日付: 確認 2026-09-06
  確度: 高

- 事実: 2026-05-13 に Agent SDK / `claude -p` / サードパーティアプリの利用をサブスクの通常枠から切り離し、月額クレジット(Pro $20、Max 5x $100、Max 20x $200、繰越・プール不可)に移す発表があったが、施行日の 2026-06-15 当日に一時停止された。原文: 「We're pausing the changes to Claude Agent SDK usage described below. For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription's usage limits.」
  URL: https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
  出典日付: ページ更新 2026-06-16、確認 2026-09-06
  確度: 高

- 事実: 2026-09-06 時点で、上記の一時停止の解除・再開についての続報は見つからなかった。
  URL: https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
  出典日付: 確認 2026-09-06
  確度: 中

- 事実: `claude -p` と Agent SDK は規約・課金方針のいずれの記述でも常に同列に扱われており、両者を別扱いする記述はない。
  URL: https://code.claude.com/docs/en/legal-and-compliance
  出典日付: 確認 2026-09-06
  確度: 高

- 事実: OpenAI の Codex CLI / IDE 拡張 / ChatGPT デスクトップは "Sign in with ChatGPT" で Plus/Pro の枠を使えるが、公式は "for local work" としており、自作の別アプリで使えるかは明記されていない。
  URL: https://learn.chatgpt.com/docs/auth
  出典日付: ページに日付記載なし、確認 2026-09-06
  確度: 中

- 事実: OpenAI Agents SDK は API キー認証のみとされる(DeepWiki 経由の二次情報)。
  URL: (二次情報、DeepWiki)
  出典日付: 確認 2026-09-06
  確度: 中

- 事実: OpenAI の利用規約原文は 403 でフェッチできず、二次情報のみで確認した。
  URL: (アクセス不可)
  出典日付: 確認 2026-09-06
  確度: 低〜中

- 事実: Gemini CLI は Google アカウントで無料枠(個人向け Code Assist 経由、1 日 1000 リクエスト / 60 rpm とされる)を使えるが、自作アプリへの転用可否は未確認。
  URL: https://geminicli.com/docs/resources/quota-and-pricing/
  出典日付: 確認 2026-09-06
  確度: 低

## グレーゾーン・未確認

「自分一人が使うローカルアプリ」が規約の言う "ordinary individual use" に含まれるのか、それとも "products or services" に当たるのかは条文が沈黙しており判断できない。また、別枠課金の一時停止は解除される可能性が高く、継続的なウォッチが必要。

## 影響する論点

- 決定 7(Claude Agent SDK に依存させない)
- モデル・ベンダーの選定(open-questions.md)
