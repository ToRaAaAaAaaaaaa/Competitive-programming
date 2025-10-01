def __main__():
    D = int(input())
    N = int(input())
    L = [None] * N
    R = [None] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    
    appearence = [0] * D
    for start, end in zip(L, R):
        appearence[start-1] += 1
        if end < D:
            appearence[end] -= 1
    
    cnt = 0
    for ans in appearence:
        cnt += ans
        print(cnt)

if __name__ == '__main__':
    __main__()

