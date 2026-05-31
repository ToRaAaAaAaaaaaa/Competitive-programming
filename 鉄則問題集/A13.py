N, K = map(int, input().split())
A = list(map(int, input().split()))
gap_list = [0 for _ in range(N-1)]

A = sorted(A)
for a in range(N-1):
    gap_list[a] = A[a+1] - A[a]

cnt = 0
gap_sum = 0
for i, gap in enumerate(gap_list):
    gap_sum = 0
    for j in range(i, N-1):
        gap_sum += gap_list[j]
        if gap_sum <= K:
            cnt += 1
        else:
            break
print(cnt)