class Dog:
    def __init__(self , name , breed):  #here __init__ is the just like the constructor in cpp or java
        self.name = name
        self.breed = breed
    def display(self):
        print("Name: " + self.name)
        print("Breed: " + self.breed)

class Cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color

#Creating the object of class 
d1 = Dog("Tommy" , "German Shepherd!")
d1.display()

# d2 = Dog()      ## Gives error as __init__ has 2 parameters 

#Internal Picture is >>>
d2 = Dog("Charlie" , "Golden Retriwal")
# Dog.__init__(d2 , "Charlie" , "Golden Retriwal")   # Python calls this internally 

# Inheritance in python 
#Single Inheritance 
class Vehicle:
    def __init__(self):
        self.company = "Land Rover"
        self.model = "Defender Octa"
        print("Inside the vehicle Constructor!")
    def show1(self):
        print("Company: " , self.company)
        print("Model: ",self.model)
        pass

class Car(Vehicle):
    def __init__(self):
        super().__init__()   ##Always call parent constructor right
        self.airbag = True
        print("Constructor of the car!!")
    def show2(self):
        print("Company: " , self.company)
        print("Model: " , self.model)
        print("Air Bag: " , self.airbag)
        pass

c1 = Car()
c1.show1()
c1.show2()


class A:
    name = "om"
    branch = "computer"
    skills = "Fullstack-development"

class B:
    year = "2025-2026"
    degree = "BE"

class C(A,B):
    def show(self):
        print("Name: " , self.name)
        print("Branch: " , self.branch)
        print("skills: " , self.skills)
        print("Year: " , self.year)
        print("Degree: " , self.degree)
            
print("------------------------------------------")
cx = C()
cx.show()
print("Name outside show: " , cx.name)
print("------------------------------------------")

#If u are not creating the constructor i.e __init__ method thats completely fine but if u are in inheritance and u are inheriting current class from xanother one then u must call constructor of parent class in child class manually 
# using super().__init__(para1 , para2 , para3 ....)


#Duplicate attributes conflict solved by the Method Resolution Order
# Basically the attrbute that comes first will be accessed in the child class 
# Later on same variable if arrived through another class it will not override that variable right 


class X:
    name = "om"
   
class Y:
   name = "gholap"

class Z(X,Y):
    def show(self):
        print("Name: " , self.name)
    def show(self):
        print("Name inside show: " , self.name)
            
print("------------------------------------------")
z = Z()
z.show()
print("Name inside show: " , z.name)
print("------------------------------------------")
