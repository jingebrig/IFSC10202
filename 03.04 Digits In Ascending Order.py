#Given a three-digit integer, print "YES" if its digits are in ascending order left to right, print "NO" otherwise.
#Do not try to sort the number. Determine each digit and use "if" statements.

# Prompt the user for a three-digit integer
num = int(input("Enter a three-digit number: "))

# Extract each digit
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

# Check if digits are in strictly ascending order
if hundreds < tens and tens < ones:
    print("YES")
else:
    print("NO")