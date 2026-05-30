S = input()
DP = [[0 for _ in range(3)] for nm in range(len(S))]

DP[0][ord(S[0]) - ord("a")] = 1

for i in range(1, len(S)):
    for val in ["a", "b", "c"]:
        if S[i] == val:
            DP[i][ord(val) - ord("a")] = DP[i-1][0] + DP[i-1][1] + DP[i-1][2] + 1
        else:
            DP[i][ord(val) - ord("a")] = DP[i-1][ord(val) - ord("a")]
        DP[i][ord(val) - ord("a")] = DP[i][ord(val) - ord("a")] % 998244353

print(sum(DP[len(S) - 1]) % 998244353)