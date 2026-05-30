A = []
fo = [0 for i in range(3)]
fi = [0 for i in range(3)]
si = [0 for i in range(3)]
for n in range(3):
    D = list(map(int, input().split()))
    for i in range(6):
        if D[i] == 4:
            fo[n] += (1 / 6)
        if D[i] == 5:
            fi[n] += (1 / 6)
        if D[i] == 6:
            si[n] += (1 / 6)

ans = 0
for l in range(3):
    for m in range(3):
        for n in range(3):
            if l != m and l != n and m != n:
                ans += l * m * No

print(ans)