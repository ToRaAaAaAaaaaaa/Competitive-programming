N, L, R = map(int, input().split())
ans = 0
for youser in range(1, N+1):
    X, Y = map(int, input().split())
    if X <= L and R <= Y:
        ans += 1

print(ans)