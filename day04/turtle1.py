import turtle as t

def star(sz):
    """draw a star"""
    for n in range(5):
        t.fd(sz)
        t.rt(144)

star(100)

turtle.mainloop()