# r = radius
# d = distance

from math import pi
from math import sin
from math import cos
from math import acos

print("Great Circle Calculator")

r = float(input("Enter Radius of Sphere: "))

x1 = float(input("Starting Point - Enter Latitude: "))
x1rads = x1 * pi / 180

y1 = float(input("Starting Point - Enter Longitude: "))
y1rads = y1 * pi / 180

x2 = float(input("End Point - Enter Latitude: "))
x2rads = x2 * pi / 180

y2 = float(input("End Point - Enter Longitude: "))
y2rads = y2 * pi / 180

d = r * acos(sin(x1rads) * sin(x2rads) + cos(x1rads) * cos(x2rads) * cos(y1rads - y2rads))

print("The Great Circle Distance is: ", round(d,2))