# Program demonstrating set methods in Python
# Each method is explained with numbered comments

# Creating a set
numbers = {10, 20, 30, 40}
print("Original set:", numbers)

# --------------------------------------------------
# 1. add(element)
# Adds a single element to the set
numbers.add(50)
print("1. After add(50):", numbers)

# --------------------------------------------------
# 2. update(iterable)
# Adds multiple elements from another iterable
numbers.update([60, 70])
print("2. After update([60, 70]):", numbers)

# --------------------------------------------------
# 3. remove(element)
# Removes a specified element
# Raises an error if element is not found
numbers.remove(20)
print("3. After remove(20):", numbers)

# --------------------------------------------------
# 4. discard(element)
# Removes an element if present (no error if absent)
numbers.discard(100)
print("4. After discard(100):", numbers)

# --------------------------------------------------
# 5. pop()
# Removes and returns a random element
removed_element = numbers.pop()
print("5. After pop():", numbers)
print("   Popped element:", removed_element)

# --------------------------------------------------
# 6. clear()
# Removes all elements from the set
temp_set = numbers.copy()
temp_set.clear()
print("6. After clear():", temp_set)

# --------------------------------------------------
# 7. copy()
# Creates a shallow copy of the set
numbers_copy = numbers.copy()
print("7. Copied set:", numbers_copy)

# --------------------------------------------------
# 8. union()
# Returns a new set with elements from both sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("8. Union:", set_a.union(set_b))

# --------------------------------------------------
# 9. intersection()
# Returns common elements between sets
print("9. Intersection:", set_a.intersection(set_b))

# --------------------------------------------------
# 10. difference()
# Returns elements present in set_a but not in set_b
print("10. Difference (A - B):", set_a.difference(set_b))

# --------------------------------------------------
# 11. symmetric_difference()
# Returns elements present in either set but not in both
print("11. Symmetric Difference:", set_a.symmetric_difference(set_b))

# --------------------------------------------------
# 12. intersection_update()
# Updates set_a with common elements
temp = set_a.copy()
temp.intersection_update(set_b)
print("12. After intersection_update():", temp)

# --------------------------------------------------
# 13. difference_update()
# Updates set_a by removing common elements
temp = set_a.copy()
temp.difference_update(set_b)
print("13. After difference_update():", temp)

# --------------------------------------------------
# 14. symmetric_difference_update()
# Updates set_a with symmetric difference
temp = set_a.copy()
temp.symmetric_difference_update(set_b)
print("14. After symmetric_difference_update():", temp)

# --------------------------------------------------
# 15. issubset()
# Checks if a set is a subset of another set
small_set = {1, 2}
print("15. Is small_set subset of set_a?", small_set.issubset(set_a))

# --------------------------------------------------
# 16. issuperset()
# Checks if a set is a superset of another set
print("16. Is set_a superset of small_set?", set_a.issuperset(small_set))

# --------------------------------------------------
# 17. isdisjoint()
# Checks if two sets have no common elements
print("17. Are set_a and {6, 7} disjoint?", set_a.isdisjoint({6, 7}))

# --------------------------------------------------
# 18. in keyword
# Checks if an element exists in the set
print("18. Is 30 in set?", 30 in numbers)

# --------------------------------------------------
# 19. not in keyword
# Checks if an element does not exist
print("19. Is 100 not in set?", 100 not in numbers)
