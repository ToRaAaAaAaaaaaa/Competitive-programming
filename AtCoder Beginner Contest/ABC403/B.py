def __main__():
    T = input()
    U = input()

    for i in range(len(T)-len(U)+1):
        TF = 1
        for t, u in zip(range(i, i + len(U)), range(len(U))):
            if T[t] == '?' or T[t] == U[u]:
                continue
            else:
                TF = 0
                break
        if TF == 1:
            break


    if TF==1:
        print('Yes')
    else:
        print('No')

if __name__ =='__main__':
    __main__()
