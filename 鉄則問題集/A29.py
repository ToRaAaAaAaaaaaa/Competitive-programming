a, b = map(int, input().split())

ans = 1
tmp = a
while b >= 1:
    if b % 2 == 0:
        tmp *= tmp
    else:
        ans *= tmp
        tmp *= tmp
        ans %= (10**9+7)
    tmp %= (10**9+7)
    b = b // 2
print(ans)