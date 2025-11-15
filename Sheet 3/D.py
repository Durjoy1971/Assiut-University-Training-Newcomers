n = int(input())

array = list(map(int, input().split()))

for i in range(n):
    if array[i] < 10:
        print(f"A[{i}] = {array[i]}")