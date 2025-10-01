def __main__():
    S = str(input())
    reversed_S = str(S)[::-1]
    cnt = 0
    for i, s in enumerate(reversed_S):
        if i == 0:
            if int(s) == 0:
                above = 10
            else:
                above = int(s)
                cnt += above
            continue
        
        if int(s) == 0:
            now = 10
        else:
            now = int(s)
        
        if now >= above:
            cnt += now - above
        else:
            cnt += 10 + now - above
        
        above = now
    
    print(cnt + len(S))

if __name__ == '__main__':
    __main__()