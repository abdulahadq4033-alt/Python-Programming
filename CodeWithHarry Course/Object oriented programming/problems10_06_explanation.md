In Python, 'self' is NOT a keyword.
It is just a convention used to refer to the current object.

You can replace 'self' with any valid variable name like:
- slf
- harry
- obj

Python automatically passes the object as the first argument
when calling an instance method.

So:
s1.display()

internally becomes:
Student.display(s1)
