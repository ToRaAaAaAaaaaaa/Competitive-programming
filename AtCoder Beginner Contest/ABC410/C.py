N, Q = map(int, input().split())
ans_list = [i for i in range(1, N+1)]

k = 0
for q in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    p = query[1] - 1 + k
    x = query[2]
    ans_list[p % N] = x
  elif query[0] == 2:
    p = query[1] - 1  + k
    print(ans_list[p % N])
  else:
    k += query[1]
    # move_list = ans_list[:k-1]
    # ans_list = ans_list[k:]
    # ans_list.extend(move_list) extendは便利