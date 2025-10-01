N = int(input())
T = [None] * (N)
A = [None] * (N)

for i in range(N):
    T[i], A[i] = map(str, input().split())
    A[i] = int(A[i])

for a in range(N):
    A[a] = A[a] % 10000
Answer = 0
for j in range(N):
    if T[j] == "+":
        Answer += A[j]
    elif T[j] == "-":
        Answer -= A[j]
        if Answer < 0:
            Answer += 10000
    else:
        Answer *= A[j]
        Answer = Answer % 10000
    ans = Answer % 10000
    print(ans)