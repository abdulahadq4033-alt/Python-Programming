# 5. Write a program which finds out whether a given name is present in a list or not.
l=["A","B","C","D"]

name=input("Enter your name: ")

if(name in l):
    print("It is in the list")
else:
    print("It is not in the list. Get out!")