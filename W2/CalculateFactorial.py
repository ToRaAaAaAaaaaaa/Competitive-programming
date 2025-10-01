def CalculateFactorial(g):
    ans=1
    if g==0:
        return ans
    else:
        for i in range(1, g+1):
            ans = ans * i
        return ans

g=int(input())
print(CalculateFactorial(g))