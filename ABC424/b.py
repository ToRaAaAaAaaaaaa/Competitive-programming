N,M,K = map(int, input().split())
ans_list=[[0]*(M+1) for _ in range(N+1)]
ans=[]
for _ in range(K):
    A,B=map(int, input().split())
    ans_list[A][B]=1
    if sum(ans_list[A])==M:
        ans.append(A)
    
print(' '.join(map(str, ans)))