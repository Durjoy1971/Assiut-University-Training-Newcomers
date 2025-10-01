a , b = input().split()

a = float(a)
b = float(b)

if(a == 0.0 and b == 0.0):
    print("Origem")
elif(a >= 0.01 and b >= 0.01):
    print("Q1")
elif(a <= -0.01 and b >= 0.01):
    print("Q2")
elif(a <= -0.01 and b <= -0.01):
    print("Q3")
elif(a >= 0.01 and b <= -0.01):
    print("Q4")
elif(a == 0.0):
    print("Eixo Y")
elif(b == 0.0):
    print("Eixo X")