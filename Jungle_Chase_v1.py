#from function_within_function import outcome
#from random import randint
from sys import argv
from sys import exit

def chances():
	i=random.randint(0,1)
	return i

def outcome():	
	chances()
	if chances() == 1:
		return 1
	else:
		return 0



def swim():
	print '''
	you now have two options, either swim fast to the land, which is noisy and you can risk the creature hearing you
	and catching you, or swim real slow but risk him seeing you and catching you from under.
	
	so what do you want to do.

	Swim fast or slow?
	'''

	swimming= raw_input('\t>>> ')

	if "fast" in swimming:
		print "\tYou made it, he was on the other side and cant climb this bank"
	elif "slow" in swimming:
		caught()
	else:
		"\tyou should have picked fast or slow"
		exit(0)



def in_water():
	print '''
	As soon as you jump in the water, you surfice to get your breath back,right at that time,
	you hear a bigger spalsh near you, but you cant see where the splash was!

	you have two options now, either Dive under the water and hope your breath can keep you under
	until the creature goes away, OR swim to the surface!

	which do you rather do,

	Swim or Dive?
	'''

	swim_or_dive=raw_input('\t>>> ')

	if "swim" in swim_or_dive:
		swim()

	elif "dive" in swim_or_dive:
		print '''
		You ran out of breath, you see something swiming real fast towards, Oh Shit, this thing
		was made to live in the water, it is Fast!
		'''
		caught()

def chances_result():
	if outcome() == 1:
		print "\n\n\tYou made it through the jump!!!"
		print "\tThank God!!!"
		in_water()

	else:
		print "\tYou didnt make it, it was too deep of a jump"
		print "\tSorry, may you RIP!"		




def climb_down():
	print '''\n\nyou grab the robe, buckle your self tight, and start going down
	You start seeing the water, damn its far down!
	All of a sudden, you feel a strong pull upwards!!!
	you see this huge figrue, standing on the edge and pulling you up!!!

	what do you want to do??
	Do you want to Jump and risk the chance or say screw it and go up and face that thing.
	So whats it going to be, Fight or jump?'''

	robe = raw_input ('\t>>> ')

	if "fight" in robe:
		caught()
	else:
		chances_result()


def caught():
	print "\n\n\tYou got caught, you had no chance with this creature!\n\n"
	exit(0)

def flight():
	print "\n\n\t All of a sudden, you come to the edge of a cliff!"
	print "\tyou cant see how deep the cliff is, but you can hear water falls under you"
	print "\tThe sound is loud, so its either a huge waterfall or a not soo deep cliff"
	print "\tbut its too dark!!"

	print "\n\t you find a robe already tied to a tree and running down the cliff, as if someone been here before"
	print "\n\tHURRY, the breating sound is getting closer!!!, HURRY UP!!!!"
	print "\n\n\tNo Time!  Do you want to JUMP or climb down the robe??? "

	jump_or_climb= raw_input('\t>>> ')

	if "jump" in jump_or_climb:
		chances_result()

	else:
		climb_down()




def story():
	print '''
	You are walking down a dark tree aisle, The moon is bright and whole, its just past midnight,
	its soo quite, you can hear the bugs and mosquito conspiring who wants to get you first!

	Mid way through the way, you start hearing dired leafs and old branches cracking behind you, deep in the woods,
	you brush it off and continue walking,

	The noises start getting louder and closer, you look back!

	Nothing!

	you cant see a thing,  everything goes quite for a short amount of time, then you hear the sounds again,
	this time its really close, its like almost 10 feet too close to comfort!

	you look back, there is something in the dark, you cant figure out if he/it is facing you or the otherside,
	then it starts moving towards in short burst and really eerie footings!

	What do you want to do??? 

	Fight, and stand your ground

	Or 

	flight, and dont take the risk, especially since you have no idea what it is!!!

	'''

	fight_or_flight = raw_input('\t>>> ')

	if "fight" in fight_or_flight or "stand" in fight_or_flight:
		caught()

	elif "flight" in fight_or_flight or "run" in fight_or_flight:
		print "\n\n\tGood choice!\n\n"
		print "\tRUN, RUN, RUN \n\n"
		print "\tYou can hear the creature breathing loud while chasing you, but he isnt as fast as you are!!!"
		flight()

	else:
		print "\tyou dont want to play or you dont understand English, its either fight or flight"
		exit(0)

story()

