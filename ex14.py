from sys import argv

script, user_name = argv

prompt = '#'

print "\n\n\n"
print "Hi %s, my name is %s\n" %(user_name,script)
print "I'd like to ask you a few questions.\n\n"
print "Do you like me %s?\n" %user_name
like = raw_input(prompt)

print "Where do you live %s?" %user_name
lives=raw_input(prompt)

print "\nWhat kind of computer do you have?"
computer=raw_input(prompt)

print """

Alright, do you said %s about liking me.
you live in %s, No idea where that is, and you have %s computer.Cool""" %(like, lives, computer)

print "\n\n\n\n"
