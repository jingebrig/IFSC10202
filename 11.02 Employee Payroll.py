#Create a class named Employee that has the following attributes:
    #FirstName
    #LastName
    #IDNumber
    #HoursWorked
    #Wage
#Create an initializer that accepts the FirstName, LastName, IDNumber, and Wage and assigns them to the appropriate attribute. Set HoursWorked to 0.
#Create a method called WeeklyPay, which calculates the weekly pay. Weekly pay is defined as 1 times the wage for hours 0-40, and 1.5 times wage for hours greater than 40
#In your main program, create the following function:
    #find_employee - which has the Employee list and the EmployeeID as the arguments. This function searches the list and looks 
    # for a match on the EmployeeID. The function returns the index of the employee. 
    # If the item is not found a -1 is returned. See the find_ball function in 11.01 - Creating a List of Objects Using Instantiation
#Read the 11.02 Employees.txt file and create a list of employee objects
#Read the 11.02 Hours.txt file, update the hour worked for the appropriate employee
#Print the results

# Employee class definition
class Employee:
    def __init__(self, first_name, last_name, id_number, wage):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.wage = wage
        self.hours_worked = 0

    # Calculate weekly pay
    def weekly_pay(self):
        if self.hours_worked <= 40:
            return self.hours_worked * self.wage
        else:
            overtime_hours = self.hours_worked - 40
            return 40 * self.wage + overtime_hours * self.wage * 1.5


# Function to find employee by ID
def find_employee(employee_list, employee_id):
    index = 0
    while index < len(employee_list):
        if employee_list[index].id_number == employee_id:
            return index
        index += 1
    return -1


# ----------------------
# Read employees
# ----------------------
file = open("11.02 Employees.txt", "r")
employee_list = []

line = file.readline()
while line != "":
    parts = line.strip().split(',')
    first_name = parts[0].strip()
    last_name = parts[1].strip()
    id_number = int(parts[2].strip())
    wage = float(parts[3].strip())
    employee = Employee(first_name, last_name, id_number, wage)
    employee_list.append(employee)
    line = file.readline()
file.close()


# ----------------------
# Update hours worked
# ----------------------
file = open("11.02 Hours.txt", "r")

line = file.readline()
while line != "":
    parts = line.strip().split(',')
    emp_id = int(parts[0].strip())
    hours = float(parts[1].strip())
    index = find_employee(employee_list, emp_id)
    if index != -1:
        employee_list[index].hours_worked = hours
    line = file.readline()
file.close()


# ----------------------
# Print employee payroll
# ----------------------
print(f"{'First':>6} {'Last':>6} {'ID':>8} {'Hours':>7} {'Hourly':>7} {'Weekly':>7}")
print(f"{'Name':>6} {'Name':>6} {'Number':>8} {'Worked':>7} {'Wage':>7} {'Pay':>7}")

index = 0
while index < len(employee_list):
    emp = employee_list[index]
    print(f"{emp.first_name:>6} {emp.last_name:>6} {emp.id_number:>8} {emp.hours_worked:7.2f} "
          f"{emp.wage:7.2f} {emp.weekly_pay():7.2f}")
    index += 1