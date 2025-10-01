n = float(input())

if 0.00 <= n <= 25.00:
    print("Interval [0,25]")
elif 25.00 < n <= 50.00:
    print("Interval (25,50]")
elif 50.00 < n <= 75.00:
    print("Interval (50,75]")
elif 75.00 < n <= 100.00:
    print("Interval (75,100]")
else:
    print("Out of Intervals")