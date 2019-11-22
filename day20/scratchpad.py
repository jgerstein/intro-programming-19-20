import code
from random import randint

class Character:
    """Character class"""

    def __init__(self, name, x=0, y=0):
        """Constructor for the Character class"""
        self.name = name
        self.x = x
        self.y = y

    def is_here(self, x, y):
        """Return True if the Character is at specified location, False otherwise"""
        if self.x == x and self.y == y:
            return True
        else:
            return False

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __repr__(self):
        return f"< {self.name} @ {self.x},{self.y} >"


def show_map():
    for y in range(7):
        for x in range(10):
            occupied = False
            # Everything in here refers to a cell with coordinates (x,y)
            for c in characters:
                if c.is_here(x,y):
                    occupied = True
            if occupied:
                print("@", end="")
            else:
                print(f".", end="")
        print()

characters = [
    Character('Tommy', 5, 1),
    Character('Markus', 4, 2),
    Character('Choncho', 2, 3),
    Character('Kevin'),
    Character('Ethan', 8, 2),
    Character('Melody', 7, 3)
]

# print(characters)
code.interact(local=locals())