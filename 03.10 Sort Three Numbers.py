#Prompt for three integers and print them in ascending order.
#Don't try to use the sort statement

# Prompt the user for three integers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

# Compare and order manually
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

# Print in ascending order
print(a, b, c)