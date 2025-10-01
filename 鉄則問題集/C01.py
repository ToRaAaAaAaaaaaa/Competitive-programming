def __main__():
    N = float(input())
    tax = 0.1

    tax_N = N * (1 + tax)
    print(int(tax_N))
    
if __name__ == '__main__':
    __main__()