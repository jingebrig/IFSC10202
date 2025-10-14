#Prompt for a sequence of numbers, the last number being a carriage return.
#Print the largest value of the numbers.
#If no data is entered (only a carriage was entered), print "Sequence Length is 0".
#Do not use any library calls such as max.

#Enter a Number (CR to quit): 1
#Enter a Number (CR to quit): 9
#Enter a Number (CR to quit): 7
#Enter a Number (CR to quit):
#Maximum: 9

value = input("Enter a Number (CR to quit): ")
if value != '':
    maximum = int(value)
    while value != '':
        if int(value) > maximum:
            maximum = int(value)
        value = input("Enter a Number (CR to quit): ")
    print("Maximum: {}".format(maximum))
else:
    print("Sequence Length is 0")
    