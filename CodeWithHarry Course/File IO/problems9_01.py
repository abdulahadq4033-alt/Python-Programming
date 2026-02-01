# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.
with open("something.txt") as f:
    content= f.read()
    if("twinkle" in content):
        print("twinkle is present")
    else:
        print("The word twinkle is not present")