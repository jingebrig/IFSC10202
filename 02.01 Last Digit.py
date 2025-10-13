#Prompt for a number and print its last digit.
#Be sure to use to F-Strings to create your output.
#Use only math for your solution; do no use any string functions.

# Prompt the user for a number
num = int(input("Enter a number: "))

# Get the last digit using math
last_digit = abs(num % 10)

# Print the result using an f-string
print(f"Last digit: {last_digit}")