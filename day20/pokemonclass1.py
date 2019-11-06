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







code.interact(local=locals())