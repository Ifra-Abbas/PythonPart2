

class Car:
    s=12 # variable in the class is an attribute
    def hello(): # function inside the class is the method
        print("hello! kesy ho")

# you can access attributes and methods after accessing the class
print(Car.s)
print(Car.hello())

class Bag:
    name="NotYourBrand"

    def details(self):
        print("Bag's Company")

Channel=Bag() # call the class in variable so then that variable is now an object
print(Channel.details())
print(Channel.name)

# constractors

class Bag:
    def __init__(self,materials,zips,pockets):
        self.materials=materials
        self.zips=zips
        self.pockets=pockets
        
# what is the self ---> is thing that target the location of the object        
reebok=Bag("leather",3,2)
channel=Bag("Polyester",3,4)

print(reebok.pockets)
print(channel.materials)


# variables and functions inside the class --> Attributes and the methods

class Animal:
    a=12
    def __init__(self,name):
        self.name=name #instance attribute or Object
    def hello(self): # instance method or object method
        print(f"hello! {self.name}")
    @classmethod
    def details(c):  #class methods or whatever the parameter we give them captures the class location
        print("ifraa")  #here we can not do self.name 
    @staticmethod
    def speak(): #static no self or no c --> it is not targetting any location
        print("I am static method")

obj=Animal("lion")
print(obj.hello())
print(obj.details())
obj.speak()






