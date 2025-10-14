#Prompt for a sequence of numbers, the last number being a carriage return.
#Print the maximum and second maximum of the sequence.
#Assume that at least two numbers will always be entered.
#Hint: Each time you find a new maximum, the old maximum becomes the second maximum.

#Enter First Number: 1
#Enter Second Number: 9
#Enter a Number (CR to quit): 2
#Enter a Number (CR to quit): 3
#Enter a Number (CR to quit): 4
#Enter a Number (CR to quit): 5
#Enter a Number (CR to quit): 6
#Enter a Number (CR to quit): 7
#Enter a Number (CR to quit): 8
#Enter a Number (CR to quit): 10
#Enter a Number (CR to quit): 
#First Maximum: 10
#Second Maximum: 9

# Prompt for the first two numbers
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

# Initialize maximums
if num1 > num2:
    max1 = num1
    max2 = num2
else:
    max1 = num2
    max2 = num1

# Continue prompting for more numbers
while True:
    user_input = input("Enter a Number (CR to quit): ")
    if user_input == "":   # Stop on blank line
        break

    num = int(user_input)

    # Update maximums as needed
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

# Print results
print("First Maximum:", int(max1) if max1.is_integer() else max1)
print("Second Maximum:", int(max2) if max2.is_integer() else max2)