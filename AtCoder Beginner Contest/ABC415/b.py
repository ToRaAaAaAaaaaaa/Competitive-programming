S = input()
cnt = 0
ans = ''
for s in range(1, len(S)+1):
    if S[s-1] == '#' and cnt == 0:
        ans += f'{s}'
        cnt += 1
    elif S[s-1] == '#' and cnt == 1:
        ans += f',{s}'
        print(ans)
        cnt = 0
        ans = ''
