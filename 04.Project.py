n = int(input("Enter Maximum Height: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()

for k in range(j, 1, -1):
    for l in range(k, 1, -1):
        print("*", end="")
    print()