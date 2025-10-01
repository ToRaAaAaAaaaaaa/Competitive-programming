N = int(input())

ans_num = ''
ans = 0
for i in range(N):
    c, l = map(str, input().split())
    l = int(l)
    ans += l
    if ans <= 100:
        for _ in range(l):
            ans_num = ans_num + c
        if i == N-1:
            print(ans_num)
    else:
        print('Too Long')
        break