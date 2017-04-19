#lambda is a way of writting functions in one line
#its the quick and dirty way of doing functions

#This is one way for writting a function
def convert_list_to_int(iterable):
	return map(int,iterable) #we are mapping each iterable to an integer 

print convert_list_to_int(["123", "456", "789"])


#This is another way for writting a function

def convert_list_to_int1(iterable): return map(int, iterable) #we are mapping each iterable to an integer 

print convert_list_to_int1(["11", "34","55"])



#Here is the lambda way
convert_list_to_int3 = lambda iterable: map(int, iterable)

print convert_list_to_int3(["1232", "343", "343444"])
