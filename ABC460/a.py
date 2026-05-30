n, m = map(int, input().split())
cnt = 0
while n % m != 0:
    m = n % m
    cnt += 1

print(cnt+1)