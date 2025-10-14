#Prompt for a sequence of numbers, the last number being a carriage return.
#Print largest value and the index the largest value of the numbers.
#If no data is entered (only a carriage was entered), print "Sequence Length is 0".
#Do not use any library calls, such as max or index.

#Enter a Number (CR to quit): 1
#Enter a Number (CR to quit): 9
#Enter a Number (CR to quit): 7
#Enter a Number (CR to quit): 
#Maximum: 9
#Index of Maximum: 2
 
#Enter a Number (CR to quit): 
#Sequence Length is 0

# Initialize variables
largest = None
index_of_largest = -1
count = 0
position = 0

# Prompt for sequence of numbers
while True:
    user_input = input("Enter a Number (CR to quit): ")
    if user_input == "":   # Stop on blank line
        break

    num = int(user_input)
    count += 1
    position += 1

    # Update largest value and its index
    if largest is None or num > largest:
        largest = num
        index_of_largest = position

# Check for empty input
if count == 0:
    print("Sequence Length is 0")
else:
    print("Maximum:", largest)
    print("Index of Maximum:", index_of_largest)