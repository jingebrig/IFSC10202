class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname.strip()
        self.LastName = lastname.strip()
        self.TNumber = tnumber.strip()
        self.Grades = []

    def RunningAverage(self):
        total = 0
        count = 0
        for score in self.Grades:
            if score != "":
                total += float(score)
                count += 1
        if count == 0:
            return 0
        return total / count

    def TotalAverage(self):
        total = 0
        for score in self.Grades:
            if score != "":
                total += float(score)
        if len(self.Grades) == 0:
            return 0
        return total / len(self.Grades)

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(student)

    def find_student(self, tnumber):
        index = 0
        for s in self.Studentlist:
            if s.TNumber == tnumber.strip():
                return index
            index += 1
        return -1

    def add_student_from_file(self, filename):
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            self.add_student(parts[0], parts[1], parts[2])
        file.close()

    def add_scores_from_file(self, filename):
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            tnumber = parts[0]
            score = ""
            if len(parts) > 1:
                score = parts[1]
            index = self.find_student(tnumber)
            if index != -1:
                self.Studentlist[index].Grades.append(score)
        file.close()

    def print_student_list(self):
        print("       First         Last           ID      Running     Semester       Letter")
        print("        Name         Name       Number      Average      Average        Grade")
        print("------------ ------------ ------------ ------------ ------------ ------------")
        for s in self.Studentlist:
            print(f"{s.FirstName:>12}{s.LastName:>12}{s.TNumber:>12}"
                  f"{s.RunningAverage():>12.2f}{s.TotalAverage():>12.2f}{s.LetterGrade():>12}")


students = StudentList()
students.add_student_from_file("11.Project Students.txt")
students.add_scores_from_file("11.Project Scores.txt")
students.print_student_list()