N=int(input())
A=list(map(int, input().split()))
setA=sorted(set(A))
H={setA[i]:0 for i in range(len(setA))}
for i in range(N):
    H[A[i]]+=1
answer=0
for num, j in enumerate(H):
    if H[j]>1:
        if H[j]%2==0:
            J=H[j]//2
            K=J*(H[j]-1)
        else:
            J=(H[j]-1)//2
            K=J*H[j]
        answer+=K*(N-H[j])

print(answer)