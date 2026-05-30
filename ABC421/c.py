N = int(input())
S = input()
alp_list = []
ans = 0
ans2 = 0

for i in range(2*N):
    if S[i] == 'A':
        alp_list.append(i+1)

for j in range(1, N+1):
    ans += abs(alp_list[j-1] - (2*j - 1))

for k in range(1, N+1):
    ans2 += abs(alp_list[k-1] - 2*k)

print(min(ans, ans2))