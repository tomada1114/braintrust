# オーナーが実装前にやること

handoff.md を引き継ぐ前に、オーナー自身が行う作業。終わったら状態を更新する。
作成日: 2026-09-21

| # | やること | 補足 | 状態 |
| --- | --- | --- | --- |
| 1 | Apple Developer Program に加入する | 実装と検証を始める時点で加入済みの前提(decisions.md 2026-09-21)。署名と公証、Homebrew への登録に必要。開発中もアクセシビリティ権限をビルドをまたいで保つのに効く見込み | 後回し(2026-09-22)。検証 6 の署名と権限は加入後に再検証 |
| 2 | GitHub で `hintjump` のリポジトリ名(と必要なら組織名)を確保する | 調査時点では未使用(research/app-name-collisions.md)。取られる前に | 済(2026-09-22、public で作成: github.com/tomada1114/hintjump) |
| 3 | ドメインを取るなら `hintjump.com` / `.app` / `.dev` を確認して取得する | 調査時点では DNS レコードなし。取るかどうか自体は任意 | 未 |
| 4 | macos-app-template から新しいリポジトリを作り、`scripts/bootstrap.sh Hintjump --bundle-id-prefix <prefix> --github-user <user> --author "<name>" --email <email>` を実行する | テンプレート本体には入れない。手順はテンプレートの README「Using This Template」 | 済(2026-09-22、bundle ID 接頭辞 io.github.tomada1114) |
| 5 | 新しいリポジトリで `just install && just check` が通ることを確認する | テンプレートの手順 3 | 済(2026-09-22) |
| 6 | 署名と公証の secrets を新しいリポジトリに設定する | テンプレートの `docs/distribution.md`。1 の加入後 | 未 |
| 7 | ~~`docs/plan/keyboard-nav-mac/` を新しいリポジトリにコピーする~~ | 取りやめ。計画ディレクトリは持ち込まない(braintrust の docs/decisions.md 2026-09-22)。必要な内容は公開して困らない形に書き直して Issue に載せる | 不要 |
| 8 | 計画ディレクトリを公開リポジトリに含めるか決める | 含めないと決定(2026-09-22) | 済 |
| 9 | handoff.md を元に、公開して困らない形に書き直した Issue を新しいリポジトリに切って始める | 最初の作業は handoff.md「最初にやる検証」の 6 つ | 未 |

任意

- 商標データベース(USPTO など)で Hintjump を照会する。調査では行っていない
- Homebrew が未署名・未公証の cask を受け付けないという記述を、Homebrew 公式で確認する(テンプレートの docs/distribution.md の記述のみで未確認)
