#Create a class called Pet which has the following attributes:
    #Name - name of pet
    #Type - type of pet, such as "Cat", "Dog", etc
    #Age - age of pet
#The constructor for the Pet class should not have any arguments.
#Read the 10.01 Pets.txt file, create three pet objects, one for each line, and print the object attributes for the pets using the .format method
#Print the Name, Type, and Age attributes from each of the pet objects

filename = "10.01 Pets.txt"
file = open(filename, "r")

table = []
line = file.readline()

while line != "":
    row = line.strip().split(",")
    table.append(row)
    line = file.readline()

file.close()

print(f"{table[i][j]:>10}", end=" ")

class pet ():
    def __init__(self, name, type, age):
        self.Name = name
        self.Type = type
        self.Age = age