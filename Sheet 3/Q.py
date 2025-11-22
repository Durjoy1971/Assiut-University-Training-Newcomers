test_case = int(input())

for _ in range(test_case):
    count = 0
    n = int(input())
    array = list(map(int, input().split()))
    for i in range(n):
        for j in range(i, n):
            min = array[i]
            condition = True
            for k in range(i, j+1):
                if min > array[k]:
                    condition = False
                else:
                    min = array[k]
            if condition:
                count += 1
            if not condition:
                break
    print(count)