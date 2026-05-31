def __main__():
    H, W = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(H)]

    # 累積和テーブル作成
    S = [[0] * (W+1) for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            S[i+1][j+1] = S[i+1][j] + S[i][j+1] - S[i][j] + X[i][j]

    # クエリ処理
    Q = int(input())
    for _ in range(Q):
        ax, ay, bx, by = map(int, input().split())
        # 1-indexなら-1調整も忘れずに
        ax -= 1; ay -= 1
        total = S[bx][by] - S[ax][by] - S[bx][ay] + S[ax][ay]
        print(total)


if __name__ == '__main__':
    __main__()