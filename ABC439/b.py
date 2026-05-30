N = str(input())
number = []
I = 0
tf=1
while I!=1:
    for i in range(len(N)):
        I += int(N[i])**2
    if I==1:
        break
    if I in number:
        print('No')
        tf=0
        break
    number.append(I)
    N=str(I)

    I = 0
if tf:
    print('Yes')