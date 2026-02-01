# 6. Write a python function which converts 
# cm= inches x 2.54
def inch_to_cms(inch):
    return inch*2.54

n=int(input("Enter a number in inches: "))
print("In cms: ", inch_to_cms(n))