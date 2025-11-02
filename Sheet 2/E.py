n = int(input())
a = list(map(int, input().split()))

max_number = a[0]

for i in range(1, n):
    if a[i] > max_number:
        max_number = a[i]

print(max_number)