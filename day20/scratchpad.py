import code

class Pokemon:
    """Pokemon class"""
    
    def __init__(self, name, nickname="", level=1, hp=10, defense=10, atk=10, speed=3):
        """Constructor for the Pokemon class"""
        self.name = name
        if nickname != "":
            self.nickname = nickname
        else:
            self.nickname = self.name.upper()
        self.level = 0
        self.hp = 0
        self.defense = 0
        self.atk = 0
        self.speed = 0
        self.type = ""
        self.gender = ""
        self.size = ""
        self.region = ""
        self.gen = 0
        self.item = ""

p1 = Pokemon(level=100, name='Pikachu', nickname='Ethan', hp=9001, defense=1, atk=100)
p2 = Pokemon('starmie', 'Tommy Kemps')
p3 = Pokemon('mewtwo', 'Sebastian')
p4 = Pokemon("eevee")

code.interact(local=locals())