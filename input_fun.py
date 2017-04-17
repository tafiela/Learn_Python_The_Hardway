from sys import argv

script, user = argv

prompt = '>>>'

print " hi %s, i am your %s program, here to help" %(user, script)
print "would you like to play a game %s" %user
game=raw_input(prompt) #this will allow you to input and captures it under the game variable
game=game.lower() #taking the input and making it lower


if game == 'yes' or game == 'y':
	print "Excellent, you sound like fun already %s" %user
	print "How old are you?"
	age=int(raw_input(prompt))
	print "where do you live %s?" %user
	live = raw_input(prompt)

	print """

	Awesome, so to be safe, your name is %s.
	you live in %s, and you are %d years old, sweet! nice to meet you! \n\n """ %(user,live,age)
else:

	print "that sucks, we would have had fun %s" %user