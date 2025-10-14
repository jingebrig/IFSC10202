#You have a two files. You want to compare them line by line and print the differences.
#Create a program that performs the following:
    #Opens the file 06.05 CompareFileA.txt file for reading
    #Opens the file 06.05 CompareFileB.txt file for reading
    #Read a line from both files
    #If the line from both files is not the same, print the line number and the contents of both lines
    #Print the number of differences

fileAname = "06.05 CompareFileA.txt"
fileBname = "06.05 CompareFileB.txt"

fileA = open(fileAname, 'r')
fileB = open(fileBname, 'r')

lineA = fileA.readline()
lineB = fileB.readline()

line_number = 1
differences = 0

while lineA != "" or lineB != "":
    if lineA != lineB:
        print(f"Line: {line_number} - File A: {lineA.strip()}")
        print(f"Line: {line_number} - File B: {lineB.strip()}\n")
        differences += 1

    lineA = fileA.readline()
    lineB = fileB.readline()
    line_number += 1

fileA.close()
fileB.close()

print(f"{differences} differences")