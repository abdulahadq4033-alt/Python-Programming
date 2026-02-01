class Student:
    school = "ABC Public School"   # class attribute

    def __init__(self, name):
        self.name = name           # instance attribute


s1 = Student("Rahul")
s2 = Student("Amit")

print(s1.name)        # instance attribute
print(s2.name)

print(s1.school)      # class attribute
print(s2.school)
