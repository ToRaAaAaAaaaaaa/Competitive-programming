import sys
input = sys.stdin.readline
N, Q = map(int, input().split())

block = [0 for _ in range(N)]
num = {i: 0 for i in range(Q+1)}
num[0] = N
rm = 0

for i in range(Q):
    n, q = map(int, input().split())
    if n == 1:
        block[q-1] += 1
        num[block[q-1]] += 1
        if num[block[q-1]] == N:
            rm += 1
    else:
        if q + rm > Q:
            print(0)
        else:
            ans = num[q+rm]
            print(ans)