#Enter a three digit number and reverse the digits.
#Be sure to use to F-Strings to create your output.
#Use only math for your solution; do not use any string functions.

# Prompt the user for a three-digit number
num = int(input("Enter A 3 Digit Number: "))

# Extract each digit using math
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

# Reverse the digits to form a new number
reversed_num = ones * 100 + tens * 10 + hundreds

# Print the result using an f-string
print(f"Reverse Of Digits: {reversed_num}")