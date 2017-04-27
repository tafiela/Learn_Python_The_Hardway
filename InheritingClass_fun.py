

#Changes to the BaseClass affects all classes with Inherit FROM it!!!!

class BaseClass(object):
    def printHam(self):
        print 'Ham'
  
  
#class InheritingClass inherited class BaseClass methods       
class InheritingClass(BaseClass):
    pass 

x = InheritingClass()
x.printHam()