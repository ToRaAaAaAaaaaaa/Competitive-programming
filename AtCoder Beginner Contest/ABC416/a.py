N, L, R = map(int, input().split())
S = input()
tf = 1
for i in range(L-1, R):
  if S[i] == 'o':
    continue
  else:
    tf = 0
    break

if tf == 1:
  print('Yes')
else:
  print('No')
