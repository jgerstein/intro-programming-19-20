import turtle as t

def circles(sz):
    "Use recursion to make a lot of circles"
    t.circle(sz)
    t.circle(-sz)
    if sz > 3:
        circles(sz*.95)
    return

def spiral(sz, growth, ang, max_length):
    """Use recursion to make a spiral"""
    t.fd(sz)
    t.rt(ang)
    if sz < max_length:
        spiral(sz * growth, growth, ang, max_length)
    return


t.speed(0)
spiral(1, 1.04, 34, 300)

t.mainloop()