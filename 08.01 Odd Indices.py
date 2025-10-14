#Prompt for a string containing integers separated by spaces.
#Load the values into a list
#Print the values with ane odd index number (a[1], a[3], a[5]...).
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)

# Prompt for input
nums = input("Enter Values Separated by Spaces: ").split()

# Convert string values to integers
for i in range(len(nums)):
    nums[i] = int(nums[i])

# Print values with odd indices
for i in range(len(nums)):
    if i % 2 == 1:
        print(nums[i])