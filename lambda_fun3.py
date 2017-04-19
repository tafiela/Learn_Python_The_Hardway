#lambda is a way of writting functions in one line
#its the quick and dirty way of doing functions

#This is one way for writting a function
def remove_duplicates(iterable):
	return set(iterable) #SET(x) removes duplicates and returns one iterable of the duplicate

print remove_duplicates("Mohammmmmmmad")
print remove_duplicates("we" "eeee" "we""ee")


#This is another way for writting a function

def remove_duplicates1(iterable): return set(iterable)

print remove_duplicates1("Rooooot")
print remove_duplicates1([1,2,2,1,1,1,3])


#Here is the lambda way
remove_duplicates3 = lambda iterable: set(iterable)
print remove_duplicates3("Helllloooooooo")
print remove_duplicates3([1,2,3,2,2,3,6,7])
