"""
====================================================
            OPERATOR OVERLOADING IN PYTHON
====================================================

Operator Overloading allows us to define **custom behavior** for
operators (+, -, *, ==, <, >, etc.) when they are used with objects
of a class.

In other words, **we can "overload" operators to work with our classes**.

----------------------------------------------------
WHY USE OPERATOR OVERLOADING?
----------------------------------------------------
- Make objects behave like built-in types
- Add functionality to operators for custom classes
- Improve code readability
- Support arithmetic, comparison, and other operations

====================================================
SYNTAX
====================================================

class ClassName:
    def __add__(self, other):
        # define addition behavior
        return result

Supported operators and their corresponding dunder methods:
+  -> __add__
-  -> __sub__
*  -> __mul__
/  -> __truediv__
== -> __eq__
<  -> __lt__
>  -> __gt__
len() -> __len__()
str() -> __str__()

"""

"""
====================================================
EXAMPLE 1: OVERLOADING + OPERATOR
====================================================
"""

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):   # Overload +
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)
print("Sum of numbers using overloaded + :", n1 + n2)

"""
OUTPUT:
Sum of numbers using overloaded + : 30
"""

"""
====================================================
EXAMPLE 2: OVERLOADING - OPERATOR
====================================================
"""

class NumberSub:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):   # Overload -
        return self.value - other.value

n1 = NumberSub(50)
n2 = NumberSub(20)
print("Difference using overloaded - :", n1 - n2)

"""
OUTPUT:
Difference using overloaded - : 30
"""

"""
====================================================
EXAMPLE 3: OVERLOADING * OPERATOR
====================================================
"""

class NumberMul:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):   # Overload *
        return self.value * other.value

n1 = NumberMul(5)
n2 = NumberMul(6)
print("Multiplication using overloaded * :", n1 * n2)

"""
OUTPUT:
Multiplication using overloaded * : 30
"""

"""
====================================================
EXAMPLE 4: OVERLOADING == OPERATOR
====================================================
"""

class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):   # Overload ==
        return self.age == other.age

p1 = Person(25)
p2 = Person(25)
p3 = Person(30)

print("Are p1 and p2 equal? :", p1 == p2)
print("Are p1 and p3 equal? :", p1 == p3)

"""
OUTPUT:
Are p1 and p2 equal? : True
Are p1 and p3 equal? : False
"""

"""
====================================================
EXAMPLE 5: OVERLOADING < AND >
====================================================
"""

class Marks:
    def __init__(self, score):
        self.score = score

    def __lt__(self, other):   # <
        return self.score < other.score

    def __gt__(self, other):   # >
        return self.score > other.score

m1 = Marks(75)
m2 = Marks(85)

print("m1 < m2 ?", m1 < m2)
print("m1 > m2 ?", m1 > m2)

"""
OUTPUT:
m1 < m2 ? True
m1 > m2 ? False
"""

"""
====================================================
EXAMPLE 6: OVERLOADING __str__ FOR PRINTING
====================================================
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):   # Overload str()
        return f"Book: {self.title}, Author: {self.author}"

b = Book("Python Basics", "Harry")
print(b)

"""
OUTPUT:
Book: Python Basics, Author: Harry
"""

"""
====================================================
KEY POINTS
====================================================
- Operator overloading allows **custom behavior for operators**
- Implemented using **dunder methods** (__add__, __sub__, __mul__, etc.)
- Makes objects behave like built-in types
- Widely used in real-world Python classes
"""
