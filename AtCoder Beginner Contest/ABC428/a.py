S,A,B,X=map(int, input().split())
cnt = X//(A+B)
subcnt=min(X%(A+B),A)
print(S*(cnt*A+subcnt))