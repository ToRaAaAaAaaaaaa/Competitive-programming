N, A, B = map(int, input().split())
S=input()

L=[0 for _ in range(N)]
b_cnt=0
a_cnt=0
for i in range(N):
    if S[i]=='a':
        a_cnt+=1
        L[i]=a_cnt
    elif S[i]=='b':
        b_cnt+=1
        L[i]=b_cnt
        if b_cnt==B:
            a_cnt=0
            b_cnt=0
print(answer)
            


