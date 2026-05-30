N, K = map(int, input().split())
L = []
A = []
for _ in range(N):
    la = list(map(int, input().split()))
    l = la[0]
    a = la[1:]
    L.append(l)
    A.append(a)
C = list(map(int, input().split()))

i = 0
while K > 0:
    K -= L[i]*C[i]
    if K < 0:
        flag = i
        K = -K
        break
    i += 1

print(A[flag][K // L[flag]])