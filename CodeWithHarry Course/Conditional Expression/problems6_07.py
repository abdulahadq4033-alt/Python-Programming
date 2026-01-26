# 7. Write a program to find out whether a given post is talking about “Harry” or not.
d=input("Enter post: ")
if("Harry".lower() in d.lower()):
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")