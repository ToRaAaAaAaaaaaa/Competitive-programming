def __main__():
    A, B, C, D = map(int, input().split())

    if A > C:
        print('Yes')
    elif A == C and B >= D:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    __main__()