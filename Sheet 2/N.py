s = input()

n = int(input())

# input() -> input => string "25_23_3"
# input().split(' ') -> ['25', '23', '3']
# map(int, input().split()) -> map object of integers -> map object of [25, 23, 3]
# list(map(int, input().split())) -> [25, 23, 3]

arr = list(map(int, input().split()))

for i in range(n):
    number_of_iteration = arr[i]
    print(s*number_of_iteration)