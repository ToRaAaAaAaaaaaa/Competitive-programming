N,K=map(int, input().split())
S=input()
ans = []
MaxCnt=0
for i in range(N-K+1):
    cnt = 0
    X=[S[i+k]for k in range(K)]
    for j in range(N-K+1):
        Y=[S[j+k]for k in range(K)]
        if X==Y:
            cnt+=1
    if cnt>MaxCnt:
        MaxCnt=cnt

for i in range(N-K+1):
    cnt = 0
    X=[S[i+k]for k in range(K)]
    for j in range(N-K+1):
        Y=[S[j+k]for k in range(K)]
        if X==Y:
            cnt+=1
    if cnt==MaxCnt:
        if X in ans:continue
        ans.append(X)

print(MaxCnt)
ANS=sorted([''.join(map(str, ans[s]))for s in range(len(ans))])
print(' '.join(map(str, ANS)))