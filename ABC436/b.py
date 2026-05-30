N = int(input())
A = [[None for j in range(N)]for i in range(N)]

A[0][(N-1)//2] = 1
r, c = 0, (N-1)//2
k = 1

for i in range(N**2 - 1):
    rmN, cmN = (r-1)%N, (c+1)%N
    if A[rmN][cmN]==None:
        A[rmN][cmN] = k+1
        r, c = rmN, cmN
    else:
        A[(r+1)%N][c] = k+1
        r, c = (r+1)%N, c
    k += 1

for i in range(N):
    print(' '.join(map(str, A[i])))