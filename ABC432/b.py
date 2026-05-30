X = str(input())
ans = [int(x) for x in X]
ans = sorted(ans)
tf = 1
if ans[0]==0:
    tf=0
for i in range(len(ans)):
    if tf==0 and ans[i]>0:
        ans[0] = ans[i]
        ans[i] = 0
        tf=1
print(''.join(map(str, ans)))