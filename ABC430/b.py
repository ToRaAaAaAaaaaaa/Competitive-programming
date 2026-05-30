N, M = map(int, input().split())
S=[]
for _ in range(N):
    s=str(input())
    ss=[s[sss]for sss in range(len(s))]
    S.append(ss) 

f=[]
for i in range(N-M+1):
    for j in range(N-M+1):
        cuts=[[S[n][m]for m in range(j,M+j)]for n in range(i,M+i)]
        if cuts not in f:
            f.append(cuts)
print(len(f))