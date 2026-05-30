N=int(input())
S=0
for i in range(1,N+1):
    S+=(-1)**i * i**3
print(S)