a , b = map(int, input().split())

answer = 1

for i in range(1, min(a, b)+1):
    if (a % i == 0) and (b % i == 0):
        answer = i

print(answer)