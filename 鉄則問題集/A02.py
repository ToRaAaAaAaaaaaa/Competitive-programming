def __main__():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] == X:
            print('Yes')
            break
        else:
            if i==N-1:
                print('No')
            continue

if __name__ == '__main__':
    __main__()

