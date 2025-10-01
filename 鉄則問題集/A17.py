N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None for _ in range(N+1)]
dp[1] = 0
dp[2] = A[0]

for i in range(3, N+1):
    dp[i] = min(dp[i-1] + A[i-2], dp[i-2] + B[i-3])

Answer = []
Place = int(N)
while True:
    Answer.append(Place)
    if Place == 1:
        break
    if dp[Place-1] + A[Place-2] == dp[Place]:
        Place -= 1
    elif dp[Place-2] + B[Place-3] == dp[Place]:
        Place -= 2
Answer.reverse()
print(len(Answer))
print(' '.join(map(str, Answer)))