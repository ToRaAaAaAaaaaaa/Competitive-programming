X, Y, Z = map(int, input().split())
tf = 0
for i in range(0, 100):
  if (X+i)%(Y+i) == 0 and (X+i)//(Y+i) == Z:
    print('Yes')
    tf = 1
    break
if tf == 0:
  print('No')