# PROGRAM: Demonstration of loops in Python
# A loop is used to execute a block of code repeatedly

# --------------------------------------------------
# 1. for LOOP
# The for loop is used when the number of iterations is known in advance
# It iterates over a sequence like list, tuple, string, or range

print("1. for loop example")

for i in range(1, 6):
    # range(1, 6) generates numbers from 1 to 5
    print(i)

# --------------------------------------------------
# 2. while LOOP
# The while loop is used when the number of iterations is NOT known beforehand
# It keeps running as long as the condition is True

print("\n2. while loop example")

count = 1
while count <= 5:
    # This loop runs until count becomes greater than 5
    print(count)
    count += 1  # increment is necessary to avoid infinite loop

# --------------------------------------------------
# 3. for loop with else
# The else block executes when the loop completes normally (without break)

print("\n3. for loop with else")

for i in range(3):
    print(i)
else:
    # This executes after the for loop finishes completely
    print("Loop finished successfully")

# --------------------------------------------------
# 4. while loop with else
# else runs when while loop condition becomes False naturally

print("\n4. while loop with else")

x = 3
while x > 0:
    print(x)
    x -= 1
else:
    print("While loop ended")

# --------------------------------------------------
# 5. break statement
# break is used to terminate the loop immediately

print("\n5. break statement")

for i in range(1, 6):
    if i == 3:
        break  # exits the loop when i equals 3
    print(i)

# --------------------------------------------------
# 6. continue statement
# continue skips the current iteration and moves to the next one

print("\n6. continue statement")

for i in range(1, 6):
    if i == 3:
        continue  # skips printing 3
    print(i)

# --------------------------------------------------
# 7. pass statement
# pass is a null statement; it does nothing
# It is used when a statement is required syntactically

print("\n7. pass statement")

for i in range(1, 4):
    if i == 2:
        pass  # placeholder, no action taken
    print(i)

# --------------------------------------------------
# 8. Nested loops
# A loop inside another loop is called a nested loop

print("\n8. nested loops example")

for i in range(1, 4):
    for j in range(1, 4):
        # Inner loop runs fully for each iteration of outer loop
        print(i, j)
