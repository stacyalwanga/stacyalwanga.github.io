import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Value Input")
    sys.exit(1)

try:
    results = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0")
    sys.exit(1)

print(f"{x} / {y} is {results}")