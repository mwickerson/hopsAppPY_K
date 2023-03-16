"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"



"""
██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗     
██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝     
██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗    
██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║    
╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝    
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     
                                                             
██╗    ██╗██╗████████╗██╗  ██╗                               
██║    ██║██║╚══██╔══╝██║  ██║                               
██║ █╗ ██║██║   ██║   ███████║                               
██║███╗██║██║   ██║   ██╔══██║                               
╚███╔███╔╝██║   ██║   ██║  ██║                               
 ╚══╝╚══╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝                               
                                                             
 ██████╗██╗      █████╗ ███████╗███████╗███████╗███████╗     
██╔════╝██║     ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝     
██║     ██║     ███████║███████╗███████╗█████╗  ███████╗     
██║     ██║     ██╔══██║╚════██║╚════██║██╔══╝  ╚════██║     
╚██████╗███████╗██║  ██║███████║███████║███████╗███████║     
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝ 
"""
"""
work with Python's classes
which enable you to create custom objects and methods
create a class
create objectrs based on the class
work with those objects
"""

#understand the concept of classes and instances
#create a class and instantiate it
#understand the class and the instance attributes
#set class instance attributes
#understand class, instance and static methods
#create an instance method
#create a class method
#create a static method
#review the class's code and understand the difference between the class and instance methods

#understanding classes and instances
#declare a class for a type of object
#then create instances of that class - individual objects based on that class

#when should you use classes?
#when you need to create a new type of object that python doesn't already have
#classes are useful for encapsulating data and functionality
#encapsulation is the process of combining data and functions into a single unit
#you can define attributes to store data and methods to perform operations on that data

#How do you create a class?
#create a header statement that begins with the keyword class
#followed by the name of the class
#followed by a colon
#then indent the body of the class by four spaces

#for example:
#class SculptureOffice:
#    pass
#pass is a placeholder for code that you will write later
# can you wrap this into a @hops.component()?
class SculptureOffice:
    pass

#How do you create an instance of a class?
#creating an instance of a class is called instantiation
#to do this you call the class name as if it were a function
#you create a variable and assign it to the result of the class name function call
#the variable is called an instance of the class
#example:
sculpture_office = SculptureOffice()

#How are Python Class names usually capitalized?
#PascalCase is the convention for naming classes in Python
#this means that each word in the name begins with a capital letter
#French mathematician Blaise Pascal is credited with inventing Pascal's Triangle

#How do you create an instance of a class?
#creating an instance of a class is called instantiation
#to do this you call the class name as if it were a function
#you create a variable and assign it to the result of the class name function call
#the variable is called an instance of the class
#example:
#sculpture_office = SculptureOffice()
#this illustrates the relationship between the class and the instance
#SculptureOffice is the class
#sculpture_office is the instance

#Create a Class and Instantiate Instances
#create the SculptureFaculty class and create two instances of it
#verify their class type using the type() function 
# and compare the two instances to prove that they are different

"""
 ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗               
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝               
██║     ██████╔╝█████╗  ███████║   ██║   █████╗                 
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝                 
╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗               
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝               
                                                                
 ██████╗██╗      █████╗ ███████╗███████╗                        
██╔════╝██║     ██╔══██╗██╔════╝██╔════╝                        
██║     ██║     ███████║███████╗███████╗                        
██║     ██║     ██╔══██║╚════██║╚════██║                        
╚██████╗███████╗██║  ██║███████║███████║                        
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝                        
                                                                
██╗███╗   ██╗███████╗████████╗ █████╗ ███╗   ██╗ ██████╗███████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔════╝██╔════╝
██║██╔██╗ ██║███████╗   ██║   ███████║██╔██╗ ██║██║     █████╗  
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║╚██╗██║██║     ██╔══╝  
██║██║ ╚████║███████║   ██║   ██║  ██║██║ ╚████║╚██████╗███████╗
"""

#Create a Class and Instantiate Instances
class SculptureFaculty:
    pass

#instantiate two instances of the class
sculpture_faculty_1 = SculptureFaculty()
sculpture_faculty_2 = SculptureFaculty()
print (type(sculpture_faculty_1))
print (type(sculpture_faculty_2))
print (sculpture_faculty_1 == sculpture_faculty_2)


#Understanding Class and Instance Attributes
# set two types of attributes on a class
# class attributes and instance attributes
# create both types of attributes
#learn about the __init__() method of the class object
#a special method that is called when an instance of the class is created
# and the keyword self which refers to the instance of the class

#Class Attribute applies to all instances of the class
# access through the class name or the instance name
#Instance Attribute applies to a single instance of the class
#not shared with other instances of the class
#understading How you set Class Attributes
# place a variable assignment statement inside the class definition body

#understanding How you set Instance Attributes
# use the __init__() method

class SculptureFaculty:
    #class attribute
    sculpture_faculty = "Sculpture Faculty"

    #instance attribute
    def __init__(self, name, department):
        self.name = name
        self.department = department

class SculptureFaculty:
    #class attribute
    sculpture_faculty = "Sculpture Faculty"
    sculpture_students = 12
    def __init__(self, name, department):
        self.name = name
        self.department = department

fulltime = SculptureFaculty("John", "Sculpture")
parttime = SculptureFaculty("Jane", "Sculpture")
print (fulltime.name)
print (parttime.name)
print (fulltime.department)
print (parttime.department)

#put this class into a @hops.coimponent()
@hops.component(
    "/sculpture_faculty",
    name="SculptureFaculty",
    description="SculptureFaculty",
    inputs= [
        hs.HopsString("name", "name", "name"),
        hs.HopsString("department", "department", "department")
    ],
    outputs=[
        hs.HopsString("name", "name", "name"),
        hs.HopsString("department", "department", "department")
    ]
)
def sculpturefaculty(name, department):
    sculpture_faculty = SculptureFaculty(name, department)
    return sculpture_faculty.name, sculpture_faculty.department

#Grasp Class, Instance and Static Methods
#understand the difference between class, instance and static methods
#a methond is a unit of code that performs and action on an object
#it is similar to a function but it is defined inside a class
#bound to the class and its instances rather than being a global function
#python has three types of methods
#class methods
#instance methods
#static methods
#learn when to use each type of method

#Class Methods
#class methods are methods that are bound to the class rather than the object's instance
#they have access to the state of the class as it takes the class as an argument
"""
 ██████╗  ██████╗██╗      █████╗ ███████╗███████╗███╗   ███╗███████╗████████╗██╗  ██╗ ██████╗ ██████╗     
██╔═══██╗██╔════╝██║     ██╔══██╗██╔════╝██╔════╝████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗    
██║██╗██║██║     ██║     ███████║███████╗███████╗██╔████╔██║█████╗     ██║   ███████║██║   ██║██║  ██║    
██║██║██║██║     ██║     ██╔══██║╚════██║╚════██║██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██║  ██║    
╚█║████╔╝╚██████╗███████╗██║  ██║███████║███████║██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝    
 ╚╝╚═══╝  ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝     
                                                                                                          
██████╗ ███████╗ ██████╗ ██████╗ ██████╗  █████╗ ████████╗ ██████╗ ██████╗                                
██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗                               
██║  ██║█████╗  ██║     ██║   ██║██████╔╝███████║   ██║   ██║   ██║██████╔╝                               
██║  ██║██╔══╝  ██║     ██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗                               
██████╔╝███████╗╚██████╗╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║                               
╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   
"""
#they are defined with the @classmethod decorator
#they are used to create factory methods 

#Instance Methods
#instance methods are methods that are bound to the object's instance
#the self.__class__ attribute is used to access the class from the instance
#they are used to create the object's representation
 
#Static Methods
#static methods are methods that are not bound to the class or object's instance
#they are defined with the @staticmethod decorator
#they are used to create utility functions

#Which type of method should you use in your class?
# instance methods are most common
# class methods are used when you need to create factory methods
# static methods are used when you need to create utility functions
"""
 ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗               
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝               
██║     ██████╔╝█████╗  ███████║   ██║   █████╗                 
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝                 
╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗               
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝               
                                                                
██╗███╗   ██╗███████╗████████╗ █████╗ ███╗   ██╗ ██████╗███████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔════╝██╔════╝
██║██╔██╗ ██║███████╗   ██║   ███████║██╔██╗ ██║██║     █████╗  
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║╚██╗██║██║     ██╔══╝  
██║██║ ╚████║███████║   ██║   ██║  ██║██║ ╚████║╚██████╗███████╗
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
                                                                
███╗   ███╗███████╗████████╗██╗  ██╗ ██████╗ ██████╗            
████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗           
██╔████╔██║█████╗     ██║   ███████║██║   ██║██║  ██║           
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██║  ██║           
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝           
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  
"""
#Create an Instance Method
# to do this you define a method inside the class definition
# the first line of the method definition is the method header
# this consists of the keyword def, the method name, and the parameters
#including parentheses and a colon
# this first starts the class definition body
# the second is a docstring
# the third is the method body, an instance method called getFacultyName:

class SculptureFaculty:
    #the def __init__() method appears before the getFacultyName() method
    #instance attribute
    def __init__(self, name, department):
        self.name = name
        self.department = department


    def getFacultyName(self):
        """Return the name of the faculty member"""
        faculty = f"{self.name} is a member of the {self.department} department."
        return (faculty)

# call an instance method
# create a new instance of the class
# call the instance method using the instance name and the method name
# pass the instance as the first argument
# the self parameter is automatically passed to the instance method
# example
sculpture_faculty = SculptureFaculty("Michael Wickerson", "Sculpture")
print (sculpture_faculty.getFacultyName())

#put this class into a @hops.coimponent()
@hops.component(
    "/sculpture_faculty3",
    name="SculptureFaculty3",
    description="SculptureFaculty3",
    inputs= [
        hs.HopsString("name", "name", "name"),
        hs.HopsString("department", "department", "department")
    ],
    outputs=[
        hs.HopsString("name", "name", "name")
    ]
)
def sculpture_faculty3(name, department):
    sculpture_faculty = SculptureFaculty(name, department)
    return sculpture_faculty3.getFacultyName()


"""
 ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗    
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝    
██║     ██████╔╝█████╗  ███████║   ██║   █████╗      
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝      
╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗    
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    
                                                     
███████╗████████╗ █████╗ ████████╗██╗ ██████╗        
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔════╝        
███████╗   ██║   ███████║   ██║   ██║██║             
╚════██║   ██║   ██╔══██║   ██║   ██║██║             
███████║   ██║   ██║  ██║   ██║   ██║╚██████╗        
╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝        
                                                     
███╗   ███╗███████╗████████╗██╗  ██╗ ██████╗ ██████╗ 
████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗
██╔████╔██║█████╗     ██║   ███████║██║   ██║██║  ██║
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██║  ██║
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
"""
#Create a Static Method
# there are two different ways to create a class method and a static method

"""
 ██████╗ ███████╗████████╗ █████╗ ████████╗██╗ ██████╗███╗   ███╗███████╗████████╗██╗  ██╗ ██████╗ ██████╗     
██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔════╝████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗    
██║██╗██║███████╗   ██║   ███████║   ██║   ██║██║     ██╔████╔██║█████╗     ██║   ███████║██║   ██║██║  ██║    
██║██║██║╚════██║   ██║   ██╔══██║   ██║   ██║██║     ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██║  ██║    
╚█║████╔╝███████║   ██║   ██║  ██║   ██║   ██║╚██████╗██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝    
 ╚╝╚═══╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝     
                                                                                                               
██████╗ ███████╗ ██████╗ ██████╗ ██████╗  █████╗ ████████╗ ██████╗ ██████╗                                     
██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗                                    
██║  ██║█████╗  ██║     ██║   ██║██████╔╝███████║   ██║   ██║   ██║██████╔╝                                    
██║  ██║██╔══╝  ██║     ██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗                                    
██████╔╝███████╗╚██████╗╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║                                    
╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   
"""
# the first way is to use the @staticmethod decorator
# this tells python to treat the method as a class method

# the second way is to use the classmethod() method or the staticmethod() method
# these methods are not decorators, they are methods of the class object
# use decorators to be more concise

#create a Class Method
# class methods are methods that are bound to the class and not the object of the class
# use a decorator to create a class method

#example
class SculptureFaculty():
    def __init__(self, name, department):
        self.name = name
        self.department = department

    @classmethod
    def getFacultyName(self):
        #create a new instance of the class
        sculpture_faculty = SculptureFaculty("John", "Sculpture")
        return sculpture_faculty.name + " teaches " + sculpture_faculty.department
        
#call the class method
print(SculptureFaculty.getFacultyName())
print (SculptureFaculty.getFacultyName())

#put this class into a @hops.coimponent()
@hops.component(
    "/sculpture_faculty",
    name = "sculpture_faculty",
    description = "This is a class method",
    inputs = [
        hs.HopsString("name", "The name of the faculty member"), 
        hs.HopsString("department", "The department of the faculty member")
    ],
    outputs = [
        hs.HopsString("faculty_name", "The name of the faculty member")
    ]
)
def sculpture_faculty(name, department):
    #create a new instance of the class
    sculpture_faculty = SculptureFaculty(name, department)
    return sculpture_faculty.name + " teaches " + sculpture_faculty.department

#Call a Class Method
# you can call a class method from the class or from an instance of the class
#example
print (SculptureFaculty.getFacultyName())
#from an instance of the class
sculpture_faculty = SculptureFaculty("John", "Sculpture")
print (sculpture_faculty.getFacultyName())

#create a static method
# static methods are methods that are bound to a class rather than the objects for that class
#place the method's code in a class, but you don't need to reference the class or the object
#procede it with the @staticmethod decorator
#this tells python to treat the method as a static method

#example
class SculptureFaculty():
    def __init__(self, name, department):
        self.name = name
        self.department = department

    @staticmethod
    def getFacultyName():
        #create a new instance of the class
        sculpture_faculty = SculptureFaculty("John", "Sculpture")
        return sculpture_faculty.name + " teaches " + sculpture_faculty.department

#use the staticmethod() method
#create an instance method called convert()
#use the staticmethod() method to convert the method to a static method
#example
class SculptureFaculty():
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def convert(self):
        return self.name + " teaches " + self.department

    convert = staticmethod(convert)


SculptureFaculty.convert = staticmethod(SculptureFaculty.convert)

#Call a Static Method
#via the class name and the method name or via the object name and the method name
#example say you instantiate an object called sculpture_faculty that includes the static method Michael

class SculptureFaculty():
    def __init__(self, name, department):
        self.name = name
        self.department = department

    @staticmethod
    def getFacultyName():
        #create a new instance of the class
        sculpture_faculty = SculptureFaculty("John", "Sculpture")
        return sculpture_faculty.name + " teaches " + sculpture_faculty.department  

#call the static method
print (SculptureFaculty.getFacultyName())
#call the static method via the object
sculpture_faculty = SculptureFaculty("John", "Sculpture")
print (sculpture_faculty.getFacultyName())


#Create an Instance Method
class SculptureFaculty():
    school = "KCAI"
    education = "BFA"
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def getInfo(self):
        de = (
            f"{self.name} teaches {self.department} at {self.school}."
            f" {self.name} has a {self.education} in Sculpture."
        )
a = SculptureFaculty("Jill", "Sculpture")
b = SculptureFaculty("Michael", "Sculpture")
print(a.name) 
print(a.department)
print(a.school) 
print(a.education)
print(a.getInfo())
print(b.name)
print(b.department)
print(b.school)
print(b.education)
print(b.getInfo())

#wrap this in a @hops.component()
@hops.component(
    "/sculpture_faculty",
    name = "sculpture_faculty",
    description = "This is an instance method",
    inputs = [
        hs.HopsString("name", "The name of the faculty member"), 
        hs.HopsString("department", "The department of the faculty member")
    ],
    outputs = [
        hs.HopsString("faculty_name", "The name of the faculty member")
    ]
)
def sculpture_faculty(name, department):
    #create a new instance of the class
    sculpture_faculty = SculptureFaculty(name, department)
    return sculpture_faculty.name + " teaches " + sculpture_faculty.department



#Create a Class Method
class SculptureFaculty():
    school = "KCAI"
    education = "BFA"
    @classmethod
    def getFacultyName(self):
        fi = (self.school + " has a " + self.education + " in Sculpture.")
        fi = fi + " The faculty members are: "
        return fi
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def getInfo(self):
        de = (
            f"{self.name} teaches {self.department} at {self.school}."
            f" {self.name} has a {self.education} in Sculpture."
        )
        return de

a = SculptureFaculty("Jill", "Sculpture")
b = SculptureFaculty("Michael", "Sculpture")
print(a.name)
print(a.department)
print(a.school)
print(a.education)
print(a.getInfo())
print(b.name)
print(b.department)
print(b.school)
print(b.education)
print(b.getInfo())

#wrap this in a @hops.component()
@hops.component(
    "/sculpture_faculty",
    name = "sculpture_faculty",
    description = "This is a class method",
    inputs = [
        hs.HopsString("name", "The name of the faculty member"), 
        hs.HopsString("department", "The department of the faculty member")
    ],
    outputs = [
        hs.HopsString("faculty_name", "The name of the faculty member")
    ]
)
def sculpture_faculty(name, department):
    #create a new instance of the class
    sculpture_faculty = SculptureFaculty(name, department)
    return sculpture_faculty.name + " teaches " + sculpture_faculty.department


#Create a Static Method

#Class's code
#class definition
class SculptureFaculty():
    #statments that define the class attributes school and education
    school = "KCAI offers"
    education = "BFA"
    # the class decorator
    @classmethod
    def getFacultyName(self):
        #create a new instance of the class
        fi = self.school + " a "
        fi = fi + self.education + " in Sculpture"
        return fi
    #the __init__ method declares  and populated variables for each new instance of the class
    def __init__(self, name, department):       
        self.name = name
        self.department = department
    #the getInfo() method displays info about the instance
    def getInfo(self):
        de = (
            f"{self.name} teaches {self.department} at {self.school}."
            f" {self.name} has a {self.education} in Sculpture."
        )
        return de
    # the @staticmethod decorator introduces the addtion() method, which adds two numbers
    @staticmethod
    def addition(x):
        return x + x
    # the @staticmethod decorator introduces the subtraction() method, which subtracts two numbers      
    @staticmethod
    def subtraction(x):
        return x - x
# create two instances of the class a and b
a = SculptureFaculty("Jill", "Sculpture")
b = SculptureFaculty("Michael", "Sculpture")
print (a.getInfo())
print (b.getInfo())
#instantiate the static method
print (SculptureFaculty.addition(5))
print (SculptureFaculty.getFacultyName())

#wrap this in a @hops.component()
@hops.component(
    "/sculpture_faculty",
    name = "sculpture_faculty",
    description = "This is a static method",
    inputs = [
        hs.HopsString("name", "The name of the faculty member"),
        hs.HopsString("department", "The department of the faculty member")
    ],
    outputs = [
        hs.HopsString("faculty_name", "The name of the faculty member")
    ]
)
def sculpture_faculty(name, department):
    #create a new instance of the class
    sculpture_faculty = SculptureFaculty(name, department)
    return sculpture_faculty.name + " teaches " + sculpture_faculty.department


if __name__ == "__main__":
    app.run(debug=True)
