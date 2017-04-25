#you can use unlimited arguments in a function by using the *args argument

#here is an example :

def test1(*args):
	for i in args:
		print i 


test1(1,2,3,4,"hello")


print "\n\nSecond Excercise:"

def test2(*args):
	for i in args:
		print i 

lst=[1,2,3,4,"Hello"]
test2(lst)

print "if we want it to print them separate, we can do the following :"
test2(*lst)