#Enter a positive real number and print its fractional part.
#Be sure to use to F-Strings to create your output.
#Use only math for your solution; do no use any string functions.
#Hint: Round the result to 10 digits using the round function.

# Prompt the user for a positive real number
num = float(input("Enter A number: "))

# Extract the fractional part using only math
fractional_part = num - int(num)

# Round the result to 10 digits
fractional_part = round(fractional_part, 10)

# Print the result using an f-string
print(f"Fractional Part: {fractional_part}")