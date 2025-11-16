n = int(input())

array = list(map(int, input().split()))
array.reverse()
print(" ".join(map(str, array)))