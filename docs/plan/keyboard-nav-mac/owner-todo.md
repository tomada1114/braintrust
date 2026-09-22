# オーナーが実装前にやること

handoff.md を引き継ぐ前に、オーナー自身が行う作業。終わったら状態を更新する。
作成日: 2026-09-21

| # | やること | 補足 | 状態 |
| --- | --- | --- | --- |
| 1 | Apple Developer Program に加入する | 実装と検証を始める時点で加入済みの前提(decisions.md 2026-09-21)。署名と公証、Homebrew への登録に必要。開発中もアクセシビリティ権限をビルドをまたいで保つのに効く見込み | 未 |
| 2 | GitHub で `hintjump` のリポジトリ名(と必要なら組織名)を確保する | 調査時点では未使用(research/app-name-collisions.md)。取られる前に | 未 |
| 3 | ドメインを取るなら `hintjump.com` / `.app` / `.dev` を確認して取得する | 調査時点では DNS レコードなし。取るかどうか自体は任意 | 未 |
| 4 | macos-app-template から新しいリポジトリを作り、`scripts/bootstrap.sh Hintjump --bundle-id-prefix <prefix> --github-user <user> --author "<name>" --email <email>` を実行する | テンプレート本体には入れない。手順はテンプレートの README「Using This Template」 | 未 |
| 5 | 新しいリポジトリで `just install && just check` が通ることを確認する | テンプレートの手順 3 | 未 |
| 6 | 署名と公証の secrets を新しいリポジトリに設定する | テンプレートの `docs/distribution.md`。1 の加入後 | 未 |
| 7 | `docs/plan/keyboard-nav-mac/` を新しいリポジトリにコピーする | handoff.md、overview.md、experience.md、decisions.md、open-questions.md、research/、このファイル | 未 |
| 8 | 計画ディレクトリを公開リポジトリに含めるか決める | Homerow への率直な評価やオーナーの機材の話が入っている。含めないなら `.gitignore` で外す | 未 |
| 9 | 新しいリポジトリの最初のセッションに handoff.md を読ませて始める | 最初の作業は handoff.md「最初にやる検証」の 6 つ | 未 |

任意

- 商標データベース(USPTO など)で Hintjump を照会する。調査では行っていない
- Homebrew が未署名・未公証の cask を受け付けないという記述を、Homebrew 公式で確認する(テンプレートの docs/distribution.md の記述のみで未確認)
