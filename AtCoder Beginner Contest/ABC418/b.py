S = input()
cnt = 0
start = []
end = []
ans = 0

for s in range(len(S)):
    if S[s] == 't' and cnt == 0:
        start.append(s+1)
        cnt += 1
    elif S[s] == 't':
        start.append(s+1)
        end.append(s+1)
        cnt += 1

end.sort(reverse=True)

if len(start) > 0 and len(end) > 0:
    if (end[0] - start[0] + 1) >= 3:
        cnt += 1
        for i in range(len(start)):
            cnt -= 1
            cntcopy = cnt
            for j in range(len(end)):
                if (end[j] - start[i] + 1) < 3:
                    continue
                else:
                    if i == 0 and j == 0:
                        ans = (cntcopy - 2) / ((end[j] - start[i] + 1) - 2)
                    else:
                        ans = max(ans, (cntcopy - 2) / ((end[j] - start[i] + 1) - 2))
                cntcopy -= 1
    print(ans)
else:
    print(0)