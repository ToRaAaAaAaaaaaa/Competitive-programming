T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    num = S[0]
    S_filled = sorted(set(S[1:N-1]))
    cnt = 0
    tf = 0
    ans = 0
    for i, s in enumerate(S_filled):
        if 2*num >= S[N-1]:
            tf = 1
            break
        elif num * 2 == s:
            num = s
            cnt += 1
        elif num * 2 > s:
            ans = i
        elif s > num * 2:
            num = S_filled[i-1]
            cnt += 1
            if 2*num >= S[N-1]:
                tf = 1
                break
        print(cnt)
    if tf == 0:
        print(-1)
    else:
        print(cnt+2)
    