#Prompt for two two-digit numbers.
#Merge them into single number as follows:
    #Tens digit from first number
    #Tens digit from second number
    #Units digit from first number
    #Units digit form second number
#Be sure to use to F-Strings to create your output.
#Use only math for your solution; do not use any string functions.

# Prompt the user for two two-digit numbers
num1 = int(input("Enter First 2 Digit Number: "))
num2 = int(input("Enter Second 2 Digit Number: "))

# Extract digits using math
tens1 = num1 // 10
ones1 = num1 % 10
tens2 = num2 // 10
ones2 = num2 % 10

# Merge the digits as specified:
# Tens from first, tens from second, ones from first, ones from second
merged = tens1 * 1000 + tens2 * 100 + ones1 * 10 + ones2

# Print the result using f-string
print(f"Merged Number: {merged}")