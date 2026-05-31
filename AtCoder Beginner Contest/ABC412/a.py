N = int(input())
cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    if b - a > 0:
        cnt += 1

print(cnt)