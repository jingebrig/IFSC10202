#Enter a two digit number and swap their digits and create a new two digit number.
#Be sure to use to F-Strings to create your output.
#Use only math for your solution; do not use any string functions.

# Prompt the user for a two-digit number
num = int(input("Enter a two-digit number: "))

# Extract the tens and ones digits using math
tens = num // 10
ones = num % 10

# Swap the digits to form a new number
swapped = ones * 10 + tens

# Print the result using f-strings
print(f"Swapped Number: {swapped}.")