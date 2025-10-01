N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

top_card = [0 for _ in range(100)]

for i in range(N):
    if A[i][0] == 1:
        top_card.insert(0, A[i][1])
    else:
        print(top_card[0])
        top_card.remove(top_card[0])


