#A school decided to replace the desks in three classrooms. Each desk seats two students.
#Given the number of students in each class, determine the smallest possible number of desks that can be purchased.
#The program should:
#Read three integers: the number of students in each of the three classerooms A, B and C respectively.
#Use floor division to find the number of desk that has two students and use modulus to find the number of desks that have one student.
#Add the number of desks needed for each classroom and print the total.

#Example
#Classroom A has 20 students and thus needs 10 desks.
#Classroom B has 21 students, so they can get by with no fewer than 11 desks.
#Classroom C has 22 and also needs 11 desks
#32 desks in total (10 + 11 + 11)
#Enter Classroom A: 20
#Enter Classroom B: 21
#Enter Classroom C: 20
#31

a = int(input("Enter Classroom A: "))
b = int(input("Enter Classroom B: "))
c = int(input("Enter Classroom C: "))

desks_a = (a // 2) + (a % 2)
desks_b = (b // 2) + (b % 2)
desks_c = (c // 2) + (c % 2)

total_desks = desks_a + desks_b + desks_c

print(total_desks)