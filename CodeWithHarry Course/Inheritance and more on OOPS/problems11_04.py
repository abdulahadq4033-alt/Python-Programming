# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):  # Overload +
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):  # Overload *
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)

    def __str__(self):      # For readable printing
        return f"{self.r} + {self.i}i"


# Create objects of your Complex class
c1 = Complex(1, 2)
c2 = Complex(3, 4)

# Test addition
c3 = c1 + c2
print("Sum:", c3)

# Test multiplication
c4 = c1 * c2
print("Product:", c4)
