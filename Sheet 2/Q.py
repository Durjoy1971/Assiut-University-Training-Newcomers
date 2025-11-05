t = int(input())

for _ in range(t):
    n = input()
    # Reversing the string n
    n = n[::-1]
    # how to iterate through the string and print each character in new line
    for character in n:
        print(character, end=' ')
    print()