"""
====================================================
          @PROPERTY AND @SETTER IN PYTHON
====================================================

In Python, @property and @setter are used to:
- Control access to class data
- Protect internal variables
- Allow validation
- Keep the code clean and Pythonic

They help implement **encapsulation**.

====================================================
WHY USE @PROPERTY?
====================================================
1. Provides a **read-only** access to internal variables
2. Protects the internal state
3. Allows using method logic like an attribute
4. Cleaner syntax than normal getter methods

----------------------------------------------------
EXAMPLE 1: @property
----------------------------------------------------
"""

class Student:
    def __init__(self, marks):
        self._marks = marks   # protected variable

    @property
    def marks(self):
        """Getter method to access marks"""
        return self._marks

s = Student(80)
print("Student marks (using @property):", s.marks)


"""
OUTPUT:
Student marks (using @property): 80
"""


"""
====================================================
WHY USE @SETTER?
====================================================
1. Allows controlled modification of data
2. Enables validation
3. Prevents invalid values
4. Keeps attribute-style access (s.marks = 90)

----------------------------------------------------
EXAMPLE 2: @property + @setter
----------------------------------------------------
"""

class StudentWithSetter:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        """Getter method"""
        return self._marks

    @marks.setter
    def marks(self, value):
        """Setter method with validation"""
        if value < 0 or value > 100:
            print("Invalid marks! Must be 0-100")
        else:
            self._marks = value

st = StudentWithSetter(85)
print("Initial marks:", st.marks)

st.marks = 150   # ❌ Invalid marks
st.marks = 95    # ✅ Valid marks
print("Updated marks:", st.marks)


"""
OUTPUT:
Initial marks: 85
Invalid marks! Must be 0-100
Updated marks: 95
"""


"""
====================================================
ADVANTAGES OF @PROPERTY AND @SETTER
====================================================
- Protect internal variables (_marks)
- Prevent invalid data assignment
- Can make attributes read-only (no setter)
- Cleaner syntax (s.marks instead of s.get_marks())
- Supports encapsulation and validation

----------------------------------------------------
REAL-WORLD EXAMPLE: BANK ACCOUNT
----------------------------------------------------
"""

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        """Get account balance"""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Set account balance with validation"""
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self._balance = amount

acc = BankAccount(1000)
print("Initial balance:", acc.balance)

acc.balance = -500   # ❌ invalid
acc.balance = 1500   # ✅ valid
print("Updated balance:", acc.balance)


"""
OUTPUT:
Initial balance: 1000
Balance cannot be negative!
Updated balance: 1500
"""


"""
====================================================
KEY POINTS / INTERVIEW NOTES
====================================================
- @property → getter (read-only access)
- @setter → controlled setter (write access)
- Both together → encapsulation in Python
- Syntax is cleaner than traditional get/set methods
- Protects internal variables and allows validation
- Widely used in real-world Python classes

====================================================
END OF README
====================================================
"""
