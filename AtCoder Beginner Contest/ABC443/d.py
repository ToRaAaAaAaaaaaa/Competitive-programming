T = int(input())
for i in range(T):
    N = int(input())
    R = list(map(int, input().split()))
    R_cnt = sum(R)
    for i in range(N-1):
        if R[i] > R[i+1]:
            R[i] = R[i+1]+1

        elif R[i] < R[i+1]:
            R[i+1] = R[i]+1

    for i in range(N-2, -1, -1):
        if R[i] > R[i+1]:
            R[i] = R[i+1]+1

        elif R[i] < R[i+1]:
            R[i+1] = R[i]+1
        
    cnt = R_cnt - sum(R)
    print(cnt)