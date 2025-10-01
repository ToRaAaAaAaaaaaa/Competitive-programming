def discover(A,B,skill_list,skill_cnt):
    for X in [A,B]:
        L=0
        R=skill_cnt
        while R>L:
            M=(L+R)//2
            if X<skill_list[M]:
                R=M-1
            elif skill_list[M]<X:
                L=M+1
            elif skill_list[M]==X:
                return True
    return False


N=int(input())
skill_list=[]
skillcard=[]
skill_cnt=0

for x in range(1,N+1):
    A,B=map(int, input().split())
    skill_list.append([min(A,B),max(A,B),x])

skill_list.sort
for y in range(4):
    for a,b,i in skill_list:
        if a==b==0:
            skillcard.append(i)
            skill_list+-1
        elif y%2==0 and discover(a):
            skillcard.append(i)
