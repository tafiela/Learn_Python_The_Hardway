stuff = {"Name":"John", "age":10, "gender": "Male"} #this is a dictionary 

print stuff["Name"]
print stuff["age"]
print "So your name is %s, you are only %d year old %s?" %(stuff["Name"],stuff["age"],stuff["gender"])


print "\n\nLets add some stuff to this dict\n\n"

stuff["city"] = "New York"

print stuff #dict does not order its output 

for i in stuff:
	print i +" is",stuff[i] #since we can not concatanate int with str using the
							# "+" sign we wull use the "," to add the stuff[i]



print "\n\nLets add more stuff to this dict\n\n"

stuff["born"] = "Portland"
stuff["Smoker"]="Yes"

print stuff

print "\n\nLets remove (or delete) some stuff\n\n"

del stuff["Name"]
del stuff["age"]

print stuff