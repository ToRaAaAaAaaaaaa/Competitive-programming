def __main__():
    N, M = map(int, input().split())
    X = [0 for _ in range(N+2)]
    Y = [0 for _ in range(N+2)]
    for _ in range(M):
        L, R = map(int, input().split())
        X[L-1] += 1
        X[R] -= 1
    
    for i in range(N+2):
        Y[i] = Y[i-1] + X[i]
    Y = Y[:N]
    print(min(Y))
    
        
if __name__ == '__main__':
    __main__()