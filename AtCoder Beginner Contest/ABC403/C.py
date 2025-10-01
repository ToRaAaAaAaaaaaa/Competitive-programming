def __main__():
    N, M, Q = map(int, input().split())
    figures = [set() for _ in range(N)]
    check_all = [False] * N
    for _ in range(Q):
        query = list(map(int, input().split()))
        num, content = query[0], query[1:]
        user = content[0] - 1
        if num == 1:
            figures[user].add(content[1])
        elif num == 2:
            check_all[user] = True
        elif num == 3:
            if content[1] in figures[user] or check_all[user] == True:
                print('Yes')
            else:
                print('No')

if __name__ =='__main__':
    __main__()
