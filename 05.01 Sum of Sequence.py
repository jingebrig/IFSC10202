#Prompt for a sequence of numbers, the last number being a carriage return.
#Print the sum of the numbers.

# Initialize sum
total = 0

# Loop until user presses Enter on a blank line
while True:
    user_input = input("Enter a Number (CR to quit): ")
    if user_input == "":   # stop when input is blank
        break
    total += int(user_input)  # add to total (use int() if only integers are needed)

# Print the total sum
print("Sum:", total)