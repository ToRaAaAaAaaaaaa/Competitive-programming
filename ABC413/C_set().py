N, Q = map(int, input().split())
A = list(map(int, input().split()))

black_list = set()
dimention = 0
for i, a in enumerate(A):
    if a in black_list:
        if (a-1 in black_list) and (a+1 in black_list):
            dimention += 1
        elif (a-1 not in black_list) and (a+1 not in black_list):
            dimention -= 1
        black_list.remove(a)
    else:
        if (a-1 in black_list) and (a+1 in black_list):
            dimention -= 1
        elif (a-1 not in black_list) and (a+1 not in black_list):
            dimention += 1
        black_list.add(a)
    print(dimention)
    