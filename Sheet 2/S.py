t = int(input())

for i in range(t):
    a , b = map(int, input().split())
    if(a > b):
        a, b = b, a
    total = sum(j for j in range(a+1, b) if j % 2 != 0)
    print(total)