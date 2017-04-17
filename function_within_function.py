import random 

def chances():
	i=random.randint(0,1)
	return i

def outcome():	
	chances()
	if chances() == 1:
		return 1
	else:
		return 0


outcome()
