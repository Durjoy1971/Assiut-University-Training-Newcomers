n = int(input())

array = list(map(int, input().split()))

min_value = min(array)
find_index = array.index(min_value)

print(f"{min_value} {find_index+1}")