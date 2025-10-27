

# Step 1 - Define the class object "Point"
class Point:
# Step 2 - Define the initializer and any default values
    def __init__(self, Xvalue, Yvalue):
# Step 3 - Define the object attributes
        self.x = Xvalue
        self.y = Yvalue
# Step 4 - Define the methods for the object
# ToString returns a nicely formated string to represent the data point
    def ToString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"