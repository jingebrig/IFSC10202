#Prompt for three integers: two are equal to each other and the third one is different.
#Print the index number of the different one, either 1, 2 or 3.

# Prompt the user for three integers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

# Determine which one is different
if a == b and a != c:
    print(3)
elif a == c and a != b:
    print(2)
else:
    print(1)