import code

class Pokemon:
    """Pokemon class"""

    def __init__(self, name, nickname="", hp=100, level=1, speech=""):
    
        self.name = name
        if nickname != "":
            self.nickname = nickname
        else:
            self.nickname = self.name.upper()
        self.hp = hp
        self.level = level
        if speech != "":
            self.speech = speech
        else:
            self.speech = f"{self.name}!"

    """Implement later
    self.type = ""
    self.shiny = False
    self.weight = 0
    self.moveset = []
    self.nature = ""

    """

    def speak(self):
        print(f"{self.nickname} says {self.speech}")


lillian = Pokemon("mew", "Lillian", 300, 5, "mew")
mikey = Pokemon("shuckle", "Mikey Graham", 500, 4, "shuckleshuckle")
allan = Pokemon("empoleon", "Allan", speech="penguin")
ditto = Pokemon("ditto", level=100, hp=10000)

code.interact(local=locals())