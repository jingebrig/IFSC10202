filename = "09.Project Distances.csv"
file = open(filename, "r")

table = []
line = file.readline()

while line != "":
    row = line.strip().split(",")
    table.append(row)
    line = file.readline()

file.close()

for i in range(len(table)):
    for j in range(len(table[i])):
        print(f"{table[i][j]:>10}", end=" ")
    print()

from_city = input("Enter From City: ")
to_city = input("Enter To City: ")

from_index = -1
for i in range(1, len(table)):
    if table[i][0].lower() == from_city.lower():
        from_index = i
        break

to_index = -1
for j in range(1, len(table[0])):
    if table[0][j].lower() == to_city.lower():
        to_index = j
        break

if from_index == -1:
    print("Invalid From City")
elif to_index == -1:
    print("Invalid To City")
else:
    distance = table[from_index][to_index]
    print(f"{from_city} to {to_city} - {distance} miles")