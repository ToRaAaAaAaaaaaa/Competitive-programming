H, W = map(int, input().split())
G = []
for i in range(H):
    S = input()
    G.append([S[j] for j in range(W)])

cnt = 0
L = []
for ha in range(H):
    for hb in range(H):
        for wa in range(W):
            for wb in range(W):
                flag = True
                if ha <= hb and wa <=wb:
                    for i in range(ha, hb+1):
                        for j in range(wa, wb+1):
                            if G[i][j] == G[ha + hb - i][wa + wb - j]:
                                continue
                            else:
                                flag = False
                    if flag:
                        cnt += 1
print(cnt)