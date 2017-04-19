#lambda is a way of writting functions in one line
#its the quick and dirty way of doing functions

#This is one way for writting a function

def multiply1(a,b,c):
	return a*b*c

print multiply1(2,3,4)

#This is another way for writting a function

def multiply2(a,b,c): return a*b*c 

print multiply2(4,5,6)


#Here is the lambda way
multiply3 = lambda a,b,c : a*b*c 

print multiply3(7,8,9)