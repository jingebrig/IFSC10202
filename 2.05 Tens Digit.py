#Enter a number and print its tens digit.
#Be sure to use to F-Strings to create your output.
#Use only math for your solution; do not use any string functions.

num = int(input("Enter A Number: "))
tens = num // 10 % 10
print(f"Tens Digit: {tens}")