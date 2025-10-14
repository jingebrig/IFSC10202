# Prompt for inputs
from_value = float(input("Enter From Value: "))
from_unit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
to_unit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")

# Open and read the conversion file
filename = "09.04 Conversion.txt"
file = open(filename, 'r')

# Load into a 2D list
a = []
line = file.readline()
while line != "":
    parts = line.split()
    row = []
    for p in parts:
        row.append(p)
    a.append(row)
    line = file.readline()
file.close()

# Search for FromUnit in the first column
from_index = -1
for i in range(1, len(a)):
    if a[i][0] == from_unit:
        from_index = i
        break

if from_index == -1:
    print("FromUnit is not valid")
    quit()

# Search for ToUnit in the first row
to_index = -1
for j in range(1, len(a[0])):
    if a[0][j] == to_unit:
        to_index = j
        break

if to_index == -1:
    print("ToUnit is not valid")
    quit()

# Perform conversion
multiplier = float(a[from_index][to_index])
result = round(from_value * multiplier, 7)

# Display result
print(str(from_value) + " " + from_unit + " => " + str(result) + " " + to_unit)