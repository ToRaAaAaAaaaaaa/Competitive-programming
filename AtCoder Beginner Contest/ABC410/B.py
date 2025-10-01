N, Q = map(int, input().split())
X = list(map(int, input().split()))
N_list = [0 for _ in range(N)]
ans_list = [0 for _ in range(Q)]
min_N_list = 0

for i, x in enumerate(X):
  if x > 0:
    N_list[x-1] += 1
    ans_list[i] = x
  elif x == 0:
    min_N_list = min(N_list)
    for n in range(N):
      if N_list[n] == min_N_list:
        N_list[n] += 1
        ans_list[i] = n+1
        break
print(" ".join(map(str, ans_list)))