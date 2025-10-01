a, s, b, q, c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

if s == '+':
    if a + b == c:
        print('Yes')
    else:
        print(a+b)
elif s == '-':
    if a - b == c:
        print('Yes')
    else:
        print(a-b)
elif s == '*':
    if a * b == c:
        print('Yes')
    else:
        print(a*b)