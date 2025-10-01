a = float(input())

if a - int(a) == 0:
    print(f"int {int(a)}")
else:
    print(f"float {int(a)} {a - int(a):.3f}")