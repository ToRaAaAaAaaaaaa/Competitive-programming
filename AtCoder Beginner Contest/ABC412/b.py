S = input()
T = input()
Omoji_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

tf = 1
for s in range(len(S)):
    if s == 0:
        continue
    elif S[s] in Omoji_list:
        if S[s-1] not in T:
            print('No')
            tf = 0
            break

if tf == 1:
    print('Yes')
    