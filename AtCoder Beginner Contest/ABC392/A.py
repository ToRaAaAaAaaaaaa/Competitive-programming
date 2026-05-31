a, b, c = map(float, input().split())
if a * b == c:
    print('Yes')
elif a * c == b:
    print('Yes')
elif b * c == a:
    print('Yes')
else:
    print('No')