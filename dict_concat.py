a={1:"a", 2:"b", 3:"c"}
b={4:"d", 5:"e", 6:"f"}

#c=a.copy()
#c.update(b)
#print c 

#OR

def combine_dict(a,b):
	c=a.copy()
	c.update(b)
	return c 

c= combine_dict(a,b)
print c 