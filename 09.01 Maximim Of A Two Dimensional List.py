#Given two integers representing the rows and columns (m×n), and subsequent m rows of n elements
    #Input the number of rows and columns in the list
    #Input the array
    #Print the array.
    #Find the index position of the maximum element and print two numbers representing the index (i×j) or the row number and the column number. 
        #If there exist multiple such elements in different rows, print the one with smaller row number. 
        # If there multiple such elements occur on the same row, output the smallest column number.

# Prompt for number of rows and columns
size_input = input("Enter the number of rows and columns: ").split()
m = int(size_input[0])
n = int(size_input[1])

# Initialize 2D list
array = []

# Input array data
for i in range(m):
    line = input("Enter a line of data: ").split()
    row = []
    for j in range(n):
        row.append(int(line[j]))
    array.append(row)

# Print the array
for i in range(m):
    for j in range(n):
        print(array[i][j], end=" ")
    print()

# Initialize tracking variables
max_value = array[0][0]
max_row = 0
max_col = 0

# Find the maximum element and its position
for i in range(m):
    for j in range(n):
        if array[i][j] > max_value:
            max_value = array[i][j]
            max_row = i
            max_col = j

# Print result
print(f"The maximum value {max_value} occurred in row {max_row} column {max_col}")