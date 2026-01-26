# 1. Write a program to find the greatest of four numbers entered by the user.
a =int(input("Enter number 1: "))
b =int(input("Enter number 2: "))
c =int(input("Enter number 3: "))
d =int(input("Enter number 4: "))

if(a>b and a>c and a>d):
    print(f"{a} is the greatest")

elif(b>a and b>c and b>d):
    print(f"{b} is the greatest")  

elif(c>a and c>b and c>d):
    print(f"{c} is the greatest")

elif(d>a and d>b and d>c):
    print(f"{d} is the greatest")