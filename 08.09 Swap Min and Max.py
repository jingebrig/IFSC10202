#Prompt for a string containing integers separated by spaces.
#Load the values into a list.
#Swap the minimum and maximum elements in the list.
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)

# Prompt for input
nums = input("Enter Values Separated by Spaces: ").split()

# Convert to integers
for i in range(len(nums)):
    nums[i] = int(nums[i])

# Initialize min and max values and their indices
min_val = nums[0]
max_val = nums[0]
min_index = 0
max_index = 0

# Find min and max
for i in range(1, len(nums)):
    if nums[i] < min_val:
        min_val = nums[i]
        min_index = i
    if nums[i] > max_val:
        max_val = nums[i]
        max_index = i

# Swap min and max
temp = nums[min_index]
nums[min_index] = nums[max_index]
nums[max_index] = temp

# Print result
print("Swapped Minimum and Maximum:", end=" ")
for i in range(len(nums)):
    print(nums[i], end=" ")
print()