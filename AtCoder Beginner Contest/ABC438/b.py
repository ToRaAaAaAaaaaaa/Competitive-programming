N, M = map(int, input().split())
S = input()
T = input()
ans = 10**9
for i in range(N-M+1):
    A = 0
    for j in range(M):
        if int(S[i+j]) > int(T[j]):
            a = int(S[i+j])-int(T[j])
        elif int(S[i+j]) < int(T[j]):
            a = int(S[i+j]) + 10 - int(T[j])
        else:
            a=0
        A+=a
    if A < ans:
        ans = A
print(ans)