

class MyStuff(object):
	def __init__(self):
		self.tangerine = "And this is how you do it"

	def apple(stuff):
		print "This is my apple"

c=MyStuff()
c.apple()
print c.tangerine

#Two ways to get things from MyStuff Class

#module style
c.apples()
print c.tangerine

#class style

c=MyStuff()
c.apple()
print c.tangerine