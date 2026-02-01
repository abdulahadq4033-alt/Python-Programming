# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
import math
class calculator:
    def __init__(self, n):
        self.n=n
    def square(self):
        print(f"The square is {self.n*2}")
    def cube(self):
        print(f"The cube is {self.n**3}")
    def sqrt(self):
        print(f"The sqrt is {math.sqrt(self.n)}")

a=calculator(9)
a.square()
a.cube()
a.sqrt()