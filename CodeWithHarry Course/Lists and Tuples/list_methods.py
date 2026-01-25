# Program demonstrating all commonly used list methods in Python
# Each method is explained with numbered comments

# Initial list
numbers = [10, 20, 30, 40]
print("Original list:", numbers)

# --------------------------------------------------
# 1. append(element)
# Adds an element to the end of the list
numbers.append(50)
print("1. After append(50):", numbers)

# --------------------------------------------------
# 2. insert(index, element)
# Inserts an element at a specific index
numbers.insert(2, 25)
print("2. After insert(2, 25):", numbers)

# --------------------------------------------------
# 3. extend(iterable)
# Adds elements of another list to the current list
numbers.extend([60, 70])
print("3. After extend([60, 70]):", numbers)

# --------------------------------------------------
# 4. remove(element)
# Removes the first occurrence of the specified element
numbers.remove(30)
print("4. After remove(30):", numbers)

# --------------------------------------------------
# 5. pop()
# Removes and returns the element at the given index (last by default)
removed_element = numbers.pop()
print("5. After pop():", numbers)
print("   Popped element:", removed_element)

# --------------------------------------------------
# 6. pop(index)
# Removes and returns element at a specific index
numbers.pop(1)
print("6. After pop(1):", numbers)

# --------------------------------------------------
# 7. clear()
# Removes all elements from the list
temp_list = numbers.copy()
temp_list.clear()
print("7. After clear():", temp_list)

# --------------------------------------------------
# 8. index(element)
# Returns the index of the first occurrence of an element
print("8. Index of 40:", numbers.index(40))

# --------------------------------------------------
# 9. count(element)
# Counts how many times an element appears
numbers.append(40)
print("9. Count of 40:", numbers.count(40))

# --------------------------------------------------
# 10. sort()
# Sorts the list in ascending order
numbers.sort()
print("10. After sort():", numbers)

# --------------------------------------------------
# 11. sort(reverse=True)
# Sorts the list in descending order
numbers.sort(reverse=True)
print("11. After sort(reverse=True):", numbers)

# --------------------------------------------------
# 12. reverse()
# Reverses the order of the list
numbers.reverse()
print("12. After reverse():", numbers)

# --------------------------------------------------
# 13. copy()
# Creates a shallow copy of the list
numbers_copy = numbers.copy()
print("13. Copied list:", numbers_copy)

# --------------------------------------------------
# 14. len()
# Returns the number of elements in the list
print("14. Length of list:", len(numbers))

# --------------------------------------------------
# 15. min()
# Returns the smallest element in the list
print("15. Minimum element:", min(numbers))

# --------------------------------------------------
# 16. max()
# Returns the largest element in the list
print("16. Maximum element:", max(numbers))

# --------------------------------------------------
# 17. sum()
# Returns the sum of all numeric elements
print("17. Sum of elements:", sum(numbers))

# --------------------------------------------------
# 18. in keyword
# Checks if an element exists in the list
print("18. Is 40 in list?", 40 in numbers)

# --------------------------------------------------
# 19. not in keyword
# Checks if an element does not exist in the list
print("19. Is 100 not in list?", 100 not in numbers)

# --------------------------------------------------
# 20. del statement
# Deletes an element using index
del numbers[0]
print("20. After del numbers[0]:", numbers)
