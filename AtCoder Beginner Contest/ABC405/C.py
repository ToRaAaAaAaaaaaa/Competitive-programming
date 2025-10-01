def __main__():
    N = int(input())
    A = list(map(int, input().split()))

    A_sum = sum(A)
    ans = 0
    for i in range(N-1):
        A_sum -= A[i]
        ans += A_sum * A[i]
    
    print(ans)


if __name__ == '__main__':
    __main__()