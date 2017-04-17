print "You enter a dark room with two doors. Do you go through door #1 or door #2? "
door = raw_input('> ')

def bear1(x):
	return x+10


if door == "1":
	print "There's a giant bear here easting a cheese cake. What do you do? "
	print "\n1. Take the cake."
	print "2. Scream at the bear."

	bear= raw_input("> ")

	if bear == "1":
		print "The bears eats your ass off! Good Job!"
	elif bear == "2":
		print "The bear eats your legs off! Good Job!"
	else:
		print "Well, doing", bear1(int(bear)) ,  "is probably better. Bear runs away."
	#	print "Well, doing %s is better, the Bear runs away" %bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good Job!"
	else:
		print "The insanity rots yours eyes into a pool of much. Good Job!"

else:
	print "You stumble around and fall on a knife and die. Good Job!"

