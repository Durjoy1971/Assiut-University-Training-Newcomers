# Python Knowledge Guide - Sheet 2 (A-Z Problems)

## 🎯 Purpose

This guide summarizes the key Python concepts and logic used to solve problems A.py through Z.py from Sheet 2. It is designed for:

- Beginners learning Python
- Programmers transitioning from other languages
- Anyone seeking to understand the logic and syntax behind each problem

---

## 📚 Table of Contents

1. [Input/Output Patterns](#1-inputoutput-patterns)
2. [Data Types & Type Conversion](#2-data-types--type-conversion)
3. [Loops & Iteration](#3-loops--iteration)
4. [Conditional Statements](#4-conditional-statements)
5. [Functions & Problem Logic](#5-functions--problem-logic)
6. [String & List Operations](#6-string--list-operations)
7. [Mathematical Operations](#7-mathematical-operations)
8. [Problem-by-Problem Concepts](#8-problem-by-problem-concepts)

---

## 1. Input/Output Patterns

### Reading Input

```python
n = int(input())                # Single integer input
a, b = map(int, input().split()) # Two integers on one line
arr = list(map(int, input().split())) # List of integers
s = input()                     # String input
```

### Printing Output

```python
print(value)                    # Print value
print(a, b, sep='\n')           # Print each value on new line
print(f"{a} * {b} = {a*b}")      # Formatted output
print(i, end=' ')               # Print on same line, space-separated
```

**Used in:** All problems (A-Z)

---

## 2. Data Types & Type Conversion

- `int()`, `str()`, `map()` for type conversion
- Lists for collections of numbers
- Strings for text and digit manipulation

**Used in:** A.py, B.py, C.py, E.py, I.py, N.py, U.py, Z.py

---

## 3. Loops & Iteration

- `for` loops for fixed or range-based iteration
- `while` loops for indefinite repetition (e.g., until correct input)
- Nested loops for combinatorial problems

**Used in:** B.py, D.py, F.py, G.py, J.py, K.py, L.py, M.py, O.py, P.py, Q.py, R.py, S.py, T.py, V.py, W.py, Z.py

---

## 4. Conditional Statements

- `if`, `elif`, `else` for branching logic
- Used for checks (even/odd, positive/negative, prime, etc.)

**Used in:** B.py, C.py, D.py, H.py, I.py, J.py, K.py, L.py, M.py, N.py, Q.py, R.py, S.py

---

## 5. Functions & Problem Logic

- Custom functions for repeated logic (e.g., prime checking, lucky number)
- Use of return values for boolean checks

**Used in:** H.py, J.py, M.py

---

## 6. String & List Operations

- String reversal, multiplication, joining
- List creation, iteration, and manipulation

**Used in:** I.py, N.py, Q.py

---

## 7. Mathematical Operations

- Arithmetic: +, -, \*, /, %, //, \*\*
- Factorial, sum, max, min, GCD
- Fibonacci sequence, digit sum

**Used in:** C.py, E.py, F.py, G.py, L.py, U.py, V.py, Y.py, Z.py

## 🎓 Learning Path Recommendation

- Start with A, B, C for basic I/O and counting
- Move to D, E, F, G for loops and calculations
- Practice H, J, K, L, M for functions and number theory
- Try N, O, P, Q, R, S, T, U, V, W for string/list/pattern logic
- Y, Z for sequences and combinatorics

---

## 💡 Tips & Pitfalls

- Always use `int()` for numeric input
- Use `map(int, input().split())` for multiple integers
- For patterns, use string multiplication and spaces
- For combinatorics, use nested loops
- For prime/lucky checks, use helper functions
- For sum/count, use built-in `sum()` and `range()`

---

**Happy Coding! 🚀**
