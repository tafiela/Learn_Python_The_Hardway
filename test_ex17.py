from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Hi, you are about to merge the file contents from %s to %s" %(from_file, to_file)
print "if you would like to continue, hit RETURN"
print "otherwise, hit CTRL-C (^C)"

raw_input(">")

Ofile = open(from_file) #you can shorten your code by combining two lines of code on the same line with the ";"
ofile=Ofile.read()

print "the length of the from file %s is %d" %(from_file, len(ofile))
print "Lets confirm if the to file %r exists" %exists(to_file)

print "\nLets open the to file and update it with the from file content"
tfile = open(to_file, "a+")
tfile.write(ofile)

print "update complete"

tfile.close()
Ofile.close()