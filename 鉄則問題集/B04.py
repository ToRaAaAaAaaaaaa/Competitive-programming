def __main__():
    N = input()
    num = len(N)-1
    ans = 0
    keta = 0
    
    for i in range(num, -1, -1):
        if N[i] == '1':
            ans += 2**keta
        keta += 1
    print(ans)
    
if __name__ == '__main__':
    __main__()