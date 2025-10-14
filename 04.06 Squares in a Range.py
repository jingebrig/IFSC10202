#Given two integers A and B, print the squares of all integer numbers between them inclusively as shown below.
#Be sure to print the formula as shown.
#There are no spaces around * and =.
#You can use either the sep= argument of the print() statement or the .format method.

# Prompt the user for two integers
A = int(input("Enter A: "))
B = int(input("Enter B: "))

# Print the squares between A and B inclusively
for i in range(A, B + 1):
    print("{}*{}={}".format(i, i, i * i))