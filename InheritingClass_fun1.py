

#Changes to the BaseClass affects all classes with Inherit FROM it!!!!

class Character (object): #Base
    def __init__(self,name):
        self.health = 100 #this is an attribute (variable)
        self.name = name 
    def printName(self):
        print self.name 
  
#class Blacksmith  inherited class Character  methods       
class Blacksmith(Character):
    def __init__(self,name, forgeName): #this is the __init__ for the Blacksmith
        super(Blacksmith,self).__init__(name) #Super basically called the __init__ function of the character
        self.forge = Forge(forgeName)
        
class Forge(object):
    def __init__(self, forgeName):
        self.name = forgeName 

        
bs = Blacksmith("Bob", "Rick's Forge")
#we passed the Blacksmith class with the Bob and Ricks Forge attributes
#Since Blacksmith takes (self, name, forgeName) arguments 
#name became = Bob 
#forgeName became = Ricks Forge

bs.printName()
print bs.forge.name
        
