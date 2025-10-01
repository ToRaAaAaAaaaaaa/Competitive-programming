def __main__():
    R, X = map(int, input().split())

    if (1600 <= R and R <= 2999) and X == 1:
        print('Yes')
    elif (1200 <= R and R <= 2399) and X == 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    __main__()