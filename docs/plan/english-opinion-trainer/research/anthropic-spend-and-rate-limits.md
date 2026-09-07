# Anthropic の支出上限・レート制限と API キーの保護手段

- 調査日: 2026-09-07
- 調査手段: Sonnet サブエージェント 1 体 + メインによる原文確認（rate-limits ページを直接取得）
- 問い: 他人に URL を配る小さな公開アプリで、Anthropic の API キーを守る手段として公式に何が用意されているか。

## 結論

ベンダー側に用意されているのは **「組織」と「ワークスペース」の 2 層だけ**。API キー単位の支出上限もレート制限も存在しない。キーに設定できるのは有効期限とワークスペースへの紐付けだけで、IP 制限・リファラー制限・エンドポイント単位の権限スコープはない（IP 許可リストは存在するが Enterprise プラン限定・組織単位）。

したがって「利用者 1 人につき小額上限つきのキーを 1 本配る」という形は取れない。不特定多数に URL を配るなら、**レート制限と不正利用対策はサーバーレス関数側の自前実装になる**。ベンダー側の上限は最後の砦として働くが、リクエスト元を区別しないので、1 人の乱用で全員が止まる。

なお、上限到達時のエラーは 2 種類あり、取り違えると原因を誤診する。ティアの自動施行上限は 429、自分で設定した上限は 400。

## 根拠

### 上限の 2 層構造

- 事実: "There are two types of limits: 1. **Spend limits** set a maximum monthly cost an organization can incur for API usage. 2. **Rate limits** set the maximum number of API requests an organization can make over a defined period of time." / "The API enforces service-configured limits at the organization level, but you may also set user-configurable limits for your organization's workspaces."
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし（ページに更新日表示なし）
  - 確度: 高（メインが原文確認）

### 上限到達時の挙動（2 種類ある）

- 事実: ティアの月間上限に到達すると **HTTP 429**。"Once you reach your tier's spend cap, API usage pauses until 00:00 UTC on the first day of the next month, unless you request a higher limit sooner. While usage is paused, API requests return HTTP 429" — エラー型は `rate_limit_error`、`error.details.error_code` は `enforced_spend_limit_reached`。"the response has no `retry-after` header. Retrying, including the SDKs' automatic retries, fails until access resumes."
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認）
- 事実: 自分で設定した上限に到達すると **HTTP 400**。"When usage reaches a spend limit you set, requests return HTTP 400 with error type `invalid_request_error`. The message begins `You have reached your specified API usage limits`, or `You have reached your specified workspace API usage limits` for a workspace limit"
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認）

### ワークスペース単位でできること

- 事実: "To protect Workspaces in your Organization from potential overuse, you can set custom spend and rate limits per Workspace." 注意書きとして "You can't set limits on the default Workspace." / "If not set, Workspace limits match the Organization's limit." / "Organization-wide limits always apply, even if Workspace limits add up to more."
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認）
- 事実: ワークスペースの支出上限画面には閾値アラートがある。"Spend limits: Cap monthly spending and configure alerts when spending reaches certain thresholds"
  - URL: https://platform.claude.com/docs/en/manage-claude/workspaces
  - 出典日付: 記載なし
  - 確度: 高

### API キー単位の上限は存在しない

- 事実: rate-limits ページ全体を通して「API キー単位の支出上限」「API キー単位のレート制限」という概念が一度も登場しない。レスポンスヘッダーの説明も "The `anthropic-ratelimit-tokens-*` headers display the values for the most restrictive limit currently in effect"（組織かワークスペースのいずれか）としており、キーは制限の単位として扱われていない。
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 中（不在の確認は「言及がない」ことに基づく推論。ただしメインが全文を確認済み）
- 事実: Admin API の Retrieve API Key が返す APIKey オブジェクトのフィールドは `id, created_at, created_by, expires_at, name, partial_key_hint, principal, scope, status, type, workspace_id` のみで、支出上限・レート制限に相当するフィールドがない。
  - URL: https://platform.claude.com/docs/en/api/admin/api_keys/retrieve
  - 出典日付: 記載なし
  - 確度: 高（フィールドが列挙されたうえで存在しない、という直接証拠）

### API キーに設定できること

- 事実: 有効期限を設定できる。"you choose an expiration: a preset (3 hours, 1 day, 7 days, or 30 days), a custom duration, or **Never**" / "After a key expires, requests made with it return a `401 authentication_error`. Create a new key to restore access; expired keys cannot be reactivated."
  - URL: https://platform.claude.com/docs/en/manage-claude/authentication
  - 出典日付: 記載なし
  - 確度: 高
- 事実: キーの `scope` は `{"type":"workspace","workspace_id":...}` か `{"type":"organization"}` のみ。権限は紐づく principal（ユーザーまたはサービスアカウント）から継承する。"Personal keys and service account keys are identity-backed: each belongs to a user or service account your organization already manages, and every request acts as that identity."
  - URL: https://platform.claude.com/docs/en/manage-claude/authentication
  - 出典日付: 記載なし
  - 確度: 高
- 事実: IP 許可リストは存在するが Enterprise プラン限定・組織単位。"IP allowlisting enables Enterprise plan administrators to control which IP addresses can access Claude through their organization." 有効化は営業・サポート経由で CIDR レンジを渡す運用。
  - URL: https://support.claude.com/en/articles/13200993-restrict-access-to-claude-with-ip-allowlisting
  - 出典日付: 記載なし（"Updated this week" とのみ表示）
  - 確度: 中（存在は確実だが、pay-as-you-go の API キーに及ぶかは不明。グレーゾーン参照）

### ティアと、このアプリに効く実数値

- 事実: 月間支出上限は Start $500 / Build $1,000 / Scale $200,000。"Organizations on the Custom tier have no monthly spend cap"
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認、既存の landscape の記録と一致）
- 事実: **新規アカウントは Start より下の Evaluation ティアから始まることがある。** "New organizations and organizations with limited usage history may start in the Evaluation tier, with limits below the standard limits shown on this page while account history is established... they increase automatically as your organization builds usage history."
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認）
- 事実: Haiku 4.5 の Start ティアのレート制限は 1,000 RPM / 2,000,000 ITPM / 400,000 OTPM。
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認）
- 事実: 上限引き上げの申請は "you can request them there once you're using at least 50% of your current limits."
  - URL: https://support.claude.com/en/articles/8243635-our-approach-to-rate-limits-for-the-claude-api
  - 出典日付: 2026-06-26（ページ内表記）
  - 確度: 中（サポート記事。より新しい docs 側には同じ 50% 条件の明記が見当たらず、古い記述の可能性）

### 監視

- 事実: Usage & Cost Admin API がある。"Filter by API key, workspace, model, service tier, context window, data residency, or speed" — **API キー単位での使用量・コスト集計は可能**。
  - URL: https://platform.claude.com/docs/en/manage-claude/usage-cost-api
  - 出典日付: 記載なし
  - 確度: 高
- 事実: Console の Usage ページにレート制限のチャート（Rate Limit - Input Tokens / Output Tokens）がある。
  - URL: https://platform.claude.com/docs/en/api/rate-limits
  - 出典日付: 記載なし
  - 確度: 高（メインが原文確認）

## グレーゾーン・未確認

- **IP 許可リストが pay-as-you-go の API キー経由のリクエストにも適用されるか**: 調べたが分からなかった。サポート記事は「Enterprise プラン管理者が組織を通じた Claude へのアクセスを制御する」としか書いておらず、claude.ai のログイン限定なのか platform.claude.com の API 認証にも及ぶのかを区別する記述が見つからない。いずれにせよ Enterprise 限定なので、今回の運用では使えない可能性が高い。
- **ティア自動昇格の具体的な閾値・期間**: 非公開。「利用実績とアカウントの健全性に基づき自動的に」としか書かれておらず、新規アカウントがいつまで Evaluation / Start の低い上限に留まるかは事前に見積もれない。
- **組織レベル（ワークスペースでなく）の閾値アラートが pay-as-you-go の Console にあるか**: 確認できたのは Claude Enterprise 向けのブログ記事（75% / 90% 通知、2026-07-02）のみで、API 課金側の docs には記述が見当たらない。Console の Billing 画面はログインが必要で今回は直接確認していない。
- **リファラー / ドメイン制限機能の有無**: 一次情報のどのページにも "referrer" や "domain restriction" に相当する語が登場しなかった。これは機能が存在しないことの積極的証拠ではなく、見つからなかったという消極的確認にとどまる。
- **「キー単位の上限がない」という結論そのもの**: 不在の確認である以上、文書化されていない機能がある可能性は排除できない。反証となる記述はどこにも見つからなかった、というのが到達点。
- 参照した Anthropic の docs ページはいずれも**更新日を表示していない**。したがってこのファイル全体の鮮度は「2026-09-07 に取得した」ということしか保証しない。

## 影響する論点

- `open-questions.md`「公開範囲と LLM 呼び出しの保護」— 直接効く。他人に配るなら自前のレート制限か入口が必須、という結論を裏づける。ベンダー側で使えるのは①ワークスペース単位の支出上限 + 閾値アラート、②ワークスペース単位のレート制限、③Usage / Cost API による後追い監視、④キーの有効期限による定期ローテーション、の 4 点のみ。
- `decisions.md` 2026-09-07「最初から従量課金の API キーで開発する」— 少額の支出上限は組織かワークスペースに掛ける形になる。ただし **default ワークスペースには上限を設定できない**ので、このアプリ専用のワークスペースを別に作る必要がある。
- `docs/landscape/2026-09-llm-apis.md` — 「上限到達で 400 または 429」の記述を、ティア自動施行 = 429 / 自分で設定 = 400 と書き分けられる。次回更新時の材料。
