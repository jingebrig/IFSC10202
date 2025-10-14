#Prompt for a string that contains the letter "h" at least two times.
#In the string, remove the first and last occurance of the letter "h" as well as all the characters between them, then print the result.

text = input("Enter a string that contains the letter h at least two times: ")

first_h = text.find("h")
last_h = text.rfind("h")

result = text[:first_h] + text[last_h + 1:]

print(result)