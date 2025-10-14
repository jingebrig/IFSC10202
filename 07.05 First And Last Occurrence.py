#Prompt for a string. Determine if the string contains the letter "f"
    #If the string contains one letter "f", print the index
    #If the string contains more than one letter "f", print the index of the first and last occurance
    #If the string does not contain any letter "f", then print zero (0)

text = input("Enter a string: ")

if "f" not in text:
    print(0)
elif text.count("f") == 1:
    print(text.find("f"))
else:
    print(text.find("f"), text.rfind("f"))