N,M = map(int, input().split())
ans = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    ans[A].append(B)
    ans[B].append(A)

for i in range(1,N+1):
    print(f"{i}:" + " {" + ', '.join(map(str, ans[i])) + "}")