#Create a class named Car that has the following attributes
    #Year - Year the car was manufactured
    #Make - Maker of the car
    #Speed - Current speed of the car
#Constructor
    #The constructor should accept the car's year and make. The speed should be set to zero.
#Methods
    #Accelerate - Adds the value to the cars current speed
    #Brake - Subtract the value from the cars current speed (don't go below zero)
#The first record in the 10.03 Cars.txt contains the year and the make. Instantiate one car object with this data.
#The rest of the 10.03 Cars.txt contains acceleration and brake information.
    #If the number is greater than zero, call the Accelerate method to add that amount of speed to the car.
    #If the number is less that zero. call the Brake method to subtract that amount of speed from the car.
#Print the change of speed value and the current speed value

# Car class definition
class Car:
    def __init__(self, year, make):
        """Constructor accepts year and make, speed set to 0."""
        self.year = year
        self.make = make
        self.speed = 0

    def accelerate(self, value):
        """Add value to current speed."""
        self.speed += value

    def brake(self, value):
        """Subtract value from speed, not below zero."""
        self.speed -= value
        if self.speed < 0:
            self.speed = 0


# Open the file
file = open("10.03 Cars.txt", "r")

# Read first line: car's year and make
first_line = file.readline()
parts = first_line.strip().split(',')
year = int(parts[0].strip())
make = parts[1].strip()

# Instantiate car object
car = Car(year, make)

print(f"Make: {car.make}")
print(f"Year: {car.year}\n")
print(f"{'Change':>6} {'Speed':>6}")

# Read the rest of the file and update speed
line = file.readline()
while line != "":
    change = int(line.strip())
    if change > 0:
        car.accelerate(change)
    elif change < 0:
        car.brake(-change)  # brake expects positive value

    print(f"{change:>6} {car.speed:>6}")
    line = file.readline()

file.close()