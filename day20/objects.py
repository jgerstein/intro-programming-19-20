import code

class Person:
    """Person class"""
    
    def __init__(self, name, age):
        """Constructor for the Person class"""
        self.name = name
        self.age = age



    def get_older(self):
        self.age += 1
    
    def introduce(self):
        if self.name != '':
            print(f"Hi, I'm {self.name}")
        else:
            print("I have no idea who I am!")

# p1 = Person('Nicole')
# p2 = Person('Harsh')
# p3 = Person('Ron')
# p4 = Person('Cory')

code.interact(local=locals())
