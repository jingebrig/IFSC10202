from math import pi
def diameter():
    d = x * 2
    return d
def circumference():
    2 * pi * x
def area():
    pi * x^2

radiusfile = open("06.01 Radius.txt", "r")
x = radiusfile.readline()

while x != "":
    recordcount = 0
    print(x)
    x = radiusfile.readline()
radiusfile.close()