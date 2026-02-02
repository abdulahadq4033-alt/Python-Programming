print("=== SIMPLE CALCULATOR ===")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1-4): ")

match choice:
    case "1":
        print("Result:", a + b)

    case "2":
        print("Result:", a - b)

    case "3":
        print("Result:", a * b)

    case "4":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero")

    case _:
        print("Invalid choice")
