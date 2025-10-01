def __main__():
    X = int(input())
    cnt = 0
    for n in range(1, X+1):
        if X < 2**n or X%2==1:
            break
        A = 2**n
        num_B = (pow(X / A, 0.5))
        cnt += (num_B + 1) // 2
    print(int(cnt))

if __name__=='__main__':
    __main__()

        
