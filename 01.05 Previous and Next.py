#Write a program that prompts for an integer number and prints its previous and next numbers.
#Display the results exactly as shown below. There shouldn't be a space before the period.
#Remember that you can convert the numbers to strings using the function 'str'.

#Enter Number: 179
#The next number for the number 179 is 180.
#The previous number for the number 179 is 178.

num = int(input("Enter Number: "))
print("The next number for the number ",(num) ,"is ", (num + 1))
print("The previous number for the number ",(num) ,"is ", (num - 1))