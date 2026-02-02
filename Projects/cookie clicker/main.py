cookies = 0
cookies_per_click = 1
auto_cookies = 0

click_upgrade_cost = 10
auto_upgrade_cost = 25

game_running = True

print("🍪 COOKIE CLICKER 🍪")
print("Each input is one turn.\n")

while game_running:
    # Auto cookies per turn
    cookies += auto_cookies

    print("\nChoose an option:")
    print("1. Click cookie")
    print("2. Upgrade click (+1)")
    print("3. Upgrade auto (+1 per turn)")
    print("4. Show stats")
    print("5. Help")
    print("0. Exit")

    choice = input("> ")

    if choice == "1":
        cookies += cookies_per_click
        print(f"You clicked the cookie! +{cookies_per_click} cookies")

    elif choice == "2":
        if cookies >= click_upgrade_cost:
            cookies -= click_upgrade_cost
            cookies_per_click += 1
            click_upgrade_cost += 10
            print("Click power upgraded!")
        else:
            print("Not enough cookies.")

    elif choice == "3":
        if cookies >= auto_upgrade_cost:
            cookies -= auto_upgrade_cost
            auto_cookies += 1
            auto_upgrade_cost += 25
            print("Auto cookie gained (+1 per turn)")
        else:
            print("Not enough cookies.")

    elif choice == "4":
        print("\n--- STATS ---")
        print(f"Cookies: {cookies}")
        print(f"Cookies per click: {cookies_per_click}")
        print(f"Auto cookies per turn: {auto_cookies}")
        print(f"Click upgrade cost: {click_upgrade_cost}")
        print(f"Auto upgrade cost: {auto_upgrade_cost}")

    elif choice == "5":
        print("\n--- HELP ---")
        print("1 -> Click cookie")
        print("2 -> Upgrade click")
        print("3 -> Upgrade auto")
        print("4 -> View stats")
        print("0 -> Exit")

    elif choice == "0":
        print("Thanks for playing Cookie Clicker! 🍪")
        game_running = False

    else:
        print("Invalid option. Choose a number from the menu.")
