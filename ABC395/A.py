N = int(input())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    if i == 0:
        continue
    elif A[i] <= A[i-1]:
        print("No")
        break
    else:
        count += 1

if count == N-1:
    print("Yes")




