T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    # abc = min(a, b, c)
    # a-=abc
    # b-=abc
    # c-=abc
    # aac = min(a//2, c)
    # print(abc+aac)
    print(min(a, c, (a+b+c)//3))