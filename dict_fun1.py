#Write a python script to add a key to a dictionary

example = {1:2 , "House":"Mouse", "12345":"6789", 200:-300}
dic1={1:1, 2:2, 3:3}
dic2 = {"a":"a", "b":"b" , "c":"c"}
dic3 = {"House":"Home", "Car":"wheels", "boat":"ship"}
dicx= {"a":1,"b":2,"c":3, "d":4}



example["SomeKey"]="Value"

print example


print "\n" * 5
print "-"*10 
print "\n"*3

#printing the key and value in dictionary, dict has the .items() which will return the key and value in tuple

dic10={1:1, 2:2, 3:3}


for k,v in dic10.items():
	print k,v 

#Write a python script to concatenate the following dicitionaries to create a new one

print "\n" * 5
print "-"*10 
print "\n"*3

dic1={1:1, 2:2, 3:3}
dic2 = {"a":"a", "b":"b" , "c":"c"}
dic3 = {"House":"Home", "Car":"wheels", "boat":"ship"}

def merge_dict(a,b):
	c=a.copy() #we copied the dict a
	c.update(b) #we updated dict b with dict a
	return c 

c= merge_dict(dic1,dic2) #here we assigned the return of merge_dict(a,b) function to c
d=merge_dict(c,dic3) #we ran the merge_dict(a,b) again on c and dict 3 to have the full dict

print d 

#Write a Python script to check if a given key already exists in a dictionary
print "\n" * 5
print "-"*10 
print "\n"*3

def is_key_found(x):
	if x in d:
		print "%s was found!" %x
	else:
		print "Not found"

is_key_found(1)
is_key_found(0)
is_key_found('ship')

#Write a Python program to iterate over dictionaries using for loops

print "\n" * 5
print "-"*10 
print "\n"*3

for key, value in dic3.items():         
	print key,value 



#Write a Python script to generate and print a dictionary that contains a number 
#(between 1 and n) in the form (x, x*x). 
#Sample Dictionary ( n = 5) : 
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#http://www.w3resource.com/python-exercises/dictionary/#EDITOR
print "\n" * 5
print "-"*10 
print "\n"*3

#n = int(raw_input("Whats the range? "))
n=10
dict20 = dict()

for i in range(1, n+1):
	dict20[i]=i**i
	print dict20



#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 
#(both included) and the values are square of keys. Go to the editor
#Sample Dictionary 
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
print "\n" * 5
print "-"*10 
print "\n"*3

dict30 = dict()

for i in range(1,16):
	dict30[i]=i**2
	#return dict30
	print dict30

#Write a Python script to merge two Python dictionaries.

print "\n" * 5
print "-"*10 
print "\n"*3

def merge_two_dict(a,b):
	t=a.copy()
	t.update(b)
	return t

t= merge_two_dict(example, dic1)
print t 


#Write a Python program to iterate over dictionaries using for loops.


print "\n" * 5
print "-"*10 
print "\n"*3


for k,v in dic1.items():
	print k ,"----> ", v 

#Write a Python program to sum all the values in a dictionary.
print "\n" * 5
print "-"*10 
print "\n"*3

print sum(dicx.values())
print dicx.values()

# Write a Python program to multiply all the items (values) in a dictionary
print "\n" * 5
print "-"*10 
print "\n"*3

result = 1#this is used the first time only 
for i in dicx: #it will iterate through the values (items) in dicx and multiply by i
	result = result *dicx[i]

print result


#Write a Python program to remove a key from a dictionary
print "\n" * 5
print "-"*10 
print "\n"*3


del dicx["c"]
print dicx

#adding the key again
dicx["c"]=3
print dicx 

#Write a Python program to map two lists into a dictionary

print "\n" * 5
print "-"*10 
print "\n"*3


keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

color_dict = dict(zip(keys,values))
print color_dict