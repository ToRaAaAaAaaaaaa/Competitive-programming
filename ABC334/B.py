A, M, L, R = map(int, input().split())

ans = 0
if L <= A and A <= R:
    ans += (abs(A-L) + abs(R-A))//M
    if ans > 0:
        ans += 1
elif A <= L:
    ans += 1
    ans += (abs(R-A) - abs(L-A))//M
    if ans > 0:
        ans += 1
elif R <= A:
    ans += (abs(A-L) - abs(A-R))//M
    if ans > 0:
        ans += 1
print(ans)