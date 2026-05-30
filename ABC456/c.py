S = input()
c = 1
cnt = 0
for i in range(len(S)):
    if i == 0:
        cnt += c
        c += 1
        continue
    elif S[i] != S[i-1]:
        cnt += c
        c += 1
    else:
        c = 1
        cnt += 1
        c += 1
    cnt = cnt % 998244353
print(cnt)