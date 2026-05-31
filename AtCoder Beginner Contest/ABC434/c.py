for _ in range(int(input())):
    N, H = map(int, input().split())
    T, L, U = [], [], []
    for i in range(N):
        t, l, u = map(int, input().split())
        T.append(t)
        L.append(l)
        U.append(u)
    time = 0
    tf = 1
    for i in range(N):
        if H <= L[i] and (L[i] - H) // (T[i] - time) <= 1:
            if i<N and U[i+1] < L[i]:
                H = max(H - (T[i] - time), L[i])
            elif i<N and U[i] < L[i+1]:
                H = min(H)
        elif H >= U[i] and (H - U[i]) // (T[i] - time) <= 1:
        elif L[i] < H < U[i]:
        time += T[i]