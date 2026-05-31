# import sys
# sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B, reverse=True)

i = 0
j = 0
ans = 0
while i < n and j < m:
    if A[i] * 2 >= B[j]:
        i += 1
        j += 1
        ans += 1
    else:
        j += 1

print(ans)
