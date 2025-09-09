token = input().split()
a, b = map(int, token)

if max(a,b) % min(a,b) == 0:
    print("Multiples")
else:
    print("No Multiples")