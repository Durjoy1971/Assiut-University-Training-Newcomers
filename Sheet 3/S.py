N = []
M1, M2 = map(int, input().split())
for _ in range(M1):
    row = list(map(int, input().split()))
    N.append(row)

X = int(input())
found = False

for i in range(M1):
    for j in range(M2):
        if X == N[i][j]:
            found = True
            break
    if found:
        break

if not found:
    print("will take number")
else:
    print("will not take number")