from collections import deque

N,Q = map(int, input().split())
A=deque(map(int, input().split()))
T=[list(map(int, input().split()))for _ in range(Q)]
Sum_list=deque(0)
for i in range(1,N):
    Sum_list.append(A[i-1]+Sum_list[i-1])

for i in range(Q):
    q=T[i][0]
    if q==1:
        c=T[i][1]
        M = Sum_list[c]
        for j in range(1,N):
            Sum_list[j]=Sum_list[]-M
    else:
        l,r=T[i][1],T[i][2]
        print(Sum_list[r-1]-Sum_list[l-1])