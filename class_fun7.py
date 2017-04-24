class x(y): #Make a class x that is-a Y 
#Salmon is a fish
    def __init__ (self,J): #Class X has-a self and J parameters
    #salmon has eyes  
        pass
    def M(self, J): #Class x has a function (or method) that takes self and J as parameters
        pass

foo = x() #sets foo to an instance in class X 
foo.M(J)#from foo get function M, call it with parameters self and J 
foo.K = Q #from foo get the K attribute (or variable) and assign it to Q 
