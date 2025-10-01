N = int(input())
people = [None] * (N+1)
for i in range(1, N+1):
    people[i] = input()
X, Y = map(str, input().split())
if people[int(X)] == Y:
    print('Yes')
else:
    print('No')