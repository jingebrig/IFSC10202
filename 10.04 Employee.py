#Create a class named Employee that has the following attributes:
    #FirstName
    #LastName
    #IDNumber
    #HoursWorked
    #Wage
#Create an initializer that accepts the FirstName, LastName, IDNumber, HoursWorked, and Wage and assigns them to the appropriate attribute.
#The Employee class should have method called WeeklyPay, which calculates the weekly pay.
    #Weekly pay is defined as 1 times the wage for hours 0-40, and 1.5 times wage for hours greater than 40
#As you read each line from Payroll.txt, you will create one Employee object. You can reuse this object as you read the next employee.
#Print the FirstName, LastName, IDNumber, HoursWorked, HourlyWage, and WeeklyPay for each employee

# Employee class definition
class Employee:
    def __init__(self, first_name, last_name, id_number, hours_worked, wage):
        """Initialize employee attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.hours_worked = hours_worked
        self.wage = wage

    def weekly_pay(self):
        """Calculate weekly pay with overtime."""
        if self.hours_worked <= 40:
            pay = self.hours_worked * self.wage
        else:
            overtime_hours = self.hours_worked - 40
            pay = (40 * self.wage) + (overtime_hours * self.wage * 1.5)
        return pay


# Open the payroll file
file = open("10.04 Payroll.txt", "r")

# Print table header
print(f"{'First':>6} {'Last':>6} {'ID':>8} {'Hours':>7} {'Hourly':>8} {'Weekly':>8}")
print(f"{'Name':>6} {'Name':>6} {'Number':>8} {'Worked':>7} {'Wage':>8} {'Pay':>8}")

# Read each line and process employee
line = file.readline()
while line != "":
    parts = line.strip().split(',')
    first_name = parts[0].strip()
    last_name = parts[1].strip()
    id_number = int(parts[2].strip())
    hours_worked = float(parts[3].strip())
    wage = float(parts[4].strip())

    # Create Employee object
    employee = Employee(first_name, last_name, id_number, hours_worked, wage)

    # Print employee info
    print(f"{employee.first_name:>6} {employee.last_name:>6} {employee.id_number:>8} "
          f"{employee.hours_worked:7.2f} {employee.wage:8.2f} {employee.weekly_pay():8.2f}")

    line = file.readline()

file.close()