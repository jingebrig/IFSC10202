#In mathematics, the factorial of an integer N, denoted by N! is the following product:
#N! = 1 × 2 × … × N
#For the given integer N, calculate the value N!
#Don't use the math module in this exercise.

# Prompt the user for an integer N
N = int(input("Enter Number: "))

# Initialize factorial result
factorial = 1

# Calculate N! using a loop
for i in range(1, N + 1):
    factorial *= i

# Print the result
print(factorial)