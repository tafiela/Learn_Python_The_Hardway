class Parent(object):
    def altered(self):
        print "PARENT altered"
        
class Child(Parent):
    def altered(self):
        print "CHILD, BEFORE PARENT has been altered()"
        super(Child, self).altered() #since it called Parent.altered() it will print "PARENT altered" here 
        print "CHILD, AFTER PARENT has been altered()"
        
dad = Parent()
son=Child()

print "this is the output of dad.altered() : "
dad.altered()
print "\nthis is the output of  son.altered():"
son.altered()



