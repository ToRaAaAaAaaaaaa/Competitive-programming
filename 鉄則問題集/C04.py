def __main__():
    N = int(input())
    num = []
    halfN = N // 2

    for i in range(1, halfN+1):
        if N % i == 0:
            num.append(i)
    
    num.append(N)
    num.sort()
    for j in num:
        print(j)


if __name__ == '__main__':
    __main__()