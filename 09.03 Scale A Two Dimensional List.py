#Create a function called print_list(a), where a is a two dimensional list. The function should print the list row by row, with one space between each element
#Create a function called scale_list(a, s) that multiplies every value in the list by the scale factor, where
    #a is a two dimensional list
    #s is the scale factor
#Read the values in the file 09.03 NumbersList.txt into a two dimensional array
#Print the list by calling print_list(a).
#Prompt for a scale factor.
#Multiply every value in the list by the scale factor using a function called scaled_list(a, s).
#Print the scaled list by calling print_list(a).

def print_list(a):
    # Print the list row by row
    for r in range(len(a)):
        for c in range(len(a[r])):
            print(a[r][c], end=" ")
        print()


def scale_list(a, s):
    # Multiply every value in the list by the scale factor
    for r in range(len(a)):
        for c in range(len(a[r])):
            a[r][c] = a[r][c] * s


# Read file into a 2D list
filename = "09.03 NumbersList.txt"
file = open(filename, 'r')

a = []
line = file.readline()
while line != "":
    values = line.split()
    row = []
    for v in values:
        row.append(int(v))
    a.append(row)
    line = file.readline()
file.close()

# Print original list
print_list(a)

# Prompt for scale factor
s = int(input("Enter scale value: "))

# Scale the list
scale_list(a, s)

# Print scaled list
print_list(a)