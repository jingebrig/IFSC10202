n = int(input("Enter N: "))

for step in range(1, n+1):
    for k in range(1, step+1):
        print(k, end="")
    print()