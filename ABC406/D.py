def __main__():
    H, W, N = map(int, input().split())
    index_dust = [0 for _ in range(H)]
    row_dust = [0 for _ in range(W)]
    for _ in range(N):
        X, Y = map(int, input().split())
        index_dust[X-1] += 1
        row_dust[Y-1] += 1
    
    Q = int(input())
    for q in range(Q):
        os, qi = map(int, input().split())
        if os == 1:
            print(index_dust[qi-1])
            index_dust[qi-1] = 0
            
        else:
            print(row_dust[qi-1])
            row_dust[qi-1] = 0

if __name__ == '__main__':
    __main__()