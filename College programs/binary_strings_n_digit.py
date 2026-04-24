def generate_binary_strings(n):
    """Generates all binary strings of n-bit length."""
    if n <= 0:
        return

    def backtrack(current_string):
        # Base case: if the string is complete
        if len(current_string) == n:
            print("".join(current_string))
            return

        # Add '0'
        current_string.append('0')
        backtrack(current_string)
        current_string.pop()

        # Add '1'
        current_string.append('1')
        backtrack(current_string)
        current_string.pop()

    backtrack([])

# Example Usage:
print("Binary strings of length 3:")
generate_binary_strings(3)
