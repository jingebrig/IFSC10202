#Prompt for a string containing integers separated by spaces.
#Load the values into a list.
#Find and print the elements that appear in the list only once. The elements must be printed in the order in which they occur in the original list.
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)
#Hint: Loop through each element of the list, then loop through the list to look for a match. Be sure that you do not match the element to itself.

# Prompt for input
nums = input("Enter Values Separated by Spaces: ").split()

# Convert all to integers
for i in range(len(nums)):
    nums[i] = int(nums[i])

print("Unique Elements:", end=" ")

# Loop through each element to find unique ones
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j] and i != j:
            count += 1
    if count == 0:
        print(nums[i], end=" ")

print()