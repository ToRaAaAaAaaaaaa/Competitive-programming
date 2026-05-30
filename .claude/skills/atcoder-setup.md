---
description: AtCoderコンテストフォルダを作成し、問題リンクと進捗ログをCLAUDE.mdに記録する。引数にコンテスト番号（例: ABC458）を渡す。引数がない場合はカレントディレクトリ名を使用する。コンテスト開始前に実行することを想定。
---

引数または現在のディレクトリ名からコンテスト番号を特定し、以下の手順を実行してください。

## 手順

### 1. コンテスト番号の確定
- 引数があれば使う（例: `ABC458`, `abc458` いずれも受け付ける）
- なければカレントディレクトリ名を使う
- 小文字に変換して `contest_id` とする（例: `abc458`）
- 表示用に大文字を `contest_name` とする（例: `ABC458`）
- コンテスト番号の数値部分を `contest_num` とする（例: `458`）

### 2. ディレクトリ作成
```
mkdir -p {contest_name}
```

### 3. CLAUDE.md の作成
`{contest_name}/CLAUDE.md` を以下の形式で作成する（既存の場合は上書き確認）:

```markdown
## 前提：学習サポートの姿勢
これは学習のための競技プログラミング練習です。以下の姿勢で接してください。

- **人間主導**：ユーザーが考え、実装する。Claudeはあくまでサポート役
- **答えを先に言わない**：解法・コードをいきなり出さない。詰まっている部分だけヒントを出す
- **気づきを促す**：「この部分の計算量はどうなりますか？」「この関数はご存知ですか？」など問いかけ形式で
- **知らない実装・関数の紹介はOK**：解答そのものではなく、使えるツールの紹介は積極的に
- **聞かれたら答える**：ユーザーが「わからない」「教えて」と言ったときは丁寧に説明する

問題や解説のリンクが必要なときは、このファイルの情報を使ってください。聞かれる前でも、問題番号や解説が話題になったら積極的にリンクを提示してください。進捗ログは作業の都度更新してください。

# {contest_name} - AtCoder Beginner Contest {contest_num}

## コンテスト情報
- コンテストページ: https://atcoder.jp/contests/{contest_id}
- 問題一覧: https://atcoder.jp/contests/{contest_id}/tasks
- 解説トップ: https://atcoder.jp/contests/{contest_id}/editorial

## 問題リンク
| 問題 | リンク |
|------|--------|
| A | https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_a |
| B | https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_b |
| C | https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_c |
| D | https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_d |
| E | https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_e |
| F | https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_f |
| G | https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_g |

## 解説リンク（コンテスト終了後に記入）
- 解説トップ: https://atcoder.jp/contests/{contest_id}/editorial

## 進捗ログ
| 問題 | 状態 | メモ |
|------|------|------|
| A | 未着手 | |
| B | 未着手 | |
| C | 未着手 | |
| D | 未着手 | |
| E | 未着手 | |
| F | 未着手 | |
| G | 未着手 | |

状態の種類: `未着手` / `取り組み中` / `AC` / `断念`
```

### 4. 解答ファイルの作成
`{contest_name}/` 直下に `a.py` 〜 `g.py` を作成する（すでに存在するファイルは上書きしない）。中身は空ファイル。

### 5. 完了報告
作成したファイルのパスを報告する。
