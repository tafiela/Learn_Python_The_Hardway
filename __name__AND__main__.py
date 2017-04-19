def main():
	print "First module Name: {}".format(__name__)



#bascially if we ran a module directly the __name__ will equal to __main__
#if we imported a code with import * the __name__ will equal the code imported
if __name__ == __main__:
	main()