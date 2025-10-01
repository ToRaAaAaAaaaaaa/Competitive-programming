def __main__():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    tf_list = [0 for _ in range(M)]
    cnt = 0

    for a in range(N):
        tf_list[A[a] - 1] += 1
        if not 0 in tf_list:
            ans = N - cnt
            print(ans)
            break
        cnt += 1
    
    if 0 in tf_list:
        print(0)

if __name__ == '__main__':
    __main__()