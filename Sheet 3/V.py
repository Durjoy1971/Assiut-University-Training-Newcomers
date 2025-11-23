n, m = map(int, input().split())

ar = list(map(int, input().split()))

# we will use map to count occurrences of each element in ar
count_map = {}
for num in ar:
    if num in count_map:
        count_map[num] += 1
    else:
        count_map[num] = 1

# time complexity is O(n)
# time complexity to find each element in map is O(1)

for i in range(1, m + 1):
    print(count_map.get(i, 0))

