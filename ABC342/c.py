N=int(input())
S=input()
Q=int(input())
C=[]
D=[]
ALP={alp:i+1 for i,alp in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])}
ALPh={i+1:alp for i,alp in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])}

for _ in range(Q):
 c,d=map(str, input().split())
 C.append(c)
 D.append(d)

for i in range(Q):
 for j in range(1,27):
  if ALPh[j]==C[i]:
   ALPh[j]=D[i]
# print(ALP)
ans=[ALPh[ALP[S[s]]]for s in range(N)]
print(''.join(map(str, ans)))