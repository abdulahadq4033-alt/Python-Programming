class Grandparent:
    def house(self):
        print("Grandparent owns a house")

class Parent(Grandparent):
    def car(self):
        print("Parent owns a car")

class Child(Parent):   # Multilevel inheritance
    def bike(self):
        print("Child owns a bike")

c = Child()
c.house()   # from Grandparent
c.car()     # from Parent
c.bike()    # Child's own method
