n=int(input("enter the range"))
a=0
b=1
i=1
print(a)
print(b)
while i<n-1:
    c=a+b
    a=b
    b=c
    print(c)
    i=i+1
