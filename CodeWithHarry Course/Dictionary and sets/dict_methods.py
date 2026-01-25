# Program demonstrating dictionary methods in Python
# Each method is explained with numbered comments

# Creating a dictionary
student = {
    "name": "Ahad",
    "age": 18,
    "course": "AI & ML"
}

print("Original dictionary:", student)

# --------------------------------------------------
# 1. len()
# Returns the number of key-value pairs in the dictionary
print("1. Length of dictionary:", len(student))

# --------------------------------------------------
# 2. keys()
# Returns all keys in the dictionary
print("2. Keys:", student.keys())

# --------------------------------------------------
# 3. values()
# Returns all values in the dictionary
print("3. Values:", student.values())

# --------------------------------------------------
# 4. items()
# Returns key-value pairs as tuples
print("4. Items:", student.items())

# --------------------------------------------------
# 5. get(key)
# Returns value of the specified key
# Does NOT raise error if key is missing
print("5. Get name:", student.get("name"))

# --------------------------------------------------
# 6. get(key, default)
# Returns default value if key is not found
print("6. Get grade with default:", student.get("grade", "Not Assigned"))

# --------------------------------------------------
# 7. update()
# Updates dictionary with another dictionary
student.update({"grade": "A"})
print("7. After update():", student)

# --------------------------------------------------
# 8. pop(key)
# Removes specified key and returns its value
removed_value = student.pop("age")
print("8. After pop('age'):", student)
print("   Popped value:", removed_value)

# --------------------------------------------------
# 9. popitem()
# Removes and returns the last inserted key-value pair
last_item = student.popitem()
print("9. After popitem():", student)
print("   Popped item:", last_item)

# --------------------------------------------------
# 10. setdefault(key, default)
# Returns value of key; inserts key if it does not exist
student.setdefault("college", "VJIT")
print("10. After setdefault():", student)

# --------------------------------------------------
# 11. copy()
# Creates a shallow copy of the dictionary
student_copy = student.copy()
print("11. Copied dictionary:", student_copy)

# --------------------------------------------------
# 12. clear()
# Removes all key-value pairs
temp_dict = student.copy()
temp_dict.clear()
print("12. After clear():", temp_dict)

# --------------------------------------------------
# 13. fromkeys(keys, value)
# Creates a new dictionary using given keys and value
keys = ("id", "department", "year")
new_dict = dict.fromkeys(keys, "Not Assigned")
print("13. Dictionary from keys:", new_dict)

# --------------------------------------------------
# 14. in keyword
# Checks if a key exists in the dictionary
print("14. Is 'name' a key?", "name" in student)

# --------------------------------------------------
# 15. not in keyword
# Checks if a key does not exist
print("15. Is 'age' not a key?", "age" not in student)
