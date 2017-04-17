print "Lets practice everything."
print 'You\'d need to know \'bout escape with \\ that do \n newlines and \t tabs'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "__________"
print poem
print "__________"

five = 10-2 + 3-6 #equals to 5
print "\n\n\nThis should be five: %s " %five

def secret_formula(started):
	jelly_beans = started * 5
	jars = jelly_beans * 3
	crates = jars * 10
	return  jars, crates, jelly_beans #is this working like the argv? order matters

start_point = 20
beans, jars, crates = secret_formula(start_point)  #is this like argv?

print "\n\nWith a starting point of : %d " %start_point
print "\n\nWe'd have %d beans, %d jars, and %d crates." %(beans, jars,crates)

start_point = start_point / 10
print "\n\n******* "
print "\n\n\n\nWe can also do that this way."
print "\n\nWe'd have %d beans,  %d jars, and %d crates." %secret_formula(start_point)