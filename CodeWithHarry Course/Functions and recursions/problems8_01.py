# 1. Write a program using functions to find greatest of three numbers
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))

def greatest(a,b,c):
    if(a>b and a>c):
        print(f"{a} is the greatest")
    elif(b>a and b>c):
        print(f"{b} is the greatest")
    elif(c>a and c>b):
        print(f"{c} is the greatest")

greatest(a,b,c)

