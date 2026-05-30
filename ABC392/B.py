n, m = map(int, input().split())
value = list(map(int, input().split()))
if n == len(value):
    print(0)
else:
    N = [u for u in range(1, n+1)]
    for i in value:
        for a in N:
            if a == i:
                N.remove(a)
    print(len(N))
    print(" ".join(map(str, N)))
