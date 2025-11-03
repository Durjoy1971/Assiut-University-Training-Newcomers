t = int(input())

for i in range(t):
    n = int(input())
    # factorial calculation
    fact = 1
    for j in range(1, n + 1):
        fact *= j
    print(fact)