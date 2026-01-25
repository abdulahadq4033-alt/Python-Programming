# Program demonstrating all escape sequence characters in Python
# Each escape sequence is explained using comments

# --------------------------------------------------
# 1. \n → New Line
# Moves the cursor to the next line
print("1. New Line Example:\nHello\nWorld")

# --------------------------------------------------
# 2. \t → Horizontal Tab
# Adds a tab space between words
print("2. Tab Example:\tHello\tWorld")

# --------------------------------------------------
# 3. \\ → Backslash
# Used to print a single backslash
print("3. Backslash Example: C:\\Python\\Files")

# --------------------------------------------------
# 4. \' → Single Quote
# Allows single quote inside a single-quoted string
print('4. Single Quote Example: It\'s Python')

# --------------------------------------------------
# 5. \" → Double Quote
# Allows double quote inside a double-quoted string
print("5. Double Quote Example: He said \"Hello\"")

# --------------------------------------------------
# 6. \b → Backspace
# Removes the character before it (console dependent)
print("6. Backspace Example: Hello\bWorld")

# --------------------------------------------------
# 7. \r → Carriage Return
# Moves cursor to beginning of the line
print("7. Carriage Return Example: Hello\rWorld")

# --------------------------------------------------
# 8. \f → Form Feed
# Moves cursor to next page (rarely used)
print("8. Form Feed Example: Hello\fWorld")

# --------------------------------------------------
# 9. \v → Vertical Tab
# Moves text vertically
print("9. Vertical Tab Example: Hello\vWorld")

# --------------------------------------------------
# 10. \a → Alert / Bell
# Produces a beep sound (system dependent)
print("10. Alert Example:\a")

# --------------------------------------------------
# Numeric Escape Sequences

# --------------------------------------------------
# 11. \ooo → Octal Value
# Represents a character using octal number
print("11. Octal Value Example:", "\101")  # A

# --------------------------------------------------
# 12. \xhh → Hexadecimal Value
# Represents a character using hexadecimal number
print("12. Hexadecimal Value Example:", "\x41")  # A

# --------------------------------------------------
# Unicode Escape Sequences

# --------------------------------------------------
# 13. \uXXXX → Unicode (16-bit)
# Used to represent Unicode characters
print("13. Unicode 16-bit Example:", "\u03A9")  # Ω

# --------------------------------------------------
# 14. \UXXXXXXXX → Unicode (32-bit)
# Used for extended Unicode characters
print("14. Unicode 32-bit Example:", "\U0001F600")  # 😀

# --------------------------------------------------
# 15. \N{name} → Unicode by Character Name
# Uses official Unicode character name
print("15. Unicode by Name Example:", "\N{GREEK CAPITAL LETTER DELTA}")  # Δ

# --------------------------------------------------
# Raw String Example

# --------------------------------------------------
# 16. r"" → Raw String
# Treats backslashes as normal characters
# Useful for file paths and regular expressions
print("16. Raw String Example:", r"C:\new\folder\test.txt")
