MAX = 5
stack = []
top = -1

# Recursive push function
def push():
    global top

    if top == MAX - 1:
        print("Stack Overflow! Cannot push.")
        return

    value = int(input("Enter value to push: "))
    stack.append(value)
    top += 1

    choice = int(input("Do you want to push another element? (1 = Yes / 0 = No): "))
    if choice == 1:
        push()   # recursive call


# Recursive pop function
def pop():
    global top

    if top == -1:
        print("Stack Underflow! Stack is empty.")
        return

    print("Popped element:", stack.pop())
    top -= 1

    choice = int(input("Do you want to pop another element? (1 = Yes / 0 = No): "))
    if choice == 1:
        pop()    # recursive call


# Display stack elements
def display():
    if top == -1:
        print("Stack is empty.")
        return

    print("Stack elements:")
    for i in range(top, -1, -1):
        print(stack[i])


# Main program (do–while simulation)
def main():
    while True:
        print("\n--- STACK MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        # Switch statement using match-case
        match choice:
            case 1:
                push()
            case 2:
                pop()
            case 3:
                display()
            case 4:
                print("Exiting program...")
                break
            case _:
                print("Invalid choice! Try again.")


main()
