# class variables

class Dog:
    species = "Canis familiaris"  # class variable
    isAlive = True  # class variable

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age  # instance variable

    def get_info(self):
        return f"{self.name} is {self.age} years old and belongs to the species {self.species}."
    
    def sleep(self):
        return f"{self.name} is sleeping."
    def eat(self):
        return f"{self.name} is eating yet it is {self.age} years old."
        
    
# Creating instances of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("max",8)
dog3 = Dog("Tommy",16)

print(dog1.isAlive) 
# print(dog2.isAlive) 
print(dog3.isAlive) 

print(dog1.get_info())
print(dog2.get_info())  
# print(dog3.get_info())  

# print(dog1.eat())
print(dog2.eat())  
print(dog3.eat()) 

