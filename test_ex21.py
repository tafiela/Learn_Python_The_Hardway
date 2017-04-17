
def add(a,b):
	print "ADDING %d and %d" %(a,b)
	return a+b #returning a value that could be assigned to a variable, unlike print it it vanishes after its been called

def subtract(a,b):
	print "SUBTRACTING %d - %d" %(a,b)
	return a-b

def multiply(a,b):
	print "MULTIPLING %d * %d" %(a,b)
	return a*b

def divide(a,b):
	print "DIVIDING %d / %d " %(a,b)
	return a/b





a=int(raw_input("What number you like a to be?"))
b = int(raw_input("What number would you like b to be?"))


addition = add(a,b)
subtraction = subtract(a,b)
multipication=multiply  (a,b)
division = divide (a,b)



print "\nlets do some math with just functions!"


def mathstuff(a,b):
	print addition, subtraction,multipication, division


mathstuff(a,b)



