import turtle as t
import random
import math
t.speed(0)

def right_triangle(a, b):
    """draw a right triangle given two sides"""
    t.fd(a)         # side 1
    t.lt(90)
    t.fd(b)         # side 2
    ang = math.degrees(math.atan2(a, b))
    t.lt(180 - ang)
    t.fd(math.hypot(a, b))
    return

def repeated_pattern(reps, sz, set_ang=False):
    """draw a repeated pattern"""
    for n in range(reps):
        t.fd(sz)
        if set_ang == False:
            t.rt(180-360/reps)
        else:
            t.rt(set_ang)

repeated_pattern(20, 100)
t.penup()
t.goto(200, 150)
t.pendown()
repeated_pattern(30, 100, 110)

t.mainloop()