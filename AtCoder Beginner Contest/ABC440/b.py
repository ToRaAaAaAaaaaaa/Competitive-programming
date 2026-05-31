N=int(input())
T = list(map(int, input().split()))

t = [[T[i], i+1]for i in range(N)]

T=sorted(t)

T=sorted(T)
T = [T[i][1]for i in range(N)]
print(T[0], T[1], T[2])
