#Prompt for two integer values A and B.
#If A < B, print all numbers from A to B inclusively in ascending order.
#If A ≥ B, print all numbers from B to A inclusively in descending order.

# Prompt the user for two integers
A = int(input("Enter A: "))
B = int(input("Enter B: "))

# Check order and print accordingly
if A < B:
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, B - 1, -1):
        print(i)