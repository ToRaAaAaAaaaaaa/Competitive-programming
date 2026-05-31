import sys
input = sys.stdin.readline

h, w = map(int, input().split())
S = []
D = []
L = [[-1 for j in range(w)]for i in range(h)]
for i in range(h):
    s = input()
    S.append([s[j] for j in range(w)])
    for j in range(w):
        if s[j] == "#":
            D.append([i, j])
flag = 0
if len(D) == h*w:
    flag = 1

pm = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

nd = []
for i, j in D:
    for k, l in pm:
        N, M = i + k, j + l
        if 0<= N < h and 0 <= M < w and S[N][M] == ".":
            nd.append([N, M])
            S[N][M] = "#"
            L[N][M] = 1
for i, j in D:
    S[i][j] = "."
D = nd

d = 0
while D:
    nd = []
    for i, j in D:
        for k, l in pm:
            N, M = i + k, j + l
            if 0<= N < h and 0 <= M < w and L[N][M] == -1:
                L[N][M] = d
                nd.append([N, M])
    d += 1
    D = nd

ans = [["." for j in range(w)]for i in range(h)]

if flag == 0:
    for i in range(h):
        for j in range(w):
            if L[i][j] % 2 == 0:
                ans[i][j] = "#"
    for i in range(h):
        print("".join(map(str, ans[i])))
else:
    for i in range(h):
        print("".join(map(str, ans[i])))


