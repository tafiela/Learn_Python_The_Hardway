#using the *args and **kwargs enables us to enter as many arguments as we need in a function
#one thing to note, depending on which argument we used first order matters!!!

#For example:

def test1(*args, **kwargs):
	for arg in args:
		print arg 

	for item in kwargs.items():
		print item 

#Now we have *args first and **kwargs second
#we need to put regular arhuments first and then keyword second as follow:

test1(1,2,3,4,5,x=5,y=7) #this will print with no issues as the 1,2,3,4,5 were taken as the *args arguments and the x=5,y=7 as the **kwargs
