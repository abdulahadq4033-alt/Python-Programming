"""
====================================================
            EXCEPTION HANDLING IN PYTHON
====================================================

An exception is a runtime error that occurs while a
program is executing and disrupts the normal flow
of the program.

This file is intended to be used as a REFERENCE /
README, not mainly for execution.
"""

# ==================================================
# 1. WHAT IS AN EXCEPTION?
# ==================================================
# An exception is an error that happens at runtime.
# If it is not handled, the program stops abruptly.
#
# Examples:
# - ZeroDivisionError
# - ValueError
# - TypeError
# - FileNotFoundError
# - IndexError


# ==================================================
# 2. WHY EXCEPTION HANDLING IS IMPORTANT
# ==================================================
# - Prevents program crashes
# - Handles unexpected user input
# - Improves program reliability
# - Makes debugging easier


# ==================================================
# 3. EXCEPTION HANDLING KEYWORDS
# ==================================================
# try     : Code that may cause an exception
# except  : Handles the exception
# else    : Executes if no exception occurs
# finally : Executes no matter what
# raise   : Used to manually raise an exception


# ==================================================
# 4. BASIC SYNTAX
# ==================================================
"""
try:
    # risky code
except ExceptionType:
    # handling code
"""


# ==================================================
# 5. PROGRAM WITHOUT EXCEPTION HANDLING
# ==================================================
"""
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(a / b)

If b = 0, the program crashes.
"""


# ==================================================
# 6. PROGRAM WITH try-except
# ==================================================
"""
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
"""


# ==================================================
# 7. try-except-else
# ==================================================
# The else block runs ONLY if no exception occurs.
"""
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print("Calculation successful")
"""


# ==================================================
# 8. try-except-finally
# ==================================================
# The finally block ALWAYS executes.
# It is commonly used for cleanup operations.
"""
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
"""


# ==================================================
# 9. RAISING AN EXCEPTION
# ==================================================
# You can manually raise exceptions using 'raise'.
"""
age = int(input("Enter age: "))

if age < 18:
    raise ValueError("Age must be 18 or above")

print("Access granted")
"""


# ==================================================
# 10. CUSTOM EXCEPTIONS
# ==================================================
"""
class NegativeNumberError(Exception):
    pass

num = int(input("Enter a number"))

if num < 0:
    raise NegativeNumberError("Negative numbers not allowed")
"""


# ==================================================
# 11. COMMON PYTHON EXCEPTIONS
# ==================================================
# ZeroDivisionError   -> Division by zero
# ValueError          -> Invalid value
# TypeError           -> Wrong data type
# IndexError          -> Index out of range
# KeyError            -> Missing dictionary key
# FileNotFoundError   -> File not found


# ==================================================
# 12. BEST PRACTICES
# ==================================================
# - Catch specific exceptions
# - Avoid empty except blocks
# - Use finally for cleanup
# - Do not overuse raise
# - Keep error messages meaningful


# ==================================================
# END OF EXCEPTION HANDLING REFERENCE
# ==================================================
