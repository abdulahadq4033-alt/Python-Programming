"""
====================================================
            INHERITANCE IN PYTHON 
====================================================

Inheritance is an Object-Oriented Programming (OOP) concept
where one class (child/subclass) acquires the properties and
methods of another class (parent/superclass).

----------------------------------------------------
WHY USE INHERITANCE?
----------------------------------------------------
1. Code reusability (no rewriting same code)
2. Easy maintenance
3. Logical class structure
4. Faster development
5. Supports real-world relationships

----------------------------------------------------
BASIC IDEA
----------------------------------------------------
Parent Class  --->  Child Class

The child class can:
- Use parent methods
- Add new methods
- Override parent methods

----------------------------------------------------
SYNTAX
----------------------------------------------------
class ChildClass(ParentClass):
    pass

====================================================
1. SINGLE INHERITANCE
====================================================
One child inherits from one parent.
"""

class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    pass

c = Child()
c.show()


"""
====================================================
2. MULTIPLE INHERITANCE
====================================================
One child inherits from multiple parents.
"""

class Father:
    def skill1(self):
        print("Father skill: Driving")

class Mother:
    def skill2(self):
        print("Mother skill: Cooking")

class ChildMultiple(Father, Mother):
    pass

cm = ChildMultiple()
cm.skill1()
cm.skill2()


"""
====================================================
3. MULTILEVEL INHERITANCE
====================================================
A chain of inheritance.
Grandparent -> Parent -> Child
"""

class Grandparent:
    def g(self):
        print("Grandparent property")

class ParentLevel(Grandparent):
    def p(self):
        print("Parent property")

class ChildLevel(ParentLevel):
    def c(self):
        print("Child property")

cl = ChildLevel()
cl.g()
cl.p()
cl.c()


"""
====================================================
4. HIERARCHICAL INHERITANCE
====================================================
Multiple children inherit from the same parent.
"""

class ParentCommon:
    def show(self):
        print("Common parent method")

class Child1(ParentCommon):
    pass

class Child2(ParentCommon):
    pass

c1 = Child1()
c2 = Child2()
c1.show()
c2.show()


"""
====================================================
5. HYBRID INHERITANCE
====================================================
Combination of two or more types of inheritance.
"""

class A:
    def a(self):
        print("Class A")

class B(A):
    def b(self):
        print("Class B")

class C(A):
    def c(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.a()
d.b()
d.c()


"""
====================================================
METHOD OVERRIDING
====================================================
When a child class provides its own version
of a parent method.
"""

class ParentOverride:
    def show(self):
        print("Parent show")

class ChildOverride(ParentOverride):
    def show(self):
        print("Child show (overridden)")

co = ChildOverride()
co.show()


"""
====================================================
USING super()
====================================================
Used to call parent class methods from child class.
"""

class ParentSuper:
    def show(self):
        print("Parent method")

class ChildSuper(ParentSuper):
    def show(self):
        super().show()
        print("Child method")

cs = ChildSuper()
cs.show()


"""
====================================================
IMPORTANT NOTES
====================================================
- 'self' refers to the current object
- Parent methods are automatically available
- Python supports multiple inheritance
- Python uses MRO (Method Resolution Order)
- Use inheritance only for IS-A relationships

Examples:
Dog IS-A Animal     -> Correct
Engine IS-A Car     -> Wrong

====================================================
CONCLUSION
====================================================
Inheritance allows:
- Sharing of behavior
- Cleaner and scalable code
- Logical relationships between classes

Used properly, inheritance makes programs
easy to understand, maintain, and extend.
====================================================
"""
