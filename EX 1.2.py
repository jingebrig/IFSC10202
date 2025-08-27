# Start the Python interpreter and use it as a calculator.
# 1. How many seconds are there in 42 minutes 42 seconds?
# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
#    mile in minutes and seconds)? What is your average speed in miles per hour?

mins = 42
secs = 42

# 1 minutes = 60 seconds
# x minutes = x * 60 seconds
total_secs = mins * 60 + secs

print("There are", total_secs, "seconds in 42 minutes 42 seconds.")


# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile

# 1.61 kms = 1 miles
# 1 km = 1 / 1.61 miles
# x km = x / 1.61 miles

print ("There are", (10 / 1.61), "miles in 10 kilometers.")


#3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
#   mile in minutes and seconds)? What is your average speed in miles per hour?

# average speed = total distance / total time
# 1.61 kms = 1 miles
# 1 km = 1 / 1.61 miles
# x km = x / 1.61 miles

# 60 minutes = 1 hour
# 1 minutes = 1 / 60 hour
# x minutes = x / 60 hour
# 
# 3600 seconds = 1 hour
# 1 seconds = 1 / 3600 hours
# y seconds = y / 3600 hours
# 

total_time = 42 / 60.0 + 42 / 3600.0    # in hours
total_dist = 10 / 1.61                  # in miles

avg_speed = total_dist / total_time

print("Average speed:",(avg_speed), "miles per hour")