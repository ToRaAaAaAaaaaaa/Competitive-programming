def __main__():
    A = int(input())

    if 400 % A == 0:
        print(400 // A)
    else:
        print(-1)

if __name__ == '__main__':
    __main__()