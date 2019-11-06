import random

class Cat:
    """Class describing a cat"""

    animal_type = "mammal"

    def __init__(self, name, age):
        """Constructor for Cat class"""
        self.name = name
        self.age = age
        self.hunger = random.randint(1, 20)
    
    def speak(self):
        """Make a cat speak"""
        print(f"{self.name} meows at you")
    
    def feed(self, food):
        if self.hunger > 0:
            self.hunger -= food
            print(f"{self.name} was hungry and ate your food. Their hunger level is now {self.hunger}")
        else:
            print(f"{self.name} isn't hungry and refuses your food")

fred = Cat("Fred", 15)
momo = Cat("Maurice", 9)

for n in range(3):
    fred.feed(2)
    momo.feed(1)
    print('\n')