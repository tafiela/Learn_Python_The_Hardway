class Parent(object):
    
    def override(self):
        print "PARENT override!"
        
class Child(object):
    
    def override(self): #a more specific function for the Child class, this will run instead of the Parent Class override function
        print "CHILD override!"
        
dad = Parent()
son = Child()

dad.override()
son.override()