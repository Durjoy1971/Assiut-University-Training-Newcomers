n , m = map(int, input().split())

ar = list(map(int, input().split()))
br = list(map(int, input().split()))

i = j = count = 0

while i < n and j < m:
    if ar[i] == br[j]:
        count += 1
        i += 1
        j += 1
    else:
        i += 1

if count == m:
    print("YES")
else:
    print("NO")