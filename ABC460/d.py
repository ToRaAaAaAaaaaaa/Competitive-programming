# import sys
# sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
S = []
L = [[-1 for i in range(W)]for j in range(H)]
sharpl = []
for i in range(H):
    s = [a for a in input()]
    S.append(s)
    for j in range(W):
        if s[j] == "#":
            sharpl.append([i, j])

for i in range(H):
    for j in range(W):
        ml = []
        for k in range(len(sharpl)):
            ml.append(max(abs(i - sharpl[k][0]), abs(j - sharpl[k][0])))
        num = min(ml)
        if num % 2 == 0:
            L[i][j] = "#"
        else:
            L[i][j] = "."

for i in range(H):
    print(''.join(map(str, L[i])))
