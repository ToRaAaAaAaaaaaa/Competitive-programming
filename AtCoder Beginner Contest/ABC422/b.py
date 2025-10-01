H, W = map(int, input().split())
tf,cnt = 0,0
f = 0
bw = []
for _ in range(H):
    S = input()
    bw.append([S[n] for n in range(W)])


for i in range(H):
    for j in range(W):
        if bw[i][j] == '#':
            cnt = 0
            f = 1
            if i != 0 and bw[i-1][j] == '#':
                cnt += 1
            if i != (H-1) and bw[i+1][j] == '#':
                cnt += 1
            if j != 0 and bw[i][j-1] == '#':
                cnt += 1
            if j != (W-1) and bw[i][j+1] == '#':
                cnt += 1
        if f == 1 and (cnt == 1 or cnt == 3 or cnt == 0):
            tf = 1
            break
    if tf == 1:
        break
if tf == 0 or f == 0:
    print('Yes')
else:
    print('No')

        