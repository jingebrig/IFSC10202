#Prompt for a string consisting of exactly two words separated by a space.
#Print a new string with the first and second word positions swapped (the second word is printed first).
#This task should not use loops or an if statement.

text = input("Enter a string: ")

space = text.find(" ")
new_text = text[space + 1:] + " " + text[:space]

print(new_text)