def __main__():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = str(input())
        X = [0 for _ in range(N)]
        minS = 0
        for n in range(N):
            if S[n] == '1':
                X[n] = X[n-1] + 1
            else:
                X[n] = X[n-1] - 1
            if X[minS-1] > X[n]:
                minS = n + 1
        # print(X)
        # print(minS, 'minS')
        S_left = S[:minS]
        S_right = S[minS:]

        print(S_left, S_right)
        cnt = 0
        for l in S_left:
            if l == "1":
                cnt += 1
        for r in S_right:
            if r == "0":
                cnt += 1
        print(cnt)
            
        
if __name__ == '__main__':
    __main__()