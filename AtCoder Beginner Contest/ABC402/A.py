def __main__():
    N = input()
    ans = []
    
    for i in range(len(N)):
        if N[i].isupper():
            ans.append(N[i])
        else:
            continue
    
    print(''.join(map(str, ans)))



if __name__ =='__main__':
    __main__()
