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
    