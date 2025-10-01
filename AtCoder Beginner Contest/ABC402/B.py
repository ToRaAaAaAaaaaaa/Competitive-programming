def __main__():
    N = int(input())
    qx = [list(map(int, input().split())) for _ in range(N)]
    row = []

    for i in range(N):
        if qx[i][0] == 1:
            row.append(qx[i][1])
        else:
            print(row[0])
            row.remove(row[0])

if __name__ =='__main__':
    __main__()
