# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
letter = '''
 Dear <|Name|>,
 You are selected!
 <|Date|>
 '''
print(letter.replace("<|Name|>", "Marcos").replace("<|Date|>", "24nd August")) 
# Chaining:
# Chaining means calling multiple methods one after another in a single line of code, 
# where the output of one method becomes the input of the next.