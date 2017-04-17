def test(stuff):
	hopes = stuff * 70
	interest = stuff * 10
	likes = stuff *30
	return likes,hopes, interest 

stuff = 1000
snaps,hellos , grasss = test(stuff) #order matters,  you need to align the varibale alignment for the function test(stuff) with the return of 
									#the function  so in this case snaps = likes, hellos = hopes, grasss = interest

print '''\nprinting it in the same order as :

		1- interest, likes, hopes = test(stuff)
		2- using this function :
			
			def test(stuff):
				hopes = stuff * 70
				interest = stuff * 10
				likes = stuff *30
				return interest,likes,hopes
'''


'''print """\n\nWe'd have %d interest ( stuff * 10),

%d likes (stuff * 30) ,   and

%d hopes (stuff * 70)\n\n\n""" %(likes, hopes,hello)'''



print """\n\nWe'd have %d ,

%d   ,   and

%d \n\n\n""" %(snaps,hellos,grasss) 
