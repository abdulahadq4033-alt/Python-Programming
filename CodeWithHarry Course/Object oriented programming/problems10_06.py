# 6. Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

class Student:
    def __init__(harry, name, marks):
        harry.name = name
        harry.marks = marks

    def display(harry):
        print(f"Name: {harry.name}")
        print(f"Marks: {harry.marks}")

s1 = Student("Harry", 95)
s1.display()
