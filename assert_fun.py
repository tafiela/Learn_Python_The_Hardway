print "How old are you? "
age=int(raw_input('> '))
#it checks for errors automatically 

assert age > 0, "How is your age negative" # it will throw an AssertionError with this message <How is your age negative>
											#As such,  AssertionError: How is your age negative
print "Your age is %d" %age

