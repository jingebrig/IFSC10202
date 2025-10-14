#A palindrome is a number which reads the same when read forward as it it does when read backward.
#Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.
#Hint: put the units, tens, hundreds, and thousands in separate variables. Do not use any string functions.

# Prompt the user for a four-digit integer
num = int(input("Enter a four-digit integer: "))

# Extract each digit
thousands = num // 1000
hundreds = (num // 100) % 10
tens = (num // 10) % 10
ones = num % 10

# Check for palindrome: first equals last, second equals third
if thousands == ones and hundreds == tens:
    print("YES")
else:
    print("NO")