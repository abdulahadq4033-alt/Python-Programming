# type() function is used to know the datatype of a variable
# typecasting is used to convert one datatype to another datatype
a=31
t=type(a)
print(t)
print(type(a))
b=float(a) # converting integer to float
print(b)
print(type(b))
c=str(a) # converting integer to string
print(c)
print(type(c))
print("The value of a is "+ str(a)) # concatenation of string and integer is not possible without typecasting
d=int(b) # converting float to integer
print(d)
print(type(d))
