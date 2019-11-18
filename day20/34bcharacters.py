import code

class Character:
    """Character class. Base class for all types of characters"""

    def __init__(self, name, x=0, y=0):
        """Constructor for Character class"""
        self.name = name
        self.x = x
        self.y = y

    def check_loc(self, x, y):
        if x == self.x and y == self.y:
            return True
        else:
            return False

    def __repr__(self):
        return f"<{self.name} @ {self.x}, {self.y}>" 

characters = [
    Character('Harsh', 5, 4),
    Character('Rachel', 3, 7),
    Character('Cory'),
    Character('Morgan', 2, 1),
    Character('Myles', 1, 6)
    ]

for y in range(10):
    for x in range(10):
        occupied = False
        for c in characters:
            if c.check_loc(x, y):
                occupied = True
        if occupied:
            print(' @ ', end='|')
        else:
            print(f"{x},{y}", end="|")
    print()

code.interact(local=locals())