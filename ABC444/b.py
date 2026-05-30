N, K = map(int, input().split())
cnt = 0
for i in range(N):
    I = str(i + 1)
    A = [int(I[j]) for j in range(len(I))]
    if sum(A) == K:
        cnt += 1
print(cnt)