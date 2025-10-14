#Prompt for a sequence of numbers, the last number being a carriage return.
#Print the number of elements in this sequence are greater than their previous element.

#Enter a Number (CR to quit): 1
#Enter a Number (CR to quit): 5
#Enter a Number (CR to quit): 2
#Enter a Number (CR to quit): 4
#Enter a Number (CR to quit): 3
#Enter a Number (CR to quit):
#Number of Values Greater Than the Previous: 2
 
#Enter a Number (CR): 
#Sequence Length is 0

# Initialize counters
count_greater = 0
previous = None

# Prompt for numbers until a blank line
while True:
    user_input = input("Enter a Number (CR to quit): ")
    if user_input == "":   # stop when Enter is pressed on a blank line
        break

    num = int(user_input)

    # Compare with previous number (skip first number)
    if previous is not None and num > previous:
        count_greater += 1

    previous = num  # update previous number

# Print the result
print("Number of Values Greater Than the Previous:", count_greater)