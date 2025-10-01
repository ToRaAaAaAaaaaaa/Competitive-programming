def __main__():
    N = int(input())
    A = list(map(int, input().split()))

    min_len = N
    mini = 0
    num = None

    for i in range(N):
        An = A[i]
        length = 2
        for j in range(mini, N):
            if i == j:
                # print(An)
                continue
            elif An == A[j]:
                min_len = min(length, min_len)
                # print("min_len{min_len}")
                num = An
                break
            else:
                length += 1
                # print(length)
        mini += 1

    if num is None:
        print("-1")
    else:
        print(min_len)


if __name__ == "__main__":
    __main__()