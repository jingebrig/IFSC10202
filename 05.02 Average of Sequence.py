#Prompt for a sequence of numbers, the last number being carriage return
#Print the average of the numbers
#If no data is entered (only a carriage was entered), you will generate an error (division by zero). If no data is entered, print "Sequence Length is 0".

#Enter a Number (CR to quit): 1
#Enter a Number (CR to quit): 7
#Enter a Number (CR to quit): 9
#Enter a Number (CR to quit): 
#Average: 5.666666666666667

sequencesum = 0
sequencecount = 0
value = input("Enter a Number (CR to quit): ")
while value != '':
    sequencesum += int(value)
    sequencecount += 1
    value = input("Enter a Number (CR to quit): ")
if sequencecount != 0:                               #avoid division by 0
    sequenceaverage = sequencesum / sequencecount 
    print("Average: {}".format(sequenceaverage))
else:
    print("Sequence Lenth is 0")