#Enter a two digit number and print out its digits separately.
#Be sure to use to F-Strings to create your output.
#Use only math for your solution; do not use any string functions.

# Prompt the user for a two-digit number
num = int(input("Enter a two-digit number: "))

# Extract the tens and ones digits using math
tens = num // 10
ones = num % 10

# Print the digits separately using f-strings
print(f"Ones Digit: {ones}")
print(f"Tens Digit: {tens}")