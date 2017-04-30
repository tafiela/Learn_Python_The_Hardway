class Parent (object):
    
    def implicit(self):
        print "PARENT implicit()"
        
class Child(Parent):
    pass #This tells python that there is a class called Child but not defined, instead all its definition take it from class Parent

dad = Parent()
son = Child()

dad.implicit() #this will print the PARENT implicit()
son.implicit()  #this will print the PARENT implicit()


'''
This shows you that, if you put functions in a base class (i.e., Parent), then all subclasses (i.e., Child)
will automatically get those features. Very handy for repetitive code you need in many classes.

'''