import turtle as t

def circles(sz, reps):
    for n in range(reps):
        t.circle(sz)
        t.rt(360/reps)
    if sz > 3:
        circles(sz * .8, reps)

t.speed(0)
circles(100, 2)

t.mainloop()