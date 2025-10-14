#Prompt for a string containing integers separated by spaces.
#Load the values into a list.
#Determine the element in the list with the largest value.
#Print the value of the largest element and then the index number.
#If the largest element is not unique, print the index of the first instance.
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)

# Prompt for input
nums = input("Enter Values Separated by Spaces: ").split()

# Convert strings to integers
for i in range(len(nums)):
    nums[i] = int(nums[i])

# Initialize largest value and index
largest = nums[0]
largest_index = 0

# Loop through list to find largest value
for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        largest_index = i

# Print results
print("Largest Value:", largest)
print("Index of Largest Value:", largest_index)