n = int(input())
array = list(map(int, input().split()))



even = odd = positive = negative = 0

for i in range(n):
    num = array[i]
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Positive: {positive}")
print(f"Negative: {negative}")