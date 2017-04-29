#Class is a way of writting code for objects

class my_class():
	def method1(self):
		print "my_class method1"
	def method2(self, sometext):
		print "my_class method2: " + sometext

def main():
	c=my_class()
	c.method1()
	c.method2("This is some text")

if __name__ == "__main__": #if the __name__ == "__main__" : meaning if the code is local (not imported)
	main() #run main()