# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner
Marks=[]
f1=int(input("Enter the mark: "))
Marks.append(f1)
f2=int(input("Enter the mark: "))
Marks.append(f2)
f3=int(input("Enter the mark: "))
Marks.append(f3)
f4=int(input("Enter the mark: "))
Marks.append(f4)
f5=int(input("Enter the mark: "))
Marks.append(f5)
f6=int(input("Enter the mark: "))
Marks.append(f6)

Marks.sort()

print(Marks)