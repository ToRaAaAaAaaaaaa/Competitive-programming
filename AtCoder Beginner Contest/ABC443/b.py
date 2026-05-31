N, K = map(int, input().split())
cnt = -1
while K > 0:
    K-=N
    N += 1
    cnt += 1

print(cnt)