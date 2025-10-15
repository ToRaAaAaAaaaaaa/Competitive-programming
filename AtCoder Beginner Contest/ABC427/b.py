N=int(input())
Az=1
ans=0
for i in range(N):
 if i<1:ans += Az
 else:
  A=0
  for j in str(ans):A+=int(j)
  ans=ans+A
print(ans)