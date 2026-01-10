N = int(input())
A = list(map(int, input().split()))

max_break = 0
cnt = 0
tf = 1
for i in range(N):
    cnt += 1
    if A[i] + i - 1 > max_break:
        max_break = A[i] + i - 1
    if i >= max_break:
        print(cnt)
        tf = 0
        break
if tf:
    print(cnt)