#lambda is a way of writting functions in one line
#its the quick and dirty way of doing functions

#This is one way for writting a function
def sumRGB(r,g,b):
	return r+g+b
print sumRGB(2,3,4)

#This is another way for writting a function
def sumRGB(r,g,b): return r+g+b
print sumRGB(10, 22, 33)

#Here is the lambda way
sumRGB = lambda r,g,b: r+g+b #lambda ALWAYS returns a values this is why we didnt explicitly say return
print sumRGB(1,2,3)


