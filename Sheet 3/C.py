n = int(input())
for number in input().split():
    number = int(number)
    if number == 0:
        print('0', end=' ')
    elif number < 0:
        print(2, end=' ')
    else:
        print(1, end=' ')