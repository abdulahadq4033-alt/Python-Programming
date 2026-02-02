"""
WALRUS OPERATOR (:=) EXPLANATION

The walrus operator allows you to:
1. Assign a value to a variable
2. Use that value immediately in an expression

Syntax:
    variable := expression

It was introduced in Python 3.8
"""

print("=== WALRUS OPERATOR (:=) DEMO ===\n")

# ----------------------------------------
# Example 1: WITHOUT walrus operator
# ----------------------------------------
print("Example 1: Without walrus operator")

num = int(input("Enter a number: "))
if num > 10:
    print("Number is greater than 10")

# ----------------------------------------
# Example 2: WITH walrus operator
# ----------------------------------------
print("\nExample 2: With walrus operator")

if (num := int(input("Enter a number: "))) > 10:
    print("Number is greater than 10")

print(f"Stored value of num is: {num}")

# ----------------------------------------
# Example 3: Loop example
# ----------------------------------------
print("\nExample 3: Using walrus operator in a loop")

while (n := int(input("Enter a number (0 to stop): "))) != 0:
    print(f"You entered: {n}")

print("Loop ended")

# ----------------------------------------
# Example 4: List processing
# ----------------------------------------
print("\nExample 4: Walrus operator with length check")

data = [10, 20, 30, 40, 50]

if (length := len(data)) > 3:
    print(f"List has {length} elements")

# ----------------------------------------
# Why use the walrus operator?
# ----------------------------------------
print("\nWhy use the walrus operator?")
print("- Avoids repeating function calls")
print("- Makes code shorter and cleaner")
print("- Useful in conditions and loops")

print("\n=== END OF DEMO ===")
