# Program demonstrating tuple operations and methods in Python
# Each operation/method is explained with numbered comments

# Creating a tuple
numbers = (10, 20, 30, 40, 20)
print("Original tuple:", numbers)

# --------------------------------------------------
# 1. len()
# Returns the number of elements in the tuple
print("1. Length of tuple:", len(numbers))

# --------------------------------------------------
# 2. count(element)
# Returns the number of times an element appears in the tuple
print("2. Count of 20:", numbers.count(20))

# --------------------------------------------------
# 3. index(element)
# Returns the index of the first occurrence of an element
print("3. Index of 30:", numbers.index(30))

# --------------------------------------------------
# 4. Accessing elements using indexing
# Tuples support indexing like lists
print("4. Element at index 2:", numbers[2])

# --------------------------------------------------
# 5. Negative indexing
# Access elements from the end
print("5. Last element:", numbers[-1])

# --------------------------------------------------
# 6. Slicing
# Extracts a portion of the tuple
print("6. Slicing (1 to 4):", numbers[1:4])

# --------------------------------------------------
# 7. Concatenation (+)
# Joins two tuples
new_tuple = numbers + (50, 60)
print("7. After concatenation:", new_tuple)

# --------------------------------------------------
# 8. Repetition (*)
# Repeats elements of the tuple
repeated_tuple = (1, 2) * 3
print("8. After repetition:", repeated_tuple)

# --------------------------------------------------
# 9. in keyword
# Checks if an element exists in the tuple
print("9. Is 40 in tuple?", 40 in numbers)

# --------------------------------------------------
# 10. not in keyword
# Checks if an element does not exist
print("10. Is 100 not in tuple?", 100 not in numbers)

# --------------------------------------------------
# 11. Iterating through a tuple
# Tuples can be looped using for loop
print("11. Iterating through tuple:")
for item in numbers:
    print(item, end=" ")
print()

# --------------------------------------------------
# 12. min()
# Returns the smallest element
print("12. Minimum element:", min(numbers))

# --------------------------------------------------
# 13. max()
# Returns the largest element
print("13. Maximum element:", max(numbers))

# --------------------------------------------------
# 14. sum()
# Returns the sum of elements
print("14. Sum of elements:", sum(numbers))

# --------------------------------------------------
# 15. tuple() constructor
# Converts another data type into a tuple
list_data = [1, 2, 3]
converted_tuple = tuple(list_data)
print("15. Tuple from list:", converted_tuple)

# --------------------------------------------------
# 16. Packing
# Multiple values assigned to a tuple
packed_tuple = 1, 2, 3
print("16. Packed tuple:", packed_tuple)

# --------------------------------------------------
# 17. Unpacking
# Assigning tuple values to variables
a, b, c = packed_tuple
print("17. Unpacked values:", a, b, c)

# --------------------------------------------------
# 18. Nested tuple
# Tuple inside another tuple
nested_tuple = (1, (2, 3), 4)
print("18. Nested tuple:", nested_tuple)

# --------------------------------------------------
# 19. Immutability demonstration
# Tuples cannot be modified (this would cause an error)
# numbers[0] = 99  # ❌ TypeError

print("19. Tuples are immutable (cannot be modified)")
