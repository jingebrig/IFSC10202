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
	outputfile.write(line)
	inputrecordcount += 1
	outputrecordcount += 1
	line = inputfile.readline()

if line== str("**Insert Merge File Here**"):
	outputfile.write(line)
	mergerecordcount += 1
	outputrecordcount += 1
	line = mergefile.readline()

inputfile.close()
mergefile.close()
outputfile.close()

print("{} input records written".format(inputrecordcount))
print("{} merge records written".format(mergerecordcount))
print("{} output records written".format(outputrecordcount))


