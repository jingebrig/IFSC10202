#Prompt for a string containing integers separated by spaces.
#Load the values into a list.
#Print the values that are odd.
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)

# Prompt for input
nums = input("Enter Values Separated by Spaces: ").split()

# Convert each element to integer
for i in range(len(nums)):
    nums[i] = int(nums[i])

# Print odd numbers
for i in range(len(nums)):
    if nums[i] % 2 == 1:
        print(nums[i])