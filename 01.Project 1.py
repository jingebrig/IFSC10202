# Write a program that prompts for a length of time in seconds.
# Note: Assume there are 365 days is a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds in a minute
# Calculate and print:
# Number of years in the length of time
# Number of days in the length of time
# Number of hours in the length of time
# Number of minutes in the length of time
# Number of seconds in the length of time
# Hint: Integer divide the length of time by the number of seconds in a year,  then subtract the amount of time in years from the length of time.  
# Repeat for days, hours, and minutes.

seconds_year = 31536000
seconds_day = 86400
seconds_hour = 3600
seconds_minute = 60

numberofseconds = int(input("Enter Length of Time in Seconds: "))  # Input statement with a prompt  

years = numberofseconds // seconds_year
numberofseconds = numberofseconds - (years * seconds_year)

days = numberofseconds // seconds_day
numberofseconds = numberofseconds - (days * seconds_day)

hours = numberofseconds // seconds_hour
numberofseconds = numberofseconds - (hours * seconds_hour)

minutes = numberofseconds // seconds_minute
numberofseconds = numberofseconds - (minutes * seconds_minute)

print("Years:",years)
print("Days:",days)
print("Hours:",hours)
print("Minutes:",minutes)
print("Seconds:",numberofseconds)