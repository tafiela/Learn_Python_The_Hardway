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

print "\nlets do some math with just functions!"

age = add(20,30)
height = subtract(78,4)
weight = multiply(90,2)
iq=divide(100,2)


#print " this is without assigning it to a varibale : \n"

#add(20,30)
#subtract(78,4)
#multiply(90,2)
#divide(100,2)


print "\nAge: %d, Height: %d, weight: %d, IQ: %d" %(age,height,weight,iq)

#A Puzzle for the extra credit, type it in anyway

print "\nhere is a puzzle."

what = add(age,subtract(height, multiply(weight, divide(iq,2))))

print "\nThats becoms : ", what, "can you do it by hand?\n"