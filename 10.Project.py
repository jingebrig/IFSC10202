class Student:
    def __init__(self, firstname="", lastname="", tnumber="", scores=None):
        if scores is None:
            scores = []
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores

    def RunningAverage(self):
        total = 0
        count = 0
        for g in self.Grades:
            if g != "":
                total += float(g)
                count += 1
        return total / count if count > 0 else 0

    def TotalAverage(self):
        total = 0
        count = len(self.Grades)
        for g in self.Grades:
            if g != "":
                total += float(g)
        return total / count if count > 0 else 0

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


studentfile = open("10.Project Student Scores.txt")

x = studentfile.readline()
y = x.strip().split(",")
y = [item.strip() for item in y]
student1 = Student(y[0], y[1], y[2], y[3:])

x = studentfile.readline()
y = x.strip().split(",")
y = [item.strip() for item in y]
student2 = Student(y[0], y[1], y[2], y[3:])

x = studentfile.readline()
y = x.strip().split(",")
y = [item.strip() for item in y]
student3 = Student(y[0], y[1], y[2], y[3:])

print("{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}".format(
    "First", "Last", "ID", "Running", "Semester", "Letter"))
print("{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}".format(
    "Name", "Name", "Number", "Average", "Average", "Grade"))
print("{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}".format(
    "-"*12, "-"*12, "-"*12, "-"*12, "-"*12, "-"*12))

print("{:>12s}{:>12s}{:>12s}{:>12.2f}{:>12.2f}{:>12s}".format(
    student1.FirstName, student1.LastName, student1.TNumber,
    student1.RunningAverage(), student1.TotalAverage(), student1.LetterGrade()))

print("{:>12s}{:>12s}{:>12s}{:>12.2f}{:>12.2f}{:>12s}".format(
    student2.FirstName, student2.LastName, student2.TNumber,
    student2.RunningAverage(), student2.TotalAverage(), student2.LetterGrade()))

print("{:>12s}{:>12s}{:>12s}{:>12.2f}{:>12.2f}{:>12s}".format(
    student3.FirstName, student3.LastName, student3.TNumber,
    student3.RunningAverage(), student3.TotalAverage(), student3.LetterGrade()))