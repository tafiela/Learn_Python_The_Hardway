#this one is like your scripts with argv
def print_bunch(*args):
	arg1, arg2, arg3, arg4 = args
	print "arg1: %r, arg2: %r , arg3: %r, arg4: %r" %(arg1, arg2, arg3, arg4)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r " %(arg1, arg2)

#this just takes one argument
def print_one(arg1):
	print "arg1: %r" %arg1

#this one takes no arguments
def print_none():
	print "i got nothing"


print_bunch("Zed", "Shaw","third", "fourth")
print_two_again("ZZed", "Sshaw")
print_one ("First!")
print_none ()
