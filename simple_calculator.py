# Program to make simple calculator
a=float(input("Enter a number: "))
b=float(input("Enter another number: "))
print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("Multiplication", a*b)
if(b==0):
    print("Cannot divide by zero")
else:
    print("Division: ",a/b)
