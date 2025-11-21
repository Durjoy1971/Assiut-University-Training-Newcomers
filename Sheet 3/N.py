a, b = map(int,input().split())

array = list(input())

counter = array.count('-')

if counter == 0 or counter > 1 or array[a] != '-':
    print('No')
else:
    print('Yes')