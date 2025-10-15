# Open the distances file
filename = "09.Project Distances.csv"
file = open(filename, "r")

# Create the 2D list (table)
table = []
line = file.readline()

while line != "":
    # Split the line by commas and strip newlines
    row = line.strip().split(",")
    table.append(row)
    line = file.readline()

file.close()

# ---- Print the 2D list neatly ----
for i in range(len(table)):
    for j in range(len(table[i])):
        print(f"{table[i][j]:>10}", end=" ")
    print()

# ---- Prompt for cities ----
from_city = input("Enter From City: ")
to_city = input("Enter To City: ")

# ---- Search for From City in first column ----
from_index = -1
for i in range(1, len(table)):       # start at 1 (skip header)
    if table[i][0].lower() == from_city.lower():
        from_index = i
        break

# ---- Search for To City in first row ----
to_index = -1
for j in range(1, len(table[0])):    # start at 1 (skip header)
    if table[0][j].lower() == to_city.lower():
        to_index = j
        break

# ---- Output ----
if from_index == -1:
    print("Invalid From City")
elif to_index == -1:
    print("Invalid To City")
else:
    distance = table[from_index][to_index]
    print(f"{from_city} to {to_city} - {distance} miles")