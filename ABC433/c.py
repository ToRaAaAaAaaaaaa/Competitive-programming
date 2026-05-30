S = str(input())
L = len(S)
num_list=[]
cnt_list=[]
cnt = 0
for i in range(L):
  if i == 0:
    num_list.append(int(S[i]))
    cnt += 1
  elif S[i]==S[i-1]:
    cnt += 1
  elif S[i]!=S[i-1]:
    cnt_list.append(cnt)
    cnt = 1
    num_list.append(int(S[i]))
  if i == L-1:
    cnt_list.append(cnt)
# print(num_list)
# print(cnt_list)

nl = len(num_list)
cl = len(cnt_list)

ans = 0

for j in range(1,nl):
  if num_list[j] - num_list[j-1] == 1:
    ans += min(cnt_list[j], cnt_list[j-1])
print(ans)