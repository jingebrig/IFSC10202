#Prompt for a string.
#Remove all of the letter "@" from the string and print it.

text = input("Enter a string: ")
text = text.replace("@", "")
print(text)