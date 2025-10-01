def __main__():
    N = int(input())
    A = list(map(int, input().split()))

    max_num = max(A)
    for x in range(max_num+2):
        ans = 0
        for i, a in enumerate(A):
            if a >= x:
                ans += 1
        if ans < x:
            print(x-1)
            break

    

if __name__ == '__main__':
    __main__()