#Create a class called Pet which has the following attributes:
    #Name - name of pet
    #Type - type of pet, such as "Cat", "Dog", etc
    #Age - age of pet
#The constructor for the Pet class should not have any arguments.
#Read the 10.01 Pets.txt file, create three pet objects, one for each line, and print the object attributes for the pets using the .format method
#Print the Name, Type, and Age attributes from each of the pet objects

class Pet:
    def __init__(self, name="", pet_type="", age=0):
        self.Name = name
        self.Type = pet_type
        self.Age = age

petfile = open("10.01 Pets.txt")
x = petfile.readline()
y = x.split(",")

pet1 = Pet(y[0].strip(), y[1].strip(), int(y[2].strip()))
x = petfile.readline()
y = x.split(",")

pet2 = Pet(y[0].strip(), y[1].strip(), int(y[2].strip()))
x = petfile.readline()
y = x.split(",")

pet3 = Pet(y[0].strip(), y[1].strip(), int(y[2].strip()))
x = petfile.readline()
y = x.split(",")

print("{:>10s}{:>10s}{:>10s}".format("Name", "Type", "Age"))
print("{:>10s}{:>10s}{:>10}".format(pet1.Name, pet1.Type, pet1.Age))
print("{:>10s}{:>10s}{:>10}".format(pet2.Name, pet2.Type, pet2.Age))
print("{:>10s}{:>10s}{:>10}".format(pet3.Name, pet3.Type, pet3.Age))