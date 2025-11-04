# import math

def prime_checker(num):
    if num <= 1:
        return False
    # for i in range(2, math.isqrt(num) + 1):
    # for i in range(2, int(num**0.5) + 1):
    #     if num % i == 0:
    #         return False
    i = 1
    while i * i <= num:
        if i > 1 and num % i == 0:
            return False
        i += 1
    return True

x = int(input())

if prime_checker(x):
    print("YES")
else:
    print("NO")