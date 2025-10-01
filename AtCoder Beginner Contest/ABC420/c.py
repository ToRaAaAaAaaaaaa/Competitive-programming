N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Min_list = []
Sum = 0
for i in range(N):
    Min_list.append(min(A[i], B[i]))
    Sum += Min_list[i]

for j in range(Q):
    c, X, V = map(str, input().split())
    X = int(X)
    V = int(V)
    if c == 'A':
        if Min_list[X-1] == A[X-1] and B[X-1] != A[X-1]:
            Min_list[X-1] = min(V, B[X-1])
            if Min_list[X-1] == V:
                Sum += (V-A[X-1])
            else:
                Sum += (B[X-1]-A[X-1])
        else:
            Min_list[X-1] = min(V, B[X-1])
            if Min_list[X-1] == V:
                Sum += (V-B[X-1])
        A[X-1] = V
    elif c == 'B':
        if Min_list[X-1] == B[X-1] and B[X-1] != A[X-1]:
            Min_list[X-1] = min(A[X-1], V)
            if Min_list[X-1] == V:
                Sum += (V-B[X-1])
            else:
                Sum += (A[X-1]-B[X-1])
        else:
            Min_list[X-1] = min(A[X-1], V)
            if Min_list[X-1] == V:
                Sum += (V-A[X-1])
        B[X-1] = V
    print(Sum)
            