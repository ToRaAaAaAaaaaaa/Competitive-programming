N=int(input())
A=list(map(int, input().split()))

S=[]
seisu=[-1]*N
tf=1
for i in range(N):
    if A[i]>0:
        if A[i] in S:
            print('No')
            tf=0
            break
        else:
            S.append(A[i])
            seisu[i]=A[i]
if tf==1:
    for j in range(N):
        n=1
        while seisu[j]<0:
            if not n in seisu:
                seisu[j]=n
            else:
                n+=1
    print('Yes')
    print(' '.join(map(str, seisu)))