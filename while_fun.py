from sys import argv	#this way it will enable me to add input to the script 
from sys import exit	#this will exit the program after completing the while statement

script, x = argv #when running it from shell you would type python while_fun.py 3 (3 is an example of a number)

x = int(x) # here we are making sure x is an int

def while_fun(x):

	teeth_cleaned = False # we are setting the variable to False
	while True:  #bascially infinate loop 
	#with the while loop it will continue repeating until something calls Exit(0) or a parameter has been met
		if x >4 :
			exit(0)


		elif x < 4 and teeth_cleaned:
			#bascially saying if x was less than 4 AND False, which is True AND False, which is FALSE
			print "\n\n\n\t ************ \n\n\n"
			print "This was a TRUE and False statement"
			print "Since the X was smaller than 4"
			print "X was %d in this case" %x
			print "And the teeth_cleaned was set to False"
			print "\n\n\n"
			x+=1

		elif x < 4 and not teeth_cleaned:
			print "\n\n\n\t ************ \n\n\n"
			print "This was a TRUE and True statement"
			print "Since the X was smaller than 4"
			print "X was %d in this case" %x
			print "And the teeth_cleaned was set to True since its Not(teeth_cleaned) which equals to Not (False) which is TRUE"
			print "\n\n\n"
			x+=1
			teeth_cleaned = True

		elif x==4 or teeth_cleaned:
			print "\n\n\n\t ************ \n\n\n"
			print "This was a TRUE OR False statement"
			print "Since the X was equal to 4"
			print "X was %d in this case" %x
			print "And the teeth_cleaned was set to False"
			print "\n\n\n"
			x+=1

		

		else:
			print "\n\n\t ***  Function completed  *** \n\n"
			exit(0)


while_fun(x)


