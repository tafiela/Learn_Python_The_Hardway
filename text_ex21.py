
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

def mathstuff(a,b):
	return add(a,b)
	return subtract(a,b)
	return multiply(a,b)
	return divide(a,b)


print "\nlets do some math with just functions!"

mathstuff(10,2)


