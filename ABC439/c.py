N = int(input())
n=int(N**0.5) + 1
ans = []
for i in range(1, n):
    if i**2 + (i+1)**2 > N:
        break
    for j in range(i+1, n):
        num = i**2 + j**2
        if num > N:
            break
        ans.append(num)

ans = sorted(ans)
A = []
if len(ans)>=3:
    if  ans[0]!=ans[1]:
        A.append(ans[0])
    for i in range(1, len(ans)-1):
        if ans[i-1]!=ans[i]!=ans[i+1]:
            A.append(ans[i])
    if ans[-2]!=ans[-1]:
        A.append(ans[-1])
    print(len(A))
    print(' '.join(map(str, A)))
else:
    print(len(ans))
    print(' '.join(map(str, ans)))