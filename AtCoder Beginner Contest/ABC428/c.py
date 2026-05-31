from collections import deque
Q=int(input())
query=[list(map(str, input().split()))for _ in range(Q)]
L=deque()
N=deque()
n=0
SUM=0
dic={'(':1,')':-1}
for i in range(Q):
    if len(query[i])==2:
        x,y=int(query[i][0]),query[i][1]
        L.append(y)
        SUM+=dic[y]
        if SUM<0:
            N.append(len(L)-1)
    else:
        x=int(query[i][0])
        if N and len(L)-1==N[-1]:
            N.pop()
        SUM-=dic[L[-1]]
        L.pop()
    if len(L)==0:
        print('Yes')
    elif SUM==0 and L[0]=='(' and L[-1]==')':
        if len(N):print('No')
        else:print('Yes')
    else:print('No')