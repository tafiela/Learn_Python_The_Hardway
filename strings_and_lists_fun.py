
lst = [1,2,3,4,5,6]
lst_str = ["1,2,3,4,5,6"]
string = "We are the people"
print "\n******************************"
print "For i in lst: print i "
#for i in lst: print i 
for i in lst:
	print i
print "\n******************************"
print "\nFor i in lst_str: print i "
for i in lst_str:
	print i

print "\n******************************"
print "\nFor i in string: print i "
for i in string:
	print i


lst.append(7) 
print lst 


lst_str.append(7) #adding 7 to the list
print lst_str

v=string.split(" ") #able to split a string 
print v

print "#".join(v) #here are joining the v items with the #

print lst_str.pop()
print lst.pop()

