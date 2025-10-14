#Prompt for a string containing integers separated by spaces.
#Load the values into a list.
#Print all of the elements that are greater than the previous element.
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)

# Prompt for input
nums = input("Enter Values Separated by Spaces: ").split()

# Convert strings to integers
for i in range(len(nums)):
    nums[i] = int(nums[i])

# Print values greater than the previous one
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        print(nums[i])