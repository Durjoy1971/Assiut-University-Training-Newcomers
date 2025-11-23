row, col = map(int, input().split())

arr = [['x'] * (col + 2) for _ in range(row + 2)]

for i in range(1, row + 1):
    line = input()
    for j in range(1, col + 1):
        arr[i][j] = line[j - 1]

a, b = map(int, input().split())

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

flag = True
for dx, dy in directions:
    if arr[a + dx][b + dy] != 'x':
        flag = False
        break

print("yes" if flag else "no")
