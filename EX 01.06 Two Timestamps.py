#A timestamp consists of three numbers:
#number of hours
#number of minutes
#number of seconds
#Given two timestamps, calculate how many seconds are between them.
#Assume that the moment of the first timestamp occurred before the moment of the second timestamp.

#First Timestamp
#Enter Hours: 6
#Enter Minutes: 1
#Enter Seconds: 30
#Second Timestamp
#Enter Hours: 6
#Enter Minutes: 2
#Enter Seconds: 10
#40

print("First Timestamp")
h1 = int(input("Enter Hours: "))
h1s = h1 * 3600
m1 = int(input("Enter Minutes: "))
m1s = m1 * 60
s1 = int(input("Enter Seconds: "))
t1s = (h1s + m1s + s1)

print("Second Timestamp")
h2 = int(input("Enter Hours: "))
h2s = h2 * 3600
m2 = int(input("Enter Minutes: "))
m2s = m2 * 60
s2 = int(input("Enter Seconds: "))
t2s = (h2s + m2s + s2)

elapsed = t2s - t1s

if t2s < t1s :
    print("Second Timestamp must occur after First Timestamp")

elif t2s > t1s :
    print(elapsed)