def __main__():
    N = int(input())
    A = list(map(int, input().split()))

    A_max = max(A)
    A.remove(A_max)
    A_sec_max = max(A)

    sum = A_max + A_sec_max
    print(sum)
    
if __name__ == '__main__':
    __main__()