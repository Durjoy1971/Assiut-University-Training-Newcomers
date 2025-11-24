test_case = int(input())
for _ in range(test_case):
    a, b, c = map(int, input().split())
    print(min(a, c, (a + b + c) // 3))
       