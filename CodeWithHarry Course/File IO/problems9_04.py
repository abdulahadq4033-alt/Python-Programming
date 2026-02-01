# 4. A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 
word = "donkey"

with open("donkey.txt", "r") as f:
    content = f.read()

content_new = content.lower().replace(word, "#####")

with open("donkey.txt", "w") as f:
    f.write(content_new)
