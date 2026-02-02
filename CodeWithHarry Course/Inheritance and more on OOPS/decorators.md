"""
====================================================
              DECORATORS IN PYTHON 
====================================================

A decorator in Python is a function that:
- Takes another function or method as input
- Adds extra functionality to it
- Without modifying the original code

Decorators follow the idea:
"Functions are first-class objects in Python"

====================================================
WHY USE DECORATORS?
====================================================
1. Code reusability
2. Cleaner code
3. Separation of logic
4. Easy modification of behavior

====================================================
BASIC DECORATOR SYNTAX
====================================================

def decorator(func):
    def wrapper():
        # extra work
        func()
    return wrapper

@decorator
def my_function():
    pass

====================================================
TYPES OF DECORATORS IN PYTHON
====================================================

1. Function Decorators
2. Class Method Decorators
3. Static Method Decorators
4. Property Decorators
5. Built-in Decorators
====================================================
"""


"""
====================================================
1. FUNCTION DECORATOR
====================================================
Used to modify the behavior of a function.
"""

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()


"""
OUTPUT:
Before function call
Hello
After function call
"""


"""
====================================================
2. CLASS METHOD DECORATOR (@classmethod)
====================================================
Used to define a method that works with the class
instead of the object.
"""

class DemoClassMethod:
    count = 0

    @classmethod
    def increase(cls):
        cls.count += 1

DemoClassMethod.increase()
DemoClassMethod.increase()
print(DemoClassMethod.count)


"""
OUTPUT:
2
"""


"""
====================================================
3. STATIC METHOD DECORATOR (@staticmethod)
====================================================
Used when a method:
- Does not use object (self)
- Does not use class (cls)
"""

class DemoStaticMethod:
    @staticmethod
    def greet():
        print("Hello from static method")

DemoStaticMethod.greet()


"""
OUTPUT:
Hello from static method
"""


"""
====================================================
4. PROPERTY DECORATOR (@property)
====================================================
Used to access a method like an attribute.
Helps in data hiding and validation.
"""

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

s = Student(90)
print(s.marks)


"""
OUTPUT:
90
"""


"""
====================================================
PROPERTY SETTER DECORATOR (@property_name.setter)
====================================================
Used to modify the value of a property.
"""

class StudentSetter:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        self._marks = value

st = StudentSetter(80)
print(st.marks)
st.marks = 95
print(st.marks)


"""
OUTPUT:
80
95
"""


"""
====================================================
5. BUILT-IN DECORATORS
====================================================

Some commonly used built-in decorators:
- @classmethod
- @staticmethod
- @property

They are provided by Python itself.
====================================================
"""


"""
====================================================
SUMMARY
====================================================

Decorator        Purpose
------------------------------------
Function         Modify functions
@classmethod     Work with class data
@staticmethod    Utility methods
@property           Getter method
@setter          Setter method

====================================================
CONCLUSION
====================================================
Decorators allow adding functionality to functions
and methods in a clean and reusable way.

They are heavily used in:
- Frameworks
- Libraries
- Real-world applications

"""
