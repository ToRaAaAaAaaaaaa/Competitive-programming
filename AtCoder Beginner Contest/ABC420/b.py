N, M = map(int, input().split())
num_list = [0 for _ in range(N)]
S = [input() for _ in range(N)]
for i in range(M):
    t = 0
    f = 0
    for n in range(N):
        num = S[n]
        if num[i] == '1':
            t += 1
        else:
            f += 1
    
    if t > f and f > 0:
        for nn in range(N):
            nnum = S[nn]
            if nnum[i] == '0':
                num_list[nn] += 1
    elif f > t and t > 0:
        for nn in range(N):
            nnum = S[nn]
            if nnum[i] == '1':
                num_list[nn] += 1
    elif f == 0 or t == 0:
        for nn in range(N):
            num_list[nn] += 1


Max = max(num_list)
ans = []
for j in range(N):
    if num_list[j] == Max:
        ans.append(j+1)
print(' '.join(map(str, ans)))