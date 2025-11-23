# Python Knowledge Guide - Sheet 3 (Arrays & Matrices)

## 🎯 Purpose
This guide provides all essential Python knowledge needed to solve problems A.py through Z.py in Sheet 3. It focuses on **Lists (Arrays)**, **2D Matrices**, and common algorithmic techniques like **Two Pointers** and **Prefix Sums**.

---

## 📚 Table of Contents
1. [List Basics & Methods](#1-list-basics--methods)
2. [Array Algorithms](#2-array-algorithms)
3. [Two Pointers Technique](#3-two-pointers-technique)
4. [Frequency Arrays & Maps](#4-frequency-arrays--maps)
5. [2D Arrays (Matrices)](#5-2d-arrays-matrices)
6. [Advanced Techniques](#6-advanced-techniques)
7. [Problem-by-Problem Concepts](#7-problem-by-problem-concepts)

---

## 1. List Basics & Methods

### Creating & Reading Lists
```python
# Read N integers into a list
n = int(input())
array = list(map(int, input().split()))

# Initialize list with specific size and value
zeros = [0] * n
```

### Common Methods
```python
# Append: Add element to end
array.append(10)

# Sort: Order elements (ascending by default)
array.sort()                   # Modifies in-place
array.sort(reverse=True)       # Descending order

# Reverse: Flip order
array.reverse()                # Modifies in-place
reversed_arr = array[::-1]     # Creates new reversed list

# Index: Find position of first occurrence
idx = array.index(value)       # Raises ValueError if not found

# Count: Number of occurrences
cnt = array.count(value)
```

**Used in:** A.py, D.py, F.py, H.py, J.py, M.py

---

## 2. Array Algorithms

### Min / Max & Swapping
```python
# Find minimum and maximum
min_val = min(array)
max_val = max(array)

# Find their indices
min_idx = array.index(min_val)

# Swap elements
array[i], array[j] = array[j], array[i]
```

### Linear Search
```python
# Find if element exists and print index
found = False
for i in range(n):
    if array[i] == target:
        print(i)
        found = True
        break
if not found:
    print(-1)
```

**Used in:** B.py, E.py, M.py

---

## 3. Two Pointers Technique

Efficiently traverse an array from both ends or two positions.

### Palindrome Check (Converging Pointers)
```python
left = 0
right = n - 1
is_palindrome = True

while left <= right:
    if array[left] != array[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
```

### Subsequence Check (Parallel Pointers)
```python
# Check if 'sub' is a subsequence of 'main'
i = 0  # Pointer for main
j = 0  # Pointer for sub

while i < n and j < m:
    if main[i] == sub[j]:
        j += 1  # Move sub pointer only on match
    i += 1      # Always move main pointer

if j == m:
    print("YES")
```

**Used in:** G.py, U.py

---

## 4. Frequency Arrays & Maps

Counting occurrences of elements efficiently.

### Using Dictionary (Map)
Best for large values or non-integer keys.
```python
count_map = {}
for num in array:
    if num in count_map:
        count_map[num] += 1
    else:
        count_map[num] = 1

# Get count safely
print(count_map.get(target, 0))
```

### Using Fixed Size Array (Frequency Array)
Best when range of values is small (e.g., 1 to 100000).
```python
freq = [0] * 100001
for num in array:
    freq[num] += 1
```

**Used in:** J.py, R.py, V.py

---

## 5. 2D Arrays (Matrices)

### Reading a Matrix
```python
rows, cols = map(int, input().split())
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
```

### Diagonals
```python
# Main Diagonal (i == j)
if i == j:
    sum_main += matrix[i][j]

# Secondary Diagonal (i + j == n - 1)
if i + j == n - 1:
    sum_secondary += matrix[i][j]
```

### Neighbor Checking (Direction Arrays)
Efficiently check 8 neighbors (up, down, left, right, diagonals).
```python
dx = [-1, -1, -1,  0, 0,  1, 1, 1]
dy = [-1,  0,  1, -1, 1, -1, 0, 1]

for k in range(8):
    ni = i + dx[k]
    nj = j + dy[k]
    # Check bounds
    if 0 <= ni < rows and 0 <= nj < cols:
        # Process neighbor matrix[ni][nj]
```

**Used in:** S.py, T.py, W.py, X.py

---

## 6. Advanced Techniques

### Prefix Sum (Range Sum Query)
Calculate sum of range [L, R] in O(1) time after O(N) preprocessing.
```python
# Preprocessing
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + array[i-1]

# Query [L, R] (1-based)
range_sum = prefix[R] - prefix[L-1]
```

### Binary Search
Find element in **sorted** array in O(log N).
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return "found"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "not found"
```

### Fibonacci Sequence (Generation)
```python
fib = [0, 0, 1]  # Starting values
for i in range(3, n + 1):
    next_val = fib[i-2] + fib[i-1]
    fib.append(next_val)
```

**Used in:** O.py, Y.py, Z.py

---

## 7. Problem-by-Problem Concepts

### A.py - Summation
**Concept:** Iterating through `input().split()` and summing values.

### B.py - Searching
**Concept:** Linear search with index tracking and a `found` flag.

### C.py - Replacement
**Concept:** Conditional logic inside a loop to print different values based on input.

### D.py - Positions
**Concept:** Enumerating list with `range(n)` to access both index `i` and value `array[i]`.

### E.py - Lowest Number
**Concept:** Using `min()` to find value and `index()` to find position.

### F.py - Reversing
**Concept:** `array.reverse()` or slicing `[::-1]` to print in reverse.

### G.py - Palindrome Array
**Concept:** **Two Pointers** comparing start and end elements moving inwards.

### H.py - Sorting
**Concept:** `array.sort()` for ascending order.

### I.py - Smallest Pair
**Concept:** Nested loops to check all pairs `(i, j)` and find minimum result.

### J.py - Lucky Array
**Concept:** Frequency counting of the minimum element.

### K.py - Sum Digits
**Concept:** Treating input as string and iterating characters to sum digits.

### L.py - Max Subarray
**Concept:** Generating subarrays (nested loops) and finding max elements.

### M.py - Replace MinMax
**Concept:** Swapping elements using tuple unpacking: `a[i], a[j] = a[j], a[i]`.

### N.py - Check Code
**Concept:** String validation, checking specific positions and character types.

### O.py - Fibonacci
**Concept:** Generating sequence iteratively using previous two values.

### P.py - Minimize Number
**Concept:** While loop to repeatedly perform division until condition fails.

### Q.py - Count Subarrays
**Concept:** Nested loops to generate all subarrays and check a condition (non-decreasing).

### R.py - Permutation with Arrays
**Concept:** Checking if two arrays contain same elements (marking used elements).

### S.py - Search In Matrix
**Concept:** Nested loops to traverse 2D array and search for a value.

### T.py - Matrix Diagonals
**Concept:** Summing elements where `i == j` (Main) and `i + j == n - 1` (Secondary).

### U.py - Is B a subsequence of A
**Concept:** **Two Pointers** moving through both arrays to check order.

### V.py - Frequency Array
**Concept:** Using a dictionary/map to count occurrences of numbers in O(N).

### W.py - Mirror Array
**Concept:** Reversing each row of a matrix.

### X.py - 8 Neighbors
**Concept:** Using direction arrays `dx, dy` to check all surrounding cells in a grid.

### Y.py - Range Sum Query
**Concept:** **Prefix Sum** array for O(1) range sum queries.

### Z.py - Binary Search
**Concept:** Implementing binary search for O(log N) lookups in sorted array.

---

## 💡 Common Pitfalls & Tips

1.  **Index Out of Bounds**: Always check `0 <= i < n` when accessing arrays, especially in neighbor checking (X.py).
2.  **1-based vs 0-based**: Problem statements often use 1-based indexing, but Python is 0-based. Adjust by subtracting 1 from input indices (Y.py).
3.  **Copying Lists**: `list2 = list1` creates a reference, not a copy. Use `list2 = list1.copy()` or `list2 = list1[:]`.
4.  **Time Complexity**:
    - `count()` inside a loop is O(N^2). Use a frequency map (V.py) for O(N).
    - `sum()` inside a loop (for ranges) is O(N^2). Use Prefix Sum (Y.py) for O(N).
    - Linear search is O(N). Binary search is O(log N) but requires sorting.

---

## 🔧 Quick Reference

```python
# Input List
arr = list(map(int, input().split()))

# Input Matrix
matrix = [list(map(int, input().split())) for _ in range(rows)]

# Sort
arr.sort()

# Reverse
arr.reverse()

# Map/Frequency
count = {}
count[x] = count.get(x, 0) + 1

# Prefix Sum
P[i] = P[i-1] + A[i-1]
Sum(L, R) = P[R] - P[L-1]
```

**Happy Coding! 🚀**
