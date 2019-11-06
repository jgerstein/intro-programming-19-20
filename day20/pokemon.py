import code

class Pokemon:
    """Pokemon Class"""

    def __init__(self, species, level, hp, name=""):
        """Constructor for Pokemon"""
        self.species = species
        if name == "":
            self.name = self.species.lower()
        else:
            self.name = name
        self.level = level
        self.hp = hp

        """To include later:
        self.evolve_level = ""
        self.age = 0
        self.moves = []
        """

    def speak(self):
        """Make pokemon speak"""
        print(f"{self.name.title()} says {self.name}!")
        return

    def level_up(self):
        """Pokemon gains a level"""
        self.level += 1
        self.hp = int(self.hp * 1.1)
        


cory = Pokemon('Raichu', 100, 10000, name='Cory')
myles = Pokemon('Mewtwo', 101, 10001, 'Myles')

code.interact(local=locals())