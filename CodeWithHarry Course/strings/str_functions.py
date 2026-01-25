# Original string with extra spaces and numbers
text = "  Hello Python World 123  "

# repr() is used to display spaces clearly
print("Original string:", repr(text))

# --------------------------------------------------
# 1. len() → Returns the total number of characters in the string
print("1. Length of string:", len(text))

# --------------------------------------------------
# 2. lower() → Converts all characters to lowercase
print("2. Lowercase:", text.lower())

# --------------------------------------------------
# 3. upper() → Converts all characters to uppercase
print("3. Uppercase:", text.upper())

# --------------------------------------------------
# 4. strip() → Removes spaces from both left and right sides
print("4. Strip:", text.strip())

# --------------------------------------------------
# 5. lstrip() → Removes spaces from the left side only
print("5. Left strip:", text.lstrip())

# --------------------------------------------------
# 6. rstrip() → Removes spaces from the right side only
print("6. Right strip:", text.rstrip())

# Save stripped string for further operations
clean_text = text.strip()

# --------------------------------------------------
# 7. replace(old, new) → Replaces a word with another word
replaced_text = clean_text.replace("Python", "AI")
print("7. After replace:", replaced_text)

# --------------------------------------------------
# 8. split() → Splits the string into a list of words
words = clean_text.split()
print("8. Split into list:", words)

# --------------------------------------------------
# 9. join() → Joins list elements into a string using a separator
joined_text = "-".join(words)
print("9. Joined string:", joined_text)

# --------------------------------------------------
# 10. find() → Returns the index of the first occurrence of a substring
print("10. Position of 'World':", clean_text.find("World"))

# --------------------------------------------------
# 11. startswith() → Checks if string starts with given value
print("11. Starts with 'Hello':", clean_text.startswith("Hello"))

# --------------------------------------------------
# 12. endswith() → Checks if string ends with given value
print("12. Ends with '123':", clean_text.endswith("123"))

# --------------------------------------------------
# 13. count() → Counts how many times a character appears
print("13. Count of 'o':", clean_text.count("o"))

# --------------------------------------------------
# 14. in keyword → Checks if substring exists in string
print("14. 'Python' in string:", "Python" in clean_text)

# --------------------------------------------------
# 15. isalpha() → Returns True if string contains only alphabets
print("15. 'Hello'.isalpha():", "Hello".isalpha())

# --------------------------------------------------
# 16. isdigit() → Returns True if string contains only digits
print("16. '123'.isdigit():", "123".isdigit())

# --------------------------------------------------
# 17. isalnum() → Returns True if string contains only letters and numbers
print("17. 'Hello123'.isalnum():", "Hello123".isalnum())

# --------------------------------------------------
# 18. isspace() → Returns True if string contains only spaces
print("18. '   '.isspace():", "   ".isspace())

# --------------------------------------------------
# 19. capitalize() → Capitalizes only the first character
print("19. Capitalize:", clean_text.capitalize())

# --------------------------------------------------
# 20. title() → Capitalizes the first letter of every word
print("20. Title:", clean_text.title())

# --------------------------------------------------
# 21. f-string → Modern way to format strings
name = "Ahad"
age = 18
print(f"21. My name is {name} and I am {age} years old")

# --------------------------------------------------
# 22. swapcase() → Converts uppercase to lowercase and vice versa
print("22. Swapcase:", clean_text.swapcase())

# --------------------------------------------------
# 23. zfill(width) → Adds leading zeros until the given width
num = "42"
print("23. Zero filled number:", num.zfill(5))
