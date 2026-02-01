# 4. Add a static method in problem 2, to greet the user with hello.
class hello:
    a=4
    @staticmethod
    def greet():
        print("Good day sir/madam!")
    @staticmethod
    def t():
        print("Thank you for your time!")

o=hello()
hello.greet()
print(o.a) 
o.a=0 
hello.greet()
print(o.a) 
print(hello.a)
hello.t()