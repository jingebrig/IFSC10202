x = float(input("Enter First Number: "))
op = (input("Enter Operator (+,-,*,/): "))
y = float(input("Enter Second Number: "))
if "+" in op:
    output = x + y
elif "-" in op:
    output = x - y
elif "*" in op:
    output = x * y
elif "/" in op:
    output = x / y
else:
    print("Invalid Operator")

print(x,op,y,"=",output)