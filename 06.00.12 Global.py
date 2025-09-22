def myFunction():
	a = "A is a local variable"
	return a
	
b = myFunction()
print(a)         #change to print(b), a is only a variable in the function