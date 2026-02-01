"""
===============================
DUNDER METHODS IN PYTHON
===============================

Dunder means Double UNDERSCORE (__).

Dunder methods are special methods in Python that:
1. Start with __
2. End with __
3. Are automatically called by Python

We do NOT usually call them manually.
Python calls them when needed.

--------------------------------
Why are dunder methods used?
--------------------------------
They define how an object behaves when:
- An object is created
- An object is printed
- Operators like +, len() are used

--------------------------------
Example 1: __init__ method
--------------------------------
__init__ is called automatically when an object is created.
It is used to initialize (set up) object data.
"""

class Student:
    def __init__(self, name):
        # self refers to the current object
        self.name = name


"""
--------------------------------
Example 2: __str__ method
--------------------------------
__str__ controls what happens when we print an object.
Without __str__, Python prints a memory address.
"""

class StudentInfo:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name is {self.name}"


# Creating objects
s1 = Student("Rahul")
s2 = StudentInfo("Amit")

# Printing results
print("Object created using __init__:")
print(s1.name)

print("\nOutput controlled by __str__:")
print(s2)


"""
--------------------------------
Common Dunder Methods
--------------------------------
__init__  -> object creation
__str__   -> printing object
__len__   -> len(object)
__add__   -> + operator

--------------------------------
One-line summary:
--------------------------------
Dunder methods are special methods that tell Python
how an object should behave.
"""
