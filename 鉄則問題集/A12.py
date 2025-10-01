N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(x, N, K, A):
    sum = 0
    for i in range(N):
        sum += Mid // A[i]
    
    if sum >= K:
        return True
    return False

LEFT = 1
RIGHT = 10 ** 9
while LEFT < RIGHT:
    Mid = (LEFT + RIGHT) // 2
    Answer = check(Mid, N, K, A)

    if Answer == True:
        RIGHT = Mid
    elif Answer == False:
        LEFT = Mid + 1

print(RIGHT)