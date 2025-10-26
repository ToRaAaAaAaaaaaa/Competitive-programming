N,M,C=map(int, input().split())
A=list(map(int, input().split()))
people=[0 for _ in range(M)]
answer=[0 for _ in range(M)]
for i in range(N):
    people[A[i]]+=1
    answer[A[i]]+=1
t=1
cnt=0
while t:
    t=0
    cnt+=1
    for i in range(M):
        if answer[i]<C:answer[i]+=people[(i+cnt)%M]
        if answer[i]<C:t=1
ANSWER=0
for ans in answer:
    ANSWER+=ans
print(ANSWER)
