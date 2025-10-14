#Prompt for three numbers and print the smallest value. Do not use the MIN function.
#Try to use the cascade if-elif-else.

# Prompt the user for three numbers
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

# Determine the smallest number using if-elif-else
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

# Display the result
print(smallest)