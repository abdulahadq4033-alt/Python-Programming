class Student:
    school = "ABC Public School"   # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    def show(self):
        print("Name:", self.name)
        print("School:", self.school)

s1 = Student("Rahul")
s2 = Student("Anita")

s1.show()
s2.show()

Student.change_school("XYZ International School")

s1.show()
s2.show()
