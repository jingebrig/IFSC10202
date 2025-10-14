#Given a month - an integer from 1 (January) to 12 (December), print the number of days in the month.
#Assume that it is a non-leap year.

# Prompt the user for the month number
month = int(input("Enter month number (1-12): "))

# Determine the number of days
if month == 2:
    print("28")
elif month in (1, 3, 5, 7, 8, 10, 12):
    print("31")
else:
    print("30")