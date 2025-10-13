#Enter a three digit number and print the sum of the digits.
#Be sure to use to F-Strings to create your output.
#Use only math for your solution; do not use any string functions.

# Prompt the user for a three-digit number
num = int(input("Enter A 3 Digit Number: "))

# Extract each digit using math
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

# Compute the sum of the digits
digit_sum = hundreds + tens + ones

# Print the result using an f-string
print(f"Sum Of Digits: {digit_sum}")