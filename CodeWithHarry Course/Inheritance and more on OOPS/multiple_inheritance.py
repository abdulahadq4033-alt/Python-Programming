class Father:
    def drive(self):
        print("Father knows driving")

class Mother:
    def cook(self):
        print("Mother knows cooking")

class Child(Father, Mother):   # Multiple inheritance
    def study(self):
        print("Child is studying")

c = Child()
c.drive()   # from Father
c.cook()    # from Mother
c.study()   # Child's own method
