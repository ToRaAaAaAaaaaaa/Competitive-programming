def __main__():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = A[0]
    if ans >= 10**K:
        ans = 1

    if N >= 2:
        for i in range(1, N):
            ans *= A[i]
            if ans >= 10**K:
                ans = 1
    
    print(ans)

if __name__ == '__main__':
    __main__()