N = int(input())
S = list(map(str, input().split()))
ans = []
alp = "abcdefghijklmnopqrstuvwxyz"

dic = {}
num = 2
for i in range(len(alp)):
    if alp[i] == "d":
        num+=1
    elif alp[i] == "g":
        num+=1
    elif alp[i] == "j":
        num+=1
    elif alp[i] == "m":
        num+=1
    elif alp[i] == "p":
        num+=1
    elif alp[i] == "t":
        num+=1
    elif alp[i] == "w":
        num+=1
    dic[alp[i]] = num

for j in range(N):
    ans.append(dic[S[j][0]])
print("".join(map(str,ans)))