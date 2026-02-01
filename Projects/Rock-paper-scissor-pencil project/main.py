import random
'''
1  for Rock
-1 for Paper
2  for Scissors
0  for Pencil
'''

computer = random.choice([1, -1, 2, 0])

youstr = input("Enter your choice (r/p/s/c): ")

youDict = {
    "r": 1,
    "p": -1,
    "s": 2,
    "c": 0
}

reverseDict = {
    1: "Rock",
    -1: "Paper",
    2: "Scissors",
    0: "Pencil"
}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw")

else:
    if (you == 1 and computer in [2, 0]):
        print("You win!")

    elif (you == -1 and computer == 1):
        print("You win!")

    elif (you == 2 and computer in [-1, 0]):
        print("You win!")

    elif (you == 0 and computer == -1):
        print("You win!")

    else:
        print("You lose!")
