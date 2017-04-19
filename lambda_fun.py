#lambda is a way of writting functions in one line
#its the quick and dirty way of doing functions

#This is one way for writting a function
def square(x):
	return x*x
print square(99)

#This is another way for writting a function
def square(x): return x*x
print square(10)

#Here is the lambda way
square = lambda x: x*x #lambda ALWAYS returns a values this is why we didnt explicitly say return
print square(3)
