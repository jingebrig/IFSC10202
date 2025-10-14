#Prompt for a month (an integer from 1 to 12) and a day in the month (an integer from 1 to 31) in a common year (not a leap year).
#Print the month and the day of the next day after it.
    #The first test corresponds to March 30 - next day is March 31
    #The second test corresponds to March 31 - next day is April 1
    #The third test corresponds to December 31 - next day is January 1

# Prompt the user for the month and day
month = int(input("Enter Month: "))
day = int(input("Enter Day: "))

# Determine the number of days in the given month (common year)
if month == 2:
    days_in_month = 28
elif month in (1, 3, 5, 7, 8, 10, 12):
    days_in_month = 31
else:
    days_in_month = 30

# Compute the next day
if day < days_in_month:
    day += 1
else:
    day = 1
    month += 1
    if month > 12:
        month = 1  # move to next year (January)

# Print the result
print(f"Next Day: {month}/{day}")