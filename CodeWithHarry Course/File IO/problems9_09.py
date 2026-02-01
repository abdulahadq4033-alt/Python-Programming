# 9. Write a program to find out whether a file is identical & matches the content of another file.
with open("donkey.txt") as f:
    content1 =f.read()

with open("diary.txt") as f:
    content2 =f.read()

if(content1==content2):
    print("These files are identical")

else:
    print("These files are not identical")