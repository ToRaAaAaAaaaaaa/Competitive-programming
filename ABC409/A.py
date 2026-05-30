def __main__():
    N = int(input())
    T = input()
    A = input()
    tf = 0
    for i in range(N):
        if T[i] == A[i] and T[i] == 'o':
            print('Yes')
            tf = 1
            break
    if tf == 0:
        print('No')

if __name__ == '__main__':
    __main__()