#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
#Given an integer N > 1, print PRIME if it is a prime number and print COMPOSITE otherwise.
#Hint: Loop from 2 to ((half of N) + 1) and check to see if any number evenly divides into N.

N = int(input("Enter N: "))

# Use 0 as "prime" and 1 as "composite" indicator
composite = 0

# Loop from 2 to half of N (inclusive)
for i in range(2, (N // 2) + 1):
    if N % i == 0:
        composite = 1  # found a divisor

# Print result based on composite value
if composite == 0:
    print("PRIME")
else:
    print("COMPOSITE")