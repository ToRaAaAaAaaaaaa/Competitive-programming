def __main__():
    A, B = map(int, input().split())
    tf = 0

    for i in range(A, B+1):
        if 100 % i == 0:
            tf = 1
            break
        else:
            continue
    
    if tf == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    __main__()