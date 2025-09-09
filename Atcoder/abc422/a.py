token = input()

a=int(token[0])
b=int(token[2])

if(b<8):
    print(f"{a}-{b+1}")
elif(b==8):
    print(f"{a+1}-{1}")
