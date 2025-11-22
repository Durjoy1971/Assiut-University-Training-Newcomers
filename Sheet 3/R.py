count = 0
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Twin = 0

for i in range(n):
    for j in range(n):
        if B[i] == A[j]:
            Twin += 1
            B[i] = -100
            A[j] = -200
            break
    if Twin == n:
        break

if(Twin == n):
    print("yes")
else:
    print("no")