N = int(input())
A = list(map(int, input().split()))
v = []
for i in range(N):
    v.append(A[i])
    if len(v)>=4 and v[-1]==v[-2]==v[-3]==v[-4]:
        for j in range(4):
            v.pop()
print(len(v))