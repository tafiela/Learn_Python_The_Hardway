from sys import exit as bye


x=3
while True:
	if x <4 and x >0:
		print "x is %d" %x
		x-=1
	else:
		bye(0)
