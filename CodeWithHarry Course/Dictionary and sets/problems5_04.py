# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20') 

print(len(s))

# Why is the length 2? 
# The answer is that 20 and 20.0 are numerically equal regardless of datatype