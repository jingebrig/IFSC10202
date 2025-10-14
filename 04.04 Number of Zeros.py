#Given N numbers: the first number in the input is N, after that N integers are given.
#Count the number of zeros among the given integers and print it.
#You need to count the numbers that are equal to zero, not the number of zero digits.

# Read the number of integers
N = int(input("Enter N: "))

count_zeros = 0  # Counter for zeros

# Read N integers and count how many are zero
for i in range(N):
    num = int(input("Enter Number: "))
    if num == 0:
        count_zeros += 1

# Print the result
print(f"Number of Zeros: {count_zeros}")