a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

list1 = [a, b, c]
list2 = list1.copy()

list1.sort()
print(list1[0])
print(list1[1])
print(list1[2])
print()
print(list2[0])
print(list2[1])
print(list2[2])