#Division of an integer by another integer will always yield a floating, even if it is evenly divisible.
#The remainder operator, %, yields an integer that is the remainder after integer division.
#The floor division operator, //, yield an integer that is portion of the division where the remainder is discarded.
#Remember that division by zero is undefined. Python will give you an error and your program will stop.

print(18 / 3)   # Results in a float
print(17 / 3)   # Results in a float
print(17 // 3)  # Results in an int
print(17 % 3)   # Results in an int