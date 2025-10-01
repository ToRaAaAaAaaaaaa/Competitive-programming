N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[None for _ in range(S+1)] for _ in range(N+1)]

for i in range(S+1):
    if i == 0:
        dp[0][i] = True
    else:
        dp[0][i] = False

for n in range(1, N+1):
    for s in range(S+1):
        if dp[n-1][s] == True:
                dp[n][s] = True
        elif s == A[n-1]:
            dp[n][s] = True
        elif s - A[n-1] >= 0 and dp[n-1][s - A[n-1]] == True:
            dp[n][s] = True
        else:
            dp[n][s] = False

# print(dp)
if dp[N][S] == True:
    print('Yes')
else:
    print('No')