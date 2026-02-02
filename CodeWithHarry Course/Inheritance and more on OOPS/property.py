class Student:
    def __init__(self, marks):
        self._marks = marks   # protected variable

    @property
    def marks(self):
        return self._marks

s = Student(85)
print(s.marks)   # accessed like an attribute
