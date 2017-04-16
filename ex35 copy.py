

from sys import exit 

def gold_room():
	print "This room is full of gold. How much do you take? "

	next = raw_input('> ')

	if "0" in next or "1" in next:
		how_much = int(next)

	else:
		dead("Man, learn to type a number.")

	if how_much < 50 :
		print "Nice, You're not greedy, you win!!"
		exit(0)

	else:
		dead("You greedy bastard!")

def bear_room(): #if you selected left you will trigger this function
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False #bear_moved has been assigned to the boolean of False

	while True: #this is bascially an infinate loop until stopped, 

		next=raw_input('> ') #takes user input and assigns it to the variable called next

		if next == "take honey": #1
			dead("The bear looks at you and then slaps your face off.") #if you select take honey you will trigger the dead(why) function

		#elif next == "taunt bear" and not bear_moved: #2 #bascially saying if you entered "taunt bear" and TRUE = (Not(bear_moved=False)) , True & True = True
		#	print "The bear has moved from the door. You can go through it now."
		#	bear_moved = True #now we have updated the bear_moved from False to True 

		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")

		elif next == "open door" and bear_moved:
			gold_room()

		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go inside."
	print "Do you flee for your life or eat your head?"

	next = raw_input('> ')

	if "flee" in next:
		start()

	elif "head" in next:
		dead("Well that was a tasty!")

	else:
		cthulhu_room()


def dead(why):
	print why, "Good job!"
	exit(0)

def start(): #first thing that is being executed
	print "You are in dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input('> ')

	if next == "left":
		bear_room() #if you selected left on the input you will trigger bear_room() function

	elif next == "right":
		cthulhu_room() #if you selected right on the input you will trigger cthulhu_room() function

	else:
		dead("You stumble around the room until you starve.")

start() #starts the script 
