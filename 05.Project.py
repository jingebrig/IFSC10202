# Create a program that displays special numbers in a range. A special number is defined to be number
# that is the sum of its own digits each raised to the power of the number of digits.
# 153 is 3 digits long and is equal to 1^3 + 5^3 + 3^3
# 8208 is 4 digits long and is equal to 8^4 + 2^4 + 0^4 + 8^4
# 
# Hint: First determine the number of digits using a while loop and reminder division by 10. 
# Do not use any string functions or the len function.
# 
# Hint: Recalculate the value using the power from above and see if you get the original value
# Do not use the len function to determine the number of digits.


start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
length = 0        # use of the while loop to determine the number of digits of an integer
while start > 0:
    start //= 10  # this is equivalent to n = n // 10
    length += 1
    
    exp = length  # exp = exponent
    spec_num = digit**exp + digit**exp =



#for num in range(start, end):


#Here is another example  n:

