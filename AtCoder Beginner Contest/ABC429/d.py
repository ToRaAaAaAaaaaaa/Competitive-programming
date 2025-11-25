N,M,C=map(int, input().split())
A=list(map(int, input().split()))
setA=sorted(set(A))
people={setA[i]:0 for i in range(len(setA))}
for a in A:people[a]+=1
ANS=[]
for b in people:
 ans=0;B=b
 while ans<C:
  ans+=people[setA[B%len(setA)]];ANS.append(ans)
answer=0
for c in range(len(people)):
 if c==0:answer+=(M+setA[0]-setA[-1])*ANS[c]
 else:answer+=abs(setA[c]-setA[c-1])*ANS[c]
print(answer)