from sys import argv

script, filename = argv

#we are creating a text print showing what this script is looking to do
print "We're going to earse %s" %filename
print "if you dont want us to earse it, hit CTRL-C (^C)."
print "if you want us to continue, hit RETURN"

#here we are simply asking the user for an input, any input technically would work in this excersize 
raw_input('>')


print "Opening the file ... \n\n"
target = open(filename, 'w+') #we are opening a file with write & read privillages 


print "We're currently truncating the file, GoodBye!!!\n\n "
target.truncate() #we are removing all the content from the file here

print "Now we are going to input some data on this empty file : "
print "\n\n"

line1= raw_input('line1:  ')
line2=raw_input('line2:  ')
line3= raw_input('line3:  ')

print "\n\nNow we can update our file with the new lines ... \n\n"


target.write(line1) # we are writting the content of line1 to the file
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "file is updated\n"
#once all is complete we are closing the file, to do clean code, close the file always
target.close()
