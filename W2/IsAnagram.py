def IsAnagram(S, L):
    S,L=sorted(S),sorted(L)
    s,l=len(S),len(L)
    if s!=l:
        return 'false'
    for i in range(s):
        if S[i] != L[i]:
            return 'false'
    return 'true'

S, L = map(str, input().split())
print(IsAnagram(S, L))