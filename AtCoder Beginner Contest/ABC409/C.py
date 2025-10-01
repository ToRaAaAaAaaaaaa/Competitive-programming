def __main__():
    N, L = map(int, input().split())
    D = list(map(int, input().split()))
    X = [0] * L
    ans = 0
    
    if L % 3 == 0:
        num = 0
        X[0] = 1
        for d in range(N-1):
            num += D[d]
            num = num % (L)
            X[num] += 1
        
        ans = 0
        for i in range(L//3):
            ans += X[i] * X[i+L//3] * X[i+2*L//3]
        print(ans)
    else:
        print(ans)

if __name__ == '__main__':
    __main__()