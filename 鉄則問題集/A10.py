N = int(input())
A = list(map(int, input().split()))
D = int(input())

L_list = [0 for _ in range(N)]
R_list = [0 for _ in range(N)]

for l in range(N):
  if L_list[l-1] <= A[l]:
    L_list[l] = A[l]
  else:
    L_list[l] = L_list[l-1]

for r in range(N):
  if R_list[r-1] <= A[N-r-1]:
    R_list[r] = A[N-r-1]
  else:
    R_list[r] = R_list[r-1]

for d in range(D):
  L, R = map(int, input().split())
  ans = max(L_list[L-2], R_list[N-R-1])
  print(ans)