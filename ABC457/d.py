from math import ceil
N, K = map(int, input().split())
A = list(map(int, input().split()))

ok = 1
ng = A[0] + K + 1

def solve(m):
    X = m
    for i in range(1, N+1):
        X -= ceil((m - A[i-1]) // i)
    if X:
        return True
    else:
        return False

while ng - ok > 1:
    m = (ok + ng) // 2
    if solve(m):
        ok = m
    else:
        ng = m

print(ok)