N, T = map(int, input().split())
A = list(map(int, input().split()))
if A:
    time = 0
    n = 1

    for n in range(N):
        if n==0:
            time += A[0]
            nex = A[0] + 100
        elif nex < A[n]:
            time += (A[n]-nex)
            nex = A[n] + 100
    if T - nex > 0:
        time += (T-nex)
    print(time)



else:
    print(T)
