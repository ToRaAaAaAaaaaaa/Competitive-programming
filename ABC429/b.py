N,M=map(int, input().split())
A=list(map(int, input().split()))
S=0
for a in A:
    S+=a
t=0
for s in A:
    if S-s==M:
        print('Yes')
        t=1
        break
if t==0:
    print('No')
