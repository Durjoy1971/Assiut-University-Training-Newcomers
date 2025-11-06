while 1:
    a , b = map(int, input().split())
    
    if(a > b):
        a, b = b, a
    
    if a <= 0 or b <= 0:
        break
    
    sum = 0

    for i in range (a, b+1):
        sum += i
        print(i, end=' ')
    print(f"sum ={sum}")

