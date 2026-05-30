X = int(input())
N = int(input())
W = list(map(int, input().split()))
W_on = [0 for _ in range(N+1)]

for i in range(int(input())):
    p = int(input())
    if W_on[p]==0:
        W_on[p]=1
        X+=W[p-1]
    else:
        W_on[p]=0
        X-=W[p-1]
    print(X)