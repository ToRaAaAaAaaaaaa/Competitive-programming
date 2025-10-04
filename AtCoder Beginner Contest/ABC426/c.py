n, q = map(int, input().split())

pc = [0] + [1] * n
o = 1

for _ in range(q):
    x, y = map(int, input().split())
    res = 0
    
    while o <= x:
        res += pc[o]
        pc[y] += pc[o]
        o += 1
    
    print(res)