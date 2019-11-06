class Cat:
    """Class describing a cat"""

    animal_type = "mammal"

    def __init__(self, name, age):
        """Constructor for Cat class"""
        self.name = name
        self.age = age
    
    def speak(self):
        """Make a cat speak"""
        print(f"{self.name} meows at you")

fred = Cat("Fred", 15)
momo = Cat("Maurice", 9)

print(f"Every cat is a {Cat.animal_type}")
print(f"Fred is a {fred.animal_type}")
print(f"Maurice is a {momo.animal_type}")
print(f"{fred.name} is {fred.age} years old")
print(f"{momo.name} is {momo.age} years old")
fred.speak()
momo.speak()