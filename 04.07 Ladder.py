n=int(input("Enter N:"))
if n>9:
    print("N must be <=9")    
else:
    for i in range(1, n+1):
        for k in range(1, i+1):
            print(k, end="")
        print()