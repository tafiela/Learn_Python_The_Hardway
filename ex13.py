
from sys import argv

#when you want to run this script the first variable (something) will take the script name
#the first varibale will take the first argument you put with the script, 
#To run this you execute as follow:
# Python ex13.py First_arg Second_arg Third_arg
something, first, second, third = argv 
print "the script is called : ", something
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third varibale is: ", third 
