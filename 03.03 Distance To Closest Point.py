#Given the coordinates of the three points A, B, and C on a line, print a distance from the point A to closest point to it.
#Hint: Determine the distance from A to B by subtracting B from A, then determine the distance from A to C by subtracting C from A. Determine the smallest distance.

# Prompt the user for the coordinates
A = int(input("Enter Point A: "))
B = int(input("Enter Point B: "))
C = int(input("Enter Point C: "))

# Calculate distances from A to B and A to C
dist_AB = abs(A - B)
dist_AC = abs(A - C)

# Determine and print the smallest distance
if dist_AB < dist_AC:
    print(dist_AB)
elif dist_AC < dist_AB:
    print(dist_AC)
else:
    print(dist_AB)