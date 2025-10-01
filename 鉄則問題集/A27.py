A, B = map(int, input().split())

def GCD(A, B):
    while (A >= 1 and B >= 1):
        if A >= B:
            num = A % B
            A = num
        else:
            num = B % A
            B = num
    if A == 0:
        return B
    else:
        return A

answer = GCD(A, B)
print(answer)