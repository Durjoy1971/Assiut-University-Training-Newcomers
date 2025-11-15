k , s = map(int, input().split())
count = 0
for i in range(0, k+1):
    for j in range(0, k+1):
        ans = s - (i+j)
        if(ans >= 0 and ans <= k):
            count += 1
print(count)