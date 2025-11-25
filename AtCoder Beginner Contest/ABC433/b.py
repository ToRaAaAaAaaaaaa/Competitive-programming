N = int(input())
A = list(map(int, input().split()))
for i in range(N):
  ans = 0
  if i==0:
    print(-1)
  else:
    for j in range(i):
      if A[j] > A[i]:
        ans = j+1
    if ans == 0:
      print(-1)
    else:
      print(ans)