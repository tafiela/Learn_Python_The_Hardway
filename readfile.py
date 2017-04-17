from sys import argv 


#to open this script, from the command prompt type python scriptname.py filename
# like this :  python readfile.py textfile.txt


script, filename = argv

file = open(filename, 'r')

print file.read()
