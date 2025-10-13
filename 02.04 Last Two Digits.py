#Enter a number greater than zero and print the value its last two digits.
#Be sure to use to F-Strings to create your output.  You will have to use leading zeros.
#Use only math for your solution; do not use any string functions.

# Prompt the user for a number greater than zero
num = int(input("Enter A Number Greater Than Zero: "))

# Get the last two digits using math
last_two = num % 100

# Print with leading zeros using f-string formatting
print(f"Last Two Digits: {last_two:02d}")