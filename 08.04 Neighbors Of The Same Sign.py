#Prompt for a string containing integers separated by spaces.
#Load the values into a list.
#Find and print the first adjacent elements which have the same sign.
#If there is no such pair, leave the output blank.
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)

# Prompt for input
nums = input("Enter Values Separated by Spaces: ").split()

# Convert each string to integer
for i in range(len(nums)):
    nums[i] = int(nums[i])

# Find and print adjacent elements with the same sign
for i in range(1, len(nums)):
    if nums[i] * nums[i - 1] > 0:  # both positive or both negative
        print(nums[i - 1], nums[i])