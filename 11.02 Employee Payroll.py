Create a class named Employee that has the following attributes:
FirstName
LastName
IDNumber
HoursWorked
Wage
Create an initializer that accepts the FirstName, LastName, IDNumber, and Wage and assigns them to the appropriate attribute. Set HoursWorked to 0.
Create a method called WeeklyPay, which calculates the weekly pay. Weekly pay is defined as 1 times the wage for hours 0-40, and 1.5 times wage for hours greater than 40
In your main program, create the following function:
find_employee - which has the Employee list and the EmployeeID as the arguments. This function searches the list and looks for a match on the EmployeeID. The function returns the index of the employee. If the item is not found a -1 is returned. See the find_ball function in 11.01 - Creating a List of Objects Using Instantiation
Read the 11.02 Employees.txt file and create a list of employee objects
Read the 11.02 Hours.txt file, update the hour worked for the appropriate employee
Print the results