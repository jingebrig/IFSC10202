#Prompt for a string containg the letter "h" at least two times.
#Reverse the sequence of characters between the first letter "h" and the last letter "h"

text = input("Enter a string containg the letter h at least two times: ")

first_h = text.find("h")
last_h = text.rfind("h")

# Reverse the part between the first and last 'h'
reversed_part = text[first_h + 1:last_h][::-1]

# Combine everything back together
result = text[:first_h + 1] + reversed_part + text[last_h:]

print(result)