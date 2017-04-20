
# f = open("textfile1.txt")
print "which file would you like to open? "
file = raw_input('> ')

try:
	f = open(file) # this file doesnt exist, if we tried to run it now it will give us an error
	if file.name == "doesnt_exist.txt":
		raise Exception #raising your own exception
	# var=var1 
except IOError:
	#if the file was not found it will through an IOError and this except will catch it and provide the below
	print "Sorry. This text_file.txt does not exist!" 

except NameError:
	#if the above exception (IOError) passed, this except will catch the error we have with definning the var error
	print "Sorry. Var is not defined correctly!"

except Exception:
	print "doesnt_exist.txt", "is not cool"

#OR 

# except Exception as x:
# 	print x

else: #if the file didnt through any exception it will execute the else:
	o = f.read()
	print o 
	f.close()

finally: #this sill excute regardless of exceptions
	print "We are done!"
	