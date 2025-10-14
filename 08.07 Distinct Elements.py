#Prompt for a string containing integers in ascending order separated by spaces.
#Load the values into a list.
#Print the number of distinct elements in the list.
#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)

# Prompt for input
nums = input("Enter Values Separated by Spaces: ").split()

# Convert strings to integers
for i in range(len(nums)):
    nums[i] = int(nums[i])

# Start counting distinct elements
count = 1  # at least one distinct element if list not empty

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        count += 1

print("Number of Distinct Elements:", count)