N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

Min_list = []
Max_list = []

for i in range(N):
    Min_list.append(X*A[i])
    Max_list.append(Y*A[i])

Min_max = max(Min_list)
Max_min = min(Max_list)

if Max_min < Min_max:
    print(-1)
else:
    n = (Max_min - Min_max) // (Y-X)
    Number = Min_max + n*(Y-X)
    ans = 0
    tf = 1
    for i in range(N):
        nnn = (Number - Min_list[i])%(Y-X)
        if nnn > 0:
            tf = 0
        nn = (Number - Min_list[i])//(Y-X)
        ans += nn
    if tf == 1:
        print(ans)
    else:
        print(-1)