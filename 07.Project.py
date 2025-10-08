def ParseDegreeString(ddmmss):
    deg_symbol = chr(176)
    deg_index = ddmmss.find(deg_symbol)
    min_index = ddmmss.find("'")
    sec_index = ddmmss.find('"')

    degrees = float(ddmmss[:deg_index])
    minutes = float(ddmmss[deg_index + 1:min_index])
    seconds = float(ddmmss[min_index + 1:sec_index])

    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    return degrees + (minutes / 60) + (seconds / 3600)

inputfilename = "07.Project Angles Input.txt"
outputfilename = "07.Project Angles Output.txt"
recordcount = 0

angleinputfile = open(inputfilename,'r')
angleoutputfile = open(outputfilename, 'w')

line = angleinputfile.readline()

for line in angleinputfile:
    recordcount += 1
    ddmmss = line.strip()
    degrees, minutes, seconds = ParseDegreeString(ddmmss)
    decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
    angleoutputfile.write(f"{decimal_degrees}\n")

print(f"{recordcount} records processed")