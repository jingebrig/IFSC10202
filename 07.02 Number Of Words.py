#Prompt for a string consisting of words separated by a single space. Display how many words it has.
#Hint: Count the number of spaces.

s=(input("Enter a string: "))
x = s.find(" ") + 1
print(f"{x} words")