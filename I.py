s = input().strip()

# Remove trailing zeros (they don't affect the palindrome property the problem expects)
s = s.rstrip('0')

# If the string becomes empty (input was all zeros), treat it as a palindrome
if s == "":
    print("YES")
else:
    if s == s[::-1]:
        print("YES")
    else:
        print("NO")
        
        
