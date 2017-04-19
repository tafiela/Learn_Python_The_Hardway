

#while True:
#	numer = float(raw_input("Enter a numberator>> "))
#	denom = float(raw_input("Enter a denominator>> "))
#	print "The fraction ratio is %f" %(numer/denom)




while True:
	try: #incase an error happens in the below block of code 

		numerator = float(raw_input("Enter a numerator >> "))
		denominator = float(raw_input("Enter a denominator >> "))
		print "The fraction ratio is %f"  %(numerator/denominator)
			
	except: #handle it with this exception
				
		print "An Error has happened!"
