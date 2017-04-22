
#Classes allow us to to reuse a set of code over and over
#in this example:

#Great video on this :  https://www.youtube.com/watch?v=ZDa-Z5JzLYM


'''
We have a company with employees in it, we will need a class
so that everytime a new employee joins the company
we are able to add them properly and in standard manner
for example:

	Every employee has first name, last name, pay and email 

everytime you want to register a new employee you will have to enter those
as base minimum

Every Employee will have its own instance in memory

if you run run the below code [CODE_1]  block you will see that each print from empl1 and empl2

are in a different memory locations

'''

# print '''

# *************** CODE_1  *****************

# '''

# class Employee:
# 	pass

# empl_1 = Employee() #this will be a different instance in memory from empl_2
# empl_2 = Employee() #this will be a different instance in memory from empl_1

# print "\n\n"
# print empl_1
# print empl_2
# print "\n\n"


print '''

*************** CODE_2  *****************

'''

class Employee:

	def __init__ (self, first, last,pay): #initalize or constructor
		self.firstname = first # we are bascially saying first as a varible is self.firstname
		self.lastname =last
		self.employee_pay=pay
		self.email = first+"."+last+"@company.com"

	def fullname(self):
		return self.firstname+ " " +self.lastname


empl_1 = Employee("John", "Doe", 10000) #this will be a different instance in memory from empl_2
empl_2 = Employee("Eick", "James", 3000) #this will be a different instance in memory from empl_1

print "Employee Email is : ", empl_1.email
print "Employee Email is : ", empl_1.email


print "\n\nDifferent ways on calling methods in a class ...."
print empl_1.firstname + " " + empl_1.lastname
print empl_1.fullname() #calling the fullname method on empl_1
print Employee.fullname(empl_2)


Ejames = Employee.fullname(empl_2)
print "%s makes good money, he makes %d" %(Ejames, empl_2.employee_pay)

# empl_1.first="John"
# empl_1.last="Doe"
# empl_1.pay=10000
# empl_1.email="John.Doe@company.com"

# empl_2.first="Eick"
# empl_2.last="James"
# empl_2.pay=30000
# empl_2.email="Eick.James@company.com"
 
# print empl_1.first
# print empl_1.last










