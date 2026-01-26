# Program to check if you are eligible to vote
a=int(input("Enter your age: "))
# Independent if statement
if(a>60):
    print("You are a senior citizen")
# if-elif-else ladder
if(a>=18):
    print("You can vote")

elif(a<0):
    print("You are an idiot")

elif(a==0):
    print("Your age is zero")

else:
    print("You cannot vote")

print("Here ya go")