#Prompt for a sequence of numbers, the last number being a carriage return.
#Print the maximum value and the number of times it occurs.

#Enter a Number (CR to quit): 1
#Enter a Number (CR to quit): 2
#Enter a Number (CR to quit): 3
#Enter a Number (CR to quit): 2
#Enter a Number (CR to quit): 3
#Enter a Number (CR to quit): 3
#Enter a Number (CR to quit): 3
#Enter a Number (CR to quit):
#Maximum: 3
#Number of Occurrences : 4

# Initialize variables
max_value = None
count_max = 0

# Prompt for sequence of numbers
while True:
    user_input = input("Enter a Number (CR to quit): ")
    if user_input == "":   # Stop when Enter is pressed on a blank line
        break

    num = int(user_input)

    # If first number entered
    if max_value is None:
        max_value = num
        count_max = 1
    else:
        # If new number is greater than current max
        if num > max_value:
            max_value = num
            count_max = 1
        # If new number equals current max
        elif num == max_value:
            count_max += 1

# Print results
print("Maximum:", max_value)
print("Number of Occurrences:", count_max)