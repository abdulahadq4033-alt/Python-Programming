# 5. Repeat program 4 for a list of such words to be censored.
words = ["donkey", "idiot", "stupid"]

with open("censor.txt", "r") as f:
    content = f.read().lower()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("censor.txt", "w") as f:
    f.write(content)
