#Given three integers, determine how many of them are equal to each other.
#The program must print one of these numbers:
    #3 (if all are the same),
    #2 (if two of them are equal to each other and the third is different) or
    #0 (if all numbers are different).

# Prompt the user for three integers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

# Check for equality cases
if a == b == c:
    print(3)   # All three are equal
elif a == b or a == c or b == c:
    print(2)   # Two are equal
else:
    print(0)   # All are different