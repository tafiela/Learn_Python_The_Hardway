#Create a mapping of state to abbreviation

states = {
	'Oregon':'OR',
	'Florida': 'FL',
	'California':'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# Create a basic set of states and some cities in them

cities = {
	'CA':'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities

cities['NY']="New York"
cities['KY']="louisville"
cities['OR']="Portland"

#print out some cities 

print '_'*10
print"\n"
print "NY state has: ", cities['NY']
print "OR state has: ",cities['OR']

#print some states
print '_'*10
print"\n"
print "Michigan's abbreviation is: ",states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by using states then cities
print '_'*10
print"\n"
print "Michigan has: ", cities[states["Michigan"]]
print "Florida has: ", cities[states["Florida"]]

#print every state abbreviation
print '_'*10
print"\n"
for state, abbrev in states.items(): #key, value in states.items()
	print "%s is abbreviaed %s" %(state,abbrev)


#print every city in state
print '_'*10
print"\n"	
for i in cities:
	print cities[i] + "is in %s" %(i)

#OR

print '_'*10
print"\n"	

for abbrev, city in cities.items():
	print "%s has the city %s" %(abbrev, city)


#Now do both at the same time
print '_'*10
print"\n"	
for state,abbrev in states.items(): #always remember this is key, value in states
	print "%s state is abbreviated %s and has city %s" %(state, 
		abbrev, cities[abbrev])


print '_'*10
print"\n"	

#safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state: #putting the None makes the state False, otherwise we could put our custom msg
	print "Sorry, No Texas"



# test = states.get("Florida", None)
# print test


#get a city with a default value
city = cities.get("TX", 'Does Not Exist')
print 'The city for the state "TX" is : %s' %city

















