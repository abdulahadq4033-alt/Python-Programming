class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent constructor called")

    def show(self):
        print("Name:", self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # calls Parent's __init__
        self.age = age
        print("Child constructor called")

    def show(self):
        super().show()           # calls Parent's show()
        print("Age:", self.age)

c = Child("Marcos", 20)
c.show()
