from sys import exit 

def gold_room():
	print "This room is full of gold. How much do you take? "

	next = raw_input('> ')

	if "0" in next or "1" in next:
		how_much = int(next)

	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0) #This will exit the program cleanly 

	else:
		dead("You greedy bastard")

def bear_room():#If you selected left on the start() this functins gets called
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear? "
	bear_moved = False #we are simply assigning the variable bear_moved to False 

	while True: #bascially infinate loop until stopped
		next = raw_input('> ') #we take the user input and put it to the varibale next 

		if next == "take honey": #if the next variable equals to take honey then:
			dead ('The bear looks at you then slaps your face off.') #trigger the dead(why) function & EXITS 

		elif next == "taunt bear" and not bear_moved: #if the next variable equals to taunt bear and not(bear_moved) = True then print the below
		#elif next == "taunt bear":	
			print "The bear has moved from the door. You can go through it now. " #print this
			bear_moved = True 
		
		elif next == "taunt bear" and bear_moved: 
		# When you taunted the bear the first time, it changed the bear_moved to TRUE
		#if you taunted the bear again the statment will become TRUE (for taunt_bear) AND TRUE (since now bear_moved = True)
			dead("The bear gets pissed off and chews your leg off.")#then trigger the function dead(why)
		
		elif next == "open door" and bear_moved: #if next equals open door and bear_moved still false, trigger the gold_room() function
			gold_room()
		
		else:
			print "i got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input('> ')

	if "flee" in next:
		start()
	
	elif "head" in next:
		dead("Well that was tasty!")
	
	else:
		cthulhu_room()

def dead(why):
	print why, "Good Job!"
	exit(0)


def start(): #We start from this function
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take? "

	next = raw_input('> ') #your input is either left or right


	if next == "left": #if your input is let
		bear_room() #then this function will get triggered bear_room()
	
	elif next== "right": #if your input is right
		cthulhu_room() #this this function will get triggered
	
	else: #if your input is neither left or right then : 
		dead("You stumble around the room until you starve.") #this function will get triggered dead(why)

start()
