#Create a function called print_list(a), where a is a two dimensional list. The function should print the list row by row, with one space between each element
#Create a function called swap_columns(a, i, j) that will swap the columns i and j in list a, where
    #a is a two dimensional list
    #i and j are the numbers of columns to be swapped
#Read the values in the file *09.02 NumbersList.txt into an two dimensional list.
#Print the list by calling print_list(a).
#Prompt for the column numbers in the list to swap by calling swap_columns(a, i, j)
#Print the list with the swapped columns by calling print_list(a)

def print_list(a):
    #Prints a 2D list row by row, with spaces between elements.
    for row in a:
        for val in row:
            print(val, end=" ")
        print()

def swap_columns(a, i, j):
    #Swaps columns i and j in a 2D list.
    for row in a:
        temp = row[i]
        row[i] = row[j]
        row[j] = temp

# Read file and build 2D list
filename = "09.02 NumbersList.txt"
file = open(filename, 'r')

a = []
line = file.readline()
while line != "":
    values = line.split()
    row = []
    for val in values:
        row.append(int(val))
    a.append(row)
    line = file.readline()
file.close()

# Print original list
print_list(a)

# Prompt user for column numbers to swap
cols = input("Enter the columns to swap: ").split()
i = int(cols[0])
j = int(cols[1])

# Swap columns
swap_columns(a, i, j)

# Print updated list
print_list(a)