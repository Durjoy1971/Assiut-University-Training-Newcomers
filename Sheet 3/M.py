n = int(input())

array = list(map(int, input().split()))

min_value = min(array)
max_value = max(array)

min_index = array.index(min_value)  
max_index = array.index(max_value)

array[min_index], array[max_index] = array[max_index], array[min_index]

print(" ".join(map(str, array)))