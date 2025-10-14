#For the given integer N, calculate the sum cubes of each number from 1 to N.
    #1**3 + 2**3 + … + N**3

# Prompt the user for an integer N
N = int(input("Enter number: "))

# Initialize sum
sum_cubes = 0

# Calculate the sum of cubes from 1 to N
for i in range(1, N + 1):
    sum_cubes += i ** 3

# Print the result
print(sum_cubes)