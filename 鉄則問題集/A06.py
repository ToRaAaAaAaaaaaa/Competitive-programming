def __main__():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    LR = [list(map(int, input().split())) for _ in range(Q)]

    S = [0] * (N+1)
    for num in range(N):
        S[num + 1] += S[num] + A[num]
    
    for ques in range(Q):
        print(S[LR[ques][1]] - S[LR[ques][0]-1])
    
if __name__ == '__main__':
    __main__()
