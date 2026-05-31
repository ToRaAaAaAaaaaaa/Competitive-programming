Q = int(input())

for _ in range(Q):
    X = int(input())
    tf = 1
    Max = int(X**(0.5))
    for i in range(2, Max+1):
        if X % i == 0:
            tf = 0
            break
    if tf == 1:
        print('Yes')
    else:
        print('No')