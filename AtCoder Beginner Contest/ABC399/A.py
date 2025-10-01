def __main__():
    N = int(input())
    S = str(input())
    T = str(input())
    cnt = 0

    for i in range(N):
        if S[i] != T[i]:
            cnt += 1
    
    print(cnt)


if __name__ == "__main__":
    __main__()