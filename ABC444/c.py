N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
SA = set(A)
DA = {int(i):0 for i in SA}
for i in range(N):
    DA[A[i]] += 1
Ma = A[-1]
ma = A[0]
ans = []

if len(DA) == 1:
    ans.append(ma)
    if DA[ma] % 2 == 0:
        s = ma*2
        ans.append(s)
elif len(DA) == 2:
    if DA[ma] == DA[Ma]:
        s = ma + Ma
        ans.append(s)
    if DA[ma] % 2 == 0 and ma*2==Ma:
        s = ma*2
        ans.append(s)
else:
    if N == 3:
        ans.append(ma + A[1])
    else:
        for i in range(N):
            if (N-i) % 2 == 0:
                if A[0] + A[-1-i] == A[1] + A[-2-i]:
                    I = A[0] + A[-1-i]
                    tf = True
                    for j in range((N-i)//2):
                        if A[j] + A[-1-i-j] != A[j+1] + A[-2-i-j]:
                            tf = False
                            break
                    if tf:
                        ans.append(I)
                        break

print(' '.join(map(str, sorted(ans))))