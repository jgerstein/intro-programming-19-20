import code

class Person:
    """Person class"""
    
    age = 0
    name = ""

    def get_older(self):
        self.age += 1
    
    def introduce(self):
        if self.name != '':
            print(f"Hi, I'm {self.name}")
        else:
            print("I have no idea who I am!")

code.interact(local=locals())