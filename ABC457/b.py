N = int(input())
L = []
for _ in range(N):
    LA = list(map(int, input().split()))
    L.append(LA)
X, Y = int(input()), int(input())

print(L[X-1][Y-1])
