#kwargs is an acronym for keywords arguments as a default 
#this enables us to enter keywords in as our arguments .i.e x=3, y=7

#for Example:

def test1(x=3,y=5): #if no value was entered for the x and y, use those as default values
	print x+y



def test2(**kwargs): #when using *kwargs it deals with the arguments as dicitonary 
	for item in kwargs.items(): #since its using it as a dictionary,  we need to use the for item in argument.items() to loop through
		print item




test1()# here we didnt assign any value for the x or y so it used the default
test1(2,5) #here we explicitly told the function to use the 2 and 5 as values for x,y
test1(x=10, y=20)


test2(x=10, y=20) #with the **kwargs you need to put the varibales with their definition 
''' The output would be :

('y', 20)
('x', 10)

'''