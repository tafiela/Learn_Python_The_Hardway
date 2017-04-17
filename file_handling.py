from sys import argv

script, filename = argv

prompt = '> '

print "Please enter your user_ID : "
user_ID = int(raw_input(prompt))

if user_ID == 200018856 :

	print "Are you looking to open filename : %s" %(filename)
	fOpen=raw_input(prompt)
	fOpen = fOpen.lower()
	if fOpen == "yes":
		Openfile = open(filename)
		print Openfile.read()
		print "\n\n"

		finished = raw_input("Are you done reading?")
		finished = finished.lower()

		if finished == "yes":
			print "great, good luck!"

else:
	print "sorry, no access for you"

