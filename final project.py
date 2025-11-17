# Define a class to represent an individual employee
class Employee:
    # Constructor initializes employee attributes
    def __init__(self, empnum, firstname, lastname, address, city, state, zip):
        self.EmployeeNumber = int(empnum)          # Store employee number as an integer
        self.FirstName = firstname.strip()          # Remove extra spaces from first name
        self.LastName = lastname.strip()            # Remove extra spaces from last name
        self.Address = address.strip()              # Remove extra spaces from address
        self.City = city.strip()                    # Remove extra spaces from city
        self.State = state.strip().upper()          # Convert state to uppercase
        self.Zip = zip.strip()                      # Remove extra spaces from zip code


# Define a class to manage a list of Employee objects and related file operations
class EmployeeList:
    def __init__(self, filename):
        self.filename = filename                    # Store the filename for reading/writing employee data
        self.EmployeeList = []                      # Initialize an empty list to hold Employee objects

    # Reads employee data from the text file and loads it into EmployeeList
    def ReadEmployeeFile(self):
        file = open(self.filename, "r")             # Open file in read mode
        for line in file:                           # Loop through each line in the file
            line = line.strip()                     # Remove newline and extra spaces
            if line == "":                          # Skip empty lines
                continue
            parts = line.split(",")                 # Split line into parts (comma-separated values)
            # Create an Employee object using the split data
            emp = Employee(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6])
            self.EmployeeList.append(emp)           # Add the Employee to the list
        file.close()                                # Close the file after reading

    # Writes all employee data back to the text file
    def WriteEmployeeFile(self):
        file = open(self.filename, "w")             # Open file in write mode (overwrites existing data)
        for e in self.EmployeeList:                 # Loop through all Employee objects
            # Format each employee's data as a comma-separated line
            line = f"{e.EmployeeNumber},{e.FirstName},{e.LastName},{e.Address},{e.City},{e.State},{e.Zip}\n"
            file.write(line)                        # Write the formatted line to the file
        file.close()                                # Close the file after writing

    # Displays all employees in a formatted table
    def DisplayEmployeeList(self):
        print()
        print("Employee        First           Last            Address         City            State           Zip")
        print("Number          Name            Name")
        print("--------------- --------------- --------------- --------------- --------------- --------------- ---------------")
        for e in self.EmployeeList:
            # Print each employee’s info in aligned columns
            print(f"{str(e.EmployeeNumber):<16}{e.FirstName:<16}{e.LastName:<16}{e.Address:<16}{e.City:<16}{e.State:<16}{e.Zip:<16}")
        print()

    # Searches for an employee by employee number and returns the index in the list
    def FindEmployee(self, empnum):
        index = 0
        for e in self.EmployeeList:
            if e.EmployeeNumber == empnum:          # If found, return the index
                return index
            index += 1
        return -1                                   # Return -1 if not found

    # Returns the next available employee number (last number + 1)
    def NextEmployeeNumber(self):
        if len(self.EmployeeList) == 0:             # If list is empty, start with 1
            return 1
        last = self.EmployeeList[-1].EmployeeNumber # Get the last employee’s number
        return last + 1                             # Increment by 1 for the next employee

    # Adds a new employee to the list
    def AddEmployee(self, firstname, lastname, address, city, state, zip):
        empnum = self.NextEmployeeNumber()          # Generate a new employee number
        emp = Employee(empnum, firstname, lastname, address, city, state, zip)  # Create a new Employee object
        self.EmployeeList.append(emp)               # Add employee to list
        print("Employee Added\n")

    # Deletes an employee from the list by employee number
    def DeleteEmployee(self, empnum):
        index = self.FindEmployee(empnum)           # Find index of employee
        if index == -1:
            print("Employee Not Found\n")           # Print error if not found
        else:
            del self.EmployeeList[index]            # Remove employee from list
            print("Employee Deleted\n")

    # Updates an existing employee's information
    def UpdateEmployee(self, empnum, firstname, lastname, address, city, state, zip):
        index = self.FindEmployee(empnum)           # Find employee index
        if index == -1:
            print("Employee Not Found\n")
        else:
            # Update each attribute with new values
            self.EmployeeList[index].FirstName = firstname
            self.EmployeeList[index].LastName = lastname
            self.EmployeeList[index].Address = address
            self.EmployeeList[index].City = city
            self.EmployeeList[index].State = state
            self.EmployeeList[index].Zip = zip

    # Retrieves and returns an employee object by number
    def ReadEmployee(self, empnum):
        index = self.FindEmployee(empnum)
        if index == -1:
            return None                             # Return None if not found
        return self.EmployeeList[index]             # Otherwise, return the Employee object


# === MAIN PROGRAM ===
elist = EmployeeList("Final Project Employees.txt") # Create EmployeeList object for the given file
elist.ReadEmployeeFile()                            # Load employees from file

# Main loop for user interaction
while True:
    # Display menu options
    print("(A)dd a New Employee")
    print("(D)elete an Existing Employee")
    print("(C)hange an Existing Employee")
    print("(P)rint All Employees")
    print("(S)ave Changes to File")
    print("(Q)uit\n")

    choice = input("Enter Selection: ").upper()     # Get user input and convert to uppercase
    print()

    # === Add New Employee ===
    if choice == "A":
        firstname = input("Enter First Name: ")
        lastname = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ").upper()
        zip = input("Enter Zip: ")
        elist.AddEmployee(firstname, lastname, address, city, state, zip)

    # === Delete Employee ===
    elif choice == "D":
        empnum = int(input("Enter Employee Number: "))
        elist.DeleteEmployee(empnum)

    # === Change (Update) Employee ===
    elif choice == "C":
        empnum = int(input("Enter Employee Number: "))
        emp = elist.ReadEmployee(empnum)            # Find the employee
        if emp is None:
            print("Employee Not Found\n")
        else:
            # Submenu for changing individual fields
            while True:
                print("(F)irst Name")
                print("(L)Last Name")
                print("(A)ddress")
                print("(C)ity")
                print("(S)tate")
                print("(Z)ip")
                print("(B)ack to Main Menu\n")

                opt = input("Enter Selection: ").upper()
                print()
                if opt == "F":
                    emp.FirstName = input("Enter First Name: ")
                elif opt == "L":
                    emp.LastName = input("Enter Last Name: ")
                elif opt == "A":
                    emp.Address = input("Enter Address: ")
                elif opt == "C":
                    emp.City = input("Enter City: ")
                elif opt == "S":
                    emp.State = input("Enter State: ").upper()
                elif opt == "Z":
                    emp.Zip = input("Enter Zip: ")
                elif opt == "B":
                    break                           # Return to main menu

    # === Print All Employees ===
    elif choice == "P":
        elist.DisplayEmployeeList()

    # === Save Changes to File ===
    elif choice == "S":
        elist.WriteEmployeeFile()
        print("Changes Saved\n")

    # === Quit Program ===
    elif choice == "Q":
        print("Good-bye")
        break

    # === Invalid Selection ===
    else:
        print("Invalid Selection\n")
