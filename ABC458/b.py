H, W = map(int, input().split())

L = []
for i in range(H):
    A = []
    for j in range(W):
        a = 0
        if i in [0, H-1] and j in [0, W-1]:
            a += 1
            if H == 1 and W == 1:
                a = 0
            elif H == 1 or W == 1:
                a += 0
            else:
                a += 1
        elif i in [0, H-1] or j in [0, W-1]:
            a += 2
            if H == 1 or W == 1:
                a += 0
            else:
                a += 1
        else:
            a = 4
        A.append(a)
    L.append(A)

for i in range(H):
    print(" ".join(map(str, L[i])))
