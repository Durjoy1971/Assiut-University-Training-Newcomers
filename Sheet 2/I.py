n = list(map(int, input()))

copy_n = ''.join(map(str, n))

while n[-1] == 0:
    # time complexity O(1)
    n.pop()

# time complexity O(len(n))
n = ''.join(map(str, n))

# time complexity O(len(n))
reversed_n = n[::-1]

if copy_n == reversed_n:
    print(reversed_n, "YES", sep='\n')
else:
    print(reversed_n, "NO", sep='\n')