def __main__():
    N, M = map(int, input().split())
    K = []
    A = []
    for _ in range(M):
        KA = list(map(int, input().split()))
        K.append(KA[0])
        A.append(KA[1:])

    new_B = {val: i for i, val in enumerate(map(int, input().split()))}
    max_days_list = []

    for n, row in enumerate(A):
        for m, val in enumerate(row):
            A[n][m] = new_B[val]
        max_days_list.append(max(A[n]))
    max_days_list.sort()
    
    score = 0
    for day in range(N):
        count = 0
        for p in range(score, len(max_days_list)):
            if max_days_list[p] == day:
                count += 1
            else:
                break
        score += count
        print(score)


if __name__ =='__main__':
    __main__()