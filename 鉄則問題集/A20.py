S = input()
T = input()
s = len(S)
t = len(T)

dp = [[0 for _ in range(t+1)] for _ in range(s+1)]

for i in range(1, s+1):
    for j in range(1, t+1):
        if i >= 1 and j >= 1 and S[i-1] == T[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
        elif i >= 1 and j >= 1:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# print(dp)
print(dp[s][t])