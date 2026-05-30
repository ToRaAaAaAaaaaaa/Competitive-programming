N, Q = map(int, input().split())
UP = {i:-1 for i in range(1, N+1)}
DOWN = {i:-1 for i in range(1, N+1)}

for i in range(Q):
    C, P = map(int, input().split())
    if DOWN[C] > 0:
        UP[DOWN[C]] = -1    
    UP[P] = C
    DOWN[C] = P

ans = []
for i in range(N):
    if DOWN[i+1] == -1:
        cnt = 1
        num = i+1
        while UP[num] > 0:
            num = UP[num]
            cnt += 1
        ans.append(cnt)
    else:
        ans.append(0)

print(" ".join(map(str, ans)))
