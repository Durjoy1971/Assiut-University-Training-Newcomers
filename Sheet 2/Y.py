n = int(input())

first = 0
second = 1

for i in range(1, n+1):
    if i == 1:
        print(first, end=' ')
    elif i == 2:
        print(second, end=' ')
    else:
        next = first + second
        print(next, end=' ')
        first = second
        second = next
    