n = int(input())
array = list(map(int, input().split()))

min_value = min(array)
counter = array.count(min_value)

if(counter % 2 == 1):
    print("Lucky")
else:
    print("Unlucky")