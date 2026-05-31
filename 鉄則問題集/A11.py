N, X = map(int, input().split())
A = list(map(int, input().split()))

sort_A = sorted(A)

halfN = N // 2
if X <= sort_A[halfN-1]:
  for i in range(max(1, halfN)):
    if sort_A[i] == X:
      print(i+1)
      break
else:
  for j in range(max(1, halfN), N):
    if sort_A[j] == X:
      print(j+1)
      break