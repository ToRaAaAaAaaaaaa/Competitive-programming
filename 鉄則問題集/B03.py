def __main__():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        for j in range(i+1, N):
            for h in range(i+2, N):
                if A[i] + A[j] + A[h] == 1000:
                    ans = 1
                    break
    
    if ans == 1:
        print('Yes')
    else:
        print('No')
    
if __name__ == '__main__':
    __main__()