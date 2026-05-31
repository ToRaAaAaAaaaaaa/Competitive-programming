N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N-1):
    for j in range(1, N):
        if j<=i:
            continue
        tf = 1
        M = 0
        for k in range(i, j+1):
            M += A[k]
        for k in range(i, j+1):
            if M % A[k] == 0:
                tf = 0
                break
        if tf == 1:
            cnt +=1
print(cnt)