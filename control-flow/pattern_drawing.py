# Prompt the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the square pattern
while row < size:
    for col in range(size):
        print("*", end="")  # Print asterisks on the same line
    print()  # Move to the next line after a row is complete
    row += 1
