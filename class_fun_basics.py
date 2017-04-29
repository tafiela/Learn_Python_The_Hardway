class Student(object):
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname 
		self.studentID = fname[:3] + lname[-3:] + "MED"


	def __str__ (self): #python looks at this firsts when wanting to print 
						#the class string

		return "This is %s %s bio : ..... "	%(self.firstname, self.lastname)
		
	def __eq__(self, other): #this bascially compares two classes 
		#Now if you created two instances with the same firstname and last it will return True
		return self.firstname == other.firstname and self.lastname == other.lastname
		#Otherwise, it will return False unless you copy the same instance

	def Hello(self):
		print "Hello" + self.firstname


