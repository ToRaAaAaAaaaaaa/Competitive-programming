def CalculateAttendanceFee(g):
    if g < 5:
        return g*2000
    elif g < 20:
        return g*1800
    else:
        return g*1500

g = int(input())
print(CalculateAttendanceFee(g))