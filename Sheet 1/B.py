tokens = input().split()

a = int(tokens[0])          # integer
b = int(tokens[1])          # long long int
ch = tokens[2]              # character
c = float(tokens[3])        # float
d = float(tokens[4])        # double (Python float)

print(a, b, ch, f"{c:.2f}", f"{d:.1f}", sep='\n')