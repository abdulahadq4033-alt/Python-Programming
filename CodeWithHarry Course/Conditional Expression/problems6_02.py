# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
mark1=int(input("Enter English marks: "))
mark2=int(input("Enter Maths marks: "))
mark3=int(input("Enter Science marks: "))

# Check for total percentage:
total_marks=(mark1+mark2+mark3)/300
total_percentage = total_marks*100

if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You passed!", total_percentage)
else:
    print("You failed! Such a failure!", total_percentage)