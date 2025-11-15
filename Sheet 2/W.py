n = int(input())

for row in range(1, n + 1):
    print(' ' * (n-row),end='')
    print('*' * (row*2-1))

for row in range(1, n+1):
    print(' ' * (row-1), end='')
    print('*' * ((n*2)-(row*2-1)))