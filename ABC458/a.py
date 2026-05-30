S = input()
N = int(input())

A = []
for i in range(N, len(S) - N):
    A.append(S[i])

print("".join(map(str, A)))