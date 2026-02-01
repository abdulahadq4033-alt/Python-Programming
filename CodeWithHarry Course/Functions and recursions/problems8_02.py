# 2. Write a python program using function to convert Celsius to Fahrenheit.
# F=(C * 9/5)+32
# C=(F-3/2)*5/9
def temp(C):
    return ( C * 9/5)+32
C=int(input("Enter the temp in celcius: "))
F=temp(C)
print(f"Fahrenheit {F}")