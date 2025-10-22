filename = "Exam Two Properties.csv"
file = open(filename, "r")

properties = []
line = file.readline()

while line != "":
    row = line.strip().split(",")
    row [4] = float(row[4])
    properties.append(row)
    line = file.readline()

file.close()

print(f'{"Address":<35}{"City":<15}{"State":<10}{"Zip Code":<10}{"Price":<15}')

for prop in properties:
    print(f"{prop[0]:<35}{prop[1]:<15}{prop[2]:<10}{prop[3]:<10}${prop[4]:<14,.2f}")