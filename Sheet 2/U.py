n,a,b = map(int, input().split())

# def sum_digits(n):
#     return sum(int(digit) for digit in str(n))

# answer = 0

# for number in range(1, n+1):
#     output = sum_digits(number)
#     if a <= output and output <= b:
#         answer += number

# print(answer)

print(sum(number for number in range(1, n+1) if a <= sum(map(int,str(number))) <= b))
