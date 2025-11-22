n = int(input())

array = []

for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)

sum_main = sum_secondary = 0

for r in range(n):
    for c in range(n):
        if r == c:
            sum_main += array[r][c]
        if r + c == n-1:
            sum_secondary += array[r][c]
            
print(abs(sum_main - sum_secondary))