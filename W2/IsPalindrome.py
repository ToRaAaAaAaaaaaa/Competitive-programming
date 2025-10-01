def IsPalindrome(S):
    w=len(S)
    for i in range(w//2):
        if S[i] != S[-1*(i+1)]:
            return 'false'
    return 'true'

S = input()
print(IsPalindrome(S))