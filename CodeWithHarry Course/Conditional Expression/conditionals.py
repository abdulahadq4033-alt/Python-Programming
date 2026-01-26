# PROGRAM: Demonstration of all conditional expressions in Python

# Sample variables
a = 10
b = 20
c = 10

# --------------------------------------------------
# 1. SIMPLE if STATEMENT
# Executes the block only if the condition is True
if a < b:
    print("1. a is less than b")

# --------------------------------------------------
# 2. if - else STATEMENT
# Executes one block if condition is True, else executes the other block
if a > b:
    print("2. a is greater than b")
else:
    print("2. a is not greater than b")

# --------------------------------------------------
# 3. if - elif - else STATEMENT
# Used to check multiple conditions
if a > b:
    print("3. a is greater than b")
elif a == b:
    print("3. a is equal to b")
else:
    print("3. a is less than b")

# --------------------------------------------------
# 4. NESTED if STATEMENT
# An if statement inside another if statement
if a == c:
    if a > 5:
        print("4. a is equal to c and greater than 5")

# --------------------------------------------------
# 5. TERNARY CONDITIONAL EXPRESSION
# Short-hand if-else written in a single line
result = "5. a is greater than b" if a > b else "5. a is not greater than b"
print(result)

# --------------------------------------------------
# 6. match - case STATEMENT (Python 3.10+)
# Used as an alternative to if-elif-else for pattern matching
day = 3

match day:
    case 1:
        print("6. Monday")
    case 2:
        print("6. Tuesday")
    case 3:
        print("6. Wednesday")
    case _:
        print("6. Invalid day")

# --------------------------------------------------
# 7. CONDITIONAL EXPRESSION WITH LOGICAL OPERATORS
# Using and, or, not with conditions
if a == c and a < b:
    print("7. a is equal to c AND less than b")

if a > b or a == c:
    print("7. a is either greater than b OR equal to c")

if not a > b:
    print("7. a is NOT greater than b")
