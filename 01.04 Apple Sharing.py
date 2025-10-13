#N students take K apples from a basket and distribute them among each other evenly. The remaining (the undivisible) apples remains in the basket.
#Prompt for the number of students and apples.
#How many apples will each single student get?
#How many apples will remain in the basket?

#Number of Students: 6
#Number of Apples: 50
#8
#2

n=int(input("Number of Students: "))
k=int(input("Number of Apples: "))
applesperstudent = k // n
remainingapples = k % n
print("Apples per student:", applesperstudent)
print(remainingapples)