"""
====================================================
            DUNDER METHODS IN PYTHON 
====================================================

Dunder methods are special methods in Python.
"Dunder" stands for DOUBLE UNDERCORE.

They are written as:
__methodname__

Examples:
__init__, __str__, __add__, __len__

Python automatically calls these methods
to perform built-in operations.

====================================================
WHY DUNDER METHODS?
====================================================
- Customize object behavior
- Make objects act like built-in types
- Operator overloading
- Better object representation

====================================================
COMMON DUNDER METHODS
====================================================
"""


"""
====================================================
1. __init__  (Constructor)
====================================================
Called automatically when an object is created.
Used to initialize data.
"""

class Student:
    def __init__(self, name):
        self.name = name

s = Student("Harry")
print(s.name)


"""
====================================================
2. __str__  (String representation)
====================================================
Called when you use print(object)
"""

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book title: {self.title}"

b = Book("Python Basics")
print(b)


"""
====================================================
3. __repr__  (Official representation)
====================================================
Used for debugging and developers.
"""

class Laptop:
    def __init__(self, brand):
        self.brand = brand

    def __repr__(self):
        return f"Laptop('{self.brand}')"

l = Laptop("Dell")
print(l)


"""
====================================================
4. __add__  (Operator Overloading)
====================================================
Defines behavior of + operator
"""

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)


"""
====================================================
5. __len__  (Length of object)
====================================================
Called when len(object) is used
"""

class Bag:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

b = Bag(["book", "pen", "bottle"])
print(len(b))


"""
====================================================
6. __eq__  (Equality comparison)
====================================================
Called when == operator is used
"""

class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

p1 = Person(20)
p2 = Person(20)
print(p1 == p2)


"""
====================================================
7. __lt__  (Less than)
====================================================
Called when < operator is used
"""

class Marks:
    def __init__(self, marks):
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks

m1 = Marks(70)
m2 = Marks(85)
print(m1 < m2)


"""
====================================================
8. __del__  (Destructor)
====================================================
Called when object is deleted
"""

class Demo:
    def __del__(self):
        print("Object deleted")

d = Demo()
del d


"""
====================================================
IMPORTANT NOTES
====================================================
- Dunder methods are called automatically
- You should NOT call them directly
- They make custom objects behave like built-ins
- Used heavily in Python internals

====================================================
SOME COMMON DUNDER METHODS LIST
====================================================
__init__   Constructor
__str__    print()
__repr__   debugging
__add__    +
__sub__    -
__mul__    *
__len__    len()
__eq__     ==
__lt__     <
__gt__     >
__del__    delete object

====================================================
CONCLUSION
====================================================
Dunder methods allow you to:
- Customize class behavior
- Use operators with objects
- Integrate smoothly with Python

They are a key part of Python's OOP power.
"""
