#You have a file that has the stock prices for a week, one per line.
#Create a program that performs the following:
#Defines a function called "percentchange"
    #Accepts today stock price (floating point) and yesterdays stock price (floating point) as parameters
    #Calculates and percent change between yesterdays and todays stockprice
        #Percent Change is todays stock value - yesterdays stock value divided by yesterdays stock value time 100
    #Opens and reads the first line of 06.02 Stock.txt file
    #Prints headings and the first stock value (there is no percent change on the first day)
    #Reads the next line of input
    #Calculates and prints the stock value and the percent change from yesterday. Each column is 10 characters wide with a space between them.

def percentchange(today, yesterday):
    return ((today - yesterday) / yesterday) * 100

filename = "06.02 Stock.txt"

file = open(filename, 'r')

print("    Price     Change")

# Read the first line (first day's price)
line = file.readline()

if line != "":
    yesterday = float(line.strip())
    print(f"    {yesterday:<10.2f}")

# Read the remaining lines one by one
line = file.readline()
while line != "":
    today = float(line.strip())
    change = percentchange(today, yesterday)
    print(f"    {today:<10.2f}{change:10.2f}%")
    yesterday = today
    line = file.readline()

file.close()