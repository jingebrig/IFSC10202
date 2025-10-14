#Prompt for a string and cut it into two "equal" parts (If the length of the string is odd, place the center character in the first string, so that the first string contains one more characther than the second).
#Print a new string on a single row with the first and second halves interchanged (second half first and the first half second)
#Don't use the if statement in this task.

s = input("Enter a string: ")

# Calculate the middle index (first half gets the extra char if length is odd)
mid = (len(s) + 1) // 2

# Create the new string with halves swapped
new_text = s[mid:] + s[:mid]

print(new_text)