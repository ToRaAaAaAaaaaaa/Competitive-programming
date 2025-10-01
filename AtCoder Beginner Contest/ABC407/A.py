def __main__():
    A, B = map(int, input().split())
    num = A / B
    ans_one = A // B + 1
    ans_two = A // B
    if (ans_one - num) <= (num - ans_two):
        print(ans_one)
    else:
        print(ans_two)

if __name__ == '__main__':
    __main__()