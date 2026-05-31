N = int(input())
D = list(map(int, input().split()))

for i in range(N-1):
    distance_list = []
    distance = 0
    for j in range(i, N-1):
        distance += D[j]
        distance_list.append(distance)
    print(' '.join(map(str, distance_list)))