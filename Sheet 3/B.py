n = int(input())
numbers = list(map(int, input().split()))
index = 0
flag = False
x = int(input())
for number in numbers:
    if x == number:
        print(index)
        flag = True
        break
    index += 1
if not flag:
    print(-1)