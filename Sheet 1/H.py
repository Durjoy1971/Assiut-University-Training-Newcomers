token = input().split()

a = int(token[0])
b = int(token[1])

print(f"floor {a} / {b} = {a // b}")
print(f"ceil {a} / {b} = {(a + b - 1) // b}")
print(f"round {a} / {b} = {int(a / b + 0.5)}")