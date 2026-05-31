from math import sqrt

for i in range(int(input())):
    x, y, r, X, Y, R = map(int, input().split())
    # print(((X - x)**2 + (Y - y)) ** 0.5)
    # if sqrt(((X - x)**2 + (Y - y)**2)) <= r + R:
    #     print("Yes")
    # else:
    #     print("No")
    if (abs(r - R))**2 <= ((X - x)**2 + (Y - y)**2) <= (r + R)**2:
        print("Yes")
    else:
        print("No")