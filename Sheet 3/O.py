n = int(input())

array = [0, 0, 1]

for i in range(3, n + 1):
    next_value = array[i - 2] + array[i - 1]
    array.append(next_value)

print(array[n])