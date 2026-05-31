# 検索結果: xfce4-appfinder Alt+F3 shortcut issue
クエリ: xfce4-appfinder keyboard shortcut not working Firefox focus XGrabKey IBus focus-out-hide toggle
取得日時: 2026-05-23 00:00

## 結果1
URL: https://docs.xfce.org/xfce/xfce4-appfinder/usage
取得状況: 成功（内容は最小限）
簡易スコア: 鮮度=Mid 関連性=Mid 深さ=Low 信頼性=High
内容:
- 公式ドキュメント。Collapsed Run Mode / Expanded Search Mode の説明のみ。
- キーボードショートカット設定の具体的手順は記載なし。
- "shortcuts only work if they are not used by the desktop environment or window manager" という注意書きが Firefox Help にも存在する。

## 結果2
URL: https://github.com/xfce-mirror/xfce4-appfinder/blob/master/NEWS
取得状況: 成功
簡易スコア: 鮮度=High 関連性=High 深さ=High 信頼性=High
内容:
- 4.18.0: Xfce 4.18 要件対応
- 4.19.0: "New option to toggle window visibility of background service" 追加
- 4.19.1: Ctrl+N / Ctrl+P によるツリービューナビゲーション追加
- 4.19.2: "Add new preference to close window when focus is lost" (focus-out-hide) 追加
→ focus-out-hide は 4.19.2 以降の機能。4.18.x には存在しない。

## 結果3
URL: https://gitlab.xfce.org/xfce/xfce4-appfinder/-/issues/52
取得状況: 成功
簡易スコア: 鮮度=High 関連性=High 深さ=Mid 信頼性=High
内容:
- Issue #52: トグル機能のリクエスト（2021年）
- 同一キーで開く・閉じるを実現する xdotool ベースのスクリプト例が提案されている
- TROMjaro ディストリビューションが既に実装済みとして参照されている

## 結果4
URL: https://bbs.archlinux.org/viewtopic.php?id=143932
取得状況: 成功
簡易スコア: 鮮度=Low 関連性=High 深さ=Mid 信頼性=Mid
内容:
- xfce4-appfinder がフォーカスを受け取らない問題
- 原因: "keep a running instance in the background" を有効にしていると、ウィンドウが表示されてもフォーカスされない
- 解決: その設定を無効化することで毎回正しくフォーカスされるようになった

## 結果5
URL: https://forums.opensuse.org/t/xfce-ibus-multilingual-keyboards-global-hotkey-problem/126613
取得状況: 成功（内容は限定的）
簡易スコア: 鮮度=Mid 関連性=High 深さ=Low 信頼性=Mid
内容:
- XFCE + IBus のグローバルホットキー問題: IME の言語レイアウト切り替えにより、ショートカットが別キーとして認識される
- KDE は自動的に英語レイアウトに切り替えてグローバルショートカットを処理するが、XFCE にはその機能がない

## X11 XGrabKey 技術調査
URL: https://tronche.com/gui/x/xlib/input/XGrabKey.html / X.org man page
取得状況: 検索のみ
簡易スコア: 鮮度=High 関連性=High 深さ=High 信頼性=High
内容:
- XGrabKey は passive grab（パッシブグラブ）を確立する
- 同一キーコンビネーションに対して複数クライアントが XGrabKey を呼ぶと BadAccess エラー
- AnyModifier / AnyKey の場合は競合があれば全て失敗
- Electron / Firefox はウィンドウ内で独自のキーイベント処理を行うが、X11 レベルの passive grab はウィンドウに関係なくルートウィンドウ上で動作するため、本来は競合しないはず

## Firefox Alt+F3 調査
URL: https://support.mozilla.org/en-US/kb/keyboard-shortcuts-perform-firefox-tasks-quickly
取得状況: 成功
簡易スコア: 鮮度=High 関連性=High 深さ=Mid 信頼性=High
内容:
- Firefox の公式ショートカット一覧に Alt+F3 は存在しない
- Firefox がタブを閉じるのは Ctrl+W / Ctrl+F4 が標準
- Alt+F3 でタブが閉じるのは Firefox ネイティブの動作ではない → 別の原因が疑われる
