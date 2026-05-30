N, K  = map(int, input().split())
A = list(map(int, input().split()))
setA = set(A)
setA = sorted(setA)
setA = list(setA)

B = {setA[i]:0 for i in range(len(setA))}
for i in range(N):
    B[A[i]] += 1

C = {setA[i] * B[setA[i]]: setA[i] for i in range(len(setA))}
D = [setA[i] * B[setA[i]] for i in range(len(setA))]

E = sorted(D, reverse=True)

# F = [C[E[i]] for i in range(min(K, len(setA)))]
F = min(K, len(setA))
for i in range(len(E)):
    if i < F:
        E[i] = 0
print(sum(E))
    

# ans = 0
# for i in range(N):
#     if A[i] in F:
#         continue
#     ans += A[i]

# print(ans)
