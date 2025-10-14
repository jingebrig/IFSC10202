#You have a file that has temperatures in Fahrenheit, one per line.
#Create a program that performs the following:
    #Defines a function called "FahrToCel"
        #Accepts a Fahrenheit Temperature (floating point) as a parameter
        #Calculates the temperature in Celsius - C = (F - 32) * 5 / 9
    #Opens the file 06.03 FTemps.txt file for reading
    #Opens the file 06.03 CTemps.txt file for writing
    #Reads a line from the 06.03 FTemps.txt file
    #Calculates the Celsius temperature.
    #Writes the Celsius temperature to the 06.03 CTemps.txt file. The Celsius values should be 5 characters wide with 1 decimal digit.
    #Prints the number of records processed

def FahrToCel(fahr):
    return (fahr - 32) * 5 / 9

infilename = "06.03 FTemps.txt"
outfilename = "06.03 CTemps.txt"

infile = open(infilename, 'r')
outfile = open(outfilename, 'w')

count = 0
line = infile.readline()

while line != "":
    fahr = float(line.strip())
    celsius = FahrToCel(fahr)
    outfile.write(f"{celsius:5.1f}\n")
    count += 1
    line = infile.readline()

infile.close()
outfile.close()

print(f"{count} records written")