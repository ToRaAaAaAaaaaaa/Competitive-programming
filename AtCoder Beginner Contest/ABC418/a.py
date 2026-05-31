N = int(input())
S = input()
if N  >= 3:
    if S[N-3] == 't' and S[N-2] == 'e' and S[N-1] == 'a':
        print('Yes')
    else:
        print('No')
else:
    print('No')