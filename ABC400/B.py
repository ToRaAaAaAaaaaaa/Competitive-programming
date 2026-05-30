def __main__():
    N, M = list(map(int, input().split()))
    X = 0

    for i in range(M+1):
        X += N ** i
        if X > 10**9:
            print("inf")
            break
    
    if X <= 10**9:
        print(X)

if __name__=='__main__':
    __main__()
