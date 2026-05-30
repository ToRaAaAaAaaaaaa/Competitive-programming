def __main__():
    X, Y = map(int, input().split())
    cnt = 0
    for one in range(1, 7):
        for two in range(1, 7):
            if one + two >= X or abs(one - two) >= Y:
                cnt += 1
    print(cnt / 36)

if __name__ == '__main__':
    __main__()