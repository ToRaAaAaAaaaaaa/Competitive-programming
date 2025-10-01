def __main__():
    N = int(input())
    S = [input().strip() for _ in range(N)]

    si = 'logout'
    state = 'False'
    cnt = 0

    for i in range(N):
        if S[i] == 'login':
            state = 'True'
        elif S[i] == 'logout':
            state = 'False'
        elif S[i] == 'public':
            continue
        elif S[i] == 'private':
            if state == 'False':
                cnt += 1
    
    print(cnt)


if __name__ =='__main__':
    __main__()
