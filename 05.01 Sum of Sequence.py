#Enter a Number (CR to quit): 1
#Enter a Number (CR to quit): 7
#Enter a Number (CR to quit): 9
#Enter a Number (CR to quit): 
#Sum: 17

sequencesum = 0
value = input("Enter a Number (CR to quit): ")
while value != '':
        sequencesum += int(value)
        value = input("Enter a Number (CR to quit): ")
print("Sum: {}".format(sequencesum))