S=input()
ss=S[0]
if ss!=S[1]:
    if ss==S[-1]:
        print(S[1])
    else:
        print(ss)
else:
    for i in range(len(S)):
        if ss!=S[i]:
            print(S[i])
            break
    