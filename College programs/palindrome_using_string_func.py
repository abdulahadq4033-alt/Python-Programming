s=input("")
i,j=0, len(s)-1
is_p= True
while i<j:
    if s[i]!=s[j]:
        is_p=False
        break
    i+=1
    j-=1
if is_p:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")
