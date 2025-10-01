def __main__():
    N, S = map(int, input().split())
    T = list(map(int, input().split()))
    tf = 1
    Tm = 0
    for t in range(N):
        if (T[t] - Tm) < (S + 0.5):
            Tm = T[t]
            continue
        else:
            tf = 0
            break
    
    if tf == 1:
        print('Yes')
    else:
        print('No')
        
if __name__ == '__main__':
    __main__()