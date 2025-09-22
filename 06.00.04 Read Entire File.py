demotextfile = open("06.00.00 DemoText.txt", "r") # Open a file for reading
x = demotextfile.read()                           # Read the entire contents of the file into a single string
print(x)                                          # Print the contents - Note the embedded linefeeds
demotextfile.close()                              # Close the file