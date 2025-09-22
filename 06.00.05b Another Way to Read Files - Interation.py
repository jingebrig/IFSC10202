#You can also use automate interation to read through the file. 
#The for loop automatically reads each line in the file and checks for end of file.

# Open a file for reading
demotextfile = open("06.00.00 DemoText.txt")
# Read through the file
for x in demotextfile:
# Print the contents - Note the imbedded linefeeds
	print(x)
# Close the file
demotextfile.close()