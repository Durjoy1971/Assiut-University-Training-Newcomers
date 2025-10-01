l1, r1, l2, r2 = map(int, input().split())

if r1 < l2 or r2 < l1:
    print(-1)
else:
    print(max(l1, l2), min(r1, r2))