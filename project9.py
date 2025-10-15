# This program looks up the distance between two cities using data from a CSV file.

# Step 1: Open the file that contains the city distances
filename = "09.Project Distances.csv"
file = open(filename, "r")

# Step 2: Read the file and make a table (list of lists)
table = []              # this will store all rows
line = file.readline()  # read the first line

# Keep reading lines until there are no more
while line != "":
    # Remove the newline at the end and split by commas
    row = line.strip().split(",")
    
    # Add this row to the table
    table.append(row)

    # Read the next line
    line = file.readline()

# Step 3: Close the file when done reading
file.close()

# Step 4: Print the table so we can see what it looks like
print("Here is the distance table:\n")
for i in range(len(table)):             # go through each row
    for j in range(len(table[i])):      # go through each item in the row
        print(f"{table[i][j]:>10}", end=" ")  # print each item spaced nicely
    print()  # move to the next line

# Step 5: Ask the user for the cities
from_city = input("\nEnter From City: ")
to_city = input("Enter To City: ")

# Step 6: Find the 'from' city in the first column
from_index = -1
for i in range(1, len(table)):  # start at 1 to skip the header row
    if table[i][0].lower() == from_city.lower():
        from_index = i
        break  # stop looking once we find it

# Step 7: Find the 'to' city in the first row
to_index = -1
for j in range(1, len(table[0])):  # start at 1 to skip the header column
    if table[0][j].lower() == to_city.lower():
        to_index = j
        break

# Step 8: Show the result
if from_index == -1:
    print("Sorry, that 'From City' was not found.")
elif to_index == -1:
    print("Sorry, that 'To City' was not found.")
else:
    # Look up the distance from the table
    distance = table[from_index][to_index]
    print(f"\nThe distance from {from_city} to {to_city} is {distance} miles.")