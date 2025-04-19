class Animal:
    def __init__ (self, name, speed):
        self.name = name
        self.speed = speed
    def eat(self):
        return f"{self.name} is eating."


class Prey(Animal):
    def run(self):
        return f"{self.name} is running at a speed of {self.speed} km/h."
    
class Predator(Animal):
    def hunt(self):
        return f"{self.name} is hunting."
    
class Gazelle(Prey):
     pass
class Lion(Predator):
     pass

class Fish(Prey, Predator):
     pass   



# Creating instances of the classes
gazelle = Gazelle("Gazelle", 80)
lion = Lion("Lion", 50)
fish = Fish("Fish", 20)
# Accessing methods from the base and derived classes
print(gazelle.eat())
print(gazelle.run())
print(lion.eat())
print(lion.hunt())
print(fish.eat())
print(fish.run())
print(fish.hunt())
