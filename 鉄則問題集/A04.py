def __main__():
    N = int(input())
    ans = list()

    for _ in range(10):
        if N >= 1:
            if N % 2 == 1:
                ans.append(1)
                N = N // 2
            elif N % 2 == 0:
                ans.append(0)
                N = N // 2
        else:
            ans.append(0)

    ans = ans[::-1]
    print(''.join(map(str, ans)))

if __name__ == '__main__':
    __main__()