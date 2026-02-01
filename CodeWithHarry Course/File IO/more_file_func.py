f =open("another.txt")
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()

f.close()
