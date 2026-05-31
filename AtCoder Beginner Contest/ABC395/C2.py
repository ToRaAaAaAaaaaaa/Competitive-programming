def __main__():
    N = int(input())
    A = list(map(int, input().split()))

    min_len = N+1
    length = 2

    for i in range(N):
        newN = min(i+min_len, N)
        for j in range(i, newN):
            if i == j:
                continue
            elif A[i] == A[j]:
                min_len = min(length, min_len)
                break
            else:
                length += 1
        if min_len == 2:
            print(min_len)
            break
        elif i == N-1:
            if min_len < N:
                print(min_len)
            else:
                print(-1)
        length = 2

if __name__ == "__main__":
    __main__()