x = input()

# Determine whether X is Digit or Alphabet and if it is Alphabet determine if it is Capital Case or Small Case.
if x.isdigit():
    print("IS DIGIT")
elif x.isalpha():
    if x.isupper():
        print("ALPHA\nIS CAPITAL")
    else:
        print("ALPHA\nIS SMALL")