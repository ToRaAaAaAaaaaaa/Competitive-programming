def FizzBuzz(a,b):
    l = []
    for i in range(a, b+1):
        if i % 15 == 0:
            l.append('FizzBuzz')
        elif i % 3 == 0:
            l.append('Fizz')
        elif i % 5 == 0:
            l.append('Buzz')
        else:
            l.append(i)
    return ', '.join(map(str, l))

a, b= map(int, input().split())
print(FizzBuzz(a,b))