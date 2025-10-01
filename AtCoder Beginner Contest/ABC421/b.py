X, Y = map(int, input().split())
A = [X, Y]

for i in range(3, 11):
    num = str(A[i-2] + A[i-3])
    num = ''.join(reversed(num))
    A.append(int(num))
print(A[9])