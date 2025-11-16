n = int(input())

array = list(map(int, input().split()))

left = 0
right = n - 1
flag = True

while left <= right:
    if array[left] != array[right]:
        flag = False
        break
    left += 1
    right -= 1
    
if flag:
    print("YES")
else:
    print("NO")    