#Prompt for a string containing integers in ascending order separated by spaces.
#Load the values into a list.
#Swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.).
#Print the resulting list.
#If a list has an odd number of elements, leave the last element in place.
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)

# Prompt for input
nums = input("Enter Values Separated by Spaces: ").split()

# Convert strings to integers
for i in range(len(nums)):
    nums[i] = int(nums[i])

# Swap adjacent elements
for i in range(0, len(nums) - 1, 2):
    temp = nums[i]
    nums[i] = nums[i + 1]
    nums[i + 1] = temp

# Print the result
print("Swapped Values:", end=" ")
for i in range(len(nums)):
    print(nums[i], end=" ")
print()