import code
import random

x_bound = 15
y_bound = 6

class Character:
    """Character class. Base class for all types of characters"""

    def __init__(self, name, x=0, y=0, sym='@'):
        """Constructor for Character class"""
        self.name = name
        self.x = x
        self.y = y
        self.sym = sym

    def check_loc(self, x, y):
        if x == self.x and y == self.y:
            return True
        else:
            return False

    def update_loc(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if new_x >= 0 and new_x < x_bound:
            self.x = new_x
        if new_y >= 0 and new_y < y_bound:
            self.y = new_y

    def __repr__(self):
        return f"<{self.name} @ {self.x}, {self.y}>" 

characters = [
    Character('Harsh', 5, 4, "G"),
    Character('Rachel', 3, 2, "?"),
    Character('Cory', sym="W"),
    Character('Morgan', 12, 1, "!"),
    Character('Myles', 1, 3, "$")
    ]

def move_all():
    for c in characters:
        c.update_loc(random.randint(-1,1), random.randint(-1,1))

def show_map():
    for y in range(y_bound):
        for x in range(x_bound):
            occupied = ''
            for c in characters:
                if c.check_loc(x, y):
                    occupied = c.sym
            if occupied:
                print(occupied, end='')
            else:
                print('-', end='')
        print()

code.interact(local=locals())