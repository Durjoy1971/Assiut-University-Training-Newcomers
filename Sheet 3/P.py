n = int(input())

array = list(map(int, input().split()))
answer = 0

while array[0] % 2 == 0:
    answer += 1
    array[0] //= 2

for i in range(1, n):
    count = 0
    while array[i] % 2 == 0:
        count += 1
        array[i] //= 2
    answer = min(answer, count)

print(answer)