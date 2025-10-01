N = int(input())
A = list(map(int, input().split()))

sortA = sorted(set(A))

num = 1
B = []

for i in range(N):
    L = 1
    R = len(sortA)
    while L <= R:
        M = (L+R) // 2
        if sortA[M-1] > A[i]:
            R = M - 1
        elif sortA[M-1] < A[i]:
            L = M + 1
        elif sortA[M-1] == A[i]:
            B.append(M)
            break
print(' '.join(map(str, B)))