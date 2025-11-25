N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))
setB=sorted(set(B))
R=len(setB)
B_dic={num:0 for num in setB}
for i in range(M):
    B_dic[B[i]]+=1

# H_sort=H.sort()

cnt=0
for i in range(R):
    h=H[i]
    X=0
    Y=R-1
    while X<Y:
        Z=(X+Y)//2
        if setB[Z-1]<h<=setB[Z]:
            if B_dic[setB[Z]]:
                B_dic[setB[Z]]-=1
                cnt+=1
                break
        if h<=setB[Z]:
            Y=Z-1
        else:
            X=Z+1

if K<=cnt:
    print('Yes')
else:
    print('No')