inputfilename = "06.Project Input File.txt"
mergefilename = "06.Project Merge File.txt"
outputfilename = "06.Project Output File.txt"
inputrecordcount = 0
mergerecordcount = 0
outputrecordcount = 0

inputfile = open(inputfilename,'r')
outputfile = open(outputfilename, 'w')

line = inputfile.readline()
while line != "":
	outputfile.write(line)
    inputrecordcount += 1
    outputrecordcount += 1
	line = inputfile.readline()

if line== "**Insert Merge File Here**":
	mergefile = open(mergefilename, 'r')
	y = mergefile.readline()
	print(y)

inputfile.close()