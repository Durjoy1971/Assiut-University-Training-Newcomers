# Python Knowledge Guide - Sheet 1 (A-Z Problems)

## 🎯 Purpose
This guide provides all essential Python knowledge needed to solve problems A.py through Z.py. It's designed for:
- Beginners learning Python from scratch
- Programmers transitioning from other languages (C++, Java, etc.)
- Anyone who wants to implement logic without struggling with Python syntax

---

## 📚 Table of Contents
1. [Input/Output Basics](#1-inputoutput-basics)
2. [Data Types & Type Conversion](#2-data-types--type-conversion)
3. [String Operations](#3-string-operations)
4. [Arithmetic Operations](#4-arithmetic-operations)
5. [Conditional Statements](#5-conditional-statements)
6. [Built-in Functions](#6-built-in-functions)
7. [Lists & Collections](#7-lists--collections)
8. [String Formatting](#8-string-formatting)
9. [Mathematical Operations](#9-mathematical-operations)
10. [Problem-by-Problem Concepts](#10-problem-by-problem-concepts)

---

## 1. Input/Output Basics

### Reading Input
```python
# Single line input as string
s = input()                    # Example: "Hello"

# Reading and splitting into tokens
tokens = input().split()       # Example: "10 20" → ["10", "20"]

# Reading multiple values on same line
a, b = input().split()         # Unpacking into variables
```

### Printing Output
```python
# Simple print
print("Hello")

# Print multiple values (space-separated by default)
print(a, b, c)                 # Output: a b c

# Print with custom separator
print(a, b, c, sep='\n')       # Each on new line

# Print with custom ending (default is '\n')
print("Hello", end=' ')        # No newline at end
```

**Used in:** A.py, B.py, C.py, D.py, E.py, F.py, G.py, H.py, I.py, J.py, K.py, L.py, M.py, N.py, O.py, P.py, Q.py, R.py, S.py, T.py, U.py, V.py, W.py, X.py, Y.py

---

## 2. Data Types & Type Conversion

### Basic Types
```python
# Integer
a = 10
a = int("10")                  # String to int

# Float (handles both float and double from C++)
b = 3.14
b = float("3.14")              # String to float

# String
s = "Hello"
ch = "A"                       # Single character (no char type in Python)

# Boolean
flag = True
flag = False
```

### Type Conversion
```python
# String to number
num = int("123")               # String to integer
num = float("3.14")            # String to float

# Number to string
s = str(123)                   # Integer to string

# Checking types
isinstance(x, int)             # Check if x is integer
type(x)                        # Get type of x
```

**Used in:** B.py, C.py, D.py, E.py, F.py, G.py, H.py, I.py, J.py, K.py, O.py, P.py, Q.py, R.py, S.py, T.py, U.py, V.py, W.py, X.py, Y.py

---

## 3. String Operations

### String Methods
```python
# Character checking
s.isdigit()                    # Check if string is digit
s.isalpha()                    # Check if string is alphabetic
s.isupper()                    # Check if uppercase
s.islower()                    # Check if lowercase

# Case conversion
s.upper()                      # Convert to uppercase
s.lower()                      # Convert to lowercase

# String splitting
s.split()                      # Split by whitespace
s.split('+')                   # Split by specific character
s.split(' ')                   # Split by space

# String indexing
s[0]                           # First character
s[1]                           # Second character
s[-1]                          # Last character

# Checking substring
'+' in s                       # Check if '+' exists in string
```

**Used in:** A.py, B.py, L.py, M.py, N.py, O.py, P.py, V.py, W.py

---

## 4. Arithmetic Operations

### Basic Operations
```python
# Addition
result = a + b

# Subtraction
result = a - b

# Multiplication
result = a * b

# Division (returns float)
result = a / b                 # Example: 7/2 = 3.5

# Integer Division (floor division)
result = a // b                # Example: 7//2 = 3

# Modulo (remainder)
result = a % b                 # Example: 7%2 = 1

# Exponentiation (power)
result = a ** b                # a raised to power b
```

### Advanced Division Operations
```python
# Floor division
floor_result = a // b

# Ceiling division (manual)
ceil_result = (a + b - 1) // b

# Rounding
round_result = int(a / b + 0.5)
```

**Used in:** C.py, D.py, E.py, F.py, G.py, H.py, O.py, R.py, W.py

---

## 5. Conditional Statements

### If-Elif-Else
```python
# Simple if
if condition:
    # code block
    
# If-else
if condition:
    # code if true
else:
    # code if false

# If-elif-else chain
if condition1:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    # code
```

### Comparison Operators
```python
a == b                         # Equal to
a != b                         # Not equal to
a > b                          # Greater than
a < b                          # Less than
a >= b                         # Greater than or equal
a <= b                         # Less than or equal
```

### Logical Operators
```python
# AND
if a > 0 and b > 0:
    pass

# OR
if a > 0 or b > 0:
    pass

# NOT
if not condition:
    pass
```

**Used in:** I.py, J.py, L.py, M.py, N.py, O.py, P.py, Q.py, S.py, U.py, V.py, W.py, X.py, Y.py

---

## 6. Built-in Functions

### Min/Max Functions
```python
# Find minimum
min_val = min(a, b)            # Minimum of two values
min_val = min(a, b, c)         # Minimum of three values
min_val = min(list)            # Minimum in a list

# Find maximum
max_val = max(a, b)            # Maximum of two values
max_val = max(a, b, c)         # Maximum of three values
max_val = max(list)            # Maximum in a list
```

### Map Function
```python
# Apply function to all elements
a, b = map(int, input().split())           # Convert all to int
numbers = list(map(int, input().split()))  # Create list of ints
```

### Other Useful Functions
```python
# Absolute value
abs(-5)                        # Returns 5

# Length
len(string)                    # Length of string
len(list)                      # Length of list

# Range
range(n)                       # 0 to n-1
range(a, b)                    # a to b-1
```

**Used in:** I.py, J.py, K.py, X.py, Y.py

---

## 7. Lists & Collections

### Creating Lists
```python
# Empty list
my_list = []

# List with values
my_list = [1, 2, 3]

# From input
numbers = list(map(int, input().split()))
```

### List Operations
```python
# Accessing elements
first = my_list[0]             # First element
last = my_list[-1]             # Last element

# Sorting
my_list.sort()                 # Sort in place (modifies original)
sorted_list = sorted(my_list)  # Returns new sorted list

# Copying
new_list = my_list.copy()      # Create a copy
```

**Used in:** T.py

---

## 8. String Formatting

### F-strings (Recommended - Python 3.6+)
```python
# Basic f-string
print(f"Value is {x}")

# With expressions
print(f"{a} + {b} = {a + b}")

# Formatting numbers
print(f"{value:.2f}")          # 2 decimal places
print(f"{value:.9f}")          # 9 decimal places
print(f"{value:.1f}")          # 1 decimal place
```

### Format Method
```python
# Using .format()
print("Result = {}".format(value))
print("{} + {} = {}".format(a, b, a+b))
```

### Precision Control
```python
# Float with specific decimal places
f"{pi:.9f}"                    # 9 decimal places
f"{num:.2f}"                   # 2 decimal places
f"{num:.1f}"                   # 1 decimal place
```

**Used in:** B.py, C.py, D.py, E.py, H.py, R.py, U.py

---

## 9. Mathematical Operations

### Constants
```python
# Pi (manual definition)
pi = 3.141592653

# Or use math module
import math
pi = math.pi
```

### Math Module Functions
```python
from math import log

# Logarithm
log(x)                         # Natural logarithm (base e)
log(x, base)                   # Logarithm with custom base

# Other useful functions
import math
math.sqrt(x)                   # Square root
math.pow(x, y)                 # x raised to power y
math.floor(x)                  # Floor value
math.ceil(x)                   # Ceiling value
```

### Common Formulas
```python
# Area of circle
area = pi * (radius ** 2)

# Sum of first n natural numbers
sum_n = (n * (n + 1)) // 2

# Last digit of number
last_digit = n % 10
```

**Used in:** E.py, F.py, G.py, Y.py

---

## 10. Problem-by-Problem Concepts

### A.py - Hello World with Input
**Concepts:** `input()`, `print()`, string concatenation
```python
s = input()
print('Hello,', s)
```

### B.py - Multiple Data Types
**Concepts:** `split()`, type conversion, f-string formatting with precision
```python
tokens = input().split()
a = int(tokens[0])
c = float(tokens[3])
print(f"{c:.2f}")              # 2 decimal places
```

### C.py - Basic Arithmetic
**Concepts:** Addition, subtraction, multiplication, f-strings
```python
print(f"{a} + {b} = {a + b}")
```

### D.py - Expression Evaluation
**Concepts:** Order of operations, `.format()` method
```python
print("Difference = {}".format((a * b) - (c * d)))
```

### E.py - Circle Area with Precision
**Concepts:** Float input, exponentiation, precision formatting
```python
area = pi * (radius ** 2)
print(f"{area:.9f}")           # 9 decimal places
```

### F.py - Modulo Operation
**Concepts:** Modulo operator `%`, extracting last digit
```python
last_digit = n % 10
```

### G.py - Mathematical Formula
**Concepts:** Integer division `//`, formula implementation
```python
sum_n = (n * (n + 1)) // 2
```

### H.py - Division Types
**Concepts:** Floor `//`, ceiling (manual), rounding
```python
floor = a // b
ceil = (a + b - 1) // b
round = int(a / b + 0.5)
```

### I.py - Comparison
**Concepts:** `map()` function, if-else, comparison operators
```python
a, b = map(int, input().split())
if a >= b:
    print("Yes")
```

### J.py - Divisibility Check
**Concepts:** `min()`, `max()`, modulo for divisibility
```python
if max(a,b) % min(a,b) == 0:
    print("Multiples")
```

### K.py - Min and Max
**Concepts:** `min()` and `max()` with multiple arguments
```python
print(min(a,b,c), max(a,b,c))
```

### L.py - String Comparison
**Concepts:** String indexing, string equality
```python
f1 = input().split()[1]        # Get second word
if f1 == f2:
    print("ARE Brothers")
```

### M.py - Character Classification
**Concepts:** `isdigit()`, `isalpha()`, `isupper()`, `islower()`
```python
if x.isdigit():
    print("IS DIGIT")
elif x.isalpha():
    if x.isupper():
        print("ALPHA\nIS CAPITAL")
```

### N.py - Case Conversion
**Concepts:** `upper()`, `lower()`, case checking
```python
if x.isupper():
    print(x.lower())
else:
    print(x.upper())
```

### O.py - Simple Calculator
**Concepts:** String contains check `in`, string splitting by operator
```python
if '+' in s:
    a, b = s.split('+')
    print(int(a) + int(b))
```

### P.py - Even/Odd Check
**Concepts:** String indexing, modulo for even/odd
```python
s = int(input()[0])            # First character
if s % 2 == 0:
    print("EVEN")
```

### Q.py - Coordinate Quadrants
**Concepts:** Multiple conditions, float comparison, elif chains
```python
if a == 0.0 and b == 0.0:
    print("Origem")
elif a >= 0.01 and b >= 0.01:
    print("Q1")
```

### R.py - Time Conversion
**Concepts:** Integer division `//`, modulo `%`, sequential calculations
```python
year = n // 365
n %= 365                       # Update n with remainder
month = n // 30
```

### S.py - Range Checking
**Concepts:** Range comparisons, elif chains
```python
if 0.00 <= n <= 25.00:
    print("Interval [0,25]")
```

### T.py - Sorting with Original Order
**Concepts:** List creation, `copy()`, `sort()` method
```python
list1 = [a, b, c]
list2 = list1.copy()           # Keep original order
list1.sort()                   # Sort first list
```

### U.py - Integer vs Float Check
**Concepts:** Float to int conversion, decimal extraction
```python
if a - int(a) == 0:            # Check if no decimal part
    print(f"int {int(a)}")
else:
    print(f"float {int(a)} {a - int(a):.3f}")
```

### V.py - Comparison Validator
**Concepts:** String comparison operators, conditional logic
```python
if s == '>':
    if a > b:
        print("Right")
```

### W.py - Equation Validator
**Concepts:** Multiple operators, result validation
```python
if s == '+':
    if a + b == c:
        print('Yes')
    else:
        print(a+b)
```

### X.py - Interval Intersection
**Concepts:** Range overlap logic, `max()`, `min()`
```python
if r1 < l2 or r2 < l1:         # No overlap
    print(-1)
else:
    print(max(l1, l2), min(r1, r2))
```

### Y.py - Logarithmic Comparison
**Concepts:** `math.log()`, logarithm properties
```python
from math import log
if b*log(a) > d*log(c):        # Compare a^b vs c^d
    print('YES')
```

### Z.py - Empty File
**Status:** Not implemented yet

---

## 🎓 Learning Path Recommendation

### For Complete Beginners:
1. Start with A, B, C (Basic I/O and arithmetic)
2. Move to D, E, F, G (More arithmetic and formulas)
3. Try H (Division operations)
4. Practice I, J, K (Conditionals and built-in functions)

### For Programmers from Other Languages:
1. Focus on Python-specific syntax: `split()`, `map()`, f-strings
2. Note: No semicolons, indentation matters, no braces for blocks
3. Key differences:
   - `//` for integer division (not `/`)
   - `**` for power (not `^`)
   - String methods like `.isdigit()`, `.upper()`, `.lower()`
   - `map()` function for type conversion
   - F-strings for formatting (Python 3.6+)

### Advanced Topics:
1. String manipulation (L, M, N, O, P)
2. Complex conditionals (Q, S, V, W)
3. List operations (T)
4. Mathematical operations (Y)

---

## 💡 Common Pitfalls & Tips

### 1. Integer Division
```python
# Wrong (in Python 3)
result = 7 / 2                 # Returns 3.5 (float)

# Correct for integer division
result = 7 // 2                # Returns 3 (int)
```

### 2. Input Handling
```python
# Reading multiple integers
a, b = map(int, input().split())   # Recommended

# vs
tokens = input().split()
a = int(tokens[0])
b = int(tokens[1])                 # More verbose
```

### 3. String Indexing
```python
# Python uses 0-based indexing
s = "Hello"
s[0]                           # 'H' (first character)
s[-1]                          # 'o' (last character)
```

### 4. Precision in Output
```python
# Always specify precision for floats when required
print(f"{value:.2f}")          # 2 decimal places
print(f"{value:.9f}")          # 9 decimal places
```

### 5. Modulo for Last Digit
```python
# Get last digit of any number
last_digit = number % 10
```

### 6. Indentation Matters
```python
# Correct
if condition:
    print("Yes")               # 4 spaces or 1 tab

# Wrong
if condition:
print("Yes")                   # SyntaxError
```

---

## 🔧 Quick Reference

### Input Patterns
```python
# Single value
n = int(input())

# Multiple values (same line)
a, b = map(int, input().split())

# String input
s = input()

# Split and access
tokens = input().split()
first = tokens[0]
```

### Output Patterns
```python
# Simple
print(value)

# Multiple values
print(a, b, c)

# Formatted
print(f"{a} + {b} = {a+b}")

# With precision
print(f"{value:.2f}")

# Custom separator
print(a, b, sep='\n')
```

### Common Operations
```python
# Math
a + b, a - b, a * b            # Basic operations
a / b                          # Float division
a // b                         # Integer division
a % b                          # Modulo
a ** b                         # Power

# String
s.split()                      # Split string
s.upper(), s.lower()           # Case conversion
s.isdigit(), s.isalpha()       # Type checking
s[0], s[-1]                    # Indexing

# Comparison
min(a, b, c)                   # Minimum
max(a, b, c)                   # Maximum
```

---

## 📖 Additional Resources

### Python Documentation
- Official Python Tutorial: https://docs.python.org/3/tutorial/
- Built-in Functions: https://docs.python.org/3/library/functions.html
- String Methods: https://docs.python.org/3/library/stdtypes.html#string-methods

### Practice Tips
1. Type out the code yourself (don't copy-paste)
2. Experiment with different inputs
3. Understand why each line is needed
4. Try solving without looking at solutions first
5. Compare your solution with provided ones

---

## ✅ Checklist for Each Problem

Before solving:
- [ ] Understand the input format
- [ ] Identify required data types
- [ ] Plan the logic/formula
- [ ] Consider edge cases

While coding:
- [ ] Use correct input method
- [ ] Apply proper type conversion
- [ ] Implement logic correctly
- [ ] Format output as required

After solving:
- [ ] Test with sample inputs
- [ ] Check output format matches exactly
- [ ] Verify precision for floats
- [ ] Review for optimization

---

## 🎯 Summary

This sheet covers fundamental Python concepts:
- **Input/Output**: `input()`, `print()`, `split()`
- **Data Types**: `int`, `float`, `str`, type conversion
- **Operators**: Arithmetic, comparison, logical
- **Strings**: Methods, formatting, manipulation
- **Conditionals**: `if`, `elif`, `else`
- **Built-ins**: `min()`, `max()`, `map()`, `abs()`
- **Collections**: Lists, basic operations
- **Math**: Formulas, precision, logarithms

Master these concepts and you'll be able to implement any logic in Python without syntax barriers!

---

**Happy Coding! 🚀**
