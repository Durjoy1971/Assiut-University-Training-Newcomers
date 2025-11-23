n , q = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

# Binary search function to print a "found" if the number X exists in array otherwise, print "not found".
def binary_search(array, target):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return "found"
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "not found"

for _ in range(q):
    x = int(input())
    print(binary_search(arr, x))