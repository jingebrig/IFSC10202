#Prompt for a string containing integers separated by spaces.
#Load the values into a list.
#Determine and print the quantity of elements that are greater than both of their neighbors.
#The first and the last items of the list shouldn't be considered because they don't have two neighbors.
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)

# Prompt for input
nums = input("Enter Values Separated by Spaces: ").split()

# Convert strings to integers
for i in range(len(nums)):
    nums[i] = int(nums[i])

# Initialize counter
count = 0

# Loop through elements (ignoring first and last)
for i in range(1, len(nums) - 1):
    if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        count += 1

# Print result
print(count)