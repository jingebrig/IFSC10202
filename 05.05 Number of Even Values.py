#Prompt for a sequence of numbers, the last number being a carriage return.
#Print the number of even values.

#Enter a Number (CR to quit): 2
#Enter a Number (CR to quit): 1
#Enter a Number (CR to quit): 4
#Enter a Number (CR to quit): 
#Number of Even Values: 2

# Initialize counter for even numbers
even_count = 0

# Prompt for numbers until a blank line
while True:
    user_input = input("Enter a Number (CR to quit): ")
    if user_input == "":   # stop when Enter is pressed on blank line
        break
    num = int(user_input)

    # Check if number is even
    if num % 2 == 0:
        even_count += 1

# Print result
print("Number of Even Values:", even_count)