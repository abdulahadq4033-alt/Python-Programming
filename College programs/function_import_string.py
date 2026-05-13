#21. Write a function that takes a sentence as an input parameter and replaces the first letter of every word with the corresponding upper case letter and the rest of the letters in the word by corresponding letters in lowercase without using a built-in function 
import string  
s = "python is great"  
print("Original string:")  
print(s)  
print("After capitalizing first letter:")  
result = string.capwords(s) 
 #by using built-in functions  
print(result)
