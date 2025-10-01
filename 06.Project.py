inputfilename = "06.Project Input File.txt"
mergefilename = "06.Project Merge File.txt"
outputfilename = "06.Project Output File.txt"
inputrecordcount = 0
mergerecordcount = 0
outputrecordcount = 0

inputfile = open(inputfilename,'r')
mergefile = open(mergefilename,'r')
outputfile = open(outputfilename, 'w')

line = inputfile.readline()

while line != "":
	if line == "**Insert Merge File Here**\n":
		line = mergefile.readline()
		while line != "":
			outputfile.write(line)
			mergerecordcount += 1
			outputrecordcount += 1
			line = mergefile.readline()
		outputfile.write("\n")
		line = inputfile.readline()
	else:
		outputfile.write(line)
		inputrecordcount += 1
		outputrecordcount += 1
		line = inputfile.readline()
inputfile.close()
mergefile.close()
outputfile.close()

print("{} input file records".format(inputrecordcount))
print("{} merge file records".format(mergerecordcount))
print("{} output file records".format(outputrecordcount))