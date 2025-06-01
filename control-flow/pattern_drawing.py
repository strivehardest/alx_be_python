# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop - controls the rows (while loop)
while row < size:
    # Inner loop - controls the columns (for loop)
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Print newline after each row
    row += 1
