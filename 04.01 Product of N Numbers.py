#N numbers are given in the input. Read them and print their product.
#The first line of input contains the integer N, which is the number of integers to follow.
#Each of the next N lines contains one integer. Print the product of these N integers.

# Read the number of integers
N = int(input("Enter N: "))

product = 1  # Start with 1 because it's the multiplicative identity

# Read N integers and multiply them together
for i in range(N):
    num = int(input("Enter number: "))
    product *= num

# Print the result
print(product)