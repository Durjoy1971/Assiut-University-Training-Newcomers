N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

for row in A:
    print(' '.join(map(str, row[::-1])))