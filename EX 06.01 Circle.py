def diameter(x):
    d = x * 2
    return int(d)
from math import pi
def circumference(x):
    c = 2 * pi * x
    return int(c) 
def area(x):
    a = pi * x**2
    return int(a)

print(f'{"Radius":>15s}{"Diameter":>15s}{"Circumference":>15s}{"Area":>15s}')

radiusfile = open("06.01 Radius.txt", "r")
x = float(radiusfile.readline())


while x != "":
    print(f"{x:>15s}{"        "}{diameter(x):.5f}{"       "}{circumference(x):.5f}{"        "}{area(x):.5f}")
    
    x = float(radiusfile.readline())
radiusfile.close()