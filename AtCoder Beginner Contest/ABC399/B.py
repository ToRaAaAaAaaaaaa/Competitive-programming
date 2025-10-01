def __main__():
    N = int(input())
    point = list(map(int, input().split()))
    r = 1
    cnt = 0
    ranking = [0 for _ in range(N)]
    sort_point = sorted(point, reverse=True)
    max_point = sort_point[0]

    for i in range(N):
        for j in range(N):
            if max_point == point[j]:
                cnt += 1
                ranking[j] = r
        
        if all(n > 0 for n in ranking):
            for i in ranking:
                print(i)
            break
        r += cnt
        max_point = sort_point[r - 1]
        cnt = 0



if __name__ == "__main__":
    __main__()

