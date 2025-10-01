N = int(input())
A = list(map(int, input().split()))

pt=0
for i in range(N):
    if i == 0:
        continue
    elif A[i] == A[i-1]:
        pt += 1
        if pt == 2:
            print("Yes")
            break
    else:
        pt = 0

if pt == 0:
    print("No")
