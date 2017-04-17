from sys import argv 

script, filename = argv

txt = open(filename)

print "\n\n\n"
print "Here's your file : %s\n" %filename
print txt.read() # we issued a command on the txt file to read it
print "\n\n\n" #providing three lines of space

print "Type the filename again : "
file = raw_input('> ') #this will provide us with an input prompt and we are connecting it to the file variable 

txt_again = open(file) #we created a variable called txt_again and tied it to opening file

print txt_again.read() #we issued the command of read on the open file txt_again

print "are you done reading?"
done = raw_input('> ')

txt_again.close() #this is to close the file

if txt_again.closed: #this will confirm if the file is closed
	print "file is closed"



