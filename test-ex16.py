

from sys import argv

script, filename = argv

print "Hi, you are looking to delete the content of %s" %filename
print "If you feel you reached here by mistake, please hit CTRL+C (^C)"
print "Otherwise, hit RETURN to continue"

raw_input('>')

print "\nFile is currently being opened\n"
file = open(filename, "w+")

print "\nWe are currently deleting the content of the file ..."
file.truncate() #Note : Since you already opened the file with "w" it will overwrite the file regardless

print "\n\t***Congratulations, you removed all the content of the file.***\n"

print "Now lets add some text to file"

file=open(filename, "w+")

line1 = raw_input("Line1:  ")
line2 = raw_input("Line2:  ")
line3 = raw_input("Line3:  ")


file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)

print "lets close the file ..."
file.close()
