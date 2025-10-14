#You have a file that has text in it. Some of the lines are empty.
#Create a program that performs the following:
    #Opens the file 06.04 EmptyLinesInput.txt file for reading
    #Opens the file 06.04 EmptyLinesOutput.txt file for writing
    #Reads a line from the 06.04 EmptyLinesInput.txt file
        #If the line is not empty, write the line to 06.04 EmptyLinesOutput.txt
        #If the line is empty, do not write the line to 06.04 EmptyLinesOutput.txt
    #Prints the number of lines read and the number of lines written.

infilename = "06.04 EmptyLinesInput.txt"
outfilename = "06.04 EmptyLinesOutput.txt"

infile = open(infilename, 'r')
outfile = open(outfilename, 'w')

readcount = 0
writecount = 0

line = infile.readline()

while line != "":
    readcount += 1
    if line.strip() != "":
        outfile.write(line)
        writecount += 1
    line = infile.readline()

infile.close()
outfile.close()

print(f"{readcount} records read")
print(f"{writecount} records written")