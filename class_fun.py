#Class is like creating an object
#for example, playing world of warcraft, you have a Human class
#everytime you select a human, you are asked two inputs as a mandatory field (name and gender)

class Human():
	#in this example, every class you have to select a name and gender for it
	def __init__(self, name, gender): 
	# since every human (object) HAS a <name> and <gender>, object it self is <self>
		self.name = name
		self.gender = gender

	def speak_name(self): 
	#this is a method (not function) as it is part of a class and can only be called from the object
		print "My name is %s" %self.name
		

	def speak(self, text): #this is another method since its in a class
		print text

	def perform_math(self, math_function, *args): #again, self is the object, in the below case its Mo
		#we used *args because it allows us to input as many arguments as we want
		print "%s performed a math operation and the result was : %f" %(self.name, math_function(*args))

#below the object is Mo
Mo = Human("Mohammad", "Male") #offcourse, order matters, Mohammad will be assigned to name, Male to gender


def addition(a,b,c,d,e,f):
	#as you can see there is 6 arguments here and when we called it in the method (perform_math) we only used (*args)
	return a + b + c + d + e + f 


print Mo.name
print Mo.gender
print Mo.speak_name()
print Mo.speak("How are you?")
print Mo.perform_math(addition, 20, 30,40,50,60,70)