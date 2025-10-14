#Prompt for a sequence of numbers, the last number being a carriage return.
#Print the maximum number of consecutive equal elements.
#If a value repeats the same number of times, display the first value.

#Enter a Number (CR to quit): 1
#Enter a Number (CR to quit): 7
#Enter a Number (CR to quit): 7
#Enter a Number (CR to quit): 9
#Enter a Number (CR to quit): 1
#Enter a Number (CR to quit):
#7 repeated 2 times

# Initialize variables
previous = None
current_count = 0
max_count = 0
max_value = None

# Prompt for numbers until a blank line
while True:
    user_input = input("Enter a Number (CR to quit): ")
    if user_input == "":
        break

    num = int(user_input)

    # If same as previous number, increase count
    if num == previous:
        current_count += 1
    else:
        current_count = 1  # reset count for new number

    # Check if this run is the longest so far
    if current_count > max_count:
        max_count = current_count
        max_value = num

    previous = num  # update previous number

# Print result
if max_value is not None:
    print(f"{max_value} repeated {max_count} times")
else:
    print("No numbers were entered.")