from math import sqrt, atan, pi

# Point class
class Point:
    def __init__(self, Xvalue, Yvalue):
        self.x = Xvalue
        self.y = Yvalue

    # Format numbers like your example: minimal trailing zeros
    def ToString(self):
        return f"({self.x:.7g}, {self.y:.7g})"


# Distance between two points
def Distance(A, B):
    dx = B.x - A.x
    dy = B.y - A.y
    return sqrt(dx * dx + dy * dy)

# Midpoint between two points
def MidPoint(A, B):
    mid_x = (A.x + B.x) / 2
    mid_y = (A.y + B.y) / 2
    return Point(mid_x, mid_y)

# Angle in degrees
def XAngle(A, B):
    dx = B.x - A.x
    dy = B.y - A.y
    if dx == 0:
        return 90.0 if dy > 0 else -90.0
    slope = dy / dx
    return atan(slope) * 180 / pi


# Open the file
file = open("10.05 Points.txt", "r")

# Header
print(f"{'Point A':>15} {'Point B':>15} {'Distance':>15} {'Midpoint':>15} {'Angle':>15}")
print(f"{'-'*15} {'-'*15} {'-'*15} {'-'*15} {'-'*15}")

# Process each line
line = file.readline()
while line != "":
    values = line.strip().split(',')
    A = Point(float(values[0]), float(values[1]))
    B = Point(float(values[2]), float(values[3]))

    dist = Distance(A, B)
    mid = MidPoint(A, B)
    angle = XAngle(A, B)

    # Print row with custom formatting
    print(f"{A.ToString():>15} {B.ToString():>15} {dist:15.7f} {mid.ToString():>15} {angle:15.7f}")

    line = file.readline()

file.close()