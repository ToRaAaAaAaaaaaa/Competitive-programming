N, M = map(int, input().split())
data = []
for i in range(M):
    a, b = map(int, input().split())
    d = a - b
    data.append((d, a, b, i))

data.sort(reverse=False)

D = [item[0] for item in data]
A = [item[1] for item in data]

ans = 0
for j in range(M):
    num = (N-A[j]) // D[j]
    x = max(0,  num + 1)
    ans += x
    N -= (D[j] * x)

print(ans)