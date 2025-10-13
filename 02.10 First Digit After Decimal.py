#Prompt for a positive real number
#Print the first digit to the right of the decimal point.
#Be sure to use to F-Strings to create your output.
#Use only math for your solution; do not use any string functions.

# Prompt the user for a positive real number
num = float(input("Enter Number: "))

# Shift the decimal one place to the right and extract the first digit
tenths = int(num * 10) % 10

# Print the result using an f-string
print(f"Tenths Value: {tenths}")