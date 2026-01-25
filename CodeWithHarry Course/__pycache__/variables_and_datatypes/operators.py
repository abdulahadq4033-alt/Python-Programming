# arithmetic operators
print("Arithmetic Operators:")
a = 10 # the symbol '=' is used for assignment
b=2 # the symbol '=' is used for assignment
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)

# assignment operators
print("\nAssignment Operators:")
c = 5
print("Initial value of c:", c)
c += 3  # equivalent to c = c + 3
print("After c += 3, c =", c)
c -= 2  # equivalent to c = c - 2
print("After c -= 2, c =", c)
c *= 4  # equivalent to c = c * 4
print("After c *= 4, c =", c)
c /= 2  # equivalent to c = c / 2
print("After c /= 2, c =", c)
c %= 3  # equivalent to c = c % 3
print("After c %= 3, c =", c)
# comparison operators
print("\nComparison Operators:")
x = 15
y = 20
print("x =", x)
print("y =", y)
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
# logical operators
print("\nLogical Operators:")
# truth table for logical OR
p = True or False
q = False or False
r = True or True
s = False or True
print("Truth Table for Logical OR:")
print("True or False =", p)
print("False or False =", q)
print("True or True =", r)
print("False or True =", s)
# truth table for logical AND
p = True and False
q = False and False
r = True and True
s = False and True
print("\nTruth Table for Logical AND:")
print("True and False =", p)
print("False and False =", q)
print("True and True =", r)
print("False and True =", s)
# truth table for logical NOT
p = not True
q = not False
print("\nTruth Table for Logical NOT:")
print("not True =", p)
print("not False =", q)