S = input()
T = [None] * len(S)
for s in range(len(S)):
  if s == 0:
    if S[s] == '.':
      T[0] = 'o'
    elif S[s] == '#':
      T[0] = '#'
    else:
      T[0] = '.'
  elif S[s] == '#':
    T[s] = '#'
  elif S[s-1] == '#' and S[s] == '.':
    T[s] = 'o'
  else:
    T[s] = '.'
print(''.join(map(str, T)))
