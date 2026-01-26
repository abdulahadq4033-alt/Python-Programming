# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# 8. If languages of two friends are same; what will happen to the program in problem 6?
s={}
name=input("Enter your name: ")
lang=input("Enter your language: ")
s.update({name:lang})

name=input("Enter your name: ")
lang=input("Enter your language: ")
s.update({name:lang})

name=input("Enter your name: ")
lang=input("Enter your language: ")
s.update({name:lang})

name=input("Enter your name: ")
lang=input("Enter your language: ")
s.update({name:lang})

print(s)