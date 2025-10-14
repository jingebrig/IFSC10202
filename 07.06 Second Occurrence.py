#Prompt for a string. Determine if the string contains the letter "f".
    #Print the index of the second location of the letter "f".
    #If the string contains the letter "f" only once, then print "One f".
    #If the string does not contain the letter "f", then pring "Zero f".

text = input("Enter a string: ")

first_index = text.find("f")

if first_index == -1:
    print("Zero f")
else:
    second_index = text.find("f", first_index + 1)
    if second_index == -1:
        print("One f")
    else:
        print(second_index)