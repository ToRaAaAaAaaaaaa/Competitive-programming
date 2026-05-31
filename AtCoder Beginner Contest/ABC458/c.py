S = input()

cnt = 0
s = 0
e = len(S)

for i in range(len(S)):
    e -= 1
    if S[i] == "C":
        cnt += min(s, e) + 1
    s += 1
print(cnt)
