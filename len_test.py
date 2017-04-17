from sys import argv

script, from_file = argv
	
f= open(from_file)
ff= f.read()

d = len(ff)

print d