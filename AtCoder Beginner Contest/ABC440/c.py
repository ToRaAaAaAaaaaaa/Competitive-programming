for _ in range(int(input())):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))
    ans = 10**9
    s = 0
    score = []
    for x in range(W, W*2):
        for j in range(N):
            if (x+j+1)%(W*2) < W:
                s += C[j]
        if s < ans:
            ans = s
        if score == []:
            score.append(s)
        else:
            if score[0]==s:
                print(ans)
                break
            else:
                score.append(s)