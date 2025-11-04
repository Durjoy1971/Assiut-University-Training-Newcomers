exist = False

a, b = map(int, input().split())

# The Lucky number is any positive number that its decimal representation contains only 4 and 7.
def lucky_number(n):
    s = str(n)
    for char in s:
        if char != '4' and char != '7':
            return False
    return True    

for i in range(a, b + 1):
    if lucky_number(i):
        exist = True
        print(i, end=' ')

if not exist:
    print(-1)