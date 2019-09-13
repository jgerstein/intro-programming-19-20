import turtle as t

def star(sz, drawer=t, ):
    """draw a star"""
    for n in range(5):
        drawer.fd(sz)
        drawer.rt(144)

star(100)

turtle.mainloop()