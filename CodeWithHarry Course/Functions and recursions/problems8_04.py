# 4. Write a recursive function to calculate the sum of first n natural numbers.
# sum(n)=sum(n-1)+n
def sum_n(n): # sum is already a built-in function in python so we write it as sum_n
    if (n <= 0):
        return "Not a natural number"
    elif (n == 1):
        return 1
    else:
        return sum_n(n - 1) + n

n = int(input("Enter a natural number: "))
result = sum_n(n)
print(result)
