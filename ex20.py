from sys import argv

script, input_file = argv

#we are creating a function that will read an already open file
def print_all(f):
	print f.read()

#once a file has been read, the pointer will be set to the last charcter in the file, we use seek(0) to set the pointer to the start again
def rewind(f):
	f.seek(0) # we are bascially saying set the pointer all the way to charcter position 0
#	f.seek(10) #we are bascially saying start reading from charcter 10


#here we are creating a function that takes two variables, once we take the variables we are:
# 1- using the first variable as is
# 2- then on the same line (by using the ",") we are adding the readline, readline requires the file to be opened first
def print_a_line(line_count, f):
	print line_count, f.readline(), # since readline() scans each byte until it gets to "\n" and returns the EOL "\n" 
									#if you wont want it to return the "\n" to your output add a ","


#we are opening the file, by default open(), opens the file in read mode
current_file = open(input_file)

print"\n\nFirst let's print the whole file: \n"
print_all(current_file)

print "\n\nNow let's rewind, kind of like a tape.\n"
rewind(current_file)

print "Lets print three lines: "

# here we are saying use the integer "1" are the varibale or argument in the print_a_line function, 
# and the current_file.readline() will read the first in the current file since the pointer is set to 0 (when we did rewind)
current_line = 1
print_a_line(current_line, current_file)


# here we are saying use the current line varibale (above) and add "1" to it, making it 2, then use the 2 as the new argument in the print_a_line function
# since the pointer has read the first line by readline (from above) the pointer is now on the second line 
# when passing it to the function it will print the number 2 then the second line in file 
#current_line = current_line + 1
current_line+= 1 #this is an alternative way of writting current_line = current_line + 1
print_a_line(current_line, current_file)


# here we are saying use the current line varibale (above) and add "1" to it, making it 3, then use the 3 as the new argument in the print_a_line function
# since the pointer has read the second line by readline (from above) the pointer is now on the third line 
# when passing it to the function it will print the number 3 then the second line in file 
#current_line = current_line +1
current_line+=1 # this is an alternative way of writting current_line = current_line + 1
print_a_line(current_line, current_file)

