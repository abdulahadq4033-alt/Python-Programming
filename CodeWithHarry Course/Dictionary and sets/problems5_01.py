# 1. Write a program to create a dictionary of Spanish words with values as their English
# translation. Provide user with an option to look it up!
words={
    "Hola" : "Hello",
    "Gracias" : "Thank you",
    "Si": "yes",
}
word=input("Enter the word you want to translate: ")
print(words[word])