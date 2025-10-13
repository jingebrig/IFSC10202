#Write a program that prompts for the lenght of a race in kilometers, the prompts for the number of minutes and number of seconds needed to run the race.
#Display the average speed in Miles per Hour
#Hint: Use the int() function to convert your input to an integer.
#Hint: There are 1.61 kilometers in a mile.
#Enter Length of Race in Kilometers: 10
#Enter Minutes: 61
#Enter Seconds: 33
#6.054765352614396

# Prompt for race length in kilometers
kilometers = int(input("Enter the length of the race in kilometers: "))

# Prompt for time in minutes and seconds
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# Convert total time to hours
total_minutes = minutes + (seconds / 60)
total_hours = total_minutes / 60

# Convert kilometers to miles
miles = kilometers / 1.61

# Calculate speed in miles per hour
mph = miles / total_hours

# Display the result
print(mph)