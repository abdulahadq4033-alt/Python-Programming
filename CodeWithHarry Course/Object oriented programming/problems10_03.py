# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?
class hello:
    a=4

o=hello()
print(o.a) # Class attribute is printed
o.a=0 # Instance attribute is set
print(o.a) # Instance attribute is printed
print(hello.a)

# Hence this does not change the class attribute. o.a=0 is an instance attribute
# and it will take priority over class attribute.