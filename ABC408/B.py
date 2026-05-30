def __main__():
    N = int(input())
    A = list(map(int, input().split()))
    setA = set(A)
    setA = sorted(setA)
    print(len(setA))
    print(' '.join(str(a) for a in setA))
    
        
if __name__ == '__main__':
    __main__()