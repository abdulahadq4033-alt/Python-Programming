marks = {
    "Ronaldo" : 100,
    "Messi" : 100,
    "Neymar": 84,
    "Foden" : 74,
    "Brahim" : 23
}
print(marks, type(marks))
print(marks["Neymar"])

print(marks.get("Harry")) # Prints none
print(marks["Harry"]) # Returns an error
d={} # Empty dictionary