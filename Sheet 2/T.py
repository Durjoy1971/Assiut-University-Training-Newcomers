n = int(input())

for row in range(1, n+1):
    print(' ' * (n-row), end='')
    print('*' * (2*row - 1))