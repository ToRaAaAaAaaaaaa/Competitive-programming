A = int(input())
Al = list(map(int, input().split()))
ans = 0
for i in range(A):
    if i % 2 == 0:
        ans += Al[i]
print(ans)