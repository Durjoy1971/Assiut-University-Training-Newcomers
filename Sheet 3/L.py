test_case = int(input())
for _ in range(test_case):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        print(arr[i], end=' ')
    for i in range(n):
        maxx = arr[i]
        for j in range(i+1, n):
            maxx = max(maxx, arr[j])
            print(maxx, end=' ')
    print()