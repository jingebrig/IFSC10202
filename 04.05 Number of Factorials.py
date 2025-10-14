#Given an integer N, print the sum of: 1! + 2! + 3! + ... + N!
#This problem has a solution with only one loop, so try to discover it.
#Don't use the math library.

# Prompt the user for an integer N
N = int(input("Enter N: "))

# Initialize variables
factorial = 1
sum_factorials = 0

# Use one loop to calculate both factorial and sum
for i in range(1, N + 1):
    factorial *= i          # calculate i! incrementally
    sum_factorials += factorial  # add i! to the total sum

# Print the result
print(f"Sum of Factorials: {sum_factorials}")