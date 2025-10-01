def __main__():
    D = int(input())
    A = [int(input()) for _ in range(D)]
    Q = int(input())
    st = [list(map(int, input().split())) for _ in range(Q)]

    sum_A = list()
    iA = 0

    for i in range(D):
        iA += A[i]
        sum_A.append(iA)

    for j in range(Q):
        if sum_A[st[j][0]-1] > sum_A[st[j][1]-1]:
            print(st[j][0])
        elif sum_A[st[j][0]-1] < sum_A[st[j][1]-1]:
            print(st[j][1])
        else:
            print('Same')

if __name__ == '__main__':
    __main__()