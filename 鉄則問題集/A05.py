def __main__():
    N, K = map(int, input().split())

    cnt = 0
    for red in range(1, min(N+1, K+1)):
        if K - red == 1:
            break
        for blue in range(1, min(N+1, K+1)):
            if (K - (red+blue) > 0) and (K - (red+blue) <= N):
                cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    __main__()
 

