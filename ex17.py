from sys import argv
from os.path import exists

#assigning three varibles as arguments for the script
script, from_file, to_file = argv

#just printing what we want to do
print "\nCopying from %s to %s\n " %(from_file,to_file)

#this is one way if opening the file and reading it we can do it in one line, can you do it? 
in_file = open(from_file)
indata = in_file.read()
#in_file = open(from_file)

print "\nThe input file is %d bytes long\n" %len(indata)

print "\nDoes the output file exist? %r" %exists(to_file)

print "\nReady, hit RETURN to continue, CTRL-C to abort."
raw_input('>')
print "\n"

out_file = open(to_file, "w")
out_file.write(indata)

print "\t***Alright, all done. ***\n\n"

out_file.close()
in_file.close()