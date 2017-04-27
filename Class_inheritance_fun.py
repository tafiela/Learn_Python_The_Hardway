
class Person (object): # since we are creating a hierarchy we must add object to the Base 
    def __init__ (self, fname, lname, age ):
        self.FirstName = fname 
        self.LastName = lname 
        self.age = age 
        
    def __str__(self):
        return self.FirstName + " " + self.LastName + "  you are in the parent or BaseClass now"


    def Hello(self):
        return "Hi, my name is Bob and i am a Person"
    
    
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ This is the BaseClass ^^^^^^^^^^^^^^^^^^^^^
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


class Student(Person): #since this is an inheriting class (subClass), we need to put the superior class which is Person in this case
    def __init__(self, fname, lname, age,grades): #student has a firstname, lastname and age and for this subclass it has grades too
        super(Student,self).__init__(fname,lname,age) #since the student needs a firstname, lastname and age, instead of creating new ones
        #go to the Superior class and pull its __init__ with its variables, especailly since Student is a SubClass
        self.student_grades=grades #we have to define the grades variables 
        
    def __str__ (self):  #if this is not defined for this subclass and you tried to print this instance it will inherit the BaseClass __init__
        return self.FirstName + " " + self.LastName 
 
 # ^^^^^^^^^^^^^^^^^^^^^^^^^ This is the childClass or the SubClass ^^^^^^^^^^^^^^^^^^^^       
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

'''
at this point you can test this script by doing the following :

1- run the script by typing : python -i Class_inheritance_fun.py 
2-create a class instance : s = Student ("Rick", "James", 33, [88,67,95,100])
3-Hit enter
4- Now you should have an instance called s for a Student class
5- you can confirm by :  s [Enter] 
    <__main__.Student object at 0x026CE310>    <---- this tells you you have a new instance of Student class at that memory location

6- Now, lets test the instance:

s.student_grades
s.FirstName
s.LastName
s.age 
s.Hello()
print s      <-------- In this case it will call method __str__ and print it it out

'''
        

#################################################
######## #####        Lets Create another Class      ##############
#################################################

class Teacher(Person):
    def __init__(self, fname,lname,age,salary):
        super(Teacher,self).__init__(fname, lname, age)
        self.T_salary = salary
 
    def __str__ (self):
        return self.FirstName + " " + self.LastName +"Makes almost " + str(self.T_salary/2)
    
