A, B, C = map(int, input().split())
ans = [A, B, C]
ans = sorted(ans, reverse=True)
print(''.join(map(str, ans)))