class Employee:
    def __init__(self, employeenumber, firstname, lastname, address, city, state, zip):
        self.EmployeeNumber = int(employeenumber)
        self.FirstName = firstname.strip()
        self.LastName = lastname.strip()
        self.Address = address.strip()
        self.City = city.strip()
        self.State = state.strip().upper()
        self.Zip = int(zip)

class EmployeeList:
    def __init__(self):
        #self.FileName = filename
        self.EmployeeList = []

    def DisplayEmployeeList(self):
        print("Employee Number | First | Last | Address | City | State | Zip")
        for e in self.EmployeeList:
            print(e.EmployeeNumber, e.FirstName, e.LastName, e.Address, e.City, e.State, e.Zip)

    def ReadEmployeeFile(self, filename):
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) >= 7:
                emp = Employee(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6])
                self.EmployeeList.append(emp)
        file.close()

if __name__ == "__main__":
    el = EmployeeList()
    el.ReadEmployeeFile("Final Project Employees.txt")
    el.DisplayEmployeeList()