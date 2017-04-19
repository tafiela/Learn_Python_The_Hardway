#And operator
# it checks whether the two parameters occured or it favors the False 

print "And Operator"
print ''' 
	   True and True 
	   False and False
       True and False'''


True and True 
False and False
True and False

print "\n\n\n"
print "del Operator" 
# Deletes an itme in a list or dictionary 
print "\n"
print '''x=['a','b','c']
         del x[1]'''

x=['a','b','c']
del x[1] #this will remove the index 1, which is the "b"



print "\n\n\n"
print "from Operator"
#This tests a parameter within a range
print "\n"
print "This is specifically useful when importing modules or when importing functions from a specifc module"

print "from sys import argv"
print "from sys import exit"

print "instead of importing the entire module, you import a function in it"


print "\n\n\n"

print "While Operator"
print "\n"
print "While an instance is met, continue executing .... "
print "While True ..... This is an infinate loop until its being existed or a condition is met"


print ''' while True:
				i = 3
				if i<5:
					print "i is %d which is less than 5" %i
					i+=1
				else:
					print "No else"
'''

from sys import exit #to break the while loop
i = 3
while True:
	
	if i<5:
		print "i is %d which is less than 5" %i
		i+=1
	else:
		print "No else"
		exit(0)


print "\n\n\n"
print "As Operator"

print "\n"

print "As operator is generally used as an assignment operator"
print "for Example : import random as something"
print "from sys import exit as stop"


print "\n\n\n"
print "Global Operator"

print "\n"

print "If you created a variable in one function you can declare it global to be used in other functions by global "
print '''globvar = 0

		def set_globvar_to_one():
    		global globvar    # Needed to modify global copy of globvar
    		globvar = 1

		def print_globvar():
    		print(globvar)     # No need for global declaration to read value of globvar

		set_globvar_to_one()
		print_globvar()       # Prints 1
		'''

print "\n\n\n"
print "Assert Statement"

print "\n"

print "Assert is an automatic error Detection in your program "
print "If assert condition was set to True, the program coninues with no issues"
print "if assert condition was set to false, an AssertionError will showup"

print '''

		age = 34
		# assert (condition), Assertion Error msg
		assert age >= 0, "How is your age negative?\n" 
		print "Your age is %d" %age

		'''

age=34
assert age>=0, "How is your age negative?\n" #bascially you are saying if age is over 0, continue
												#If it was False, raise
print "Your age is %d" %age


print "\n\n\n"
print "Try Statement" #Good video on this : https://www.youtube.com/watch?v=0r8N0XwQSkk

print "\n"

print '''  Try statmenet (Try block ) is an Error handling method
		   in the Try Block you put all the code that might through an Error
		   and then you tell it how to handle the exception (or Error)

		   '''

print '''\n\n Here is an Example :\n\n

		while True:
			numerator = float(raw_input("Enter a numerator >> "))
			denominator = float(raw_input("Enter a denominator >> "))
			print "The fraction ratio is %f"  %(numerator/denominator)

	'''

print "\n\n\t When running this script it will crash on Zero denominator with this error :  ZeroDivisionError"
print "\n\n To handle this Error we can use the TRY Block, by bascially putting all the code that"
print "could give us an error in the TRY block as follow : "

print '''\n\n Here is an Example :\n\n

		while True:
			try:

				numerator = float(raw_input("Enter a numerator >> "))
				denominator = float(raw_input("Enter a denominator >> "))
				print "The fraction ratio is %f"  %(numerator/denominator)
			
			except ZeroDivisionError as TheZeroError:
				
				Print "An Error has happened!"
				print "The ERROR was :  ", TheZeroError
	'''