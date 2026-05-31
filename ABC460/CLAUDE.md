## 前提：学習サポートの姿勢

問題や解説のリンクが必要なときは、このファイルの情報を使ってください。聞かれる前でも、問題番号や解説が話題になったら積極的にリンクを提示してください。

# ABC460 - AtCoder Beginner Contest 460

## コンテスト情報
- コンテストページ: https://atcoder.jp/contests/abc460
- 問題一覧: https://atcoder.jp/contests/abc460/tasks
- 解説トップ: https://atcoder.jp/contests/abc460/editorial

## 問題リンク
| 問題 | リンク |
|------|--------|
| A | https://atcoder.jp/contests/abc460/tasks/abc460_a |
| B | https://atcoder.jp/contests/abc460/tasks/abc460_b |
| C | https://atcoder.jp/contests/abc460/tasks/abc460_c |
| D | https://atcoder.jp/contests/abc460/tasks/abc460_d |
| E | https://atcoder.jp/contests/abc460/tasks/abc460_e |
| F | https://atcoder.jp/contests/abc460/tasks/abc460_f |
| G | https://atcoder.jp/contests/abc460/tasks/abc460_g |

## 解説リンク
| 問題 | リンク |
|------|--------|
| A | https://atcoder.jp/contests/abc460/editorial/21025 |
| B | https://atcoder.jp/contests/abc460/editorial/21008 |
| C | https://atcoder.jp/contests/abc460/editorial/21026 |
| D | https://atcoder.jp/contests/abc460/editorial/21027 |
| E | https://atcoder.jp/contests/abc460/editorial/21009 |
| F | https://atcoder.jp/contests/abc460/editorial/21029 |
| G | https://atcoder.jp/contests/abc460/editorial/21012 |
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


’’’
from collections import deque
import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    a = [data[2 + i] for i in range(n)]

    INF = 10**9 + 10  # even, so unreachable cells become '.'
    HASH = ord('#')
    DOT = ord('.')
    W = m + 2  # 番兵付き幅
    size = (n + 2) * W

    # interior cells のみ文字を設定、border cells は 0 (DOT でも HASH でもない)
    grid = bytearray(size)
    for i in range(n):
        base = (i + 1) * W + 1
        for j in range(m):
            grid[base + j] = a[i][j]

    flat_dirs = (1, -1, W, -W, W+1, W-1, -W+1, -W-1)

    # 1回目の操作: 黒セルの隣接白セルを黒にする
    # grid[nb] == DOT は interior の '.' のみマッチ（border は 0 なので対象外）
    b = bytearray(size)
    for i in range(1, n + 1):
        base = i * W + 1
        for j in range(m):
            pos = base + j
            if grid[pos] == HASH:
                for fd in flat_dirs:
                    nb = pos + fd
                    if grid[nb] == DOT:
                        b[nb] = HASH

    # 多元始点BFS
    # border = 0 (even = '.') を番兵として使用（INF でないため BFS が侵入しない）
    D = [0] * size  # interior は後で INF に上書き
    for i in range(1, n + 1):
        base = i * W + 1
        for j in range(m):
            D[base + j] = INF

    Q = deque()
    for i in range(1, n + 1):
        base = i * W + 1
        for j in range(m):
            pos = base + j
            if b[pos] == HASH:
                D[pos] = 0
                Q.append(pos)

    while Q:
        pos = Q.popleft()
        d = D[pos] + 1
        for fd in flat_dirs:
            nb = pos + fd
            if D[nb] == INF:
                D[nb] = d
                Q.append(nb)

    # 距離の偶奇で最終色を決定
    out = []
    for i in range(1, n + 1):
        base = i * W + 1
        out.append(''.join('.' if D[base + j] % 2 == 0 else '#' for j in range(m)))
    sys.stdout.write('\n'.join(out) + '\n')

main()
’’’
